.PHONY: setup dev test help

help:
	@echo "make setup  — first-time setup: start Postgres + ingest knowledge base"
	@echo "make dev    — start the API server (Postgres must be running)"
	@echo "make test   — run the full test suite"

setup:
	docker compose up -d postgres
	@echo "Waiting for Postgres to be ready..."
	@sleep 3
	cd backend && python scripts/ingest_stripe_docs.py
	cd backend && python scripts/ingest_historical_tickets.py
	@echo ""
	@echo "Setup complete. Run 'make dev' to start the server."

dev:
	docker compose up -d postgres
	cd backend && uvicorn app.main:app --reload

test:
	cd backend && python -m pytest tests/ -v
