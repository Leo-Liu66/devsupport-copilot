---
source_url: https://docs.stripe.com/webhooks/signature
source_title: Resolve webhook signature verification errors
doc_category: webhooks
---

# Resolve webhook signature verification errors

Learn how to fix a common error when listening to webhook events.

When processing webhook events, we recommend securing your endpoint by [verifying](https://docs.stripe.com/webhooks.md#verify-official-libraries) that the event is coming from Stripe. To do this, use the `Stripe-Signature` header and call the `constructEvent()` function with three parameters:

- `requestBody`: The request body string sent by Stripe.
- `signature`: The Stripe-Signature header in the request sent by Stripe.
- `endpointSecret`: The secret associated with your endpoint.

This function might look like this:

If you get the following `Webhook signature verification failed` error, at least one of the three parameters you passed to the `constructEvent()` function is incorrect.

```
Webhook signature verification failed. Err: No signatures found matching the expected signature for payload.
```

## Check the endpoint secret

The most common error is using the wrong endpoint secret. If you’re using a webhook endpoint created in the [Dashboard](https://dashboard.stripe.com/test/webhooks), open the endpoint in the Dashboard and click the **Reveal secret** link near the top of the page to view the secret. If you’re using the Stripe CLI, the secret is printed in the Terminal when you run the `stripe listen` command.

In both cases, the secret starts with a `whsec_` prefix, but the secret itself is different. Don’t verify signatures on events forwarded by the CLI using the secret from a Dashboard-managed endpoint, or the other way around. Finally, print the `endpointSecret` used in your code, and make sure that it matches the one you found above.

## Check the signature

Print the `signature` parameter, and confirm that it looks similar to this:

```
t=xxx,v1=yyy,v0=zzz
```

If not, check if you have an issue in your code when trying to extract the signature from the header.