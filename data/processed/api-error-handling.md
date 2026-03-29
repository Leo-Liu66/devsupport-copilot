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

If an immediate problem prevents an API call from continuing, the Stripe Ruby library raises an exception. It’s a best practice to catch and handle exceptions.

To catch an exception, use Ruby’s `rescue` keyword. Catch `Stripe::StripeError` or its subclasses to handle Stripe-specific exceptions only. Each subclass represents a different kind of exception. When you catch an exception, you can [use its class to choose a response](https://docs.stripe.com/error-handling.md#error-types).

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

## Catch exceptions 

With this library, you don’t need to check for non-200 HTTP responses. The library translates them as exceptions.

In the rare event you need HTTP details, see [Low-level exception handling](https://docs.stripe.com/error-low-level.md) and the [Error](https://docs.stripe.com/api/errors.md) object.

If an immediate problem prevents an API call from continuing, the Stripe PHP library raises an exception. It’s a best practice to catch and handle exceptions.

To catch an exception, use PHP’s `try`/`catch` syntax. Stripe provides several exception classes you can catch. Each one represents a different kind of error. When you catch an exception, you can [use its class to choose a response](https://docs.stripe.com/error-handling.md#error-types).

| Technique                                                                                                 | Purpose                                                | When needed |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ----------- |
| [Catch exceptions](https://docs.stripe.com/error-handling.md#catch-exceptions)                            | Recover when an API call can’t continue                | Always      |
| [Monitor webhooks](https://docs.stripe.com/error-handling.md#monitor-webhooks)                            | React to notifications from Stripe                     | Sometimes   |
| [Get stored information about failures](https://docs.stripe.com/error-handling.md#use-stored-information) | Investigate past problems and support other techniques | Sometimes   |

## Catch exceptions 

With this library, you don’t need to check for non-200 HTTP responses. The library translates them as exceptions.

In the rare event you need HTTP details, see [Low-level exception handling](https://docs.stripe.com/error-low-level.md) and the [Error](https://docs.stripe.com/api/errors.md) object.

If an immediate problem prevents an API call from continuing, the Stripe Java library raises an exception. It’s a best practice to catch and handle exceptions.

To catch an exception, use Java’s `try`/`catch` syntax. Catch `StripeException` or its subclasses to handle Stripe-specific exceptions only. Each subclass represents a different kind of exception. When you catch an exception, you can [use its class to choose a response](https://docs.stripe.com/error-handling.md#error-types).

| Technique                                                                                                 | Purpose                                                | When needed |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ----------- |
| [Catch exceptions](https://docs.stripe.com/error-handling.md#catch-exceptions)                            | Recover when an API call can’t continue                | Always      |
| [Monitor webhooks](https://docs.stripe.com/error-handling.md#monitor-webhooks)                            | React to notifications from Stripe                     | Sometimes   |
| [Get stored information about failures](https://docs.stripe.com/error-handling.md#use-stored-information) | Investigate past problems and support other techniques | Sometimes   |

## Catch exceptions 

With this library, you don’t need to check for non-200 HTTP responses. The library translates them as exceptions.

In the rare event you need HTTP details, see [Low-level exception handling](https://docs.stripe.com/error-low-level.md) and the [Error](https://docs.stripe.com/api/errors.md) object.

If an immediate problem prevents an API call from continuing, the Stripe Node.js library can raise an exception. It’s a best practice to catch and handle exceptions. To enable exception raising and catch the exception, do the following:

- If you make the API call in a function, precede the function definition with the `async` keyword.
- Precede the API call itself with the `await` keyword.
- Wrap the API call in a `try`/`catch` block.

When you catch an exception, you can [use its type attribute to choose a response](https://docs.stripe.com/error-handling.md#error-types).

| Technique                                                                                                 | Purpose                                                | When needed |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ----------- |
| [Use error values](https://docs.stripe.com/error-handling.md#catch-exceptions)                            | Recover when an API call can’t continue                | Always      |
| [Monitor webhooks](https://docs.stripe.com/error-handling.md#monitor-webhooks)                            | React to notifications from Stripe                     | Sometimes   |
| [Get stored information about failures](https://docs.stripe.com/error-handling.md#use-stored-information) | Investigate past problems and support other techniques | Sometimes   |

## Use error values 

With this library, you don’t need to check for non-200 HTTP responses. The library translates them to error values.

In the rare event you need HTTP details, see [Low-level exception handling](https://docs.stripe.com/error-low-level.md) and the [Error](https://docs.stripe.com/api/errors.md) object.

API calls in the Stripe Go library return both a result value and an error value. Use multiple assignment to capture both. If the error value isn’t `nil`, it means an immediate problem prevented the API call from continuing.

If the error value is related to Stripe, you can cast it to a `stripe.Error` object, which has fields describing the problem. [Use the Type field to choose a response](https://docs.stripe.com/error-handling.md#error-types). In some cases, you can coerce the `Err` property to a more specific error type with additional information.

| Technique                                                                                                 | Purpose                                                | When needed |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ----------- |
| [Catch exceptions](https://docs.stripe.com/error-handling.md#catch-exceptions)                            | Recover when an API call can’t continue                | Always      |
| [Monitor webhooks](https://docs.stripe.com/error-handling.md#monitor-webhooks)                            | React to notifications from Stripe                     | Sometimes   |
| [Get stored information about failures](https://docs.stripe.com/error-handling.md#use-stored-information) | Investigate past problems and support other techniques | Sometimes   |

## Catch exceptions 

With this library, you don’t need to check for non-200 HTTP responses. The library translates them to exceptions.

In the rare event you need HTTP details, see [Low-level exception handling](https://docs.stripe.com/error-low-level.md) and the [Error](https://docs.stripe.com/api/errors.md) object.

If an immediate problem prevents an API call from continuing, the Stripe .NET library raises an exception. It’s a best practice to catch and handle exceptions.

To catch an exception, use .NET’s `try`/`catch` syntax. Catch a `StripeException`, then [use its Type attribute to choose a response](https://docs.stripe.com/error-handling.md#error-types).

#### Ruby

```ruby
require 'stripe'

Stripe.api_key = '<<YOUR_SECRET_KEY>>'

def example_function(params)
  begin
    Stripe::PaymentIntent.create(params)
  rescue Stripe::CardError => e
    puts "A payment error occurred: #{e.error.message} (request id: #{e.request_id})"
  rescue Stripe::InvalidRequestError => e
    puts "An invalid request occurred. (request id: #{e.request_id})"
  # Add additional catch cases for other Stripe exception types as needed.
  # See all exception types at https://docs.stripe.com/api/errors/handling?lang=ruby
  rescue Stripe::StripeError => e
    # All other Stripe errors
    puts "Status: #{e.http_status}, Code: #{e.code}, Message: #{e.message}, Request ID: #{e.request_id}"
  else
    puts "No error."
  end
end
```

After setting up exception handling, test it on a variety of data, including [test cards](https://docs.stripe.com/testing.md), to simulate different payment outcomes.

#### Error to trigger - Invalid request

#### Ruby

```ruby
example_function(
  # The required parameter currency is missing,
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_visa', # This is a test card that always succeeds when you use it in test environments. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
An invalid request occurred.
```

#### Error to trigger - Card error

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_chargeDeclinedFraudulent', # This is a test card that always produces a fraudulent charge payment error. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
A payment error occurred: Your card was declined.
```

#### Error to trigger - No error

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_visa', # This is a test card that always succeeds when you use it in test environments. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
No error.
```

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

#### Ruby

```ruby
require 'stripe'
require 'sinatra'
post '/webhook' do
  payload = request.body.read
  data = JSON.parse(payload, symbolize_names: true)

  # Get the event object
  event = Stripe::Event.construct_from(data)

  # Use the event type to find out what happened
  case event.type
  when 'payment_intent.payment_failed'

    # Get the object affected
    payment_intent = event.data.object

    # Use stored information to get an error object
    e = payment_intent.last_payment_error

    # Use its type to choose a response
    case e.type
    when 'card_error'
      puts "A payment error occurred: #{e.message}"
    when 'invalid_request'
      puts "An invalid request occurred."
    else
      puts "Another problem occurred, maybe unrelated to Stripe."
    end
  end

  content_type 'application/json'
  {
    status: 'success'
  }.to_json
end
```

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

#### Ruby

```ruby
require 'stripe'
Stripe.api_key = '<<YOUR_SECRET_KEY>>'

payment_intent = Stripe::PaymentIntent.retrieve({{PAYMENT_INTENT_ID}})
e = payment_intent.last_payment_error
if !e.nil?
  puts "PaymentIntent #{payment_intent.id} experienced a #{e.type}."
end
```

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

## Types of error and responses 

In the Stripe Ruby library, error objects belong to `stripe.error.StripeError` and its subclasses. Use the documentation for each class for advice on responding.

| Name                         | Class                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Payment error                | [Stripe::CardError](https://docs.stripe.com/error-handling.md#payment-errors)                                 | An error occurred during a payment, involving one of these situations:
  - [Payment blocked for suspected fraud](https://docs.stripe.com/error-handling.md#payment-blocked)
  - [Payment declined by the issuer](https://docs.stripe.com/error-handling.md#payment-declined).
  - [Other payment errors](https://docs.stripe.com/error-handling.md#other-payment-errors). |
| Invalid request error        | [Stripe::InvalidRequestError](https://docs.stripe.com/error-handling.md#invalid-request-errors)               | You made an API call with the wrong parameters, in the wrong state, or in an invalid way.                                                                                                                                                                                                                                                                                 |
| Connection error             | [Stripe::APIConnectionError](https://docs.stripe.com/error-handling.md#connection-errors)                     | There was a network problem between your server and Stripe.                                                                                                                                                                                                                                                                                                               |
| API error                    | [Stripe::APIError](https://docs.stripe.com/error-handling.md#api-errors)                                      | Something went wrong on Stripe’s end. (These are rare.)                                                                                                                                                                                                                                                                                                                   |
| Authentication error         | [Stripe::AuthenticationError](https://docs.stripe.com/error-handling.md#authentication-errors)                | Stripe can’t authenticate you with the information provided.                                                                                                                                                                                                                                                                                                              |
| Idempotency error            | [Stripe::IdempotencyError](https://docs.stripe.com/error-handling.md#idempotency-errors)                      | You used an [idempotency key](https://docs.stripe.com/api/idempotent_requests.md) for something unexpected, like replaying a request but passing different parameters.                                                                                                                                                                                                    |
| Permission error             | [Stripe::PermissionError](https://docs.stripe.com/error-handling.md#permission-errors)                        | The API key used for this request doesn’t have the necessary permissions.                                                                                                                                                                                                                                                                                                 |
| Rate limit error             | [Stripe::RateLimitError](https://docs.stripe.com/error-handling.md#rate-limit-errors)                         | You made too many API calls in too short a time.                                                                                                                                                                                                                                                                                                                          |
| Signature verification error | [Stripe::SignatureVerificationError](https://docs.stripe.com/error-handling.md#signature-verification-errors) | You’re using *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) [signature verification](https://docs.stripe.com/webhooks.md#verify-events) and couldn’t verify that a webhook event is authentic.                                                                                                  |

## Payment errors 

Everything in this section also applies to non-card payments. For historical reasons, payment errors have the type [Stripe::CardError](https://docs.stripe.com/error-handling.md#card-error). But in fact, they can represent a problem with any payment, regardless of the payment method.

Payment errors—sometimes called “card errors” for historical reasons—cover a wide range of common problems. They come in three categories:

- [Payment blocked for suspected fraud](https://docs.stripe.com/error-handling.md#payment-blocked)
- [Payment declined by the issuer](https://docs.stripe.com/error-handling.md#payment-declined)
- [Other payment errors](https://docs.stripe.com/error-handling.md#other-payment-errors)

To distinguish these categories or get more information about how to respond, consult the [error code](https://docs.stripe.com/error-codes.md), [decline code](https://docs.stripe.com/declines/codes.md), and [charge outcome](https://docs.stripe.com/api/charges/object.md#charge_object-outcome).

(To find the charge outcome from an error object, first get the [Payment Intent that’s involved](https://docs.stripe.com/api/errors.md#errors-payment_intent) and the [latest Charge it created](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge). See the example below for a demonstration.)

#### Ruby

```ruby
require 'stripe'
Stripe.api_key = '<<YOUR_SECRET_KEY>>'

def example_function(params)
  begin
    Stripe::PaymentIntent.create(params)
  rescue Stripe::CardError => e
    charge = Stripe::Charge.retrieve(e.error.payment_intent.latest_charge)
    if charge.outcome.type == 'blocked'
      puts 'Payment blocked for suspected fraud.'
    elsif e.code == 'card_declined'
      puts 'Payment declined by the issuer.'
    elsif e.code == 'expired_card'
      puts 'Card expired.'
    else
      puts 'Other card error.'
    end
  end
end
```

Users on API version [2022-08-01](https://docs.stripe.com/upgrades.md#2022-08-01) or older:

(To find the charge outcome from an error object, first get the [Payment Intent that’s involved](https://docs.stripe.com/api/errors.md#errors-payment_intent) and the [latest Charge it created](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-charges-data). See the example below for a demonstration.)

#### Ruby

```ruby
require 'stripe'
Stripe.api_key = '<<YOUR_SECRET_KEY>>'

def example_function(params)
  begin
    Stripe::PaymentIntent.create(params)
  rescue Stripe::CardError => e
    if e.error.payment_intent.charges.data[0].outcome.type == 'blocked'
      puts 'Payment blocked for suspected fraud.'
    elsif e.code == 'card_declined'
      puts 'Payment declined by the issuer.'
    elsif e.code == 'expired_card'
      puts 'Card expired.'
    else
      puts 'Other card error.'
    end
  end
end
```

You can trigger some common kinds of payment error with test cards. Consult these lists for options:

- [Simulating payments blocked for fraud risk](https://docs.stripe.com/testing.md#fraud-prevention)
- [Simulating declined payments and other card errors](https://docs.stripe.com/testing.md#declined-payments)

The test code below demonstrates a few possibilities.

#### Error to trigger - Blocked for suspected fraud

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_radarBlock', # This is a test card that is always blocked for suspected fraud when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Payment blocked for suspected fraud.
```

#### Error to trigger - Declined by the issuer

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_visa_chargeDeclined', # This is a test card that is always declined by the issuer when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Payment declined by the issuer.
```

#### Error to trigger - Card expired

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_chargeDeclinedExpiredCard', # This is a test card that always fails as expired when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Card expired.
```

#### Error to trigger - Other card error

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_chargeDeclinedProcessingError', # This is a test card that always fails due to a processing error when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Other payment error.
```

### Payment blocked for suspected fraud  

|  |
|  |
| **Type**                                                                                                                                                                                                                                       | `Stripe::CardError`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Codes**                                                                                                                                                                                                                                      | ```ruby
  charge = Stripe::Charge.retrieve(e.error.payment_intent.latest_charge)
  charge.outcome.type == 'blocked'
  ```

  Users on API version [2022-08-01](https://docs.stripe.com/upgrades.md#2022-08-01) or older:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **Codes** | `e.error.payment_intent.charges.data[0].outcome.type == 'blocked'` |
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
| **Type**      | `Stripe::CardError`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Codes**     | `e.error.code == "card_declined"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Problem**   | The card issuer declined the payment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Solutions** | This error can occur when your integration is working correctly. It reflects an action by the issuer, and that action might be legitimate. Use the decline code to determine what next steps are appropriate. See the [documentation on decline codes](https://docs.stripe.com/declines/codes.md) for appropriate responses to each code.

  You can also:

  - [Follow recommendations to reduce issuer declines](https://docs.stripe.com/declines/card.md#reducing-bank-declines).
  - Use [Payment Links](https://docs.stripe.com/payment-links.md), [Checkout](https://docs.stripe.com/payments/checkout.md), or [Stripe Elements](https://docs.stripe.com/payments/elements.md) for prebuilt form elements that implement those recommendations.

  Test how your integration handles declines with [test cards that simulate successful and declined payments](https://docs.stripe.com/radar/testing.md). |

### Other payment errors  

|  |
|  |
| **Type**      | `Stripe::CardError`                                                                                                                                                                                                                                      |
| **Problem**   | Another payment error occurred.                                                                                                                                                                                                                          |
| **Solutions** | This error can occur when your integration is working correctly. Use the error code to determine what next steps are appropriate. See the [documentation on error codes](https://docs.stripe.com/error-codes.md) for appropriate responses to each code. |

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

#### Ruby

```ruby
require 'stripe'
Stripe.api_key = '<<YOUR_SECRET_KEY>>'

def example_function(params)
  begin
    Stripe::PaymentIntent.create(params)
  rescue Stripe::CardError => e
    charge = Stripe::Charge.retrieve(e.error.payment_intent.latest_charge)
    if charge.outcome.type == 'blocked'
      puts 'Payment blocked for suspected fraud.'
    elsif e.code == 'card_declined'
      puts 'Payment declined by the issuer.'
    elsif e.code == 'expired_card'
      puts 'Card expired.'
    else
      puts 'Other card error.'
    end
  end
end
```

Users on API version [2022-08-01](https://docs.stripe.com/upgrades.md#2022-08-01) or older:

(To find the charge outcome from an error object, first get the [Payment Intent that’s involved](https://docs.stripe.com/api/errors.md#errors-payment_intent) and the [latest Charge it created](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-charges-data). See the example below for a demonstration.)

#### Ruby

```ruby
require 'stripe'
Stripe.api_key = '<<YOUR_SECRET_KEY>>'

def example_function(params)
  begin
    Stripe::PaymentIntent.create(params)
  rescue Stripe::CardError => e
    if e.error.payment_intent.charges.data[0].outcome.type == 'blocked'
      puts 'Payment blocked for suspected fraud.'
    elsif e.code == 'card_declined'
      puts 'Payment declined by the issuer.'
    elsif e.code == 'expired_card'
      puts 'Card expired.'
    else
      puts 'Other card error.'
    end
  end
end
```

You can trigger some common kinds of payment error with test cards. Consult these lists for options:

- [Simulating payments blocked for fraud risk](https://docs.stripe.com/testing.md#fraud-prevention)
- [Simulating declined payments and other card errors](https://docs.stripe.com/testing.md#declined-payments)

The test code below demonstrates a few possibilities.

#### Error to trigger - Blocked for suspected fraud

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_radarBlock', # This is a test card that is always blocked for suspected fraud when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Payment blocked for suspected fraud.
```

#### Error to trigger - Declined by the issuer

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_visa_chargeDeclined', # This is a test card that is always declined by the issuer when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Payment declined by the issuer.
```

#### Error to trigger - Card expired

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_chargeDeclinedExpiredCard', # This is a test card that always fails as expired when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Card expired.
```

#### Error to trigger - Other card error

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_chargeDeclinedProcessingError', # This is a test card that always fails due to a processing error when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

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

## Invalid request errors  

|  |
|  |
| **Type**      | `stripe.InvalidRequestError`                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Problem**   | You made an API call with the wrong parameters, in the wrong state, or in an invalid way.                                                                                                                                                                                                                                                                                                                                                                         |
| **Solutions** | In most cases, the problem is with the request itself. Either its parameters are invalid or it can’t be carried out in your integration’s current state.
  - Consult the [error code documentation](https://docs.stripe.com/error-codes.md) for details on the problem.
  - For convenience, you can follow the link at `e.doc_url` for documentation about the error code.
  - If the error involves a specific parameter, use `e.param` to determine which one. |

## Connection errors  

|  |
|  |
| **Type**      | `stripe.APIConnectionError`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
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
| **Type**      | `stripe.APIError`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Problem**   | Something went wrong on Stripe’s end. (These are rare.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Solutions** | Treat the result of the API call as indeterminate. That is, don’t assume that it succeeded or that it failed.

  Rely on *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) for information about the outcome. Whenever possible, Stripe fires webhooks for any new objects we create as we solve a problem.

  To set your integration up for maximum robustness in unusual situations, see [this advanced discussion of server errors.](https://docs.stripe.com/error-low-level.md#server-errors) |

## Authentication errors  

|  |
|  |
| **Type**      | `stripe.AuthenticationError`                                                                                                                                                      |
| **Problem**   | Stripe can’t authenticate you with the information provided.                                                                                                                      |
| **Solutions** | - Use the correct [API key](https://docs.stripe.com/keys.md).
  - Make sure you aren’t using a key that you [“rotated” or revoked](https://docs.stripe.com/keys.md#rolling-keys). |

## Idempotency errors  

|  |
|  |
| **Type**      | `stripe.IdempotencyError`                                                                                                                                              |
| **Problem**   | You used an [idempotency key](https://docs.stripe.com/api/idempotent_requests.md) for something unexpected, like replaying a request but passing different parameters. |
| **Solutions** | - After you use an idempotency key, only reuse it for identical API calls.
  - Use idempotency keys under the limit of 255 characters.                                 |

## Permission errors  

|  |
|  |
| **Type**      | `stripe.PermissionError`                                                                                                                                                                                                                                                                                                 |
| **Problem**   | The API key used for this request doesn’t have the necessary permissions.                                                                                                                                                                                                                                                |
| **Solutions** | - Make sure you aren’t using a [restricted API key](https://docs.stripe.com/keys-best-practices.md#limit-access) for a service it doesn’t have access to.
  - Don’t perform actions in the Dashboard while logged in as a [user role](https://docs.stripe.com/get-started/account/teams/roles.md) that lacks permission. |

## Rate limit errors  

|  |
|  |
| **Type**      | `stripe.RateLimitError`                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Problem**   | You made too many API calls in too short a time.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Solutions** | - If a single API call triggers this error, wait and try it again.
  - To handle rate-limiting automatically, retry the API call after a delay, and increase the delay exponentially if the error continues. See the documentation on [rate limits](https://docs.stripe.com/rate-limits.md) for further advice.
  - If you anticipate a large increase in traffic and want to request an increased rate limit, [contact support](https://support.stripe.com/) in advance. |

## Signature verification errors  

|  |
|  |
| **Type**      | `stripe.SignatureVerificationError`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Problem**   | You’re using *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) [signature verification](https://docs.stripe.com/webhooks.md#verify-events) and couldn’t verify that a webhook event is authentic.                                                                                                                                                                                                                                                                                                                                                                                   |
| **Solutions** | This error can occur when your integration is working correctly. If you use webhook signature verification and a third party attempts to send you a fake or malicious webhook, then verification fails and this error is the result. Catch it and respond with a `400 Bad Request` status code.

  If you receive this error when you shouldn’t—for instance, with webhooks that you know originate with Stripe—then see the documentation on [checking webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) for further advice. In particular, make sure you’re using the correct endpoint secret. This is different from your API key. |

In the Stripe PHP library, each type of error belongs to its own class. Use the documentation for each class for advice about how to respond.

| Name                         | Class                                                                                                                      | Description                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Payment error                | [Stripe\Exception\CardException](https://docs.stripe.com/error-handling.md#payment-errors)                                 | An error occurred during a payment, involving one of these situations:
  - [Payment blocked for suspected fraud](https://docs.stripe.com/error-handling.md#payment-blocked)
  - [Payment declined by the issuer](https://docs.stripe.com/error-handling.md#payment-declined).
  - [Other payment errors](https://docs.stripe.com/error-handling.md#other-payment-errors). |
| Invalid request error        | [Stripe\Exception\InvalidRequestException](https://docs.stripe.com/error-handling.md#invalid-request-errors)               | You made an API call with the wrong parameters, in the wrong state, or in an invalid way.                                                                                                                                                                                                                                                                                 |
| Connection error             | [Stripe\Exception\ApiConnectionException](https://docs.stripe.com/error-handling.md#connection-errors)                     | There was a network problem between your server and Stripe.                                                                                                                                                                                                                                                                                                               |
| API error                    | [Stripe\Exception\ApiErrorException](https://docs.stripe.com/error-handling.md#api-errors)                                 | Something went wrong on Stripe’s end. (These are rare.)                                                                                                                                                                                                                                                                                                                   |
| Authentication error         | [Stripe\Exception\AuthenticationException](https://docs.stripe.com/error-handling.md#authentication-errors)                | Stripe can’t authenticate you with the information provided.                                                                                                                                                                                                                                                                                                              |
| Idempotency error            | [Stripe\Exception\IdempotencyException](https://docs.stripe.com/error-handling.md#idempotency-errors)                      | You used an [idempotency key](https://docs.stripe.com/api/idempotent_requests.md) for something unexpected, like replaying a request but passing different parameters.                                                                                                                                                                                                    |
| Permission error             | [Stripe\Exception\PermissionException](https://docs.stripe.com/error-handling.md#permission-errors)                        | The API key used for this request doesn’t have the necessary permissions.                                                                                                                                                                                                                                                                                                 |
| Rate limit error             | [Stripe\Exception\RateLimitException](https://docs.stripe.com/error-handling.md#rate-limit-errors)                         | You made too many API calls in too short a time.                                                                                                                                                                                                                                                                                                                          |
| Signature verification error | [Stripe\Exception\SignatureVerificationException](https://docs.stripe.com/error-handling.md#signature-verification-errors) | You’re using *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) [signature verification](https://docs.stripe.com/webhooks.md#verify-events) and couldn’t verify that a webhook event is authentic.                                                                                                  |

## Payment errors 

Everything in this section also applies to non-card payments. For historical reasons, payment errors have the type [Stripe\Exception\CardException](https://docs.stripe.com/error-handling.md#card-error). But in fact, they can represent a problem with any payment, regardless of the payment method.

Payment errors—sometimes called “card errors” for historical reasons—cover a wide range of common problems. They come in three categories:

- [Payment blocked for suspected fraud](https://docs.stripe.com/error-handling.md#payment-blocked)
- [Payment declined by the issuer](https://docs.stripe.com/error-handling.md#payment-declined)
- [Other payment errors](https://docs.stripe.com/error-handling.md#other-payment-errors)

To distinguish these categories or get more information about how to respond, consult the [error code](https://docs.stripe.com/error-codes.md), [decline code](https://docs.stripe.com/declines/codes.md), and [charge outcome](https://docs.stripe.com/api/charges/object.md#charge_object-outcome).

(To find the charge outcome from an error object, first get the [Payment Intent that’s involved](https://docs.stripe.com/api/errors.md#errors-payment_intent) and the [latest Charge it created](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge). See the example below for a demonstration.)

#### Ruby

```ruby
require 'stripe'
Stripe.api_key = '<<YOUR_SECRET_KEY>>'

def example_function(params)
  begin
    Stripe::PaymentIntent.create(params)
  rescue Stripe::CardError => e
    charge = Stripe::Charge.retrieve(e.error.payment_intent.latest_charge)
    if charge.outcome.type == 'blocked'
      puts 'Payment blocked for suspected fraud.'
    elsif e.code == 'card_declined'
      puts 'Payment declined by the issuer.'
    elsif e.code == 'expired_card'
      puts 'Card expired.'
    else
      puts 'Other card error.'
    end
  end
end
```

Users on API version [2022-08-01](https://docs.stripe.com/upgrades.md#2022-08-01) or older:

(To find the charge outcome from an error object, first get the [Payment Intent that’s involved](https://docs.stripe.com/api/errors.md#errors-payment_intent) and the [latest Charge it created](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-charges-data). See the example below for a demonstration.)

#### Ruby

```ruby
require 'stripe'
Stripe.api_key = '<<YOUR_SECRET_KEY>>'

def example_function(params)
  begin
    Stripe::PaymentIntent.create(params)
  rescue Stripe::CardError => e
    if e.error.payment_intent.charges.data[0].outcome.type == 'blocked'
      puts 'Payment blocked for suspected fraud.'
    elsif e.code == 'card_declined'
      puts 'Payment declined by the issuer.'
    elsif e.code == 'expired_card'
      puts 'Card expired.'
    else
      puts 'Other card error.'
    end
  end
end
```

You can trigger some common kinds of payment error with test cards. Consult these lists for options:

- [Simulating payments blocked for fraud risk](https://docs.stripe.com/testing.md#fraud-prevention)
- [Simulating declined payments and other card errors](https://docs.stripe.com/testing.md#declined-payments)

The test code below demonstrates a few possibilities.

#### Error to trigger - Blocked for suspected fraud

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_radarBlock', # This is a test card that is always blocked for suspected fraud when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Payment blocked for suspected fraud.
```

#### Error to trigger - Declined by the issuer

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_visa_chargeDeclined', # This is a test card that is always declined by the issuer when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Payment declined by the issuer.
```

#### Error to trigger - Card expired

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_chargeDeclinedExpiredCard', # This is a test card that always fails as expired when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Card expired.
```

#### Error to trigger - Other card error

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_chargeDeclinedProcessingError', # This is a test card that always fails due to a processing error when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Other payment error.
```

### Payment blocked for suspected fraud  

|  |
|  |
| **Type**                                                                                                                                                                                                                                       | `Stripe\Exception\CardException`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Codes**                                                                                                                                                                                                                                      | ```php
  $charge = $stripe->charge->retrieve($e->getError()->payment_intent->latest_charge);
  $charge->outcome->type == 'blocked'
  ```

  Users on API version [2022-08-01](https://docs.stripe.com/upgrades.md#2022-08-01) or older:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | **Codes** | `$e->getError()->payment_intent->charges->data[0]->outcome->type == 'blocked'` |
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
| **Type**      | `Stripe\Exception\CardException`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Codes**     | `$e->getError()->code == "card_declined"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Problem**   | The card issuer declined the payment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Solutions** | This error can occur when your integration is working correctly. It reflects an action by the issuer, and that action might be legitimate. Use the decline code to determine what next steps are appropriate. See the [documentation on decline codes](https://docs.stripe.com/declines/codes.md) for appropriate responses to each code.

  You can also:

  - [Follow recommendations to reduce issuer declines](https://docs.stripe.com/declines/card.md#reducing-bank-declines).
  - Use [Payment Links](https://docs.stripe.com/payment-links.md), [Checkout](https://docs.stripe.com/payments/checkout.md), or [Stripe Elements](https://docs.stripe.com/payments/elements.md) for prebuilt form elements that implement those recommendations.

  Test how your integration handles declines with [test cards that simulate successful and declined payments](https://docs.stripe.com/radar/testing.md). |

### Other payment errors  

|  |
|  |
| **Type**      | `Stripe\Exception\CardException`                                                                                                                                                                                                                         |
| **Problem**   | Another payment error occurred.                                                                                                                                                                                                                          |
| **Solutions** | This error can occur when your integration is working correctly. Use the error code to determine what next steps are appropriate. See the [documentation on error codes](https://docs.stripe.com/error-codes.md) for appropriate responses to each code. |

## Invalid request errors  

|  |
|  |
| **Type**      | `Stripe\Exception\InvalidRequestException`                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Problem**   | You made an API call with the wrong parameters, in the wrong state, or in an invalid way.                                                                                                                                                                                                                                                                                                                                                                                                   |
| **Solutions** | In most cases, the problem is with the request itself. Either its parameters are invalid or it can’t be carried out in your integration’s current state.
  - Consult the [error code documentation](https://docs.stripe.com/error-codes.md) for details on the problem.
  - For convenience, you can follow the link at `e->getError()->doc_url` for documentation about the error code.
  - If the error involves a specific parameter, use `e->getError()->param` to determine which one. |

## Connection errors  

|  |
|  |
| **Type**      | `Stripe\Exception\ApiConnectionException`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
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
| **Type**      | `Stripe\Exception\APIException`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Problem**   | Something went wrong on Stripe’s end. (These are rare.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Solutions** | Treat the result of the API call as indeterminate. That is, don’t assume that it succeeded or that it failed.

  Rely on *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) for information about the outcome. Whenever possible, Stripe fires webhooks for any new objects we create as we solve a problem.

  To set your integration up for maximum robustness in unusual situations, see [this advanced discussion of server errors.](https://docs.stripe.com/error-low-level.md#server-errors) |

## Authentication errors  

|  |
|  |
| **Type**      | `Stripe\Exception\AuthenticationException`                                                                                                                                        |
| **Problem**   | Stripe can’t authenticate you with the information provided.                                                                                                                      |
| **Solutions** | - Use the correct [API key](https://docs.stripe.com/keys.md).
  - Make sure you aren’t using a key that you [“rotated” or revoked](https://docs.stripe.com/keys.md#rolling-keys). |

## Idempotency errors  

|  |
|  |
| **Type**      | `Stripe\Exception\IdempotencyException`                                                                                                                                |
| **Problem**   | You used an [idempotency key](https://docs.stripe.com/api/idempotent_requests.md) for something unexpected, like replaying a request but passing different parameters. |
| **Solutions** | - After you use an idempotency key, only reuse it for identical API calls.
  - Use idempotency keys under the limit of 255 characters.                                 |

## Permission errors  

|  |
|  |
| **Type**      | `Stripe\Exception\PermissionException`                                                                                                                                                                                                                                                                                   |
| **Problem**   | The API key used for this request doesn’t have the necessary permissions.                                                                                                                                                                                                                                                |
| **Solutions** | - Make sure you aren’t using a [restricted API key](https://docs.stripe.com/keys-best-practices.md#limit-access) for a service it doesn’t have access to.
  - Don’t perform actions in the Dashboard while logged in as a [user role](https://docs.stripe.com/get-started/account/teams/roles.md) that lacks permission. |

## Rate limit errors  

|  |
|  |
| **Type**      | `Stripe\Exception\RateLimitException`                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **Problem**   | You made too many API calls in too short a time.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Solutions** | - If a single API call triggers this error, wait and try it again.
  - To handle rate-limiting automatically, retry the API call after a delay, and increase the delay exponentially if the error continues. See the documentation on [rate limits](https://docs.stripe.com/rate-limits.md) for further advice.
  - If you anticipate a large increase in traffic and want to request an increased rate limit, [contact support](https://support.stripe.com/) in advance. |

## Signature verification errors  

|  |
|  |
| **Type**      | `Stripe\Exception\SignatureVerificationException`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Problem**   | You’re using *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) [signature verification](https://docs.stripe.com/webhooks.md#verify-events) and couldn’t verify that a webhook event is authentic.                                                                                                                                                                                                                                                                                                                                                                                   |
| **Solutions** | This error can occur when your integration is working correctly. If you use webhook signature verification and a third party attempts to send you a fake or malicious webhook, then verification fails and this error is the result. Catch it and respond with a `400 Bad Request` status code.

  If you receive this error when you shouldn’t—for instance, with webhooks that you know originate with Stripe—then see the documentation on [checking webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) for further advice. In particular, make sure you’re using the correct endpoint secret. This is different from your API key. |

In the Stripe Java library, each type of error belongs to its own class. Use the documentation for each class for advice about how to respond.

| Name                         | Class                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------- | --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Payment error                | [CardException](https://docs.stripe.com/error-handling.md#payment-errors)                                 | An error occurred during a payment, involving one of these situations:
  - [Payment blocked for suspected fraud](https://docs.stripe.com/error-handling.md#payment-blocked)
  - [Payment declined by the issuer](https://docs.stripe.com/error-handling.md#payment-declined).
  - [Other payment errors](https://docs.stripe.com/error-handling.md#other-payment-errors). |
| Invalid request error        | [InvalidRequestException](https://docs.stripe.com/error-handling.md#invalid-request-errors)               | You made an API call with the wrong parameters, in the wrong state, or in an invalid way.                                                                                                                                                                                                                                                                                 |
| Connection error             | [ApiConnectionException](https://docs.stripe.com/error-handling.md#connection-errors)                     | There was a network problem between your server and Stripe.                                                                                                                                                                                                                                                                                                               |
| API error                    | [APIException](https://docs.stripe.com/error-handling.md#api-errors)                                      | Something went wrong on Stripe’s end. (These are rare.)                                                                                                                                                                                                                                                                                                                   |
| Authentication error         | [AuthenticationException](https://docs.stripe.com/error-handling.md#authentication-errors)                | Stripe can’t authenticate you with the information provided.                                                                                                                                                                                                                                                                                                              |
| Idempotency error            | [IdempotencyException](https://docs.stripe.com/error-handling.md#idempotency-errors)                      | You used an [idempotency key](https://docs.stripe.com/api/idempotent_requests.md) for something unexpected, like replaying a request but passing different parameters.                                                                                                                                                                                                    |
| Permission error             | [PermissionException](https://docs.stripe.com/error-handling.md#permission-errors)                        | The API key used for this request doesn’t have the necessary permissions.                                                                                                                                                                                                                                                                                                 |
| Rate limit error             | [RateLimitException](https://docs.stripe.com/error-handling.md#rate-limit-errors)                         | You made too many API calls in too short a time.                                                                                                                                                                                                                                                                                                                          |
| Signature verification error | [SignatureVerificationException](https://docs.stripe.com/error-handling.md#signature-verification-errors) | You’re using *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) [signature verification](https://docs.stripe.com/webhooks.md#verify-events) and couldn’t verify that a webhook event is authentic.                                                                                                  |

## Payment errors 

Everything in this section also applies to non-card payments. For historical reasons, payment errors have the type [CardException](https://docs.stripe.com/error-handling.md#card-error). But in fact, they can represent a problem with any payment, regardless of the payment method.

Payment errors—sometimes called “card errors” for historical reasons—cover a wide range of common problems. They come in three categories:

- [Payment blocked for suspected fraud](https://docs.stripe.com/error-handling.md#payment-blocked)
- [Payment declined by the issuer](https://docs.stripe.com/error-handling.md#payment-declined)
- [Other payment errors](https://docs.stripe.com/error-handling.md#other-payment-errors)

To distinguish these categories or get more information about how to respond, consult the [error code](https://docs.stripe.com/error-codes.md), [decline code](https://docs.stripe.com/declines/codes.md), and [charge outcome](https://docs.stripe.com/api/charges/object.md#charge_object-outcome).

(To find the charge outcome from an error object, first get the [Payment Intent that’s involved](https://docs.stripe.com/api/errors.md#errors-payment_intent) and the [latest Charge it created](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge). See the example below for a demonstration.)

#### Ruby

```ruby
require 'stripe'
Stripe.api_key = '<<YOUR_SECRET_KEY>>'

def example_function(params)
  begin
    Stripe::PaymentIntent.create(params)
  rescue Stripe::CardError => e
    charge = Stripe::Charge.retrieve(e.error.payment_intent.latest_charge)
    if charge.outcome.type == 'blocked'
      puts 'Payment blocked for suspected fraud.'
    elsif e.code == 'card_declined'
      puts 'Payment declined by the issuer.'
    elsif e.code == 'expired_card'
      puts 'Card expired.'
    else
      puts 'Other card error.'
    end
  end
end
```

Users on API version [2022-08-01](https://docs.stripe.com/upgrades.md#2022-08-01) or older:

(To find the charge outcome from an error object, first get the [Payment Intent that’s involved](https://docs.stripe.com/api/errors.md#errors-payment_intent) and the [latest Charge it created](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-charges-data). See the example below for a demonstration.)

#### Ruby

```ruby
require 'stripe'
Stripe.api_key = '<<YOUR_SECRET_KEY>>'

def example_function(params)
  begin
    Stripe::PaymentIntent.create(params)
  rescue Stripe::CardError => e
    if e.error.payment_intent.charges.data[0].outcome.type == 'blocked'
      puts 'Payment blocked for suspected fraud.'
    elsif e.code == 'card_declined'
      puts 'Payment declined by the issuer.'
    elsif e.code == 'expired_card'
      puts 'Card expired.'
    else
      puts 'Other card error.'
    end
  end
end
```

You can trigger some common kinds of payment error with test cards. Consult these lists for options:

- [Simulating payments blocked for fraud risk](https://docs.stripe.com/testing.md#fraud-prevention)
- [Simulating declined payments and other card errors](https://docs.stripe.com/testing.md#declined-payments)

The test code below demonstrates a few possibilities.

#### Error to trigger - Blocked for suspected fraud

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_radarBlock', # This is a test card that is always blocked for suspected fraud when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Payment blocked for suspected fraud.
```

#### Error to trigger - Declined by the issuer

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_visa_chargeDeclined', # This is a test card that is always declined by the issuer when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Payment declined by the issuer.
```

#### Error to trigger - Card expired

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_chargeDeclinedExpiredCard', # This is a test card that always fails as expired when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Card expired.
```

#### Error to trigger - Other card error

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_chargeDeclinedProcessingError', # This is a test card that always fails due to a processing error when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Other payment error.
```

### Payment blocked for suspected fraud  

|  |
|  |
| **Type**                                                                                                                                                                                                                                       | `CardException`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Codes**                                                                                                                                                                                                                                      | ```java
  Charge charge = Charge.retrieve(ex.getStripeError()
               .getPaymentIntent()
               .getLatestCharge());
  charge.getOutcome().getType() == "blocked"
  ```

  Users on API version [2022-08-01](https://docs.stripe.com/upgrades.md#2022-08-01) or older:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | **Codes** | `ex.getStripeError().getPaymentIntent().getCharges().getData().get(0).getOutcome().getType() == "blocked"` |
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
| **Type**      | `CardException`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Codes**     | `e.getCode() == "card_declined"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Problem**   | The card issuer declined the payment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Solutions** | This error can occur when your integration is working correctly. It reflects an action by the issuer, and that action might be legitimate. Use the decline code to determine what next steps are appropriate. See the [documentation on decline codes](https://docs.stripe.com/declines/codes.md) for appropriate responses to each code.

  You can also:

  - [Follow recommendations to reduce issuer declines](https://docs.stripe.com/declines/card.md#reducing-bank-declines).
  - Use [Payment Links](https://docs.stripe.com/payment-links.md), [Checkout](https://docs.stripe.com/payments/checkout.md), or [Stripe Elements](https://docs.stripe.com/payments/elements.md) for prebuilt form elements that implement those recommendations.

  Test how your integration handles declines with [test cards that simulate successful and declined payments](https://docs.stripe.com/radar/testing.md). |

### Other payment errors  

|  |
|  |
| **Type**      | `CardException`                                                                                                                                                                                                                                          |
| **Problem**   | Another payment error occurred.                                                                                                                                                                                                                          |
| **Solutions** | This error can occur when your integration is working correctly. Use the error code to determine what next steps are appropriate. See the [documentation on error codes](https://docs.stripe.com/error-codes.md) for appropriate responses to each code. |

## Invalid request errors  

|  |
|  |
| **Type**      | `InvalidRequestException`                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Problem**   | You made an API call with the wrong parameters, in the wrong state, or in an invalid way.                                                                                                                                                                                                                                                                                                                                                                                  |
| **Solutions** | In most cases, the problem is with the request itself. Either its parameters are invalid or it can’t be carried out in your integration’s current state.
  - Consult the [error code documentation](https://docs.stripe.com/error-codes.md) for details on the problem.
  - For convenience, you can follow the link at `e.getDocUrl()` for documentation about the error code.
  - If the error involves a specific parameter, use `e.getParam()` to determine which one. |

## Connection errors  

|  |
|  |
| **Type**      | `APIConnectionException`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
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
| **Type**      | `APIException`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Problem**   | Something went wrong on Stripe’s end. (These are rare.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Solutions** | Treat the result of the API call as indeterminate. That is, don’t assume that it succeeded or that it failed.

  Rely on *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) for information about the outcome. Whenever possible, Stripe fires webhooks for any new objects we create as we solve a problem.

  To set your integration up for maximum robustness in unusual situations, see [this advanced discussion of server errors.](https://docs.stripe.com/error-low-level.md#server-errors) |

## Authentication errors  

|  |
|  |
| **Type**      | `AuthenticationException`                                                                                                                                                         |
| **Problem**   | Stripe can’t authenticate you with the information provided.                                                                                                                      |
| **Solutions** | - Use the correct [API key](https://docs.stripe.com/keys.md).
  - Make sure you aren’t using a key that you [“rotated” or revoked](https://docs.stripe.com/keys.md#rolling-keys). |

## Idempotency errors  

|  |
|  |
| **Type**      | `IdempotencyException`                                                                                                                                                 |
| **Problem**   | You used an [idempotency key](https://docs.stripe.com/api/idempotent_requests.md) for something unexpected, like replaying a request but passing different parameters. |
| **Solutions** | - After you use an idempotency key, only reuse it for identical API calls.
  - Use idempotency keys under the limit of 255 characters.                                 |

## Permission errors  

|  |
|  |
| **Type**      | `PermissionException`                                                                                                                                                                                                                                                                                                    |
| **Problem**   | The API key used for this request doesn’t have the necessary permissions.                                                                                                                                                                                                                                                |
| **Solutions** | - Make sure you aren’t using a [restricted API key](https://docs.stripe.com/keys-best-practices.md#limit-access) for a service it doesn’t have access to.
  - Don’t perform actions in the Dashboard while logged in as a [user role](https://docs.stripe.com/get-started/account/teams/roles.md) that lacks permission. |

## Rate limit errors  

|  |
|  |
| **Type**      | `RateLimitException`                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Problem**   | You made too many API calls in too short a time.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Solutions** | - If a single API call triggers this error, wait and try it again.
  - To handle rate-limiting automatically, retry the API call after a delay, and increase the delay exponentially if the error continues. See the documentation on [rate limits](https://docs.stripe.com/rate-limits.md) for further advice.
  - If you anticipate a large increase in traffic and want to request an increased rate limit, [contact support](https://support.stripe.com/) in advance. |

## Signature verification errors  

|  |
|  |
| **Type**      | `SignatureVerificationException`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Problem**   | You’re using *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) [signature verification](https://docs.stripe.com/webhooks.md#verify-events) and couldn’t verify that a webhook event is authentic.                                                                                                                                                                                                                                                                                                                                                                                   |
| **Solutions** | This error can occur when your integration is working correctly. If you use webhook signature verification and a third party attempts to send you a fake or malicious webhook, then verification fails and this error is the result. Catch it and respond with a `400 Bad Request` status code.

  If you receive this error when you shouldn’t—for instance, with webhooks that you know originate with Stripe—then see the documentation on [checking webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) for further advice. In particular, make sure you’re using the correct endpoint secret. This is different from your API key. |

In the Stripe Node.js library, each error object has a `type` attribute. Use the documentation for each type for advice about how to respond.

| Name                         | Type                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Payment error                | [StripeCardError](https://docs.stripe.com/error-handling.md#payment-errors)                                 | An error occurred during a payment, involving one of these situations:
  - [Payment blocked for suspected fraud](https://docs.stripe.com/error-handling.md#payment-blocked)
  - [Payment declined by the issuer](https://docs.stripe.com/error-handling.md#payment-declined).
  - [Other payment errors](https://docs.stripe.com/error-handling.md#other-payment-errors). |
| Invalid request error        | [StripeInvalidRequestError](https://docs.stripe.com/error-handling.md#invalid-request-errors)               | You made an API call with the wrong parameters, in the wrong state, or in an invalid way.                                                                                                                                                                                                                                                                                 |
| Connection error             | [StripeConnectionError](https://docs.stripe.com/error-handling.md#connection-errors)                        | There was a network problem between your server and Stripe.                                                                                                                                                                                                                                                                                                               |
| API error                    | [StripeAPIError](https://docs.stripe.com/error-handling.md#api-errors)                                      | Something went wrong on Stripe’s end. (These are rare.)                                                                                                                                                                                                                                                                                                                   |
| Authentication error         | [StripeAuthenticationError](https://docs.stripe.com/error-handling.md#authentication-errors)                | Stripe can’t authenticate you with the information provided.                                                                                                                                                                                                                                                                                                              |
| Idempotency error            | [StripeIdempotencyError](https://docs.stripe.com/error-handling.md#idempotency-errors)                      | You used an [idempotency key](https://docs.stripe.com/api/idempotent_requests.md) for something unexpected, like replaying a request but passing different parameters.                                                                                                                                                                                                    |
| Permission error             | [StripePermissionError](https://docs.stripe.com/error-handling.md#permission-errors)                        | The API key used for this request doesn’t have the necessary permissions.                                                                                                                                                                                                                                                                                                 |
| Rate limit error             | [StripeRateLimitError](https://docs.stripe.com/error-handling.md#rate-limit-errors)                         | You made too many API calls in too short a time.                                                                                                                                                                                                                                                                                                                          |
| Signature verification error | [StripeSignatureVerificationError](https://docs.stripe.com/error-handling.md#signature-verification-errors) | You’re using *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) [signature verification](https://docs.stripe.com/webhooks.md#verify-events) and couldn’t verify that a webhook event is authentic.                                                                                                  |

## Payment errors 

Everything in this section also applies to non-card payments. For historical reasons, payment errors have the type [StripeCardError](https://docs.stripe.com/error-handling.md#card-error). But in fact, they can represent a problem with any payment, regardless of the payment method.

Payment errors—sometimes called “card errors” for historical reasons—cover a wide range of common problems. They come in three categories:

- [Payment blocked for suspected fraud](https://docs.stripe.com/error-handling.md#payment-blocked)
- [Payment declined by the issuer](https://docs.stripe.com/error-handling.md#payment-declined)
- [Other payment errors](https://docs.stripe.com/error-handling.md#other-payment-errors)

To distinguish these categories or get more information about how to respond, consult the [error code](https://docs.stripe.com/error-codes.md), [decline code](https://docs.stripe.com/declines/codes.md), and [charge outcome](https://docs.stripe.com/api/charges/object.md#charge_object-outcome).

(To find the charge outcome from an error object, first get the [Payment Intent that’s involved](https://docs.stripe.com/api/errors.md#errors-payment_intent) and the [latest Charge it created](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge). See the example below for a demonstration.)

#### Ruby

```ruby
require 'stripe'
Stripe.api_key = '<<YOUR_SECRET_KEY>>'

def example_function(params)
  begin
    Stripe::PaymentIntent.create(params)
  rescue Stripe::CardError => e
    charge = Stripe::Charge.retrieve(e.error.payment_intent.latest_charge)
    if charge.outcome.type == 'blocked'
      puts 'Payment blocked for suspected fraud.'
    elsif e.code == 'card_declined'
      puts 'Payment declined by the issuer.'
    elsif e.code == 'expired_card'
      puts 'Card expired.'
    else
      puts 'Other card error.'
    end
  end
end
```

Users on API version [2022-08-01](https://docs.stripe.com/upgrades.md#2022-08-01) or older:

(To find the charge outcome from an error object, first get the [Payment Intent that’s involved](https://docs.stripe.com/api/errors.md#errors-payment_intent) and the [latest Charge it created](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-charges-data). See the example below for a demonstration.)

#### Ruby

```ruby
require 'stripe'
Stripe.api_key = '<<YOUR_SECRET_KEY>>'

def example_function(params)
  begin
    Stripe::PaymentIntent.create(params)
  rescue Stripe::CardError => e
    if e.error.payment_intent.charges.data[0].outcome.type == 'blocked'
      puts 'Payment blocked for suspected fraud.'
    elsif e.code == 'card_declined'
      puts 'Payment declined by the issuer.'
    elsif e.code == 'expired_card'
      puts 'Card expired.'
    else
      puts 'Other card error.'
    end
  end
end
```

You can trigger some common kinds of payment error with test cards. Consult these lists for options:

- [Simulating payments blocked for fraud risk](https://docs.stripe.com/testing.md#fraud-prevention)
- [Simulating declined payments and other card errors](https://docs.stripe.com/testing.md#declined-payments)

The test code below demonstrates a few possibilities.

#### Error to trigger - Blocked for suspected fraud

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_radarBlock', # This is a test card that is always blocked for suspected fraud when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Payment blocked for suspected fraud.
```

#### Error to trigger - Declined by the issuer

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_visa_chargeDeclined', # This is a test card that is always declined by the issuer when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Payment declined by the issuer.
```

#### Error to trigger - Card expired

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_chargeDeclinedExpiredCard', # This is a test card that always fails as expired when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Card expired.
```

#### Error to trigger - Other card error

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_chargeDeclinedProcessingError', # This is a test card that always fails due to a processing error when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Other payment error.
```

### Payment blocked for suspected fraud  

|  |
|  |
| **Type**                                                                                                                                                                                                                                       | `StripeCardError`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Codes**                                                                                                                                                                                                                                      | ```javascript
  const charge = await stripe.charges.retrieve(e.payment_intent.latest_charge)
  charge.outcome.type === 'blocked'
  ```

  Users on API version [2022-08-01](https://docs.stripe.com/upgrades.md#2022-08-01) or older:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | **Codes** | `e.payment_intent.charges.data[0].outcome.type === 'blocked'` |
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
| **Type**      | `StripeCardError`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| **Codes**     | `e.code === 'card_declined'`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Problem**   | The card issuer declined the payment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Solutions** | This error can occur when your integration is working correctly. It reflects an action by the issuer, and that action might be legitimate. Use the decline code to determine what next steps are appropriate. See the [documentation on decline codes](https://docs.stripe.com/declines/codes.md) for appropriate responses to each code.

  You can also:

  - [Follow recommendations to reduce issuer declines](https://docs.stripe.com/declines/card.md#reducing-bank-declines).
  - Use [Payment Links](https://docs.stripe.com/payment-links.md), [Checkout](https://docs.stripe.com/payments/checkout.md), or [Stripe Elements](https://docs.stripe.com/payments/elements.md) for prebuilt form elements that implement those recommendations.

  Test how your integration handles declines with [test cards that simulate successful and declined payments](https://docs.stripe.com/radar/testing.md). |

### Other payment errors  

|  |
|  |
| **Type**      | `StripeCardError`                                                                                                                                                                                                                                        |
| **Problem**   | Another payment error occurred.                                                                                                                                                                                                                          |
| **Solutions** | This error can occur when your integration is working correctly. Use the error code to determine what next steps are appropriate. See the [documentation on error codes](https://docs.stripe.com/error-codes.md) for appropriate responses to each code. |

## Invalid request errors  

|  |
|  |
| **Type**      | `StripeInvalidRequestError`                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Problem**   | You made an API call with the wrong parameters, in the wrong state, or in an invalid way.                                                                                                                                                                                                                                                                                                                                                                         |
| **Solutions** | In most cases, the problem is with the request itself. Either its parameters are invalid or it can’t be carried out in your integration’s current state.
  - Consult the [error code documentation](https://docs.stripe.com/error-codes.md) for details on the problem.
  - For convenience, you can follow the link at `e.doc_url` for documentation about the error code.
  - If the error involves a specific parameter, use `e.param` to determine which one. |

## Connection errors  

|  |
|  |
| **Type**      | `StripeAPIConnectionError`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
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
| **Type**      | `StripeAPIError`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Problem**   | Something went wrong on Stripe’s end. (These are rare.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Solutions** | Treat the result of the API call as indeterminate. That is, don’t assume that it succeeded or that it failed.

  Rely on *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) for information about the outcome. Whenever possible, Stripe fires webhooks for any new objects we create as we solve a problem.

  To set your integration up for maximum robustness in unusual situations, see [this advanced discussion of server errors.](https://docs.stripe.com/error-low-level.md#server-errors) |

## Authentication errors  

|  |
|  |
| **Type**      | `StripeAuthenticationError`                                                                                                                                                       |
| **Problem**   | Stripe can’t authenticate you with the information provided.                                                                                                                      |
| **Solutions** | - Use the correct [API key](https://docs.stripe.com/keys.md).
  - Make sure you aren’t using a key that you [“rotated” or revoked](https://docs.stripe.com/keys.md#rolling-keys). |

## Idempotency errors  

|  |
|  |
| **Type**      | `StripeIdempotencyError`                                                                                                                                               |
| **Problem**   | You used an [idempotency key](https://docs.stripe.com/api/idempotent_requests.md) for something unexpected, like replaying a request but passing different parameters. |
| **Solutions** | - After you use an idempotency key, only reuse it for identical API calls.
  - Use idempotency keys under the limit of 255 characters.                                 |

## Permission errors  

|  |
|  |
| **Type**      | `StripePermissionError`                                                                                                                                                                                                                                                                                                  |
| **Problem**   | The API key used for this request doesn’t have the necessary permissions.                                                                                                                                                                                                                                                |
| **Solutions** | - Make sure you aren’t using a [restricted API key](https://docs.stripe.com/keys-best-practices.md#limit-access) for a service it doesn’t have access to.
  - Don’t perform actions in the Dashboard while logged in as a [user role](https://docs.stripe.com/get-started/account/teams/roles.md) that lacks permission. |

## Rate limit errors  

|  |
|  |
| **Type**      | `StripeRateLimitError`                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Problem**   | You made too many API calls in too short a time.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Solutions** | - If a single API call triggers this error, wait and try it again.
  - To handle rate-limiting automatically, retry the API call after a delay, and increase the delay exponentially if the error continues. See the documentation on [rate limits](https://docs.stripe.com/rate-limits.md) for further advice.
  - If you anticipate a large increase in traffic and want to request an increased rate limit, [contact support](https://support.stripe.com/) in advance. |

## Signature verification errors  

|  |
|  |
| **Type**      | `StripeSignatureVerificationError`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Problem**   | You’re using *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) [signature verification](https://docs.stripe.com/webhooks.md#verify-events) and couldn’t verify that a webhook event is authentic.                                                                                                                                                                                                                                                                                                                                                                                   |
| **Solutions** | This error can occur when your integration is working correctly. If you use webhook signature verification and a third party attempts to send you a fake or malicious webhook, then verification fails and this error is the result. Catch it and respond with a `400 Bad Request` status code.

  If you receive this error when you shouldn’t—for instance, with webhooks that you know originate with Stripe—then see the documentation on [checking webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) for further advice. In particular, make sure you’re using the correct endpoint secret. This is different from your API key. |

In the Stripe Go library, each error object has a `Type` attribute. Use the documentation for each type for advice about how to respond.

| Name                  | Type                                                                                               | Description                                                                                                                                                                                                                                                                                                                                                               |
| --------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Payment error         | [stripe.ErrorTypeCard](https://docs.stripe.com/error-handling.md#payment-errors)                   | An error occurred during a payment, involving one of these situations:
  - [Payment blocked for suspected fraud](https://docs.stripe.com/error-handling.md#payment-blocked)
  - [Payment declined by the issuer](https://docs.stripe.com/error-handling.md#payment-declined).
  - [Other payment errors](https://docs.stripe.com/error-handling.md#other-payment-errors). |
| Invalid request error | [stripe.ErrorTypeInvalidRequest](https://docs.stripe.com/error-handling.md#invalid-request-errors) | You made an API call in a way that isn’t currently valid. This can include:

  - [Rate limiting error](https://docs.stripe.com/error-handling.md#rate-limiting)
  - [Authentication error](https://docs.stripe.com/error-handling.md#authentication-errors)
  - [Invalid parameters or state](https://docs.stripe.com/error-handling.md#invalid-parameters-or-state)      |
| API error             | [stripe.ErrorTypeAPI](https://docs.stripe.com/error-handling.md#api-errors)                        | Something went wrong on Stripe’s end. (These are rare.)                                                                                                                                                                                                                                                                                                                   |
| Idempotency error     | [stripe.ErrorTypeIdempotency](https://docs.stripe.com/error-handling.md#idempotency-errors)        | You used an [idempotency key](https://docs.stripe.com/api/idempotent_requests.md) for something unexpected, like replaying a request but passing different parameters.                                                                                                                                                                                                    |

## Card errors 

Everything in this section also applies to non-card payments. For historical reasons, payment errors have the type [stripe.ErrorTypeCard](https://docs.stripe.com/error-handling.md#card-error). But in fact, they can represent a problem with any payment, regardless of the payment method.

Payment errors—sometimes called “card errors” for historical reasons—cover a wide range of common problems. They come in three categories:

- [Payment blocked for suspected fraud](https://docs.stripe.com/error-handling.md#payment-blocked)
- [Payment declined by the issuer](https://docs.stripe.com/error-handling.md#payment-declined)
- [Other payment errors](https://docs.stripe.com/error-handling.md#other-payment-errors)

To distinguish these categories or get more information about how to respond, consult the [error code](https://docs.stripe.com/error-codes.md), [decline code](https://docs.stripe.com/declines/codes.md), and [charge outcome](https://docs.stripe.com/api/charges/object.md#charge_object-outcome).

(To find the charge outcome from an error object, first get the [Payment Intent that’s involved](https://docs.stripe.com/api/errors.md#errors-payment_intent) and the [latest Charge it created](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge). See the example below for a demonstration.)

#### Ruby

```ruby
require 'stripe'
Stripe.api_key = '<<YOUR_SECRET_KEY>>'

def example_function(params)
  begin
    Stripe::PaymentIntent.create(params)
  rescue Stripe::CardError => e
    charge = Stripe::Charge.retrieve(e.error.payment_intent.latest_charge)
    if charge.outcome.type == 'blocked'
      puts 'Payment blocked for suspected fraud.'
    elsif e.code == 'card_declined'
      puts 'Payment declined by the issuer.'
    elsif e.code == 'expired_card'
      puts 'Card expired.'
    else
      puts 'Other card error.'
    end
  end
end
```

Users on API version [2022-08-01](https://docs.stripe.com/upgrades.md#2022-08-01) or older:

(To find the charge outcome from an error object, first get the [Payment Intent that’s involved](https://docs.stripe.com/api/errors.md#errors-payment_intent) and the [latest Charge it created](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-charges-data). See the example below for a demonstration.)

#### Ruby

```ruby
require 'stripe'
Stripe.api_key = '<<YOUR_SECRET_KEY>>'

def example_function(params)
  begin
    Stripe::PaymentIntent.create(params)
  rescue Stripe::CardError => e
    if e.error.payment_intent.charges.data[0].outcome.type == 'blocked'
      puts 'Payment blocked for suspected fraud.'
    elsif e.code == 'card_declined'
      puts 'Payment declined by the issuer.'
    elsif e.code == 'expired_card'
      puts 'Card expired.'
    else
      puts 'Other card error.'
    end
  end
end
```

You can trigger some common kinds of payment error with test cards. Consult these lists for options:

- [Simulating payments blocked for fraud risk](https://docs.stripe.com/testing.md#fraud-prevention)
- [Simulating declined payments and other card errors](https://docs.stripe.com/testing.md#declined-payments)

The test code below demonstrates a few possibilities.

#### Error to trigger - Blocked for suspected fraud

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_radarBlock', # This is a test card that is always blocked for suspected fraud when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Payment blocked for suspected fraud.
```

#### Error to trigger - Declined by the issuer

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_visa_chargeDeclined', # This is a test card that is always declined by the issuer when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Payment declined by the issuer.
```

#### Error to trigger - Card expired

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_chargeDeclinedExpiredCard', # This is a test card that always fails as expired when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Card expired.
```

#### Error to trigger - Other card error

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_chargeDeclinedProcessingError', # This is a test card that always fails due to a processing error when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Other payment error.
```

### Blocked for suspected fraud 

|  |
|  |
| **Type**                                                                                                                                                                                                                                       | `stripe.ErrorTypeCard`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Codes**                                                                                                                                                                                                                                      | ```go
  charge = Charge.retrieve(stripeErr.PaymentIntent.LatestCharge)
  charge.Outcome.Type == "blocked"
  ```

  Users on API version [2022-08-01](https://docs.stripe.com/upgrades.md#2022-08-01) or older:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | **Codes** | `stripeErr.PaymentIntent.Charges.Data[0].Outcome.Type == "blocked"` |
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

### Declined by the issuer 

|  |
|  |
| **Type**      | `stripe.ErrorTypeCard`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Codes**     | `cardErr.Error.Code == stripe.ErrorCodeCardDeclined`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **Problem**   | The card issuer declined the payment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Solutions** | This error can occur when your integration is working correctly. It reflects an action by the issuer, and that action might be legitimate. Use the decline code to determine what next steps are appropriate. See the [documentation on decline codes](https://docs.stripe.com/declines/codes.md) for appropriate responses to each code.

  You can also:

  - [Follow recommendations to reduce issuer declines](https://docs.stripe.com/declines/card.md#reducing-bank-declines).
  - Use [Payment Links](https://docs.stripe.com/payment-links.md), [Checkout](https://docs.stripe.com/payments/checkout.md), or [Stripe Elements](https://docs.stripe.com/payments/elements.md) for prebuilt form elements that implement those recommendations.

  Test how your integration handles declines with [test cards that simulate successful and declined payments](https://docs.stripe.com/radar/testing.md). |

### Other payment errors 

|  |
|  |
| **Type**      | `stripe.ErrorTypeCard`                                                                                                                                                                                                                                   |
| **Problem**   | Another payment error occurred.                                                                                                                                                                                                                          |
| **Solutions** | This error can occur when your integration is working correctly. Use the error code to determine what next steps are appropriate. See the [documentation on error codes](https://docs.stripe.com/error-codes.md) for appropriate responses to each code. |

## Invalid request errors 

Invalid request errors cover a range of situations. The most common one is when the API request has invalid parameters or isn’t allowed in your integration’s current state. Use the error code (`stripeErr.Code`) and consult the [error code documentation](https://docs.stripe.com/error-codes.md) to find a solution. A few error codes require a special response:

- `rate_limit` and `lock_timeout` reflect [rate limit errors](https://docs.stripe.com/error-handling.md#rate-limit-errors)
- `secret_key_required` reflects an [authentication error](https://docs.stripe.com/error-handling.md#authentication-errors)
- Other error codes reflect [invalid parameters or state](https://docs.stripe.com/error-handling.md#other-invalid-request-errors)

### Rate limit errors 

|  |
|  |
| **Type**      | `stripe.ErrorTypeInvalidRequest`                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Codes**     | `stripeErr.Code == stripe.ErrorCodeRateLimit or stripeErr.Code == stripe.ErrorCodeLockTimeout`                                                                                                                                                                                                                                                                                                                                                                            |
| **Problem**   | You made too many API calls in too short a time.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Solutions** | - If a single API call triggers this error, wait and try it again.
  - To handle rate-limiting automatically, retry the API call after a delay, and increase the delay exponentially if the error continues. See the documentation on [rate limits](https://docs.stripe.com/rate-limits.md) for further advice.
  - If you anticipate a large increase in traffic and want to request an increased rate limit, [contact support](https://support.stripe.com/) in advance. |

### Authentication errors 

|  |
|  |
| **Type**      | `stripe.ErrorTypeInvalidRequest`                                                                                                                                                  |
| **Codes**     | `stripeErr.Code == stripe.ErrorCodeSecretKeyRequired`                                                                                                                             |
| **Problem**   | Stripe can’t authenticate you with the information provided.                                                                                                                      |
| **Solutions** | - Use the correct [API key](https://docs.stripe.com/keys.md).
  - Make sure you aren’t using a key that you [“rotated” or revoked](https://docs.stripe.com/keys.md#rolling-keys). |

### Invalid parameters or state 

|  |
|  |
| **Type**      | `stripe.ErrorTypeInvalidRequest`                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| **Codes**     | `stripeErr.Code != stripe.ErrorCodeRateLimit and stripeErr.Code != stripe.ErrorCodeLockTimeout and stripeErr.Code != stripe.ErrorCodeSecretKeyRequired`                                                                                                                                                                                                                                                                                                                          |
| **Problem**   | You made an API call with the wrong parameters, in the wrong state, or in an invalid way.                                                                                                                                                                                                                                                                                                                                                                                        |
| **Solutions** | In most cases, the problem is with the request itself. Either its parameters are invalid or it can’t be carried out in your integration’s current state.
  - Consult the [error code documentation](https://docs.stripe.com/error-codes.md) for details on the problem.
  - For convenience, you can follow the link at `stripeErr.DocURL` for documentation about the error code.
  - If the error involves a specific parameter, use `stripeErr.Param` to determine which one. |

## API errors 

|  |
|  |
| **Type**      | `stripe.ErrorTypeAPI`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| **Problem**   | Something went wrong on Stripe’s end. (These are rare.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Solutions** | Treat the result of the API call as indeterminate. That is, don’t assume that it succeeded or that it failed.

  Rely on *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) for information about the outcome. Whenever possible, Stripe fires webhooks for any new objects we create as we solve a problem.

  To set your integration up for maximum robustness in unusual situations, see [this advanced discussion of server errors.](https://docs.stripe.com/error-low-level.md#server-errors) |

## Idempotency errors 

|  |
|  |
| **Type**      | `stripe.ErrorTypeIdempotency`                                                                                                                                          |
| **Problem**   | You used an [idempotency key](https://docs.stripe.com/api/idempotent_requests.md) for something unexpected, like replaying a request but passing different parameters. |
| **Solutions** | - After you use an idempotency key, only reuse it for identical API calls.
  - Use idempotency keys under the limit of 255 characters.                                 |

In the Stripe .NET library, each error object has a `type` attribute. Use the documentation for each type for advice about how to respond.

| Name                         | Type                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                                               |
| ---------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Payment error                | [card_error](https://docs.stripe.com/error-handling.md#payment-errors)                                  | An error occurred during a payment, involving one of these situations:
  - [Payment blocked for suspected fraud](https://docs.stripe.com/error-handling.md#payment-blocked)
  - [Payment declined by the issuer](https://docs.stripe.com/error-handling.md#payment-declined).
  - [Other payment errors](https://docs.stripe.com/error-handling.md#other-payment-errors). |
| Invalid request error        | [invalid_request_error](https://docs.stripe.com/error-handling.md#invalid-request-errors)               | You made an API call with the wrong parameters, in the wrong state, or in an invalid way.                                                                                                                                                                                                                                                                                 |
| Connection error             | [api_connection_error](https://docs.stripe.com/error-handling.md#connection-errors)                     | There was a network problem between your server and Stripe.                                                                                                                                                                                                                                                                                                               |
| API error                    | [api_error](https://docs.stripe.com/error-handling.md#api-errors)                                       | Something went wrong on Stripe’s end. (These are rare.)                                                                                                                                                                                                                                                                                                                   |
| Authentication error         | [authentication_error](https://docs.stripe.com/error-handling.md#authentication-errors)                 | Stripe can’t authenticate you with the information provided.                                                                                                                                                                                                                                                                                                              |
| Idempotency error            | [idempotency_error](https://docs.stripe.com/error-handling.md#idempotency-errors)                       | You used an [idempotency key](https://docs.stripe.com/api/idempotent_requests.md) for something unexpected, like replaying a request but passing different parameters.                                                                                                                                                                                                    |
| Permission error             | [permission_error](https://docs.stripe.com/error-handling.md#permission-errors)                         | The API key used for this request doesn’t have the necessary permissions.                                                                                                                                                                                                                                                                                                 |
| Rate limit error             | [rate_limit_error](https://docs.stripe.com/error-handling.md#rate-limit-errors)                         | You made too many API calls in too short a time.                                                                                                                                                                                                                                                                                                                          |
| Signature verification error | [signature_verification_error](https://docs.stripe.com/error-handling.md#signature-verification-errors) | You’re using *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) [signature verification](https://docs.stripe.com/webhooks.md#verify-events) and couldn’t verify that a webhook event is authentic.                                                                                                  |

## Payment errors 

Everything in this section also applies to non-card payments. For historical reasons, payment errors have the type [card_error](https://docs.stripe.com/error-handling.md#card-error). But in fact, they can represent a problem with any payment, regardless of the payment method.

Payment errors—sometimes called “card errors” for historical reasons—cover a wide range of common problems. They come in three categories:

- [Payment blocked for suspected fraud](https://docs.stripe.com/error-handling.md#payment-blocked)
- [Payment declined by the issuer](https://docs.stripe.com/error-handling.md#payment-declined)
- [Other payment errors](https://docs.stripe.com/error-handling.md#other-payment-errors)

To distinguish these categories or get more information about how to respond, consult the [error code](https://docs.stripe.com/error-codes.md), [decline code](https://docs.stripe.com/declines/codes.md), and [charge outcome](https://docs.stripe.com/api/charges/object.md#charge_object-outcome).

(To find the charge outcome from an error object, first get the [Payment Intent that’s involved](https://docs.stripe.com/api/errors.md#errors-payment_intent) and the [latest Charge it created](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-latest_charge). See the example below for a demonstration.)

#### Ruby

```ruby
require 'stripe'
Stripe.api_key = '<<YOUR_SECRET_KEY>>'

def example_function(params)
  begin
    Stripe::PaymentIntent.create(params)
  rescue Stripe::CardError => e
    charge = Stripe::Charge.retrieve(e.error.payment_intent.latest_charge)
    if charge.outcome.type == 'blocked'
      puts 'Payment blocked for suspected fraud.'
    elsif e.code == 'card_declined'
      puts 'Payment declined by the issuer.'
    elsif e.code == 'expired_card'
      puts 'Card expired.'
    else
      puts 'Other card error.'
    end
  end
end
```

Users on API version [2022-08-01](https://docs.stripe.com/upgrades.md#2022-08-01) or older:

(To find the charge outcome from an error object, first get the [Payment Intent that’s involved](https://docs.stripe.com/api/errors.md#errors-payment_intent) and the [latest Charge it created](https://docs.stripe.com/api/payment_intents/object.md#payment_intent_object-charges-data). See the example below for a demonstration.)

#### Ruby

```ruby
require 'stripe'
Stripe.api_key = '<<YOUR_SECRET_KEY>>'

def example_function(params)
  begin
    Stripe::PaymentIntent.create(params)
  rescue Stripe::CardError => e
    if e.error.payment_intent.charges.data[0].outcome.type == 'blocked'
      puts 'Payment blocked for suspected fraud.'
    elsif e.code == 'card_declined'
      puts 'Payment declined by the issuer.'
    elsif e.code == 'expired_card'
      puts 'Card expired.'
    else
      puts 'Other card error.'
    end
  end
end
```

You can trigger some common kinds of payment error with test cards. Consult these lists for options:

- [Simulating payments blocked for fraud risk](https://docs.stripe.com/testing.md#fraud-prevention)
- [Simulating declined payments and other card errors](https://docs.stripe.com/testing.md#declined-payments)

The test code below demonstrates a few possibilities.

#### Error to trigger - Blocked for suspected fraud

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_radarBlock', # This is a test card that is always blocked for suspected fraud when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Payment blocked for suspected fraud.
```

#### Error to trigger - Declined by the issuer

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_visa_chargeDeclined', # This is a test card that is always declined by the issuer when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Payment declined by the issuer.
```

#### Error to trigger - Card expired

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_chargeDeclinedExpiredCard', # This is a test card that always fails as expired when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Card expired.
```

#### Error to trigger - Other card error

#### Ruby

```ruby
example_function(
  currency: 'usd',
  amount: 2000,
  confirm: true,
  payment_method: 'pm_card_chargeDeclinedProcessingError', # This is a test card that always fails due to a processing error when you use it in a sandbox. Use it and other test cards to test error handling in your integration. In production code, you would use a real payment method here.
)
```

```
Other payment error.
```

### Payment blocked for suspected fraud  

|  |
|  |
| **Type**                                                                                                                                                                                                                                       | `card_error`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Codes**                                                                                                                                                                                                                                      | ```dotnet
  var chargeService = new ChargeService();
  var options = new ChargeGetOptions();
  var charge = chargeService.Get(e.StripeError.PaymentIntent.LatestChargeId, options);
  charge.Outcome.Type == "blocked"
  ```

  Users on API version [2022-08-01](https://docs.stripe.com/upgrades.md#2022-08-01) or older:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | **Codes** | `e.StripeError.PaymentIntent.Charges.Data[0].Outcome.Type == "blocked"` |
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
| **Type**      | `card_error`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Codes**     | `e.StripeError.Code == "card_declined"`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| **Problem**   | The card issuer declined the payment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Solutions** | This error can occur when your integration is working correctly. It reflects an action by the issuer, and that action might be legitimate. Use the decline code to determine what next steps are appropriate. See the [documentation on decline codes](https://docs.stripe.com/declines/codes.md) for appropriate responses to each code.

  You can also:

  - [Follow recommendations to reduce issuer declines](https://docs.stripe.com/declines/card.md#reducing-bank-declines).
  - Use [Payment Links](https://docs.stripe.com/payment-links.md), [Checkout](https://docs.stripe.com/payments/checkout.md), or [Stripe Elements](https://docs.stripe.com/payments/elements.md) for prebuilt form elements that implement those recommendations.

  Test how your integration handles declines with [test cards that simulate successful and declined payments](https://docs.stripe.com/radar/testing.md). |

### Other payment errors  

|  |
|  |
| **Type**      | `card_error`                                                                                                                                                                                                                                             |
| **Problem**   | Another payment error occurred.                                                                                                                                                                                                                          |
| **Solutions** | This error can occur when your integration is working correctly. Use the error code to determine what next steps are appropriate. See the [documentation on error codes](https://docs.stripe.com/error-codes.md) for appropriate responses to each code. |

## Invalid request errors  

|  |
|  |
| **Type**      | `invalid_request_error`                                                                                                                                                                                                                                                                                                                                                                                                                       |
| **Problem**   | You made an API call with the wrong parameters, in the wrong state, or in an invalid way.                                                                                                                                                                                                                                                                                                                                                     |
| **Solutions** | In most cases, the problem is with the request itself. Either its parameters are invalid or it can’t be carried out in your integration’s current state.
  - Consult the [error code documentation](https://docs.stripe.com/error-codes.md) for details on the problem.
  - For convenience, you can follow the link at  for documentation about the error code.
  - If the error involves a specific parameter, use  to determine which one. |

## Connection errors  

|  |
|  |
| **Type**      | `api_connection_error`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
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
| **Type**      | `api_error`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Problem**   | Something went wrong on Stripe’s end. (These are rare.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| **Solutions** | Treat the result of the API call as indeterminate. That is, don’t assume that it succeeded or that it failed.

  Rely on *webhooks* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) for information about the outcome. Whenever possible, Stripe fires webhooks for any new objects we create as we solve a problem.

  To set your integration up for maximum robustness in unusual situations, see [this advanced discussion of server errors.](https://docs.stripe.com/error-low-level.md#server-errors) |

## Authentication errors  

|  |
|  |
| **Type**      | `authentication_error`                                                                                                                                                            |
| **Problem**   | Stripe can’t authenticate you with the information provided.                                                                                                                      |
| **Solutions** | - Use the correct [API key](https://docs.stripe.com/keys.md).
  - Make sure you aren’t using a key that you [“rotated” or revoked](https://docs.stripe.com/keys.md#rolling-keys). |

## Idempotency errors  

|  |
|  |
| **Type**      | `idempotency_error`                                                                                                                                                    |
| **Problem**   | You used an [idempotency key](https://docs.stripe.com/api/idempotent_requests.md) for something unexpected, like replaying a request but passing different parameters. |
| **Solutions** | - After you use an idempotency key, only reuse it for identical API calls.
  - Use idempotency keys under the limit of 255 characters.                                 |

## Permission errors  

|  |
|  |
| **Type**      | `permission_error`                                                                                                                                                                                                                                                                                                       |
| **Problem**   | The API key used for this request doesn’t have the necessary permissions.                                                                                                                                                                                                                                                |
| **Solutions** | - Make sure you aren’t using a [restricted API key](https://docs.stripe.com/keys-best-practices.md#limit-access) for a service it doesn’t have access to.
  - Don’t perform actions in the Dashboard while logged in as a [user role](https://docs.stripe.com/get-started/account/teams/roles.md) that lacks permission. |

## Rate limit errors  

|  |
|  |
| **Type**      | `rate_limit_error`                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **Problem**   | You made too many API calls in too short a time.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| **Solutions** | - If a single API call triggers this error, wait and try it again.
  - To handle rate-limiting automatically, retry the API call after a delay, and increase the delay exponentially if the error continues. See the documentation on [rate limits](https://docs.stripe.com/rate-limits.md) for further advice.
  - If you anticipate a large increase in traffic and want to request an increased rate limit, [contact support](https://support.stripe.com/) in advance. |

## Signature verification errors  

|  |
|  |
| **Type**      | `signature_verification_error`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **Problem**   | You’re using *webhook* (A webhook is a real-time push notification sent to your application as a JSON payload through HTTPS requests) [signature verification](https://docs.stripe.com/webhooks.md#verify-events) and couldn’t verify that a webhook event is authentic.                                                                                                                                                                                                                                                                                                                                                                                   |
| **Solutions** | This error can occur when your integration is working correctly. If you use webhook signature verification and a third party attempts to send you a fake or malicious webhook, then verification fails and this error is the result. Catch it and respond with a `400 Bad Request` status code.

  If you receive this error when you shouldn’t—for instance, with webhooks that you know originate with Stripe—then see the documentation on [checking webhook signatures](https://docs.stripe.com/webhooks.md#verify-events) for further advice. In particular, make sure you’re using the correct endpoint secret. This is different from your API key. |