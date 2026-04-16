---
source_url: https://docs.stripe.com/webhooks/handle-irrecoverable-events
source_title: Handle webhook event generation failures
doc_category: webhooks
---

# Handle webhook event generation failures

Learn how to handle webhooks that fail to generate.

In very rare cases, Stripe can fail to generate the `Event` object. In these cases, the event is irrecoverable. Stripe can’t deliver it to your event destinations, nor publish it in the Dashboard or in the [List Events API](https://docs.stripe.com/api/v2/core/events/list.md). Instead, Stripe creates a [v2.core.health.event_generation_failure.resolved](https://docs.stripe.com/api/v2/core/events/event-types.md#v2_event_types-v2.core.health.event_generation_failure.resolved) event to inform you that the `Event` generation failed. This guide explains how the alert works, and what you can do to recover from it.

## Delivery of failed events 

Stripe delivers `v2.core.health.event_generation_failure.resolved` events to both Workbench and to any webhook endpoints you configure to listen for them.

### Workbench

The `v2.core.health.event_generation_failure.resolved` events appear in two places in Workbench:

- The [Events](https://docs.stripe.com/workbench/overview.md#events) tab
- The [Health](https://docs.stripe.com/workbench/health.md) tab

### Webhook endpoints

Follow the [webhook setup guide](https://docs.stripe.com/webhooks.md) to register a webhook endpoint that listens to `v2.core.health.event_generation_failure.resolved` thin events. After you register the correct webhook endpoint, Stripe sends `v2.core.health.event_generation_failure.resolved` events to it.

## How to use the health event

When Stripe fails to generate a webhook event, you can process the generated [thin event](https://docs.stripe.com/event-destinations.md#thin-events) to retrieve the `v2.core.health.event_generation_failure.resolved` object, as shown in the following example.

```json
{
  "alert_id": "halert_61RFBMa6o6H87usts16RFBM10hSQlYfddqcFoEMR6CPY",
  "grouping_key": "_grouping_s8PgTvizbkORV9z5PhaJSvc4dUcAMmfRpEHKm4EeJ1glsQ5XMf",
  "impact": {
    "event_type": "payment_intent.requires_action",
    "related_object_id": "pi_1QA8PKDTvO5jCVb3TVDZP75a",
    "related_object": {
      "id": "pi_1QA8PKDTvO5jCVb3TVDZP75a",
      "type": "payment_intent",
      "url": "https://dashboard.stripe.com/payment_intents/pi_1QA8PKDTvO5jCVb3TVDZP75a"
    },
  },
  "resolved_at": "2025-10-30T16:05:44.000Z",
  "summary": "We have failed to create a notification for your Stripe account.",
}
```

The example event provides the following information about the failure:

- **Failed event**: Stripe failed to generate a `payment_intent.requires_action` event.
- **Relevant object**: The PaymentIntent that Stripe failed to generate the event for is `pi_1QA8PKDTvO5jCVb3TVDZP75a`.
- **Timestamp**: The event failed to generate at `2025-10-30T16:05:44.000Z`.
- **Account type**: The `impact` doesn’t include the `context` property, so the `payment_intent.requires_action` event didn’t occur on a connected account.

If your integration relies on receiving webhooks for the `payment_intent.requires_action` event, this failure makes it out of sync with the Stripe state. To realign your integration after you receive a `v2.core.health.event_generation_failure.resolved` webhook, poll the relevant API (in this case the [Payment Intents API](https://docs.stripe.com/api/payment_intents.md)) to retrieve the related object:

```curl
curl https://api.stripe.com/v1/payment_intents/pi_1QA8PKDTvO5jCVb3TVDZP75a \
  -u "[YOUR_VALUE]:"
```