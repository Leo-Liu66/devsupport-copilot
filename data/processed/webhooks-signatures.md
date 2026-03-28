---
source_url: https://docs.stripe.com/webhooks/signatures
source_title: Webhook signature verification
doc_category: webhooks
---

# Webhook Signature Verification

Verify that webhook events originate from Stripe before acting on them.

## Why Verify Signatures

Without verification, an attacker could send fake webhook events to your endpoint to trigger unauthorized actions. Always verify that webhook events originate from Stripe before acting on them.

Use both protections:
- **IP allowlisting**: Stripe sends webhook events from a set list of IP addresses.
- **Signature verification**: Stripe signs every webhook event by including a signature in the `Stripe-Signature` header.

## The Stripe-Signature Header

The `Stripe-Signature` header included in each signed event contains a timestamp and one or more signatures:

```
Stripe-Signature: t=1492774577,v1=5257a869e7ecebeda32affa62cdca3fa51cad7e77a0e56ff536d0ce8e108d8bd
```

Stripe generates signatures using HMAC with SHA-256. The only valid live scheme is `v1`.

## Verify with Official Libraries (Recommended)

```ruby
endpoint_secret = 'whsec_...'

post '/webhook' do
  payload = request.body.read
  sig_header = request.env['HTTP_STRIPE_SIGNATURE']

  begin
    event = Stripe::Webhook.construct_event(payload, sig_header, endpoint_secret)
  rescue JSON::ParserError => e
    status 400
    return
  rescue Stripe::SignatureVerificationError => e
    puts "Webhook signature verification failed: #{e.message}"
    status 400
    return
  end

  # Handle the event
  status 200
end
```

**Important:** Stripe requires the raw body of the request. If you're using a framework, make sure it doesn't manipulate the raw body.

## Manual Verification Steps

1. **Extract timestamp and signatures** from the header by splitting on `,` then `=`.
2. **Prepare the signed_payload** string: `timestamp + "." + request_body`.
3. **Compute expected signature** using HMAC-SHA256 with your endpoint secret.
4. **Compare signatures** using constant-time comparison to prevent timing attacks.

## Retrieve Your Endpoint's Secret

In the Dashboard, go to **Workbench → Webhooks**, select your endpoint, and click **Click to reveal**.

## Preventing Replay Attacks

Stripe includes a timestamp in the `Stripe-Signature` header. If the signature is valid but the timestamp is too old, reject the payload. The default tolerance in official libraries is 5 minutes.

**Important:** Don't use a tolerance value of `0` — this disables the recency check entirely.

## Roll Endpoint Signing Secrets Periodically

Roll secrets when you suspect a compromise or on a regular schedule. During rollover, Stripe generates one signature per active secret for up to 24 hours.
