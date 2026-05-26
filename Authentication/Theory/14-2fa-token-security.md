# 14 - 2FA Token Security

## Overview

Two-Factor Authentication systems commonly use temporary verification tokens.

These tokens must be generated securely and validated properly.

Weak token security may allow attackers to bypass MFA protections.

---

## Common Types of Verification Tokens

| Token Type | Example |
|---|---|
| SMS Codes | 6-digit numeric code |
| Authenticator Tokens | TOTP codes |
| Push Notifications | Device approval |
| Hardware Tokens | RSA-generated values |

---

## Common Security Risks

| Risk | Description |
|---|---|
| Predictable Codes | Easily guessable values |
| Long Expiration | Tokens valid too long |
| Weak Validation | Improper verification |
| SMS Interception | Stolen SMS codes |
| Token Reuse | Previously valid tokens reused |

---

## Short Numeric Tokens

Many applications use:

```text
4-digit
6-digit
```

verification codes.

Without proper protection, attackers may brute-force these tokens.

---

## SIM Swapping

Attackers may fraudulently obtain the victim's phone number.

This allows them to receive SMS-based MFA codes.

---

## Token Expiration

Verification codes should:

- expire quickly
- become invalid after usage
- require re-authentication after repeated failures

---

## Secure Token Practices

Applications should:

- Use cryptographically secure random values
- Implement short expiration windows
- Prevent token reuse
- Enforce rate limiting
- Monitor suspicious verification attempts

---

## Testing Methodology

During testing, analyze:

- token predictability
- expiration behavior
- reuse possibilities
- brute-force protections
- session validation

---

## Key Takeaways

- MFA tokens must be unpredictable and short-lived.
- Weak token validation can bypass MFA protections.
- SMS-based MFA introduces additional attack vectors.

> [!IMPORTANT]
> Verification tokens should always be validated server-side.

> [!TIP]
> Authenticator applications generally provide stronger security than SMS-based verification.