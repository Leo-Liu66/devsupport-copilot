---
source_url: https://docs.stripe.com/error-handling
source_title: Error handling
doc_category: api
---

# Error handling

Catch and respond to declines, invalid data, network problems, and more.

Stripe offers many kinds of errors. They can reflect external events, like declined payments and network interruptions, or code problems, like invalid API calls.

## Parse error data

When Stripe returns an error to your API request, you receive details about the error that help you understand how to apply the handling suggestions in this guide. These details also help you provide important information to Stripe support, if needed.

| Property          | Description                                                                                                                                                                                                                         |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `code`            | The error code.                                                                                                                                                                                                                     |
| `doc_url`         | A link to the Stripe documentation for the specific error code.                                                                                                                                                                     |
| `message`         | A description of the reason for the error.                                                                                                                                                                                          |
| `param`           | The parameter of the request that caused the error.                                                                                                                                                                                 |
| `request_log_url` | A link to the Stripe Dashboard where you can see detailed logs about the originating request and the error.                                                                                                                         |
| Request ID        | A unique identifier for the originating request that errored. The error response header includes this value (string beginning with `req`), but you can specify a print in your request, as shown in the code samples in this guide. |
| `type`            | A reference to the error category this error belongs to.                                                                                                                                                                            |

To handle errors, use some or all of the techniques in the table below. No matter what technique you use, you can follow up with our [recommended responses for each error type](https://docs.stripe.com/error-handling.md#error-types).

| Technique                                                                                                 | Purpose                                                | When needed |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ----------- |
| [Catch exceptions](https://docs.stripe.com/error-handling.md#catch-exceptions)                            | Recover when an API call can’t continue                | Always      |
| [Monitor webhooks](https://docs.stripe.com/error-handling.md#monitor-webhooks)                            | React to notifications from Stripe                     | Sometimes   |
| [Get stored information about failures](https://docs.stripe.com/error-handling.md#use-stored-information) | Investigate past problems and support other techniques | Sometimes   |

## Catch exceptions 

With this library, you don’t need to check for non-200 HTTP responses. The library translates them as exceptions.

In the rare event you need HTTP details, see [Low-level exception handling](https://docs.stripe.com/error-low-level.md) and the [Error](https://docs.stripe.com/api/errors.md) object.

If an immediate problem prevents an API call from continuing, the Stripe Python library raises an exception. It’s a best practice to catch and handle exceptions.

To catch an exception, use Python’s `try`/`except` syntax. Catch `stripe.StripeError` or its subclasses to handle Stripe-specific exceptions only. Each subclass represents a different kind of exception. When you catch an exception, you can [use its class to choose a response](https://docs.stripe.com/error-handling.md#error-types).

| Technique                                                                                                 | Purpose                                                | When needed |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ----------- |
| [Catch exceptions](https://docs.stripe.com/error-handling.md#catch-exceptions)                            | Recover when an API call can’t continue                | Always      |
| [Monitor webhooks](https://docs.stripe.com/error-handling.md#monitor-webhooks)                            | React to notifications from Stripe                     | Sometimes   |
| [Get stored information about failures](https://docs.stripe.com/error-handling.md#use-stored-information) | Investigate past problems and support other techniques | Sometimes   |

## Monitor webhooks

Stripe notifies you about many kinds of problems using *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests). This includes problems that don’t follow immediately after an API call. For example:

- You lose a dispute.
- A recurring payment fails after months of success.
- Your frontend *confirms* (Confirming a PaymentIntent indicates that the customer intends to pay with the current or provided payment method. Upon confirmation, the PaymentIntent attempts to initiate a payment) a payment, but goes offline before finding out the payment fails. (The backend still receives webhook notification, even though it wasn’t the one to make the API call.)

You don’t need to handle every webhook event type. In fact, some integrations don’t handle any.

In your webhook handler, start with the basic steps from the [webhook builder](https://docs.stripe.com/webhooks/quickstart.md): get an event object and use the event type to find out what happened. Then, if the event type indicates an error, follow these extra steps:

1. Access [event.data.object](https://docs.stripe.com/api/events/object.md#event_object-data-object) to retrieve the affected object.
1. [Use stored information](https://docs.stripe.com/error-handling.md#use-stored-information) on the affected object to gain context, including an error object.
1. [Use its type to choose a response](https://docs.stripe.com/error-handling.md#error-types).

1. Access [event[‘data’][‘object’]](https://docs.stripe.com/api/events/object.md#event_object-data-object) to retrieve the affected object.
1. [Use stored information](https://docs.stripe.com/error-handling.md#use-stored-information) on the affected object to gain context, including an error object.
1. [Use its type to choose a response](https://docs.stripe.com/error-handling.md#error-types).

1. Access [event->data->object](https://docs.stripe.com/api/events/object.md#event_object-data-object) to retrieve the affected object.
1. [Use stored information](https://docs.stripe.com/error-handling.md#use-stored-information) on the affected object to gain context, including an error object.
1. [Use its type to choose a response](https://docs.stripe.com/error-handling.md#error-types).

1. Get the affected object using an `EventDataObjectDeserializer` and casting its output to the appropriate type.
1. [Use stored information](https://docs.stripe.com/error-handling.md#use-stored-information) on the affected object to gain context, including an error object.
1. [Use its type to choose a response](https://docs.stripe.com/error-handling.md#error-types).

1. Access [event.data.object](https://docs.stripe.com/api/events/object.md#event_object-data-object) to retrieve the affected object.
1. [Use stored information](https://docs.stripe.com/error-handling.md#use-stored-information) on the affected object to gain context, including an error object.
1. [Use its type to choose a response](https://docs.stripe.com/error-handling.md#error-types).

1. Get the affected object by unmarshalling data from `event.Data.Raw`.
1. [Use stored information](https://docs.stripe.com/error-handling.md#use-stored-information) on the affected object to gain context, including an error object.
1. [Use its type to choose a response](https://docs.stripe.com/error-handling.md#error-types).

1. Get the affected object by casting [stripeEvent.Data.Object](https://docs.stripe.com/api/events/object.md#event_object-data-object) to the appropriate type.
1. [Use stored information](https://docs.stripe.com/error-handling.md#use-stored-information) on the affected object to gain context, including an error object.
1. [Use its type to choose a response](https://docs.stripe.com/error-handling.md#error-types).

To test how your integration responds to webhook events, you can [trigger webhook events locally](https://docs.stripe.com/webhooks.md#test-webhook). After completing the setup steps at that link, trigger a failed payment to see the resulting error message.

```bash
stripe trigger payment_intent.payment_failed
```

```bash
A payment error occurred: Your card was declined.
```

## Get stored information about failures 

Many objects store information about failures. That means that if something already went wrong, you can retrieve the object and examine it to learn more. In many cases, stored information is in the form of an error object, and you can [use its type to choose a response](https://docs.stripe.com/error-handling.md#error-types).

For instance:

1. Retrieve a specific payment intent.
1. Check if it experienced a payment error by determining if [last_payment_error](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-last_payment_error) is empty.
1. If it did, log the error, including its type and the affected object.

Here are common objects that store information about failures.

| Object                                                           | Attribute                 | Values                                                                                              |
| ---------------------------------------------------------------- | ------------------------- | --------------------------------------------------------------------------------------------------- |
| [Payment Intent](https://docs.stripe.com/api/payment_intents.md) | `last_payment_error`      | [An error object](https://docs.stripe.com/error-handling.md#work-with-error-objects)                |
| [Setup Intent](https://docs.stripe.com/api/setup_intents.md)     | `last_setup_error`        | [An error object](https://docs.stripe.com/error-handling.md#work-with-error-objects)                |
| [Invoice](https://docs.stripe.com/api/invoices.md)               | `last_finalization_error` | [An error object](https://docs.stripe.com/error-handling.md#work-with-error-objects)                |
| [Setup Attempt](https://docs.stripe.com/api/setup_attempts.md)   | `setup_error`             | [An error object](https://docs.stripe.com/error-handling.md#work-with-error-objects)                |
| [Payout](https://docs.stripe.com/api/payouts.md)                 | `failure_code`            | [A payout failure code](https://docs.stripe.com/api/payouts/failures.md)                            |
| [Refund](https://docs.stripe.com/api/refunds.md)                 | `failure_reason`          | [A refund failure code](https://docs.stripe.com/api/refunds/object.md#refund_object-failure_reason) |

To test code that uses stored information about failures, you often need to simulate failed transactions. You can often do this using [test cards](https://docs.stripe.com/testing.md) or test bank numbers. For example:

- [Simulate a declined payment](https://docs.stripe.com/testing.md#declined-payments), for creating failed Charges, PaymentIntents, SetupIntents, and so on.
- [Simulate a failed payout](https://docs.stripe.com/connect/testing.md#account-numbers).
- [Simulate a failed refund](https://docs.stripe.com/testing.md#refunds).

## Invalid request errors  

|  |
|  |
| **Type**      | `Stripe::InvalidRequestError`                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Problem**   | You made an API call with the wrong parameters, in the wrong state, or in an invalid way.                                                                                                                                                                                                                                                                                                                                                     |
| **Solutions** | In most cases, the problem is with the request itself. Either its parameters are invalid or it can’t be carried out in your integration’s current state.
  - Consult the [error code documentation](https://docs.stripe.com/error-codes.md) for details on the problem.
  - For convenience, you can follow the link at  for documentation about the error code.
  - If the error involves a specific parameter, use  to determine which one. |

## Connection errors  

|  |
|  |
| **Type**      | `Stripe::APIConnectionError`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Problem**   | There was a network problem between your server and Stripe.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Solutions** | Treat the result of the API call as indeterminate. That is, don’t assume that it succeeded or that it failed.

  To find out if it succeeded, you can:

  - Retrieve the relevant object from Stripe and check its status.
  - Listen for webhook notification that the operation succeeded or failed.

  To help recover from connection errors, you can:

  - When creating or updating an object, use an [idempotency key](https://docs.stripe.com/api/idempotent_requests.md). Then, if a connection error occurs, you can safely repeat the request without risk of creating a second object or performing the update twice. Repeat the request with the same idempotency key until you receive a clear success or failure. For advanced advice on this strategy, see [Low-level error handling](https://docs.stripe.com/error-low-level.md#idempotency).
  - Turn on [automatic retries](https://github.com/stripe/stripe-java?tab=readme-ov-file#configuring-automatic-retries). Then, Stripe generates idempotency keys for you, and repeats requests for you when it’s safe to do so.

  This error can mask others. It’s possible that when the connection error resolves, some other error becomes apparent. Check for errors in all of these solutions just as you would in the original request. |

## API errors  

|  |
|  |
| **Type**      | `Stripe::APIError`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Problem**   | Something went wrong on Stripe’s end. (These are rare.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Solutions** | Treat the result of the API call as indeterminate. That is, don’t assume that it succeeded or that it failed.

  Rely on *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) for information about the outcome. Whenever possible, Stripe fires webhooks for any new objects we create as we solve a problem.

  To set your integration up for maximum robustness in unusual situations, see [this advanced discussion of server errors.](https://docs.stripe.com/error-low-level.md#server-errors) |

## Authentication errors  

|  |
|  |
| **Type**      | `Stripe::AuthenticationError`                                                                                                                                                     |
| **Problem**   | Stripe can’t authenticate you with the information provided.                                                                                                                      |
| **Solutions** | - Use the correct [API key](https://docs.stripe.com/keys.md).
  - Make sure you aren’t using a key that you [“rotated” or revoked](https://docs.stripe.com/keys.md#rolling-keys). |

## Idempotency errors  

|  |
|  |
| **Type**      | `Stripe::IdempotencyError`                                                                                                                                             |
| **Problem**   | You used an [idempotency key](https://docs.stripe.com/api/idempotent_requests.md) for something unexpected, like replaying a request but passing different parameters. |
| **Solutions** | - After you use an idempotency key, only reuse it for identical API calls.
  - Use idempotency keys under the limit of 255 characters.                                 |

## Permission errors  

|  |
|  |
| **Type**      | `Stripe::PermissionError`                                                                                                                                                                                                                                                                                                |
| **Problem**   | The API key used for this request doesn’t have the necessary permissions.                                                                                                                                                                                                                                                |
| **Solutions** | - Make sure you aren’t using a [restricted API key](https://docs.stripe.com/keys-best-practices.md#limit-access) for a service it doesn’t have access to.
  - Don’t perform actions in the Dashboard while logged in as a [user role](https://docs.stripe.com/get-started/account/teams/roles.md) that lacks permission. |

## Rate limit errors  

|  |
|  |
| **Type**      | `Stripe::RateLimitError`                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Problem**   | You made too many API calls in too short a time.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Solutions** | - If a single API call triggers this error, wait and try it again.
  - To handle rate-limiting automatically, retry the API call after a delay, and increase the delay exponentially if the error continues. See the documentation on [rate limits](https://docs.stripe.com/rate-limits.md) for further advice.
  - If you anticipate a large increase in traffic and want to request an increased rate limit, [contact support](https://support.stripe.com/) in advance. |

## Signature verification errors  

|  |
|  |
| **Type**      | `Stripe::SignatureVerificationError`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Problem**   | You’re using *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) [signature verification](https://docs.stripe.com/webhooks.md#verify-events) and couldn’t verify that a webhook event is authentic.                                                                                                                                                                                                                                                                                                                                                                                   |
| **Solutions** | This error can occur when your integration is working correctly. If you use webhook signature verification and a third party attempts to send you a fake or malicious webhook, then verification fails and this error is the result. Catch it and respond with a `400 Bad Request` status code.

  If you receive this error when you shouldn’t—for instance, with webhooks that you know originate with Stripe—then see the documentation on [checking webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) for further advice. In particular, make sure you’re using the correct endpoint secret. This is different from your API key. |

In the Stripe Python library, error objects belong to `stripe.StripeError` and its subclasses. Use the documentation for each class for advice about how to respond.

| Name                         | Class                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Payment error                | [stripe.CardError](https://docs.stripe.com/error-handling.md#payment-errors)                                 | An error occurred during a payment, involving one of these situations:
  - [Payment blocked for suspected fraud](https://docs.stripe.com/error-handling.md#payment-blocked)
  - [Payment declined by the issuer](https://docs.stripe.com/error-handling.md#payment-declined).
  - [Other payment errors](https://docs.stripe.com/error-handling.md#other-payment-errors). |
| Invalid request error        | [stripe.InvalidRequestError](https://docs.stripe.com/error-handling.md#invalid-request-errors)               | You made an API call with the wrong parameters, in the wrong state, or in an invalid way.                                                                                                                                                                                                                                                                                 |
| Connection error             | [stripe.APIConnectionError](https://docs.stripe.com/error-handling.md#connection-errors)                     | There was a network problem between your server and Stripe.                                                                                                                                                                                                                                                                                                               |
| API error                    | [stripe.APIError](https://docs.stripe.com/error-handling.md#api-errors)                                      | Something went wrong on Stripe’s end. (These are rare.)                                                                                                                                                                                                                                                                                                                   |
| Authentication error         | [stripe.AuthenticationError](https://docs.stripe.com/error-handling.md#authentication-errors)                | Stripe can’t authenticate you with the information provided.                                                                                                                                                                                                                                                                                                              |
| Idempotency error            | [stripe.IdempotencyError](https://docs.stripe.com/error-handling.md#idempotency-errors)                      | You used an [idempotency key](https://docs.stripe.com/api/idempotent_requests.md) for something unexpected, like replaying a request but passing different parameters.                                                                                                                                                                                                    |
| Permission error             | [stripe.PermissionError](https://docs.stripe.com/error-handling.md#permission-errors)                        | The API key used for this request doesn’t have the necessary permissions.                                                                                                                                                                                                                                                                                                 |
| Rate limit error             | [stripe.RateLimitError](https://docs.stripe.com/error-handling.md#rate-limit-errors)                         | You made too many API calls in too short a time.                                                                                                                                                                                                                                                                                                                          |
| Signature verification error | [stripe.SignatureVerificationError](https://docs.stripe.com/error-handling.md#signature-verification-errors) | You’re using *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) [signature verification](https://docs.stripe.com/webhooks.md#verify-events) and couldn’t verify that a webhook event is authentic.                                                                                                  |

## Payment errors 

Everything in this section also applies to non-card payments. For historical reasons, payment errors have the type [stripe.CardError](https://docs.stripe.com/error-handling.md#card-error). But in fact, they can represent a problem with any payment, regardless of the payment method.

Payment errors—sometimes called “card errors” for historical reasons—cover a wide range of common problems. They come in three categories:

- [Payment blocked for suspected fraud](https://docs.stripe.com/error-handling.md#payment-blocked)
- [Payment declined by the issuer](https://docs.stripe.com/error-handling.md#payment-declined)
- [Other payment errors](https://docs.stripe.com/error-handling.md#other-payment-errors)

To distinguish these categories or get more information about how to respond, consult the [error code](https://docs.stripe.com/error-codes.md), [decline code](https://docs.stripe.com/declines/codes.md), and [charge outcome](https://docs.stripe.com/api/charges/object.md#charge_object-outcome).

(To find the charge outcome from an error object, first get the [Payment Intent that’s involved](https://docs.stripe.com/api/errors.md#errors-payment_intent) and the [latest Charge it created](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge). See the example below for a demonstration.)

Users on API version [2022-08-01](https://docs.stripe.com/upgrades.md#2022-08-01) or older:

(To find the charge outcome from an error object, first get the [Payment Intent that’s involved](https://docs.stripe.com/api/errors.md#errors-payment_intent) and the [latest Charge it created](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-charges-data). See the example below for a demonstration.)

You can trigger some common kinds of payment error with test cards. Consult these lists for options:

- [Simulating payments blocked for fraud risk](https://docs.stripe.com/testing.md#fraud-prevention)
- [Simulating declined payments and other card errors](https://docs.stripe.com/testing.md#declined-payments)

The test code below demonstrates a few possibilities.

#### Error to trigger - Blocked for suspected fraud

```
Payment blocked for suspected fraud.
```

#### Error to trigger - Declined by the issuer

```
Payment declined by the issuer.
```

#### Error to trigger - Card expired

```
Card expired.
```

#### Error to trigger - Other card error

```
Other payment error.
```

### Payment blocked for suspected fraud  

|  |
|  |
| **Type**                                                                                                                                                                                                                                       | `stripe.CardError`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Codes**                                                                                                                                                                                                                                      | ```python
  charge = stripe.Charge.retrieve(e.error.payment_intent.latest_charge)
  charge.outcome.type == 'blocked'
  ```

  Users on API version [2022-08-01](https://docs.stripe.com/upgrades.md#2022-08-01) or older:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **Codes** | `e.error.payment_intent.charges.data[0].outcome.type == 'blocked'` |
| **Problem**                                                                                                                                                                                                                                    |
| Stripe’s fraud prevention system, *Radar* (Radar for Fraud Teams helps you fine-tune how Radar operates, get fraud insights on suspicious charges, and assess your fraud management performance from a unified dashboard), blocked the payment |
| **Solutions**                                                                                                                                                                                                                                  | This error can occur when your integration is working correctly. Catch it and prompt the customer for a different payment method.

  To block fewer legitimate payments, try these:

  - [Optimize your Radar integration](https://docs.stripe.com/radar/optimize-fraud-signals.md) to collect more detailed information.
  - Use [Payment Links](https://docs.stripe.com/payment-links.md), [Checkout](https://docs.stripe.com/payments/checkout.md), or [Stripe Elements](https://docs.stripe.com/payments/elements.md) for prebuilt optimized form elements.

  *Radar for Fraud Teams* (Radar for Fraud Teams helps you fine-tune how Radar operates, get fraud insights on suspicious charges, and assess your fraud management performance from a unified dashboard) customers have these additional options:

  - To exempt a specific payment, add it to your allowlist. (Radar for Fraud Teams)
  - To change your risk tolerance, adjust your [risk settings](https://docs.stripe.com/radar/risk-settings.md). (Radar for Fraud Teams)
  - To change the criteria for blocking a payment, use [custom rules](https://docs.stripe.com/radar/rules.md). (Radar for Fraud Teams)

  You can test your integration’s settings with [test cards that simulate fraud](https://docs.stripe.com/radar/testing.md). If you have custom Radar rules, follow the testing advice in the [Radar documentation](https://docs.stripe.com/radar/testing.md). |

### Payment declined by the issuer  

|  |
|  |
| **Type**      | `stripe.CardError`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| **Codes**     | `e.code == "card_declined"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Problem**   | The card issuer declined the payment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Solutions** | This error can occur when your integration is working correctly. It reflects an action by the issuer, and that action might be legitimate. Use the decline code to determine what next steps are appropriate. See the [documentation on decline codes](https://docs.stripe.com/declines/codes.md) for appropriate responses to each code.

  You can also:

  - [Follow recommendations to reduce issuer declines](https://docs.stripe.com/declines/card.md#reducing-bank-declines).
  - Use [Payment Links](https://docs.stripe.com/payment-links.md), [Checkout](https://docs.stripe.com/payments/checkout.md), or [Stripe Elements](https://docs.stripe.com/payments/elements.md) for prebuilt form elements that implement those recommendations.

  Test how your integration handles declines with [test cards that simulate successful and declined payments](https://docs.stripe.com/radar/testing.md). |

### Other payment errors  

|  |
|  |
| **Type**      | `stripe.CardError`                                                                                                                                                                                                                                       |
| **Problem**   | Another payment error occurred.                                                                                                                                                                                                                          |
| **Solutions** | This error can occur when your integration is working correctly. Use the error code to determine what next steps are appropriate. See the [documentation on error codes](https://docs.stripe.com/error-codes.md) for appropriate responses to each code. |
