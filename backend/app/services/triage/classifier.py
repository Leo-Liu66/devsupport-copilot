from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

from app.config import settings
from app.models.ticket import (
    SEVERITY_LEVELS,
    VALID_CATEGORIES,
    TicketClassification,
)

CLASSIFIER_PROMPT = """You are a support ticket classifier for a SaaS product that uses Stripe for payments, webhooks, and billing.

Given a support ticket (subject + body), classify it into exactly one category, one severity level, a confidence score, a list of keywords, and whether more information is needed.

## CATEGORIES (choose exactly one)

1. **Webhook Issues** — Problems with receiving, verifying, or processing Stripe webhook events. Includes: webhook delivery failures, signature verification errors, event ordering, duplicate events, missed events, Connect webhook routing, webhook endpoint configuration.

2. **Payment Failures** — Problems where a payment, charge, or PaymentIntent fails or gets stuck. Includes: card declines (card_declined, insufficient_funds, do_not_honor), 3D Secure / SCA authentication problems, PaymentIntent stuck in requires_action or requires_confirmation, capture failures, currency mismatch errors, test-mode card issues.

3. **API Authentication** — Problems with Stripe API keys, authentication errors, or authorization failures. Includes: "No such API key" errors, 401/403 responses, restricted key permission issues, key rotation, test-vs-live mode key confusion, keys not working in specific environments (Docker, CI).

4. **Refund & Disputes** — Problems with issuing refunds or handling chargebacks/disputes. Includes: refund failures on disputed charges, dispute evidence submission, chargeback outcomes, partial refund display issues, refund processing time questions, dispute deadlines.

5. **Account & Configuration** — Account-level settings, access management, and platform configuration. Includes: team member access/roles, account restrictions/verification, statement descriptors, payout schedules, enabling payment methods (Apple Pay, Google Pay), general integration questions not specific to payments/webhooks/auth/refunds.

## SEVERITY LEVELS

- **P1 - Critical**: Production system is broken or blocked RIGHT NOW with active revenue impact or complete inability to operate. The issue is currently happening in production (not test mode), affects real customers or real payments, and has no workaround. Examples: webhook handler returning 500s on live payment events, signature verification failing on ALL production webhooks, API key suddenly invalid in live production.

- **P2 - High**: The core system or infrastructure is degraded in a way that broadly impacts operations — multiple customers affected, core payment flows broken, or the primary integration failing. The degradation is systemic, not scoped to a single configuration item. Examples: duplicate webhook processing affecting all events, payment failures affecting a subset of customers, API key failing in one environment but not another, dispute deadline approaching, account restricted pending verification. P2 requires broad impact: if the core infrastructure is operational and only a specific event subscription, permission scope, or configuration item is absent, that is P3.

- **P3 - Medium**: A real problem or important question that is not blocking core operations. This includes cases where the overall system is functioning correctly but a specific configuration, subscription, or permission scope is missing or misconfigured — the infrastructure is healthy, the issue is narrow in scope. Examples: a specific webhook event type not arriving while the endpoint and other event types work normally, a restricted API key returning 403 because a single permission scope is missing, how-to questions about production workflows, configuration not working as expected, need information to diagnose further.

- **P4 - Low**: General inquiry, how-to question, feature request, or test-mode-only issue with no production impact. Includes cases where the user is trying to enable or configure a feature that has never been part of their live integration — they are seeking guidance to set it up, not reporting a broken system. Examples: test card not working in test mode, understanding event ordering (informational), enabling a payment method or feature for the first time, general integration guidance.

## CONFIDENCE SCORING

Rate how certain you are about the category and severity classification (informational only):
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
- When the ticket body is vague or lacks detail, lean toward P3 - Medium severity
- Focus on what the TICKET is about, not tangential mentions. A ticket about a webhook returning 500 is "Webhook Issues" even if it mentions payments.

## NEEDS MORE INFO

Ask yourself: does resolving this ticket require investigating a specific event, transaction, or account — and if so, does the ticket provide the identifiers or technical context needed to do that investigation?

Set needs_more_info to TRUE when the ticket itself does not contain enough information to begin diagnosing or responding:
- The ticket describes a problem or situation but lacks the identifiers or details needed to investigate it — e.g. no error code, refund ID, charge ID, event ID, or steps to reproduce.
- A support engineer would have to ask the user at least one follow-up question before taking any meaningful action.

Set needs_more_info to FALSE when the ticket contains enough detail to act on immediately:
- The problem or question is clearly stated with sufficient technical context (error messages, API responses, specific event types, reproduction steps, or a well-formed how-to question).

## OVERRIDE RULE

If the ticket explicitly mentions test mode indicators (test card numbers like 4242424242424242, "test secret key", "test mode", "sk_test_", "pk_test_"), severity MUST be P4 - Low. This overrides all other severity signals."""


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
    Classify a support ticket into category, severity, confidence, keywords, and needs_more_info.

    Uses LangChain ChatOpenAI with .with_structured_output(TicketClassification)
    for guaranteed Pydantic-valid responses.

    Args:
        subject: ticket subject line
        body: ticket body text

    Returns:
        TicketClassification with category, severity, confidence, keywords, needs_more_info

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
