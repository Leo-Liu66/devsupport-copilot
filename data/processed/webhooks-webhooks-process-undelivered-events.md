---
source_url: https://docs.stripe.com/webhooks/process-undelivered-events
source_title: Process undelivered webhook events
doc_category: webhooks
---

# Process undelivered webhook events

Learn how to manually process undelivered webhook events.

If your webhook endpoint temporarily can’t process events, Stripe [automatically resends](https://docs.stripe.com/webhooks.md#automatic-retries) the undelivered events to your endpoint for up to three days, increasing the time for your webhook endpoint to eventually receive and process all events.

This guide explains how to speed up that process by manually processing the undelivered events.

## List webhook events 

Call the [List Events](https://docs.stripe.com/api/events/list.md) API with the following parameters:

- `ending_before`: Specify an event ID that was sent just before the webhook endpoint became unavailable.
- `types`: Specify the list of event types to retrieve.
- `delivery_success`: Set to `false` to retrieve events that were unsuccessfully delivered to at least one of your webhook endpoints.

Stripe only returns events created in the last 30 days.

```curl
curl -G https://api.stripe.com/v1/events \
  -u "[YOUR_VALUE]:" \
  -d ending_before=evt_001 \
  -d "types[]=payment_intent.succeeded" \
  -d "types[]=payment_intent.payment_failed" \
  -d delivery_success=false
```

By default, the response returns up to 10 events. To retrieve all events, use [auto-pagination](https://docs.stripe.com/api/pagination/auto.md) after retrieving the results.

Using `ending_before` with auto-pagination returns events in chronological order. This lets you process events in their created order.

## Process the events 

Process only unsuccessfully processed events according to your own logic to avoid processing a single event multiple times by, for example:

- Inadvertently running the script twice in a row
- Simultaneously running the script while Stripe  automatically resends some of the unprocessed events

Define the following functions that prevent processing duplication:

- `is_processing_or_processed` to check the event’s status in your database.
- `mark_as_processing` to update your database to mark the event as processing.
- `mark_as_processed` to update your database to mark the event as processed.

## Respond to automatic retries 

Stripe still considers your manually processed events as undelivered and continues to automatically retry them.

When your webhook endpoint receives an already processed event, ignore the event and return a successful response to stop future retries.

