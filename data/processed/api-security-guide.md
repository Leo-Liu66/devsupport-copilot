---
source_url: https://docs.stripe.com/security/guide
source_title: Integration security guide
doc_category: api
---

# Integration security guide

Ensure PCI compliance and secure customer-server communications.

The [Payment Card Industry Data Security Standard](https://www.pcisecuritystandards.org/pci_security/) (PCI DSS) is the global security standard for all entities that store, process, or transmit cardholder or sensitive authentication data. PCI DSS sets a baseline level of protection for consumers and helps reduce fraud and data breaches across the entire payment ecosystem. Anyone involved with the processing, transmission, or storage of card data must comply with PCI DSS.

## Validate your PCI compliance 

PCI compliance is a shared responsibility and applies to both Stripe and your business:

- Stripe is certified annually by an independent PCI Qualified Security Assessor (QSA) as a [PCI Level 1](https://www.visa.com/splisting/searchGrsp.do?companyNameCriteria=stripe,%20inc) Service Provider meeting all PCI requirements.
- As a business accepting payments, you must do so in a PCI-compliant manner, and annually attest to this compliance.

Review the documentation requirements for your business in your [Dashboard](https://dashboard.stripe.com/settings/compliance/documents) and continue reading this guide to learn how Stripe can help you become PCI compliant.

## Use low risk integrations

Some business models require the intake of untokenized PANs on a payment page. If your business handles sensitive credit card data directly when accepting payments, you might be required to meet more than 300 security controls in PCI DSS. This might require you to purchase, implement, and maintain dedicated security software and hardware, and hire external auditors to support your annual assessment requirements.

Many business models don’t need to handle sensitive card data. You can instead use one of our low risk [payment integrations](https://docs.stripe.com/payments.md) to securely collect and transmit payment information directly to Stripe without it passing through your servers, reducing your PCI obligations.

### Out-of-scope card data that you can safely store 

Stripe returns non-sensitive card information in the response to a charge request. This includes the card type, the last four digits of the card, and the expiration date. This information isn’t subject to PCI compliance, so you can store any of these properties in your database. Additionally, you can store anything returned by our [API](https://docs.stripe.com/api.md).

## See also

- [PCI DSS compliance](https://stripe.com/guides/pci-compliance)
- [Best practices for managing secret API keys](https://docs.stripe.com/keys-best-practices.md)
- [Webhooks](https://docs.stripe.com/webhooks.md)
- [Declines and failed payments](https://docs.stripe.com/declines.md)
- [Disputes overview](https://docs.stripe.com/disputes.md)