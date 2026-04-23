# DevSupport Copilot

AI-powered support ticket triage system over Stripe developer documentation. Accepts a raw support ticket, classifies it, retrieves relevant documentation, searches historical incidents, drafts a cited reply, determines routing action, and persists the result — all in a single API call.

---

## Pipeline

```
POST /tickets/analyze
        │
        ▼
   ┌─────────┐    ┌──────────┐    ┌─────────────┐    ┌───────┐
   │classify │───▶│ retrieve │───▶│ investigate │───▶│ draft │
   └─────────┘    └──────────┘    └─────────────┘    └───────┘
        │               │                │                │
   gpt-4o-mini    ChromaDB           gpt-4o-mini      gpt-4o-mini
   category +     stripe_docs        bind_tools()     cited reply
   severity       (962 chunks)       search_similar
   needs_info                        _tickets()           │
                                     │                    ▼
                               historical_tickets   ┌───────┐    ┌─────────┐
                               ChromaDB (31 docs)   │ route │───▶│ persist │
                                                    └───────┘    └─────────┘
                                                    auto_reply    PostgreSQL
                                                    escalate      tickets table
                                                    needs_info
```

6 nodes orchestrated by **LangGraph**. `investigate` is the only agentic node — the LLM decides whether to call `search_similar_tickets`; the rest are deterministic.

---

## Tech stack

| Layer | Technology |
|-------|-----------|
| API | FastAPI + Pydantic v2 |
| Workflow | LangGraph (StateGraph) |
| LLM | OpenAI gpt-4o-mini |
| Embeddings | OpenAI text-embedding-3-small |
| RAG / vector store | LangChain + ChromaDB |
| Function calling | LangChain `@tool` + `ChatOpenAI.bind_tools` |
| Database | PostgreSQL 16 + SQLAlchemy 2.0 async + asyncpg |
| Infrastructure | Docker Compose |
| Testing | pytest + pytest-asyncio (54 integration tests) |

---

## API

**Request**
```bash
curl -X POST http://localhost:8000/tickets/analyze \
  -H "Content-Type: application/json" \
  -d '{
    "subject": "Webhook 401 after key rotation",
    "body": "All webhooks returning 401 since we rotated keys yesterday."
  }'
```

**Response (abridged)**
```json
{
  "ticket_id": "TICKET-A3F2C1B0",
  "classification": {
    "category": "Webhook Issues",
    "severity": "P2 - High",
    "needs_more_info": false
  },
  "answer": {
    "answer": "After rotating your signing secret, you must update the endpoint secret in your webhook handler. Pass the new secret to `constructEvent()` [1][3].",
    "citations": [
      { "marker": "[1]", "source_title": "Resolve webhook signature verification errors", "source_url": "https://docs.stripe.com/webhooks/signature" }
    ],
    "retrieval_sufficient": true
  },
  "draft_reply": "Hi,\n\nThank you for reaching out...",
  "similar_tickets": [
    { "ticket_id": "TICKET-004", "similarity_score": 0.82, "resolution": "Customer had not updated the endpoint secret after key rotation." }
  ],
  "action": "auto_reply",
  "persisted_ticket_id": "TICKET-A3F2C1B0",
  "workflow_trace": [
    { "node": "classify",     "status": "completed", "duration_ms": 980 },
    { "node": "retrieve",     "status": "completed", "duration_ms": 2140 },
    { "node": "investigate",  "status": "completed", "duration_ms": 3200 },
    { "node": "draft",        "status": "completed", "duration_ms": 4100 },
    { "node": "route",        "status": "completed", "duration_ms": 1 },
    { "node": "persist",      "status": "completed", "duration_ms": 12 }
  ]
}
```

---

## Quick start

**Prerequisites:** Docker, Python 3.11, OpenAI API key.

```bash
# 1. Clone and install
git clone https://github.com/Leo-Liu66/devsupport-copilot
cd devsupport-copilot
pip install -e backend/

# 2. Configure
cp .env.example .env
# Set OPENAI_API_KEY in .env

# 3. Start Postgres
docker compose up -d postgres

# 4. Switch to backend/ — all subsequent commands run from here
cd backend

# 5. Ingest knowledge base into ChromaDB (one-time, ~30s, ~$0.01 in embeddings)
#    seed_tickets_with_resolutions.json is already committed — no LLM synthesis needed
python scripts/ingest_historical_tickets.py

# 6. Start the API
uvicorn app.main:app --reload
```

Server starts on **http://localhost:8000**.

- **Interactive docs (Swagger UI):** http://localhost:8000/docs — try the endpoint directly in the browser, no frontend needed.
- The server logs `schema ready` once on first start; subsequent restarts are idempotent.

> **Note:** Steps 5–6 must run from the `backend/` directory. ChromaDB resolves its data path relative to CWD — running from `backend/` keeps ingestion and the server pointing at the same `backend/chroma_db/`.

---

## Project structure

```
backend/
  app/
    models/        Pydantic contracts (TicketInput, TicketAnalysis, ...)
    routers/       POST /tickets/analyze
    services/
      rag/         Stripe docs ingestion, retrieval, cited Q&A
      triage/      Classification (category/severity), reply drafting
      workflow/    LangGraph graph, nodes, state
      tools/       search_similar_tickets, create_ticket (@tool)
    db/            SQLAlchemy ORM, async CRUD
  config.py        Pydantic settings (env-backed)
data/
  seed_tickets.json                  31 labelled test tickets
  seed_tickets_with_resolutions.json LLM-synthesised resolutions (cached)
docs/tasks/                          Implementation briefs (01–13)
```

---

## Design decisions

**Hallucination control** — citations bind to `chunk_id` from retrieval, not to LLM-generated claims. The route node escalates instead of auto-replying when `retrieval_sufficient=False`, so the system never drafts a reply it can't support with sources.

**Agentic vs deterministic** — only `investigate_node` is agentic (`bind_tools` with a 2-iteration hard cap). Ticket persistence is deterministic (`persist_node` always runs after `route`) because persistence is a pipeline requirement, not a model decision.

**Soft-fail persistence** — a DB write failure sets `persist_node.status = "failed"` and `persisted_ticket_id = null` but does not abort the 200 response. The cited answer and draft reply are still returned.
