from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from app.config import settings
from app.models.ticket import (
    SEVERITY_LEVELS,
    VALID_CATEGORIES,
    TicketClassification,
)

CLASSIFIER_PROMPT = """You are a support ticket classifier for a SaaS product that uses Stripe for payments, webhooks, and billing.

Given a support ticket (subject + body), classify it into exactly one category, one severity level, a confidence score, and a list of keywords.

## CATEGORIES (choose exactly one)

1. **Webhook Issues** — Problems with receiving, verifying, or processing Stripe webhook events. Includes: webhook delivery failures, signature verification errors, event ordering, duplicate events, missed events, Connect webhook routing, webhook endpoint configuration.

2. **Payment Failures** — Problems where a payment, charge, or PaymentIntent fails or gets stuck. Includes: card declines (card_declined, insufficient_funds, do_not_honor), 3D Secure / SCA authentication problems, PaymentIntent stuck in requires_action or requires_confirmation, capture failures, currency mismatch errors, test-mode card issues.

3. **API Authentication** — Problems with Stripe API keys, authentication errors, or authorization failures. Includes: "No such API key" errors, 401/403 responses, restricted key permission issues, key rotation, test-vs-live mode key confusion, keys not working in specific environments (Docker, CI).

4. **Refund & Disputes** — Problems with issuing refunds or handling chargebacks/disputes. Includes: refund failures on disputed charges, dispute evidence submission, chargeback outcomes, partial refund display issues, refund processing time questions, dispute deadlines.

5. **Account & Configuration** — Account-level settings, access management, and platform configuration. Includes: team member access/roles, account restrictions/verification, statement descriptors, payout schedules, enabling payment methods (Apple Pay, Google Pay), general integration questions not specific to payments/webhooks/auth/refunds.

## SEVERITY LEVELS

- **P1 - Critical**: Production system is broken or blocked RIGHT NOW with active revenue impact or complete inability to operate. The issue is currently happening in production (not test mode), affects real customers or real payments, and has no workaround. Examples: webhook handler returning 500s on live payment events, signature verification failing on ALL production webhooks, API key suddenly invalid in live production.

- **P2 - High**: A significant feature is broken or degraded in a way that impacts operations, but the system is not completely down. May affect multiple customers, have a partial workaround, or have time pressure. Examples: duplicate webhook processing, payment failures affecting a subset of customers, API key failing in one environment but not another, dispute deadline approaching, account restricted pending verification.

- **P3 - Medium**: A real problem or important question, but not time-critical and not blocking core operations. Examples: how-to questions about production workflows, configuration not working as expected, need information to diagnose further, historical issue investigation.

- **P4 - Low**: General inquiry, how-to question, feature request, or test-mode-only issue with no production impact. Examples: test card not working in test mode, understanding event ordering (informational), setting up a new feature, general integration guidance.

## CONFIDENCE SCORING

- 0.9-1.0: Category and severity are unambiguous from the ticket content.
- 0.7-0.89: Strong signal but some ambiguity (e.g., could be adjacent category).
- 0.5-0.69: Moderate uncertainty, ticket is vague or spans multiple categories.
- Below 0.5: Very unclear, guessing based on limited information.

## KEYWORDS

Extract 3-5 keywords or short phrases that:
- Identify the specific Stripe feature, API, or error involved
- Would be useful as search terms for retrieving relevant documentation
- Prefer Stripe-specific terminology (e.g., "payment_intent.succeeded", "SignatureVerificationError", "requires_action") over generic terms

## IMPORTANT RULES

- The category value MUST be exactly one of: "Webhook Issues", "Payment Failures", "API Authentication", "Refund & Disputes", "Account & Configuration"
- The severity value MUST be exactly one of: "P1 - Critical", "P2 - High", "P3 - Medium", "P4 - Low"
- When the ticket body is vague or lacks detail, lean toward P3 - Medium severity and lower confidence
- Focus on what the TICKET is about, not tangential mentions. A ticket about a webhook returning 500 is "Webhook Issues" even if it mentions payments."""


def _validate_classification(result: TicketClassification) -> TicketClassification:
    """Safety-net validation. Structured output should comply, but verify."""
    if result.category not in VALID_CATEGORIES:
        raise ValueError(
            f"Invalid category '{result.category}'. Must be one of {VALID_CATEGORIES}"
        )
    if result.severity not in SEVERITY_LEVELS:
        raise ValueError(
            f"Invalid severity '{result.severity}'. Must be one of {SEVERITY_LEVELS}"
        )
    return result


async def classify_ticket(subject: str, body: str) -> TicketClassification:
    """
    Classify a support ticket into category, severity, confidence, and keywords.

    Uses LangChain ChatOpenAI with .with_structured_output(TicketClassification)
    for guaranteed Pydantic-valid responses.

    Args:
        subject: ticket subject line
        body: ticket body text

    Returns:
        TicketClassification with category, severity, confidence, keywords

    Raises:
        ValueError: if LLM returns category/severity not in valid lists
                    (should not happen with structured output, but validated as safety net)
    """
    llm = ChatOpenAI(
        model=settings.llm_model,
        api_key=settings.openai_api_key,
        temperature=0,
    )
    structured_llm = llm.with_structured_output(TicketClassification)

    result = await structured_llm.ainvoke([
        SystemMessage(content=CLASSIFIER_PROMPT),
        HumanMessage(content=f"Subject: {subject}\n\nBody: {body}"),
    ])

    return _validate_classification(result)
