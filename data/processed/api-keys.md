---
source_url: https://docs.stripe.com/keys
source_title: API keys
doc_category: api
---

# API keys

Use API keys to authenticate API requests.

Stripe authenticates your API requests using your account’s API keys. If a request doesn’t include a valid key, Stripe returns an [invalid request error](https://docs.stripe.com/error-handling.md#invalid-request-errors). If a request includes a deleted or expired key, Stripe returns an [authentication error](https://docs.stripe.com/error-handling.md#authentication-errors).

Use the [Developers Dashboard](https://dashboard.stripe.com/test/apikeys) to create, reveal, delete, and rotate API keys. You can access your v1 API keys on the [API keys](https://dashboard.stripe.com/test/apikeys) tab.

> #### New to Stripe?
> 
> - **Building and testing?** Use your **sandbox (test mode) keys**. Sandbox keys start with `pk_test_` (publishable) and `sk_test_` (secret). They let you test without affecting live data.
- **Ready to accept real payments?** Switch to your **live mode keys**, which start with `pk_live_` and `sk_live_`. See [Switch to live mode](https://docs.stripe.com/keys.md#switch-to-live-mode) for instructions.
- **Looking for your webhook signing secret?** Webhook secrets are separate from API keys. Find them in the [Webhooks](https://dashboard.stripe.com/webhooks) section of the Dashboard under each webhook endpoint.

## Key types 

By default, all accounts have a total of four API keys:

| Type                      | Description                                                                                                                                                                                                                                                                     |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sandbox secret key        | Authenticate requests on your server when you’re testing in a sandbox. By default, you can use this key to perform any API request without restriction. Reserve this key for testing and development to make sure you don’t accidentally modify your live customers or charges. |
| Sandbox publishable key   | Test requests in your web or mobile app’s client-side code. Reserve this key for testing and development to make sure you don’t accidentally modify your live customers or charges.                                                                                             |
| Live mode secret key      | Authenticate requests on your server when in live mode. By default, you can use this key to perform any API request without restriction.                                                                                                                                        |
| Live mode publishable key | When you’re ready to launch your app, use this key in your web or mobile app’s client-side code.                                                                                                                                                                                |

Your secret and publishable keys are on the [API keys](https://dashboard.stripe.com/test/apikeys) tab in the Dashboard. If you can’t view your API keys, ask the owner of your Stripe account to add you to their [team](https://docs.stripe.com/get-started/account/teams.md) with the proper permissions.

> #### Restricted API keys
> 
> You can generate [restricted API keys](https://docs.stripe.com/keys-best-practices.md#limit-access) in the Dashboard to enable customizable and limited access to the API. However, Stripe doesn’t offer any restricted keys by default.

> #### Looking for your webhook signing secret?
> 
> Webhook signing secrets aren’t API keys. You can find the signing secret for each webhook endpoint in the [Webhooks](https://dashboard.stripe.com/webhooks) section of the Dashboard. Select an endpoint and expand the **Signing secret** section.

If you’re logged in to Stripe, our documentation populates code examples with your test API keys. Only you can see these values. If you’re not logged in, our code examples include randomly generated API keys that you can replace with your test keys. Or you can log in to see the code examples populated with your test API keys.

### Example API keys

The following table shows randomly generated examples of secret and publishable keys:

| Type        | Value                                | When to use                                                                                                                                                                                                                                                                                                                        |
| ----------- | ------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Secret      | `sk_test_[REDACTED]`   | **Server-side only.** Use this key in your back-end code (for example, in an environment variable) to make API calls to Stripe. Keep it private—never share it, commit it to source control, or expose it in a browser or mobile app. Anyone with this key can make API calls as your account.                                     |
| Publishable | `pk_test_[REDACTED]`   | **Client-side (browser or mobile app).** Use this key in your front-end code to securely collect payment information with tools like [Stripe Elements](https://docs.stripe.com/payments/elements.md) or [Stripe Checkout](https://docs.stripe.com/payments/checkout.md). This key can be public.                                   |
| Restricted  | A string that starts with `rk_test_` | **Server-side only, with limited permissions.** Like a secret key, but you choose exactly which Stripe API resources it can access. Use restricted keys instead of secret keys when you want to limit what a system or third party can do. See [restricted API keys](https://docs.stripe.com/keys-best-practices.md#limit-access). |

### Protect your keys 

Anyone can use your live mode secret key to make any API call on behalf of your account, such as creating a charge or performing a refund. Protect your keys by following these best practices:

- Store secret keys in a secrets vault or encrypted environment variables. Don’t store keys in source code or configuration files checked into version control.
- Use [restricted API keys](https://docs.stripe.com/keys.md#create-restricted-api-secret-key) instead of secret keys when possible. Restricted keys limit access to only the specific API resources your integration needs, reducing the impact of a compromised key.
- [Limit keys to specific IP addresses](https://docs.stripe.com/keys.md#limit-api-secret-keys-ip-address) so they can only be used from your known servers.
- [Rotate keys](https://docs.stripe.com/keys.md#rolling-keys) when team members with access to the keys leave your organization.
- Don’t share keys over email, chat, or other unencrypted channels.

For more detail, see [best practices for managing secret API keys](https://docs.stripe.com/keys-best-practices.md).

## Sandbox versus live mode 

All Stripe API requests occur in either a *sandbox* (A sandbox is an isolated test environment that allows you to test Stripe functionality in your account without affecting your live integration. Use sandboxes to safely experiment with new features and changes) or *live mode* (Use this mode when you’re ready to launch your app. Card networks or payment providers process payments). You can use a sandbox to access test data, and live mode to access actual account data. Each mode has its own set of API keys, and objects in one mode aren’t accessible to the other. For example, a sandbox [product object](https://docs.stripe.com/api/products/object.md) can’t be part of a live mode payment.

| Mode           | Key prefix             | Purpose                                                           |
| -------------- | ---------------------- | ----------------------------------------------------------------- |
| Sandbox (test) | `pk_test_`, `sk_test_` | Build and test your integration safely. No real charges are made. |
| Live           | `pk_live_`, `sk_live_` | Accept real payments from real customers.                         |

> #### Live mode key access
> 
> You can only reveal a live mode secret or restricted API key one time. If you lose it, you can’t retrieve it from the Dashboard. In that case, rotate or delete it, and then create a new one.

| Type      | When to use                                                                                                                                                                                 | Objects                                                                                                                                                                                 | How to use                                                                                                                                                   | Considerations                                                                                                                                                                                                                                     |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Sandboxes | Use a sandbox, and its associated test API keys, as you build your integration. In a sandbox, card networks and payment providers don’t process payments.                                   | API calls return simulated objects. For example, you can retrieve and use test `account`, `payment`, `customer`, `charge`, `refund`, `transfer`, `balance`, and `subscription` objects. | Use [test credit cards and accounts](https://docs.stripe.com/testing.md#cards). You can’t accept real payment methods or work with real accounts.            | [Identity](https://docs.stripe.com/identity.md) doesn’t perform any verification checks. Also, Connect [account objects](https://docs.stripe.com/api/accounts/object.md) don’t return sensitive fields.                                            |
| Live mode | Use live mode, and its associated live API keys, when you’re ready to launch your integration and accept real money. In live mode, card networks and payment providers do process payments. | API calls return real objects. For example, you can retrieve and use real `account`, `payment`, `customer`, `charge`, `refund`, `transfer`, `balance`, and `subscription` objects.      | Accept real credit cards and work with customer accounts. You can accept actual payment authorizations, charges, and captures for credit cards and accounts. | Disputes have a more nuanced flow and a simpler [testing process](https://docs.stripe.com/testing.md#disputes). Also, some [payment methods](https://docs.stripe.com/payments/payment-methods.md) have a more nuanced flow and require more steps. |

## Switch to live mode 

When you’re ready to accept real payments, replace your sandbox (test) API keys with your live mode keys. This is the same key page in the Dashboard—you toggle between **Test mode** and **Live mode** using the toggle in the top-right corner of the Developers Dashboard.

1. In the [Developers Dashboard](https://dashboard.stripe.com/apikeys), disable **Test mode** by toggling the mode switch in the top-right corner. The page now shows your live mode API keys.
1. Copy your **live mode publishable key** (starts with `pk_live_`) and replace the `pk_test_` key in your client-side code.
1. Reveal and copy your **live mode secret key** (starts with `sk_live_`) and replace the `sk_test_` key in your server-side code. Store it securely—you can only view it once.
1. If you use webhooks, update each webhook endpoint’s URL and copy the new **signing secret** from the [Webhooks](https://dashboard.stripe.com/webhooks) section of the Dashboard.

> #### Complete go-live checklist
> 
> Switching API keys is only one step. Review the full [go-live checklist](https://docs.stripe.com/get-started/checklist/go-live.md) to make sure your integration is production-ready.

## Organization API keys

If you have multiple Stripe business accounts in an [organization](https://docs.stripe.com/get-started/account/orgs.md), you can configure a single API key at the organization level. Organization-level API keys provide the following functionality:

- **Access any account**: Use organization API keys to access resources of any account within the organization.

- **Granular permissions**: Restrict organization API keys to grant read or write permission to only specific resources.
- **Centralized management**: Create and manage organization API keys on the [API keys](https://dashboard.stripe.com/org/api-keys/secret) tab of your organization’s Dashboard.

### Behavior

Organization API keys behave differently from account-level API keys, including:

- They don’t have a publishable key. Treat all organization API keys as secret keys.
- They all have the same `sk_org` prefix, regardless of their permission levels.
- All API requests made with an organization API key must include the `Stripe-Context` header to identify the affected account.
- All API requests made with an organization API key must include the `Stripe-Version` header to ensure consistency and predictability across your organization’s integrations.

### Use organization API keys

When you use an organization API key, you must also:

- Specify an API version by including a `Stripe-Version` header. When using a [Stripe SDK](https://docs.stripe.com/sdks/set-version.md), the SDK automatically sets the API version.
- Identify the account affected by the API request by including the `Stripe-Context` header.

For example, given the following organization structure:

```
Organization (org_6SD3oI0eSQemPzdmaGLJ5j6)
  ├── Platform account  (acct_1R3fqDP6919yCiFv)
  |   └── Connected account (acct_1032D82eZvKYlo2C)
  └── Standalone account (acct_1aTnTtAAB0hHJ26p)
```

You can use the organization API key to access the balance of the standalone account. You can also use the same key to make the same call for the platform connected account.

```curl
curl https://api.stripe.com/v1/balance \
  -u {{ORG_SECRET_KEY}}: \
  -H "Stripe-Version: {{STRIPE_API_VERSION}}" \
  -H "Stripe-Context: {{CONTEXT_ID}}"
```

In the preceding code example, replace `{{CONTEXT}}` with the relevant value:

- For the standalone account, use `acct_1aTnTtAAB0hHJ26p`.
- For the connected account, use a path that identifies both the platform and the connected account, following the format `acct_1R3fqDP6919yCiFv/acct_1032D82eZvKYlo2C`.

You must specify the relevant account using the context and the API version in any API request using an organization key.

Organizations don’t have publishable API keys because they can’t accept payments. You can use your organization API key to create a PaymentIntent for any account in your organization, but you must use existing account-specific publishable keys for the client-side operations.

## Managed API keys 

Some third-party platforms, such as [Vercel](https://vercel.com/docs/integrations/ecommerce/stripe), can create and manage API keys on your behalf when you install their integration. These keys are called managed API keys, and the platform creates them programmatically instead of you creating them manually in the Dashboard.

Managed API keys appear alongside your other keys on the [API keys](https://dashboard.stripe.com/test/apikeys) tab, labeled with the name of the managing platform.

The following table summarizes the differences between unmanaged and managed keys.

|                  | Unmanaged keys                                                      | Managed keys                                                                |
| ---------------- | ------------------------------------------------------------------- | --------------------------------------------------------------------------- |
| Key creation     | You create keys in the Dashboard                                    | The platform creates keys using the API                                     |
| User interaction | You copy keys from the Dashboard and configure them in the platform | The platform handles key setup automatically                                |
| Key delivery     | Displayed to you in the Dashboard                                   | Delivered directly to the platform                                          |
| Key management   | You control rotation and expiration                                 | The platform manages the key lifecycle; you can expire the keys at any time |

### Revoke managed key access 

You can revoke a managed API key at any time by doing one of the following:

- **Expire the key**: On the [API keys](https://dashboard.stripe.com/apikeys) tab, click the overflow menu (⋯) for the managed key and expire it. That immediately revokes the platform’s access without removing the integration.
- **Uninstall the integration**: Uninstall the platform’s app from your Stripe account. When you uninstall an app, you can choose to expire the managed keys immediately or keep them active.

## Secret and restricted keys

Use the Dashboard to create, reveal, modify, delete, and rotate secret and restricted keys.

### Create an API key

You can create a secret API key or a restricted API key. A [restricted API key](https://docs.stripe.com/keys-best-practices.md#limit-access) only allows the level of access that you specify.

#### To create a secret API key 

1. On the [API keys](https://dashboard.stripe.com/test/apikeys) tab, click **Create secret key**.
1. In the dialog, enter the verification code that Stripe sends to you by email or text message. If the dialog doesn’t continue automatically, click **Continue**.
1. Enter a name in the **Key name** field, then click **Create**.
1. Click the key value to copy it.
1. Save the key value. You can’t retrieve it later.
1. In the **Add a note** field, enter the location where you saved the key, then click **Done**.

#### To create a restricted API key 

1. On the [API keys](https://dashboard.stripe.com/test/apikeys) tab, do one of the following:
   - To create a new restricted key, click **Create restricted key**. The default value for all permissions is **None**.
   - To clone an existing key, click the overflow menu (⋯), then select **Duplicate key** for the key you want to clone. The default value for each permission is the value from the cloned key.
1. Enter a name in the **Key name** field. If you cloned an existing key, the default name is the cloned key’s name.
1. For each resource you want the new key to access, select the appropriate permission: **None**, **Read**, or **Write**. If you use Connect, you can also select the permission to allow for this key when accessing connected accounts.
1. Click **Create key**.
1. In the dialog, enter the verification code that Stripe sends to you by email or text message. If the dialog doesn’t continue automatically, click **Continue**.
1. Click the key value to copy it.
1. Save the key value. You can’t retrieve it later.
1. In the **Add a note** field, enter the location where you saved the key, then click **Done**.

### Reveal an API key

You can reveal a secret API key or a restricted API key in a sandbox or live mode.

In live mode, Stripe only shows you the API key one time (for security purposes). Store the key in a place where you won’t lose it. To remind yourself where you stored it, you can add a note on the key in the Dashboard. If you lose the key, you can rotate or delete it and create another.

> #### Reveal live mode secret keys
> 
> After you create a secret or restricted API key in live mode, we display it before you save it. You must copy the key before saving it because you can’t copy it later. You can only reveal a default secret key or a key generated by a scheduled rotation.

#### To reveal a secret API key in a sandbox 

1. On the [API keys](https://dashboard.stripe.com/test/apikeys) tab, in the **Standard keys** list, click **Reveal test key** in the **Secret key** row. You can reveal the secret API key as many times as you want.
1. Click the key value to copy it.
1. Save the key value.
1. Click **Hide test key**.

#### To reveal a secret or restricted API key in live mode 

1. On the [API keys](https://dashboard.stripe.com/apikeys) tab in live mode, in the **Standard keys** or **Restricted keys** list, click **Reveal live key** for the key you want to reveal.
1. Click the key value to copy it.
1. Save the key value.
1. Click **Hide test key**.
1. Click the overflow menu (⋯), then select **Edit key** for the key you want to add a note to.
1. In the **Note** field, enter the location where you saved the key, then click **Save**.

> Keys that you created before Stripe introduced this feature aren’t automatically hidden when they’re revealed. You must manually hide them by clicking **Hide live key**.

### Limit an API key to certain IP addresses 

You can limit a secret API key or a restricted API key to a range of IP addresses, or one or more specific IP addresses. Stripe recommends enabling IP restrictions on all live mode keys to prevent use from unauthorized locations. Use separate IP allowlists for separate keys when applicable (for example, to distinguish between staging and production environments).

IP addresses must use the IPv4 protocol, and you can specify any valid CIDR range. For example, you can specify the `100.10.38.0 - 100.10.38.255` range as `100.10.38.0/24`. All IP addresses in the range must start with `100.10.38`.

1. On the [API keys](https://dashboard.stripe.com/test/apikeys) tab, in the **Standard keys** or **Restricted keys** list, click the overflow menu (⋯) for the key you want to reveal.

1. Select **Manage IP restrictions** > **Limit use to a set of IP addresses**.

1. Do one of the following:

   - Enter one or more individual IP addresses in the **IP address** field.
   - For a range of IP addresses, enter the first address in the range (using Classless Inter-Domain Routing (CIDR) notation) in the **IP Address** field. Enter the network prefix size in the **CIDR** field.

1. To add another IP address or range, click **+ Add**.

1. Click **Save**.

### Change an API key’s name or note 

1. On the [API keys](https://dashboard.stripe.com/test/apikeys) tab, click the overflow menu (⋯) for the key you want to change.
1. Select **Edit key**.
1. Do the following:
   - To change the name, enter a new name in the **Key name** field.
   - To change the note text, enter the new note text in the **Note** field.
1. Click **Save**.

### Expire an API key 

If you expire a secret API key or a restricted API key, you must create a new one and update any code that uses the expired key. Any code that uses the expired key can no longer make API calls.

> You can’t expire a publishable key.

1. On the [API keys](https://dashboard.stripe.com/test/apikeys) tab, in the **Standard keys** or **Restricted keys** list, click the overflow menu (⋯) for the key you want to expire.
1. Select **Expire key**.
1. In the dialog, click **Expire key**. If you no longer want to expire the key, click **Cancel**.

### Rotate an API key 

Rotating an API key revokes it and generates a replacement key that’s ready to use immediately. You can also schedule an API key to rotate after a certain time. The replacement key is named as follows:

- The replacement publishable key name is always `Publishable key`.
- The replacement secret key name is always `Secret key`.
- The replacement restricted key name is the same as the rotated key.

You can rename a secret or restricted API key by editing the key.

Rotate an API key in scenarios such as:

- If you lose a secret or restricted API key in live mode, and you can’t recover it from the Dashboard.
- If a secret or restricted API key is compromised, and you need to revoke it to block any potentially malicious API requests that might use the key.
- If a team member with access to the key leaves your organization or changes roles.
- If your policy requires rotating keys at certain intervals.

#### To rotate an API key

1. On the [API keys](https://dashboard.stripe.com/test/apikeys) tab, click the overflow menu (⋯) for the key you want to rotate.
1. Select **Rotate key**.
1. Select an expiration date from the **Expiration** dropdown. If you choose **Now**, the old key is deleted. If you specify a time, the remaining time until the key expires displays below the key name.
1. Click **Rotate API key**.
1. Click the key value to copy it.
1. Save the key value. You can’t retrieve it later.
1. In the **Add a note** field, enter the location where you saved the key, then click **Save** or **Done**.

### Restore an API key’s access 

An API key might have its access limited if it hasn’t been used to create transfers, payouts, or update payout destinations for over 180 days. You can’t use a limited access key to create payouts and transfers or to create payout destinations. You can restore access to use the key normally or to perform a blocked action.

#### To restore access for an API key

1. On the [API keys](https://dashboard.stripe.com/test/apikeys) tab, click the overflow menu (⋯) for the key you want to restore.
1. Select **Restore access**.
1. Click **Restore**.

## View API request logs 

To [open the API request logs](https://docs.stripe.com/development/dashboard/request-logs.md), click the overflow menu (⋯) for any key, then select **View request logs**. Opening the logs redirects you to the Stripe Dashboard.

## See also

- [Best practices for managing secret API keys](https://docs.stripe.com/keys-best-practices.md)
- [Protecting against compromised API keys](https://support.stripe.com/questions/protecting-against-compromised-api-keys)
- [Why does my API key have limited access](https://support.stripe.com/questions/why-does-my-api-key-have-limited-access)