---
source_url: https://docs.stripe.com/payouts
source_title: Receive payouts
doc_category: refunds
---

# Receive payouts

Set up your bank account to receive payouts.

You receive funds when Stripe (or your platform) makes payouts to your bank account. Payout availability varies depending on your industry and country of operation. When you start processing live payments, Stripe typically schedules your initial payout for 7-14 days after you successfully receive your first payment. Your first payout might take longer, depending on your industry risk level and country of operation. Subsequent payouts follow your account’s [payout schedule](https://docs.stripe.com/payouts.md#payout-schedule).

You can see a comprehensive list of your payouts and the expected dates of deposit into your bank account in the [Dashboard](https://dashboard.stripe.com/test/payouts). If you’re a *Connect* (Connect is Stripe's solution for multi-party businesses, such as marketplace or software platforms, to route payments between sellers, customers, and other recipients) platform, see [Connect payouts](https://docs.stripe.com/connect/payouts-connected-accounts.md).

## Payout schedule 

Your payout schedule determines when Stripe sends money to your bank account. You can select your preferred payout schedule during onboarding or update it any time in the Stripe Dashboard.

> #### Time zone difference
> 
> All payments and payouts are processed according to [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) time, [except for Asia-Pacific (APAC) markets](https://support.stripe.com/questions/default-start-of-day-for-asia-pacific-%28apac%29-payouts). As a result, the processed date might not be the same as your local time zone.

| Payout schedule           | Description                                                                                                                                                        |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Manual payouts            | You choose when to send payouts and how much to transfer.                                                                                                          |
| Daily payouts             | Stripe automatically transfers your available funds every business day.                                                                                            |
| Weekly or monthly payouts | You can specify particular days of the week or days of the month for payouts. For example, payouts on Mondays and Thursdays, or on the 1st and 15th of each month. |
| Monthly adjustments       | If your selected payout day doesn’t exist in a given month (for example, the 31st in a 30-day month), Stripe moves the payout to the last day of that month.       |
| Non-business days         | Payouts scheduled on weekends or holidays arrive on the next business day.                                                                                         |

### How payout timing works

Choosing a payout schedule doesn’t change how long it takes for your pending balance to become available. It only controls when payouts are sent.

For example, if your account is set to daily payouts with a 3-business-day [settlement timing](https://docs.stripe.com/payouts.md#payout-speed), Stripe pays out funds daily from transactions that were captured three business days earlier.

### Country-specific payout restrictions

Some countries have preset payout schedules due to local regulations:

- Brazil and India: Payouts are always automatic and daily.
- Japan: Daily payouts aren’t available. The default schedule is manual. You can also choose weekly and monthly payout schedules.
- Thailand: The default schedule is daily automatic payouts.

These restrictions might differ if you use [cross-border payouts](https://docs.stripe.com/connect/cross-border-payouts.md).

### Manual payouts

If you turn off automatic payouts, you must manually send funds to your bank account. You can do this in the [Dashboard](https://dashboard.stripe.com/settings/payouts) or by using the API to [create payouts](https://docs.stripe.com/api.md#create_payout).

Manual payouts are available in all regions except Brazil and India, where payouts are always automatic and daily. In most regions, manual payouts typically take 1-4 business days to arrive in your bank account after initiating the manual payout.

If your Stripe account that operates in the United Kingdom has a standard [T+3 settlement timing](https://docs.stripe.com/payouts.md#payout-speed) and you initiate a manual payout during business hours, the funds typically arrive in your bank account on the same business day. This same-day payout is limited to 10 same-day manual payouts per day, with a maximum transaction amount of 1 million GBP each. All other manual payouts typically arrive within 2 business days in your bank account.

If your Stripe account that operates in the United States has a standard [T+2 settlement timing](https://docs.stripe.com/payouts.md#payout-speed) and you initiate a manual payout during business hours, the funds typically arrive in your bank account on the same business day. This payout is subject to an account limit of 10 manual payouts per day and a maximum transaction amount of 1 million USD. All other manual payouts typically arrive within 1 business day in your bank account.

## Settlement timing 

The payout schedule refers to the cadence that your funds are paid out, for example, day of the week. The settlement timing refers to the amount of time it takes for your funds to become available. Settlement timing varies per country and is typically expressed as “T+X” days. Some payment processors might start “T” from their internal settlement time, meaning when the funds land in their bank accounts.

Stripe uses “T” to refer to the transaction time, which indicates the time of the original payment confirmation or capture, and the counting starts earlier. If your Stripe account is in a country with a T+3 standard settlement timing and you use a manual payout schedule, your Stripe balance is available for payout within three business days of capturing a payment. However, if you use a daily automatic payout schedule with a T+3 standard settlement timing, Stripe pays out funds daily from transactions captured 3 business days earlier.

Most banks deposit payouts into your bank account as soon as they receive them, though some might take a few extra days to make them available. The type of business and the country you’re in can also affect payout timing.

### Definition of days

There are two definitions of days that affect settlement and payout timing:

- **Calendar days**: Includes every day, including weekends and holidays.
- **Business days**: Only includes working days, typically Monday through Friday, and excludes public holidays.

For example, a charge created on a Saturday could have two different timings depending on which definition of day you use:

- If you use calendar days, Saturday is day 0.
- If you use business days, the next Monday is day 0.

### Delay behavior per account country 

As the platform, you can set [delay_days](https://docs.stripe.com/connect/manage-payout-schedule.md#delay_days) on your connected accounts. The delay applies as a **business day** or **calendar day** delay, based on the country of the connected account. The following table shows which countries apply the delay by business or calendar day.

| Country                                                              | Delay type                       |
| -------------------------------------------------------------------- | -------------------------------- |
| AU, IN, JP, MY, NZ, TH, AE, US                                       | Business day (Monday - Friday)   |
| BR1, CA, GI, HK, LI, MX, NO, SG2, CH, GB, and supported EU countries | Calendar day (Sunday - Saturday) |

1 Delays for Pix, Boleto, debit, and prepaid payouts in Brazil apply in business days.

2 Delays for PayNow in Singapore apply in business days.

### Settlement timing by country 

Use the following collapsed table to determine your country’s settlement timing. The initial settlement timing applies to your first payout, and the default settlement timing applies to subsequent payouts.

> In some cases, risk criteria might prevent your account from changing to the default settlement timing.

### Country and settlement timing

| Country              | Initial settlement timing                                                                                              | Default settlement timing |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| Australia            | 2 business days                                                                                                        | —                         |
| Austria              | 7 calendar days                                                                                                        | 3 business days           |
| Belgium              | 7 calendar days                                                                                                        | 3 business days           |
| Bulgaria             | 7 calendar days                                                                                                        | 3 business days           |
| Brazil               | - 30 calendar days
  - 5 calendar days for international charges
  - 2 business days for Boleto and Pix payments       | —                         |
| Canada               | 7 calendar days                                                                                                        | 3 business days           |
| Croatia              | 7 calendar days                                                                                                        | 3 business days           |
| Cyprus               | 7 calendar days                                                                                                        | 3 business days           |
| Czech Republic       | 7 calendar days                                                                                                        | 3 business days           |
| Denmark              | 7 calendar days                                                                                                        | 3 business days           |
| Estonia              | 7 calendar days                                                                                                        | 3 business days           |
| Finland              | 7 calendar days                                                                                                        | 3 business days           |
| France               | 7 calendar days                                                                                                        | 3 business days           |
| Germany              | 7 calendar days                                                                                                        | 3 business days           |
| Gibraltar            | 7 calendar days                                                                                                        | 3 business days           |
| Greece               | 7 calendar days                                                                                                        | 3 business days           |
| Hong Kong            | 7 calendar days                                                                                                        | —                         |
| Hungary              | 7 calendar days                                                                                                        | 3 business days           |
| India                | - 2 business days for domestic charges
  - 5 business days for international charges                                   | —                         |
| Ireland              | 7 calendar days                                                                                                        | 3 business days           |
| Italy                | 7 calendar days                                                                                                        | 3 business days           |
| Japan                | Payouts are made once per week (on a day of your choosing) and include payments processed up to 4 business days prior. | —                         |
| Latvia               | 7 calendar days                                                                                                        | 3 business days           |
| Liechtenstein        | 7 calendar days                                                                                                        | 3 business days           |
| Lithuania            | 7 calendar days                                                                                                        | 3 business days           |
| Luxembourg           | 7 calendar days                                                                                                        | 3 business days           |
| Malaysia             | 7 calendar days                                                                                                        | —                         |
| Malta                | 7 calendar days                                                                                                        | 3 business days           |
| Mexico               | 7 calendar days                                                                                                        | 3 business days           |
| Netherlands          | 7 calendar days                                                                                                        | 3 business days           |
| New Zealand          | 4 business days                                                                                                        | —                         |
| Norway               | 7 calendar days                                                                                                        | 3 business days           |
| Poland               | 7 calendar days                                                                                                        | 3 business days           |
| Portugal             | 7 calendar days                                                                                                        | 3 business days           |
| Romania              | 7 calendar days                                                                                                        | 3 business days           |
| Singapore            | 7 calendar days                                                                                                        | —                         |
| Slovakia             | 7 calendar days                                                                                                        | 3 business days           |
| Slovenia             | 7 calendar days                                                                                                        | 3 business days           |
| Spain                | 7 calendar days                                                                                                        | 3 business days           |
| Sweden               | 7 calendar days                                                                                                        | 3 business days           |
| Switzerland          | 7 calendar days                                                                                                        | 3 business days           |
| Thailand             | 7 business days                                                                                                        | —                         |
| United Arab Emirates | 5 business days                                                                                                        | —                         |
| United Kingdom       | 7 calendar days                                                                                                        | 3 business days           |
| United States        | 2 business days                                                                                                        | —                         |

### Settlement timing by payment method 

Bank debit payment methods typically have longer settlement times than card payments because of the underlying banking systems. These payments have a higher risk of returns or reversals, which factors into their longer settlement periods.

| Payment method       | Settlement timing |
| -------------------- | ----------------- |
| ACH Debit            | 4 business days   |
| SEPA Direct Debit    | 6 business days   |
| Bacs Direct Debit    | 4 business days   |
| AU BECS Direct Debit | 2 business days   |
| NZ BECS Direct Debit | 2 business days   |
| PAD Canada           | 5 business days   |

To manage your cash flow and cover potential refunds, disputes, and fees that might lead to negative balances, you can set a [minimum balance](https://docs.stripe.com/payouts/minimum-balances-for-automatic-payouts.md) in your Stripe account.

## Accelerate settlement timing

Stripe offers products and payment methods that have reduced settlement time depending on your location and are subject to eligibility criteria.

### 2-day ACH settlement

For eligible US merchants, Stripe offers faster ACH settlement that reduces the settlement time from 4 business days to 2 business days from payment creation. For more details about eligibility and activation, see the [ACH support page](https://support.stripe.com/questions/two-day-settlement-for-ach-direct-debit).

### Instant Payouts

With [Instant Payouts](https://docs.stripe.com/payouts/instant-payouts.md), you can instantly send funds to a supported debit card or bank account. You can request Instant Payouts any time, including weekends and holidays, and funds usually appear in the associated bank account within 30 minutes. New Stripe users aren’t immediately eligible for Instant Payouts. You can check your [eligibility](https://docs.stripe.com/payouts/instant-payouts.md#eligibility-and-daily-volume-limits) in the [Dashboard](https://dashboard.stripe.com/payouts/instant_payouts_eligibility).

## Negative payouts 

Each payout reflects your available account balance at the time it was created. In some cases, you might have a negative account balance. For example, if you receive 100 USD in payments but refund 200 USD of prior payments, your account balance would be -100 USD. If you don’t receive further payments to balance out the negative amount, Stripe creates a payout that *debits* your bank account.

Your bank account must support both credit and debit transactions so that Stripe can perform any required payouts.

## Test payouts

Use the following test bank and debit card numbers to trigger certain events when testing [payouts](https://docs.stripe.com/connect/payouts-connected-accounts.md). You can only use these values while testing with test API keys.

Test payouts simulate a live payout but aren’t processed with the bank. Test accounts with Stripe Dashboard access always have payouts enabled, as long as valid external bank information and other relevant conditions are met, and never requires real identity verification.

> You can’t use test bank and debit card numbers in the Stripe Dashboard on a live mode connected account. If you’ve entered your bank account information on a live mode account, you can still use a sandbox, and test payouts will simulate a live payout without processing actual money.

### Bank numbers 

Use these test bank account numbers to test payouts. You can only use them with test API keys.

### Debit card numbers 

Use these test debit card numbers to test payouts to a debit card. You can only use them with test API keys.

#### United States

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000056655665556 | `tok_visa_debit_us_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000056655665572 | `tok_visa_debit_us_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000056755665555 | `tok_visa_debit_us_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5200828282828210 | `tok_mastercard_debit_us_transferSuccess`    | Mastercard debit. Payout succeeds.                        |
| 6011981111111113 | `tok_discover_debit_us_transferSuccess`      | Discover debit. Payout succeeds.                          |

#### Canada

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000051240000005 | `tok_visa_debit_ca_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000051240000021 | `tok_visa_debit_ca_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000051240000039 | `tok_visa_debit_ca_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5510121240000006 | `tok_mastercard_debit_ca_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Singapore

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000057020000008 | `tok_visa_debit_sg_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000057020000016 | `tok_visa_debit_sg_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000057020000024 | `tok_visa_debit_sg_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 2227200000000009 | `tok_mastercard_debit_sg_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Australia

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000050360000019 | `tok_visa_debit_au_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000050360000027 | `tok_visa_debit_au_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000050360000035 | `tok_visa_debit_au_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 4000000360000006 | `tok_visa_credit_au`                         | Visa credit. Card Not Supported (invalid card type).      |
| 5555050360000023 | `tok_mastercard_debit_au_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### United Arab Emirates

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000057840000006 | `tok_visa_debit_ae_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000057840000014 | `tok_visa_debit_ae_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000057840000022 | `tok_visa_debit_ae_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 4000007840000006 | `tok_visa_credit_ae`                         | Visa credit. Card Not Supported (invalid card type).      |
| 5555057840000002 | `tok_mastercard_debit_ae_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### United Kingdom

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000058260000203 | `tok_visa_debit_gb_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000058260000211 | `tok_visa_debit_gb_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000058260000229 | `tok_visa_debit_gb_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555058260000100 | `tok_mastercard_debit_gb_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Austria

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000050400000003 | `tok_visa_debit_at_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000050400000011 | `tok_visa_debit_at_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000050400000029 | `tok_visa_debit_at_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555050400000009 | `tok_mastercard_debit_at_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Belgium

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000050560000009 | `tok_visa_debit_be_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000050560000017 | `tok_visa_debit_be_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000050560000025 | `tok_visa_debit_be_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555050560000005 | `tok_mastercard_debit_be_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Croatia

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000051910000004 | `tok_visa_debit_hr_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000051910000012 | `tok_visa_debit_hr_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000051910000020 | `tok_visa_debit_hr_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555051910000000 | `tok_mastercard_debit_hr_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Cyprus

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000051960000003 | `tok_visa_debit_cy_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000051960000011 | `tok_visa_debit_cy_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000051960000029 | `tok_visa_debit_cy_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555051960000009 | `tok_mastercard_debit_cy_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Estonia

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000052330000004 | `tok_visa_debit_ee_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000052330000012 | `tok_visa_debit_ee_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000052330000020 | `tok_visa_debit_ee_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555052330000000 | `tok_mastercard_debit_ee_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Finland

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000052460000006 | `tok_visa_debit_fi_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000052460000014 | `tok_visa_debit_fi_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000052460000022 | `tok_visa_debit_fi_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555052460000002 | `tok_mastercard_debit_fi_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### France

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000052500000008 | `tok_visa_debit_fr_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000052500000016 | `tok_visa_debit_fr_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000052500000024 | `tok_visa_debit_fr_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555052500000004 | `tok_mastercard_debit_fr_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Germany

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000052760000037 | `tok_visa_debit_de_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000052760000011 | `tok_visa_debit_de_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000052760000029 | `tok_visa_debit_de_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555052760000009 | `tok_mastercard_debit_de_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Greece

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000053000000001 | `tok_visa_debit_gr_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000053000000019 | `tok_visa_debit_gr_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000053000000027 | `tok_visa_debit_gr_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555053000000007 | `tok_mastercard_debit_gr_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Ireland

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000053720000000 | `tok_visa_debit_ie_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000053720000018 | `tok_visa_debit_ie_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000053720000026 | `tok_visa_debit_ie_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555053720000006 | `tok_mastercard_debit_ie_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Italy

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000053800000037 | `tok_visa_debit_it_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000053800000011 | `tok_visa_debit_it_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000053800000029 | `tok_visa_debit_it_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555053800000009 | `tok_mastercard_debit_it_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Latvia

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000054280000000 | `tok_visa_debit_lv_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000054280000018 | `tok_visa_debit_lv_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000054280000026 | `tok_visa_debit_lv_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555054280000006 | `tok_mastercard_debit_lv_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Lithuania

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000054400000005 | `tok_visa_debit_lt_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000054400000013 | `tok_visa_debit_lt_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000054400000021 | `tok_visa_debit_lt_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555054400000001 | `tok_mastercard_debit_lt_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Luxembourg

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000054420000001 | `tok_visa_debit_lu_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000054420000019 | `tok_visa_debit_lu_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000054420000027 | `tok_visa_debit_lu_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555054420000007 | `tok_mastercard_debit_lu_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Malta

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000054700000002 | `tok_visa_debit_mt_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000054700000010 | `tok_visa_debit_mt_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000054700000028 | `tok_visa_debit_mt_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555054700000008 | `tok_mastercard_debit_mt_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Netherlands

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000055280000007 | `tok_visa_debit_nl_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000055280000015 | `tok_visa_debit_nl_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000055280000023 | `tok_visa_debit_nl_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555055280000003 | `tok_mastercard_debit_nl_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Portugal

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000056200000002 | `tok_visa_debit_pt_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000056200000010 | `tok_visa_debit_pt_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000056200000028 | `tok_visa_debit_pt_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555056200000008 | `tok_mastercard_debit_pt_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Slovakia

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000057030000006 | `tok_visa_debit_sk_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000057030000014 | `tok_visa_debit_sk_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000057030000022 | `tok_visa_debit_sk_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555057030000002 | `tok_mastercard_debit_sk_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Slovenia

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000057050000001 | `tok_visa_debit_si_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000057050000019 | `tok_visa_debit_si_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000057050000027 | `tok_visa_debit_si_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555057050000007 | `tok_mastercard_debit_si_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Spain

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000057240000036 | `tok_visa_debit_es_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000057240000010 | `tok_visa_debit_es_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000057240000028 | `tok_visa_debit_es_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555057240000008 | `tok_mastercard_debit_es_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Denmark

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000052080000006 | `tok_visa_debit_dk_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000052080000014 | `tok_visa_debit_dk_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000052080000022 | `tok_visa_debit_dk_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555052080000002 | `tok_mastercard_debit_dk_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Malaysia

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000054580000031 | `tok_visa_debit_my_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000054580000015 | `tok_visa_debit_my_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000054580000023 | `tok_visa_debit_my_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555054580000003 | `tok_mastercard_debit_my_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### New Zealand

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000055540000003 | `tok_visa_debit_nz_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000055540000011 | `tok_visa_debit_nz_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000055540000029 | `tok_visa_debit_nz_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555055540000165 | `tok_mastercard_debit_nz_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Norway

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000055780000002 | `tok_visa_debit_no_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000055780000010 | `tok_visa_debit_no_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000055780000028 | `tok_visa_debit_no_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555055780000008 | `tok_mastercard_debit_no_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Sweden

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000057520000003 | `tok_visa_debit_se_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000057520000011 | `tok_visa_debit_se_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000057520000029 | `tok_visa_debit_se_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555057520000009 | `tok_mastercard_debit_se_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Czechia

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000052030000007 | `tok_visa_debit_cz_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000052030000015 | `tok_visa_debit_cz_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000052030000023 | `tok_visa_debit_cz_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555052030000003 | `tok_mastercard_debit_cz_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Hungary

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000053480000000 | `tok_visa_debit_hu_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000053480000018 | `tok_visa_debit_hu_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000053480000026 | `tok_visa_debit_hu_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555053480000006 | `tok_mastercard_debit_hu_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Poland

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000056160000000 | `tok_visa_debit_pl_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000056160000018 | `tok_visa_debit_pl_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000056160000026 | `tok_visa_debit_pl_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555056160000006 | `tok_mastercard_debit_pl_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

#### Romania

| Number           | Token                                        | Type                                                      |
| ---------------- | -------------------------------------------- | --------------------------------------------------------- |
| 4000056420000030 | `tok_visa_debit_ro_transferSuccess`          | Visa debit. Payout succeeds.                              |
| 4000056420000014 | `tok_visa_debit_ro_transferFail`             | Visa debit. Payout fails with a `could_not_process` code. |
| 4000056420000022 | `tok_visa_debit_ro_instantPayoutUnsupported` | Visa debit. Card isn’t eligible for Instant Payouts.      |
| 5555056420000002 | `tok_mastercard_debit_ro_transferSuccess`    | Mastercard debit. Payout succeeds.                        |

## Payout failures 

If your bank account can’t receive a payout for any reason, your bank returns the funds to us. You’ll receive an error with the [reason for the failure](https://docs.stripe.com/api/payouts/failures.md). It can take up to 5 additional business days for your bank to return the payout and inform us that it failed. If this happens, you’re notified by email and in the [Dashboard](https://dashboard.stripe.com/test/payouts). If a payout fails, make sure your bank account details are correct by re-entering them. Stripe then reattempts the payout at the next scheduled payout interval.

> When a payout fails, the status might initially show as `paid`, but then change to `failed` within 5 business days.

Stripe sends the funds using the bank account information that you enter. If you provide incorrect information, such as a mistyped account number or an incorrect routing number, Stripe might send payouts to the wrong bank account and might not be able to recover the funds.

Any fees or losses that you incur because of incorrect information fall under your responsibility. If your banking details are correct and the payout failure is for other reasons, contact your bank. After you resolve any issues with your bank, you can reactivate the payouts by clicking **Resume Payouts**. If you don’t receive a payout from Stripe after clicking **Resume Payouts**, and you haven’t received a failure notification within a reasonable time frame, please [contact us](https://support.stripe.com/contact).

## Payout fees 

Stripe doesn’t charge you a fee to initiate normal payouts. However, most [non-primary currency payouts](https://docs.stripe.com/payouts/multicurrency-settlement.md), where you pay out money in a currency other than your Stripe account’s local currency, do incur Stripe fees.

## See also

- [Payout reconciliation report](https://docs.stripe.com/reports/payout-reconciliation.md)
- [Financial reports](https://docs.stripe.com/reports/select-a-report.md)