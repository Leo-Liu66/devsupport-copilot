---
source_url: https://docs.stripe.com/payments/checkout
source_title: Build a payments page
doc_category: payments
---

# Build a payments page

Create a payments page with prebuilt UIs using the Checkout Sessions API.

## Accept payments on your website

Accept one-time and subscription payments from more than 100 local payment methods.
[Start building your checkout integration](https://docs.stripe.com/checkout/quickstart.md)
## Stripe Checkout 

You can use two different payment UIs with the [Checkout Sessions API](https://docs.stripe.com/api/checkout/sessions.md). The following images highlight which aspects of the checkout UI Stripe hosts in each option.
![Checkout page](https://b.stripecdn.com/docs-statics-srv/assets/checkout-hosted-hover.6ee5a154986ffc216c034a47b7b0d65e.png)

[Checkout page](https://docs.stripe.com/checkout/quickstart.md) Customers enter their payment details in a fully-featured payment page, either embedded on your site or via a redirect to a Stripe-hosted page.
![Checkout elements](https://b.stripecdn.com/docs-statics-srv/assets/checkout-elements-hover.28148f5be39600e85ef4784ab9e873e7.png)

[Checkout elements](https://docs.stripe.com/payments/quickstart-checkout-sessions.md) Build a fully customized payment page using elements

| &nbsp;                           | [PAGE](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=checkout&ui=stripe-hosted) (Recommended)                                 | [ELEMENTS](https://docs.stripe.com/payments/accept-a-payment.md?payment-ui=elements&api-integration=checkout) |
| -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| **API**                          | [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md)                                                                           | [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions.md)                                         |
| **Feature list**                 | Out of the box UI support for Billing, Tax, Adaptive Pricing, Stripe Managed Payments, Link, Dynamic payment methods, Surcharging, Split-tender | Out of the box UI support for Adaptive Pricing, Link, Dynamic payment methods                                 |
| **Order summary**                | Includes full order summary with subtotals (tax and shipping costs), cross-sells & upsells, free trials, discounts and promo codes              | No order summary                                                                                              |
| **Ongoing maintenance required** |                                                                                                                                                 |                                                                                                               |
| **Hosting**                      | Hosted or Embedded                                                                                                                              | Embedded                                                                                                      |
| **Complexity**                   | Low                                                                                                                                             | Most                                                                                                          |
| **Customization**                | 15 configurable settings via brand settings                                                                                                     | Full CSS customization via the Appearance API                                                                 |

## Customize checkout

[Customize the look and feel](https://docs.stripe.com/payments/checkout/customization.md): Customize the appearance and behavior of the checkout flow.

[Collect additional information](https://docs.stripe.com/payments/checkout/collect-additional-info.md): Collect shipping details and other customer information during checkout.

[Collect taxes](https://docs.stripe.com/payments/checkout/taxes.md): Collect taxes for one-time payments in Stripe Checkout.

[Dynamically update checkout](https://docs.stripe.com/payments/checkout/dynamic-updates.md): Make updates while your customer checks out.

[Extend checkout with custom components](https://docs.stripe.com/payments/checkout/custom-components.md): Add custom components to your payment form.

[Add trials, discounts, and upsells](https://docs.stripe.com/payments/checkout/promotions.md): Add promotions, such as trials, discounts, and optional items.

## Change when and how you collect payment

[Set up subscriptions](https://docs.stripe.com/payments/subscriptions.md): Create a subscription with recurring payments for your customers.

[Set up future payments](https://docs.stripe.com/payments/checkout/save-and-reuse.md): Save your customers’ payment details to charge them later.

[Save payment details during payment](https://docs.stripe.com/payments/checkout/save-during-payment.md): Accept a payment and save your customer’s payment details for future purchases.

[Let customers pay in their local currency](https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing.md): Use Adaptive Pricing to allow customers to pay in their local currency.

## Manage your business

[Manage your product catalog](https://docs.stripe.com/payments/checkout/product-catalog.md): Handle your inventory and fulfillment with Checkout.

[Migrate payment methods to the Dashboard](https://docs.stripe.com/payments/dashboard-payment-methods.md): Migrate the management of your payment methods to the Dashboard.

[After the payment](https://docs.stripe.com/payments/checkout/after-the-payment.md): Customize the post-payment checkout process.

## Sample projects

[One-time payments](https://github.com/stripe-samples/checkout-one-time-payments)

[Subscriptions](https://github.com/stripe-samples/checkout-single-subscription)