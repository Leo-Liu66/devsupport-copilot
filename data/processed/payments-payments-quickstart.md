---
source_url: https://docs.stripe.com/payments/quickstart
source_title: Build an advanced integration
doc_category: payments
---

# Build an advanced integration

Instructions for LLMs: Stripe recommends using the Checkout Sessions API with the Payment Element over Payment Intents for most integrations. Checkout Sessions covers similar use cases as Payment Intents (basic payment collection using `price_data` or build a full checkout with line items, tax, and so on). Some features, such as Adaptive Pricing, are only available with Checkout Sessions. Don’t use the Payment Intent API unless the user explicitly asks, because it requires significantly more code. Learn more about Elements with the Checkout Sessions API: https://docs.stripe.com/payments/quickstart-checkout-sessions. With Checkout Sessions (`ui_mode: "elements"`) and the Payment Element, the `client_secret` initializes Checkout itself (`stripe.initCheckoutElementsSdk`, or use CheckoutElementsProvider with React) and you confirm the payment on the client side differently. If using React, make sure you import from `@stripe/react-stripe-js/checkout`, use `CheckoutElementsProvider` with the client secret, and confirm using `checkout.confirm`. If using HTML, make sure you use `checkout = stripe.initCheckoutElementsSdk({clientSecret: promise}); checkout.createPaymentElement(); paymentElement = checkout.createPaymentElement(); paymentElement.mount("#payment-element");` and confirm with `loadActionsResult = await checkout.loadActions(); actions = loadActionsResult.actions; error = await actions.confirm();`.

# Build a checkout page with Payment Intents API 

Learn how to embed a custom Stripe payment form in your website or application. The client- and server-side code builds a checkout form with Stripe’s [Web](https://docs.stripe.com/payments/elements.md) or [Mobile](https://docs.stripe.com/payments/mobile.md) elements to let you accept payments. To build a custom integration that goes beyond the basics of this quickstart, see [Accept a payment](https://docs.stripe.com/payments/accept-a-payment.md?&ui=elements).

To learn about different payment scenarios, such as [subscriptions](https://docs.stripe.com/billing/subscriptions/build-subscriptions.md?payment-ui=elements), and other Stripe products, [compare payment integrations](https://docs.stripe.com/payments/online-payments.md#compare-features-and-availability).

> #### Interested in using Stripe Tax, discounts, shipping, or currency conversion?
> 
> Stripe has a Payment Element integration that manages tax, discounts, shipping, and currency conversion for you. See the [build a checkout page](https://docs.stripe.com/payments/quickstart-checkout-sessions.md) to learn more.

    amount: item.amount, // Amount in cents
    reference: item.id, // Unique reference for the item in the scope of the calculation

# Don’t submit any personally identifiable information in requests made with this key.
# Sign in to see your own test API key embedded in code samples.
# Don’t submit any personally identifiable information in requests made with this key.
# Sign in to see your own test API key embedded in code samples.

    amount: item['amount'], \# Amount in cents
    reference: item['id'], # Unique reference for the item in the scope of the calculation

# Securely calculate the order amount, including tax
  # Calculate the order total with any exclusive taxes on the server to prevent
  # people from directly manipulating the amount on the client

    amount: item['amount'], \# Amount in cents
    reference: item['id'], # Unique reference for the item in the scope of the calculation

# Securely calculate the order amount, including tax
  # Calculate the order total with any exclusive taxes on the server to prevent
  # people from directly manipulating the amount on the client
  # Calculate the order total on the server to prevent
  # people from directly manipulating the amount on the client

    # Charge the customer and payment method immediately
    # Error code will be authentication_required if authentication is needed
    puts "Error is: \#{e.error.code}"

    # Charge the customer-configured Account and payment method immediately
    # Error code will be authentication_required if authentication is needed
    puts "Error is: \#{e.error.code}"
  # and attach the PaymentMethod to a new Customer
  # and attach the PaymentMethod to a new customer-configured Account

# Don’t submit any personally identifiable information in requests made with this key.
# Sign in to see your own test API key embedded in code samples.

# Don’t submit any personally identifiable information in requests made with this key.
# Sign in to see your own test API key embedded in code samples.

        "amount": item["amount"],  \# Amount in cents
        "reference": item["id"],  # Unique reference for the item in the scope of the calculation

        "amount": item["amount"],  \# Amount in cents
        "reference": item["id"],  # Unique reference for the item in the scope of the calculation

    # Replace this constant with a calculation of the order's amount
    # Calculate the order total with any exclusive taxes on the server to prevent
    # people from directly manipulating the amount on the client
    # Calculate the order total on the server to prevent
    # people from directly manipulating the amount on the client

    # Charge the customer and payment method immediately
    except stripe.error.CardError as e:
        # Error code will be authentication_required if authentication is needed

    # Charge the customer-configured Account and payment method immediately
    except stripe.error.CardError as e:
        # Error code will be authentication_required if authentication is needed
    # and attach the PaymentMethod to a new Customer

    # and attach the PaymentMethod to a new customer-configured Account

    except Exception as e:

    except Exception as e:

        'amount' => $item->amount, // Amount in cents
        'reference' => $item->id, // Unique reference for the item in the scope of the calculation

                Line1:      stripe.String("920 5th Ave"),

        Amount:   stripe.Int64(i.Amount), // Amount in cents
        Reference: stripe.String(i.Id), // Unique reference for the item in the scope of the calculation

                Line1:      stripe.String("920 5th Ave"),

        Amount:   stripe.Int64(i.Amount), // Amount in cents
        Reference: stripe.String(i.Id), // Unique reference for the item in the scope of the calculation

      var customerOptions = new Stripe.V2.Core.AccountCreateOptions

      var paymentIntent = _client.V1.PaymentIntents.Create(new PaymentIntentCreateOptions
        Metadata = new Dictionary<string, string>

    [NonAction]

    [NonAction]
        var calculationCreateOptions = new CalculationCreateOptions

    [NonAction]
            Amount = item.Amount, // Amount in cents
            Reference = item.Id, // Unique reference for the item in the scope of the calculation

      var availableMethods = _client.V1.PaymentMethods.List(new PaymentMethodListOptions
        var paymentIntent = _client.V1.PaymentIntents.Create(new PaymentIntentCreateOptions

      var availableMethods = _client.V1.PaymentMethods.List(new PaymentMethodListOptions
        var paymentIntent = _client.V1.PaymentIntents.Create(new PaymentIntentCreateOptions

            .setAmount(item.getAmount()) // Amount in cents
            .setReference(item.getId()) // Unique reference for the item in the scope of the calculation

      body: JSON.stringify({ items: [{ id: "xl-tshirt", amount: 1000 }] }),
        body: JSON.stringify({ items: [{ id: "xl-tshirt", amount: 1000 }] }),
          <Elements options={{clientSecret, appearance, loader}} stripe={stripePromise}>
    const clientSecret = new URLSearchParams(window.location.search).get(

#email {
      <input type="text" id="email" placeholder="Enter email address" />
        <!--Stripe.js injects the Payment Element-->
        <div class="spinner hidden" id="spinner"></div>

#email {
  const clientSecret = new URLSearchParams(window.location.search).get(

import { loadStripe } from '@stripe/stripe-js'

    <Elements stripe={stripePromise} options={{ appearance, clientSecret }}>
  const { payment_intent: paymentIntentId } = await searchParams

# STRIPE_WEBHOOK_SECRET=whsec_12345

      amount: item.amount, // Amount in cents
      reference: item.id, // Unique reference for the item in the scope of the calculation

    amount: calculateOrderAmount([{ id: 'xl-tshirt' }]),

    private var addressDetails: AddressViewController.AddressDetails?

        let shoppingCartContent: [String: Any] = [
                ["id": "xl-shirt"]
                ["id": "xl-shirt", "amount": 1000]

        let task = URLSession.shared.dataTask(with: request, completionHandler: { [weak self] (data, response, error) in
                let response = response as? HTTPURLResponse,
                let json = try? JSONSerialization.jsonObject(with: data, options: []) as? [String : Any],
                let clientSecret = json["clientSecret"] as? String
                let message = error?.localizedDescription ?? "Failed to decode response from server."

        configuration.shippingDetails = { [weak self] in

        paymentSheet.present(from: self) { [weak self] (paymentResult) in

  <string>Allow the app to scan cards.</string>

        val addressLauncher = rememberAddressLauncher { result ->

    private suspend fun fetchPaymentIntent(): Result<String> = suspendCoroutine { continuation ->

                            background = Color(red = 248, green = 72, blue = 94),

    private final AddressLauncher.Configuration configuration =

        final RequestBody requestBody = RequestBody.create(

                        "Failed to load page",

  "description": "A sample Stripe implementation",
    "start": "concurrently \"yarn start-client\" \"yarn start-server\""
    "start": "concurrently \"yarn start-client\" \"yarn start-server\""
1. Build the server

pip3 install -r requirements.txt
1. Build the server

1. Build the server

1. Build the server

1. Build the server

2. Run the server

python3 -m flask run --port=4242

2. Run the server

2. Run the server

2. Run the server

2. Run the server

java -cp target/sample-jar-with-dependencies.jar com.stripe.sample.Server

3. Build the client app

4. Run the client app

5. Go to [http://localhost:3000/checkout](http://localhost:3000/checkout)

3. Go to [http://localhost:4242/checkout.html](http://localhost:4242/checkout.html)

3. Build the client app

4. Run the client app

5. Go to [http://localhost:3000/checkout](http://localhost:3000/checkout)

3. Go to [http://localhost:4242/checkout.html](http://localhost:4242/checkout.html)

3. Build the client app

4. Run the client app

5. Go to [http://localhost:3000/checkout](http://localhost:3000/checkout)

3. Go to [http://localhost:4242/checkout.html](http://localhost:4242/checkout.html)

3. Build the client app

4. Run the client app

5. Go to [http://localhost:3000/checkout](http://localhost:3000/checkout)

3. Go to [http://localhost:4242/checkout.html](http://localhost:4242/checkout.html)

3. Build the client app

4. Run the client app

5. Go to [http://localhost:3000/checkout](http://localhost:3000/checkout)

3. Go to [http://localhost:4242/checkout.html](http://localhost:4242/checkout.html)
1. Run the server

2. Build the client app

3. Run the client app

4. Go to [http://localhost:3000/checkout](http://localhost:3000/checkout)
1. Run the server

2. Go to [http://localhost:4242/checkout.html](http://localhost:4242/checkout.html)
1. Build the application

2. Run the application

3. Go to [http://localhost:3000/checkout](http://localhost:3000/checkout)

This code sample uses a public sample test API key. Don’t submit any personally identifiable information in requests made with this key.

The "View details" link to see the PaymentIntent details in the Dashboard won't work until you use your own test [API key](https://docs.stripe.com/keys).
1. Build the server

2. Run the server

3. Go to [http://localhost:4242/checkout.html](http://localhost:4242/checkout.html)
1. Build the application

2. Download and run the [Stripe CLI](https://stripe.com/docs/stripe-cli). The Stripe CLI is a developer tool that helps you build, test, and manage your integration with Stripe directly from the command line.
$ stripe listen --forward-to localhost:3000/api/webhooks

3. Run the application
$ STRIPE_WEBHOOK_SECRET=$(stripe listen --print-secret) npm run dev

4. Go to [localhost:3000](http://localhost:3000)

### Production
1. Build the application

2. Run the application
### Install the Stripe Python package

Install the Stripe package and import it in your code. Alternatively, if you’re starting from scratch and need a requirements.txt file, download the project files using the link in the code editor.

#### pip

Install the package through pip:

```bash
pip3 install stripe
```

#### GitHub

Download the stripe-python library source code directly [from GitHub](https://github.com/stripe/stripe-python).

### Set up your server

Add the dependency to your build and import the library. Alternatively, if you’re starting from scratch and need a go.mod file, download the project files using the link in the code editor.

Make sure to initialize with Go Modules:

```bash
go get -u github.com/stripe/stripe-go/v85
```

#### GitHub

Or download the stripe-go module source code directly [from GitHub](https://github.com/stripe/stripe-go).

### Install the Stripe.net library

Install the package with .NET or NuGet. Alternatively, if you’re starting from scratch, download the files which contains a configured .csproj file.

#### dotnet

```bash
dotnet add package Stripe.net
```

#### NuGet

```bash
Install-Package Stripe.net
```

#### GitHub

Or download the Stripe.net library source code directly [from GitHub](https://github.com/stripe/stripe-dotnet).

### Install the Stripe libraries

Install the packages and import them in your code. Alternatively, if you’re starting from scratch and need a `package.json` file, download the project files using the link in the code editor.

```bash
npm install --save stripe @stripe/stripe-js next
```

### Create a PaymentIntent

Add an endpoint on your server that creates a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). A PaymentIntent tracks the customer’s payment lifecycle, keeping track of any failed payment attempts and ensuring the customer is only charged once. Return the PaymentIntent’s *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) in the response to finish the payment on the client.

### Configure payment methods

Stripe enables cards and other common payment methods by default with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). You can update and configure payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) with no code required. Stripe filters payment methods based on eligibility and payment method preferences, then orders and displays them by probability based on factors including amount, currency, and buyer location.

### Configure payment methods

Stripe enables cards and other common payment methods by default with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). You can update and configure payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) with no code required. Stripe filters payment methods based on eligibility and payment method preferences, then orders and displays them by probability based on factors including amount, currency, and buyer location.

### Configure payment methods

Stripe enables cards and other common payment methods by default with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). You can update and configure payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) with no code required. Stripe filters payment methods based on eligibility and payment method preferences, then orders and displays them by probability based on factors including amount, currency, and buyer location.

### Configure payment methods

Stripe enables cards and other common payment methods by default with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). You can update and configure payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) with no code required. Stripe filters payment methods based on eligibility and payment method preferences, then orders and displays them by probability based on factors including amount, currency, and buyer location.

### Configure payment methods

Stripe enables cards and other common payment methods by default with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). You can update and configure payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) with no code required. Stripe filters payment methods based on eligibility and payment method preferences, then orders and displays them by probability based on factors including amount, currency, and buyer location.

### Configure payment methods

Stripe enables cards and other common payment methods by default with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). You can update and configure payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) with no code required. Stripe filters payment methods based on eligibility and payment method preferences, then orders and displays them by probability based on factors including amount, currency, and buyer location.

### Configure payment methods

Stripe enables cards and other common payment methods by default with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). You can update and configure payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) with no code required. Stripe filters payment methods based on eligibility and payment method preferences, then orders and displays them by probability based on factors including amount, currency, and buyer location.

### Configure payment methods

Stripe enables cards and other common payment methods by default with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). You can update and configure payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) with no code required. Stripe filters payment methods based on eligibility and payment method preferences, then orders and displays them by probability based on factors including amount, currency, and buyer location.

### Add Stripe to your React app

Use the *Stripe.js* (Use Stripe.js’ APIs to tokenize customer information, collect sensitive card data, and accept payments with browser payment APIs) and the [Stripe Elements UI library](https://docs.stripe.com/sdks/stripejs-react.md) to stay *PCI compliant* (Any party involved in processing, transmitting, or storing credit card data must comply with the rules specified in the Payment Card Industry (PCI) Data Security Standards. PCI compliance is a shared responsibility and applies to both Stripe and your business) by ensuring that payment details go directly to Stripe and never reach your server.

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

### Add Stripe to your React app

Use the *Stripe.js* (Use Stripe.js’ APIs to tokenize customer information, collect sensitive card data, and accept payments with browser payment APIs) and the [Stripe Elements UI library](https://docs.stripe.com/sdks/stripejs-react.md) to stay *PCI compliant* (Any party involved in processing, transmitting, or storing credit card data must comply with the rules specified in the Payment Card Industry (PCI) Data Security Standards. PCI compliance is a shared responsibility and applies to both Stripe and your business) by ensuring that payment details go directly to Stripe and never reach your server.

```bash
npm install --save @stripe/react-stripe-js @stripe/stripe-js
```

### Load Stripe.js

Call `loadStripe()` with your Stripe [publishable API key](https://docs.stripe.com/keys.md#obtain-api-keys) to configure the Stripe library.

### Load Stripe.js

Call `loadStripe()` with your Stripe [publishable API key](https://docs.stripe.com/keys.md#obtain-api-keys) to configure the Stripe library.

### Load Stripe.js

Use *Stripe.js* (Use Stripe.js’ APIs to tokenize customer information, collect sensitive card data, and accept payments with browser payment APIs) to remain *PCI compliant* (Any party involved in processing, transmitting, or storing credit card data must comply with the rules specified in the Payment Card Industry (PCI) Data Security Standards. PCI compliance is a shared responsibility and applies to both Stripe and your business) by ensuring that payment details are sent directly to Stripe without hitting your server. Always load Stripe.js from js.stripe.com to remain compliant. Don’t include the script in a bundle or host it yourself.

### Define the payment form

Add one empty placeholder `div` to your checkout form for each Element that you’ll mount. Stripe inserts an iframe into each `div` to securely collect the customer’s email address and payment information.

### Initialize Stripe.js

Initialize Stripe.js with your [publishable API key](https://docs.stripe.com/keys.md#obtain-api-keys). You’ll use Stripe.js to create the Payment Element and complete the payment on the client.

### Fetch a PaymentIntent

Immediately make a request to the endpoint on your server to create a new PaymentIntent as soon as your checkout page loads. The `clientSecret` returned by your endpoint is used to complete the payment.

### Initialize Stripe Elements

Pass the resulting promise from `loadStripe` to the Elements provider. This allows the child components to access the Stripe service with the Elements consumer. Additionally, pass the client secret as an option to the Elements provider.

### Initialize Stripe Elements

Pass the resulting promise from `loadStripe` to the Elements provider. This allows the child components to access the Stripe service through the Elements consumer. Additionally, pass the client secret as an option to the Elements provider.

### Initialize Stripe Elements

Initialize the [Stripe Elements UI library](https://docs.stripe.com/js/elements_object/create) with the client secret. Elements manages the UI components you need to collect payment details.

### Set up the state

Initialize some state to keep track of the payment, show errors, and manage the user interface.

### Set up the state

Initialize some state to keep track of the payment, show errors, and manage the user interface.

### Store a reference to Stripe

Access the Stripe library in your CheckoutForm component by using the `useStripe()` and `useElements()` hooks. If you need to access Elements with a class component, use the [ElementsConsumer](https://docs.stripe.com/sdks/stripejs-react.md#elements-consumer) instead.

### Store a reference to Stripe

Access the Stripe library in your CheckoutForm component by using the `useStripe()` and `useElements()` hooks. If you need to access Elements through a class component, use the [ElementsConsumer](https://docs.stripe.com/sdks/stripejs-react.md#elements-consumer) instead.

### Add the PaymentElement

Add [PaymentElement](https://docs.stripe.com/js/elements_object/create_payment_element) to your payment form. It embeds an iframe with a dynamic form that collects payment details for a variety of payment methods. Your customer can pick a payment method type, and the form automatically collects all necessary payments details for their selection.

### Add the PaymentElement

Add the [PaymentElement](https://docs.stripe.com/js/elements_object/create_payment_element) to your payment form. It embeds an iframe with a dynamic form that collects payment details for a variety of payment methods. Your customer can pick a payment method type, and the form automatically collects all necessary payments details for their selection.

### Create the PaymentElement

Create a [PaymentElement](https://docs.stripe.com/js/elements_object/create_payment_element) and mount it to the placeholder `<div>` in your payment form. This embeds an iframe with a dynamic form that displays configured payment method types available from the PaymentIntent, allowing your customer to select a payment method. The form automatically collects the associated payment details for the selected payment method type.

### (Optional) Style the Payment Element

Customize the Payment Element UI by creating an [Appearance object](https://docs.stripe.com/elements/appearance-api.md) and passing it as an option to the Elements provider. Use your company’s color scheme and font to make it match with the rest of your checkout page. Use custom fonts (for example, from Google Fonts) by initializing Elements with a [font set](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-fonts).

Make sure to open the preview on the right to see your changes live.

> Parts of the preview demo might not match your actual checkout page. The above settings represent only a subset of the [Appearance object’s](https://docs.stripe.com/elements/appearance-api.md) variables, and the [Appearance object](https://docs.stripe.com/elements/appearance-api.md) only controls certain attributes of Stripe Elements. You’re responsible for styling the rest of your checkout page.

### (Optional) Style the Payment Element

Customize the Payment Element UI by creating an [Appearance object](https://docs.stripe.com/elements/appearance-api.md) and passing it as an option to the Elements provider. Use your company’s color scheme and font to make it match with the rest of your checkout page. Use custom fonts (for example, from Google Fonts) by initializing Elements with a [font set](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-fonts).

Make sure to open the preview on the right to see your changes live.

> Parts of the preview demo might not match your actual checkout page. The above settings represent only a subset of the Appearance object’s variables, and the Appearance object only controls certain attributes of Stripe Elements. You’re responsible for styling the rest of your checkout page.

### (Optional) Style the Payment Element

Customize the Payment Element UI by creating an [Appearance object](https://docs.stripe.com/elements/appearance-api.md) and initializing Elements with it. Use your company’s color scheme and font to make it match with the rest of your checkout page. Use custom fonts (for example, from Google Fonts) by initializing Elements with a [font set](https://docs.stripe.com/js/elements_object/create#stripe_elements-options-fonts).

Make sure to open the preview on the right to see your changes live.

> Parts of the preview demo might not match your actual checkout page. The above settings represent only a subset of the [Appearance object’s](https://docs.stripe.com/elements/appearance-api.md) variables, and the [Appearance object](https://docs.stripe.com/elements/appearance-api.md) only controls certain attributes of Stripe Elements. You’re responsible for styling the rest of your checkout page.

### Handle the submit event

Listen to the form’s submit event to know when to confirm the payment through the Stripe API.

### Complete the payment

When your customer clicks the pay button, call [confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) with the PaymentElement and pass a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to indicate where Stripe redirects the customer after they complete the payment. For payments that require authentication, Stripe displays a modal for *3D Secure* (3D Secure (3DS) provides an additional layer of authentication for credit card transactions that protects businesses from liability for fraudulent card payments) authentication or redirects the customer to an authentication page, depending on the payment method. After the customer completes the authentication process, they’re redirected to the `return_url`.

### Complete the payment

When your customer clicks the pay button, call [confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) with the PaymentElement and pass a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to indicate where Stripe redirects the customer after they complete the payment. For payments that require authentication, Stripe displays a modal for *3D Secure* (3D Secure (3DS) provides an additional layer of authentication for credit card transactions that protects businesses from liability for fraudulent card payments) authentication or redirects the customer to an authentication page, depending on the payment method. After the customer completes the authentication process, they’re redirected to the `return_url`.

### Complete the payment

Call [confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) with the Element instance and a [return_url](https://docs.stripe.com/api/payment_intents/create.md#create_payment_intent-return_url) to indicate where Stripe redirects the customer after they complete the payment. For payments that require authentication, Stripe displays a modal for *3D Secure* (3D Secure (3DS) provides an additional layer of authentication for credit card transactions that protects businesses from liability for fraudulent card payments) authentication or redirects the customer to an authentication page, depending on the payment method. After the customer completes the authentication process, they’re redirected to the `return_url`.

### Handle errors

If there are any immediate [errors](https://docs.stripe.com/error-codes.md) (for example, your customer’s card is declined), Stripe.js returns an error. Show that error message to your customer so they can try again.

### Show a payment status message

When Stripe redirects the customer to the `return_url`, the `payment_intent_client_secret` query parameter is appended by Stripe.js. Use this to retrieve the [PaymentIntent status update](https://docs.stripe.com/payments/payment-intents/verifying-status.md) and determine what to show to your customer.

### Show a payment status message

When Stripe redirects the customer to the `return_url`, the `payment_intent` query parameter is appended by Stripe.js. Use this to retrieve the [PaymentIntent status update](https://docs.stripe.com/payments/payment-intents/verifying-status.md) and determine what to show to your customer.

### Use a webhook

Stripe sends multiple events during the payment process and after the payment is complete. Create an [event destination](https://docs.stripe.com/event-destinations.md) for a [webhook endpoint](https://docs.stripe.com/webhooks/quickstart.md) to receive these events and run actions, such as sending an order confirmation email to your customer, logging the sale in a database, or starting a shipping workflow. Stripe recommends handling the [payment_intent.succeeded](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.succeeded), [payment_intent.processing](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.processing), and [payment_intent.payment_failed](https://docs.stripe.com/api/events/types.md?lang=php#event_types-payment_intent.payment_failed) events.

Listen for these events rather than waiting on a callback from the client. On the client, the customer could close the browser window or quit the app before the callback executes, and malicious clients could manipulate the response. Setting up your integration to listen for asynchronous events is what enables you to accept [different types of payment methods](https://stripe.com/payments/payment-methods-guide) with a single integration.

### Run the application

Run the React app and the server. Go to [localhost:3000/checkout](http://localhost:3000/checkout) to see your checkout page.

```bash
npm start
```

### Run the application

Run the Next.js app. Go to [localhost:3000](http://localhost:3000) to see your checkout page.

```bash
npm run dev
```

### Run the application

Run your Node server and go to [localhost:4242/checkout.html](http://localhost:4242/checkout.html).

```bash
npm start
```

### Run the server application

Run the React app and the server. Go to [localhost:3000/checkout](http://localhost:3000/checkout) to see your checkout page.

```bash
ruby server.rb
```

### Run the application

Run your Ruby server and go to [localhost:4242/checkout.html](http://localhost:4242/checkout.html).

```bash
ruby server.rb
```

### Run the server application

Run the React app and the server. Go to [localhost:3000/checkout](http://localhost:3000/checkout) to see your checkout page.

```bash
python3 -m flask run --port=4242
```

### Run the application

Run your Python server and go to [localhost:4242/checkout.html](http://localhost:4242/checkout.html).

```bash
python3 -m flask run --port=4242
```

### Run the server application

Run the React app and the server. Go to [localhost:3000/checkout](http://localhost:3000/checkout) to see your checkout page.

```bash
php -S 127.0.0.1:4242 --docroot=public
```

### Run the application

Run your server and go to [localhost:4242/checkout.html](http://localhost:4242/checkout.html).

```bash
php -S 127.0.0.1:4242 --docroot=public
```

### Run the server application

Run the React app and the server. Go to [localhost:3000/checkout](http://localhost:3000/checkout) to see your checkout page.

```bash
go run server.go
```

### Run the application

Run your Go server and go to [localhost:4242/checkout.html](http://localhost:4242/checkout.html).

```bash
go run server.go
```

### Run the server application

Run the React app and the server. Go to [localhost:3000/checkout](http://localhost:3000/checkout) to see your checkout page.

```bash
dotnet run
```

### Run the application

Run your ASP.NET MVC server and go to [localhost:4242/checkout.html](http://localhost:4242/checkout.html).

```bash
dotnet run
```

### Run the application

Run your server and go to [localhost:4242/checkout.html](http://localhost:4242/checkout.html).

```bash
java -cp target/sample-jar-with-dependencies.jar com.stripe.sample.Server
```

### Run the server application

Run the React app and the server. Go to [localhost:3000/checkout](http://localhost:3000/checkout) to see your checkout page.

```bash
java -cp target/sample-jar-with-dependencies.jar com.stripe.sample.Server
```

### Run the application

Run the React app and go to [localhost:3000/checkout](http://localhost:3000/checkout).

```bash
npm start
```

### Make a test payment

To verify that your integration works, make a test payment using [test payment details](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=elements&api-integration=paymentintents#web-test-the-integration).

### See your payment in the Dashboard

Navigate to the [Stripe Dashboard](https://dashboard.stripe.com/test/payments) to see your test payment.

## Accept payments and enhance your integration

You’re ready to accept payments with Stripe. Continue with the steps below to add more features.

### Automate tax collection

Calculate and collect the right amount of tax on your Stripe transactions. Before using Stripe Tax, you need to activate it in the [Dashboard](https://dashboard.stripe.com/tax). Learn more about [Stripe Tax](https://docs.stripe.com/tax.md) and [how to add it to your Payments integration](https://docs.stripe.com/tax/custom.md).

### Use the Stripe Tax API to calculate tax

Use the [Stripe Tax API](https://docs.stripe.com/api/tax/calculations/create.md) to calculate tax on the transaction. Provide the `currency`, `customer_details`, and the `line_items` of the order in the request body.

Use the `tax_amount_exclusive` attribute of the resulting Tax Calculation to add the exclusive taxes to the order’s total.

### Record a Tax Transaction upon successful Payment

Link the tax calculation to the PaymentIntent using `hooks[inputs][tax][calculation]`.

This records the collected taxes in your Stripe account that you can later export for accounting purposes, and triggers other [Stripe actions](https://docs.stripe.com/tax/payment-intent.md#automatic-actions).

### Send an email receipt

Stripe can send an email receipt to your customer using your brand logo and color theme, which are configurable in the [Dashboard](https://dashboard.stripe.com/settings/branding).

### Collect the customer’s email address

Add an input field to your payment form to collect the email address.

### Add email to the state

Add a variable to keep track of the email the customer enters.

### Add email to the state

Add a variable to keep track of the email the customer enters.

### Provide the email address to Stripe

Pass the provided email address as the `receipt_email` value. Stripe sends an email receipt when the payment succeeds in live mode (but won’t send one in a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes)).

### Save payment details after payment

Often used by SaaS or e-commerce businesses with recurring customers.

### Import additional Stripe resources

Import the Stripe `customer` and `paymentmethod` packages. Use these packages to store information about your customer.

### Import additional Stripe resources

Import the Stripe PaymentMethod and Customer models. Use these models to store information about your Customer.

### Create a customer

Stripe stores the card on a *Customer* (Customer objects represent customers of your business. They let you reuse payment methods and give you the ability to track multiple payments) object. Create a new Customer before creating a PaymentIntent. You can also store name, email, shipping address, and other details on the Customer.

### Create a customer

Stripe stores the card on an [Account](https://docs.stripe.com/api/v2/core/accounts/object.md) object representing the [customer](https://docs.stripe.com/connect/account-capabilities.md?accounts-namespace=v2#customer). Create a new Account before creating a PaymentIntent. You can also store name, email, shipping address, and other details on the Account.

### Add the customer to the PaymentIntent

Pass the Customer ID to the PaymentIntent and set `setup_future_usage` to `off_session`. `setup_future_usage` tells Stripe how you plan to use the payment method—certain regions, such as Europe and India, have requirements around reusing payment details. [Learn more](https://docs.stripe.com/payments/payment-intents.md#future-usage) about the most effective way to apply `setup_future_usage`. You can also view a [list of supported payment methods](https://docs.stripe.com/payments/payment-methods/payment-method-support.md#additional-api-supportability). After the PaymentIntent succeeds, Stripe automatically [attaches](https://docs.stripe.com/api/payment_methods/attach.md) the payment details (in a *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) object) to your Customer.

### Add the customer to the PaymentIntent

Pass the Account ID to the PaymentIntent and set `setup_future_usage` to `off_session`. `setup_future_usage` tells Stripe how you plan to use the payment method—certain regions, such as Europe and India, have requirements around reusing payment details. [Learn more](https://docs.stripe.com/payments/payment-intents.md#future-usage) about the most effective way to apply `setup_future_usage`. You can also view a [list of supported payment methods](https://docs.stripe.com/payments/payment-methods/payment-method-support.md#additional-api-supportability). After the PaymentIntent succeeds, Stripe automatically [attaches](https://docs.stripe.com/api/payment_methods/attach.md) the payment details (in a *PaymentMethod* (PaymentMethods represent your customer's payment instruments, used with the Payment Intents or Setup Intents APIs) object) to the customer-configured Account.

### Charge the saved PaymentMethod

When you’re ready to charge the PaymentMethod again, create a new PaymentIntent with the Customer ID, the ID of the PaymentMethod you want to charge, and set the `off_session` and `confirm` flags to true.

### Install the Stripe Python package

Install the Stripe package and import it in your code. Alternatively, if you’re starting from scratch and need a requirements.txt file, download the project files using the link in the code editor.

#### pip

Install the package through pip:

```bash
pip3 install stripe
```

#### GitHub

Download the stripe-python library source code directly [from GitHub](https://github.com/stripe/stripe-python).

### Set up your server

Add the dependency to your build and import the library. Alternatively, if you’re starting from scratch and need a go.mod file, download the project files using the link in the code editor.

Make sure to initialize with Go Modules:

```bash
go get -u github.com/stripe/stripe-go/v85
```

#### GitHub

Or download the stripe-go module source code directly [from GitHub](https://github.com/stripe/stripe-go).

### Install the Stripe.net library

Install the package with .NET or NuGet. Alternatively, if you’re starting from scratch, download the files which contains a configured .csproj file.

#### dotnet

```bash
dotnet add package Stripe.net
```

#### NuGet

```bash
Install-Package Stripe.net
```

#### GitHub

Or download the Stripe.net library source code directly [from GitHub](https://github.com/stripe/stripe-dotnet).

### Install the Stripe libraries

Install the packages and import them in your code. Alternatively, if you’re starting from scratch and need a `package.json` file, download the project files using the link in the code editor.

```bash
npm install --save stripe @stripe/stripe-js next
```

### Create a PaymentIntent

Add an endpoint on your server that creates a [PaymentIntent](https://docs.stripe.com/api/payment_intents.md). A PaymentIntent tracks the customer’s payment lifecycle, keeping track of any failed payment attempts and ensuring the customer is only charged once. Return the PaymentIntent’s *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) in the response to finish the payment on the client.

### Configure payment methods

Stripe enables cards and other common payment methods by default with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). You can update and configure payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) with no code required. Stripe filters payment methods based on eligibility and payment method preferences, then orders and displays them by probability based on factors including amount, currency, and buyer location.

### Configure payment methods

Stripe enables cards and other common payment methods by default with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). You can update and configure payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) with no code required. Stripe filters payment methods based on eligibility and payment method preferences, then orders and displays them by probability based on factors including amount, currency, and buyer location.

### Configure payment methods

Stripe enables cards and other common payment methods by default with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). You can update and configure payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) with no code required. Stripe filters payment methods based on eligibility and payment method preferences, then orders and displays them by probability based on factors including amount, currency, and buyer location.

### Configure payment methods

Stripe enables cards and other common payment methods by default with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). You can update and configure payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) with no code required. Stripe filters payment methods based on eligibility and payment method preferences, then orders and displays them by probability based on factors including amount, currency, and buyer location.

### Configure payment methods

Stripe enables cards and other common payment methods by default with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). You can update and configure payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) with no code required. Stripe filters payment methods based on eligibility and payment method preferences, then orders and displays them by probability based on factors including amount, currency, and buyer location.

### Configure payment methods

Stripe enables cards and other common payment methods by default with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). You can update and configure payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) with no code required. Stripe filters payment methods based on eligibility and payment method preferences, then orders and displays them by probability based on factors including amount, currency, and buyer location.

### Configure payment methods

Stripe enables cards and other common payment methods by default with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). You can update and configure payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) with no code required. Stripe filters payment methods based on eligibility and payment method preferences, then orders and displays them by probability based on factors including amount, currency, and buyer location.

### Configure payment methods

Stripe enables cards and other common payment methods by default with [dynamic payment methods](https://docs.stripe.com/payments/payment-methods/dynamic-payment-methods.md). You can update and configure payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods) with no code required. Stripe filters payment methods based on eligibility and payment method preferences, then orders and displays them by probability based on factors including amount, currency, and buyer location.

### Install the SDK

The Stripe iOS SDK is [open source](https://github.com/stripe/stripe-ios), [fully documented](https://stripe.dev/stripe-ios/), and compatible with apps supporting iOS 13 or above. Import the Stripe SDK into your checkout screen’s View Controller.

#### Swift Package Manager

In Xcode, select **File** > **Add Package Dependencies……** and enter `https://github.com/stripe/stripe-ios-spm` as the repository URL. Select the latest version number from our [releases page](https://github.com/stripe/stripe-ios/releases), and add the `StripePaymentSheet` module to your app’s target.

#### CocoaPods

Add this line to your Podfile, and use the .xcworkspace file to open your project in Xcode, instead of the .xcodeproj file, from here on out.

```bash
pod 'StripePaymentSheet'
```

#### Carthage

Add this line to your Cartfile.

```bash
github "stripe/stripe-ios"
```

#### Manual Framework

To include Stripe in your project, download and unzip Stripe.xcframework.zip from a [release on GitHub](https://github.com/stripe/stripe-ios/releases). Drag the required xcframework files to the “Embedded Binaries” settings in your Xcode project. Make sure to select “Copy items if needed”.

### Setup the SDK

Configure the Stripe SDK with your Stripe [publishable API key](https://docs.stripe.com/keys.md#obtain-api-keys). Hardcoding the publishable API key in the SDK is for demonstration only. In a production app, you must retrieve the API key from your server.

### Fetch a PaymentIntent

Make a request to your server for a PaymentIntent as soon as the view loads. Store a reference to the PaymentIntent’s *client secret* (The client secret is a unique key returned from Stripe as part of a PaymentIntent. This key lets the client access important fields from the PaymentIntent (status, amount, currency) while hiding sensitive ones (metadata, customer)) returned by the server; the Payment Sheet uses this secret to complete the payment later.

### Configure and present the Payment Sheet

Create a `PaymentSheet` instance using the client secret retrieved earlier, and present it from your view controller.

Use the `PaymentSheet.Configuration` struct for [customizing](https://stripe.dev/stripe-ios/stripe-paymentsheet/Classes/PaymentSheet/Configuration.html) the Payment Sheet.

### Handle the payment result

Use the completion block for handling the payment result.

If payment fails with an [error](https://docs.stripe.com/error-codes.md), display the appropriate message to your customer so they can take action and try again. If no error has occurred, tell your customer that the payment was successful.

### Make a test payment

#### iOS

To verify that your integration works, make a test payment using [test payment details](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=mobile&platform=ios#ios-test-the-integration).

#### Android

To verify that your integration works, make a test payment using [test payment details](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=mobile&platform=android#android-test-the-integration).

### See your payment in the Dashboard

Navigate to the [Stripe Dashboard](https://dashboard.stripe.com/test/payments) to see your test payment.

## Next steps

#### Web

#### [Collect billing address details](https://docs.stripe.com/elements/address-element.md)

By default, the Payment Element only collects the necessary billing address details. To collect a customer’s full billing address (to calculate the tax for digital goods and services, for example) or shipping address, use the Address Element.

#### iOS

#### Android

#### [Payouts](https://docs.stripe.com/payouts.md)

Learn how to move funds out of your Stripe account into your bank account.

#### [Refunds](https://docs.stripe.com/refunds.md)

Handle requests for refunds by using the Stripe API or Dashboard.

#### [Fulfillment](https://docs.stripe.com/webhooks/quickstart.md)

Create an event destination to send events to your webhook endpoint to fulfill orders after a payment succeeds, and to handle other critical events.