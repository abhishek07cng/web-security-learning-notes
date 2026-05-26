# 12 - Multi-Factor Authentication

## Overview

Multi-Factor Authentication (MFA) improves authentication security by requiring users to provide multiple authentication factors.

Instead of relying only on passwords, MFA combines multiple forms of verification.

---

## Authentication Factors

| Authentication Factor | Description | Example |
|---|---|---|
| Something You Know | Knowledge-based factor | Password, PIN |
| Something You Have | Possession-based factor | Mobile device, hardware token |
| Something You Are | Biometric factor | Fingerprint, Face ID |

---

## Why MFA Is Important

Passwords alone are vulnerable to:

- Brute-force attacks
- Credential stuffing
- Password reuse
- Phishing attacks
- Keylogging

MFA significantly reduces risk because attackers require additional verification beyond the password.

---

## Common MFA Methods

| Method | Example |
|---|---|
| SMS Verification | One-time code via SMS |
| Authenticator Apps | Google Authenticator |
| Hardware Tokens | RSA Token |
| Push Notifications | Mobile approval |
| Biometrics | Fingerprint scan |

---

## Typical MFA Workflow

1. User enters username and password
2. Server validates credentials
3. Application requests second factor
4. User submits verification code
5. Access is granted after successful validation

---

## Security Benefits

Even if attackers obtain passwords, they still require:

- physical device access
- verification token
- biometric factor

This significantly improves security.

---

## Weak MFA Implementations

Poor MFA implementation can still introduce vulnerabilities.

Examples include:

- Weak verification logic
- Predictable verification codes
- Improper session handling
- Missing validation checks

---

## Email-Based MFA Weakness

Email-based MFA is not considered true multi-factor authentication.

Why?

Because both factors rely on:

```text
Something you know
```

If attackers compromise the email account, they may bypass both authentication steps.

---

## SMS-Based MFA Risks

SMS verification introduces additional risks.

---

## SIM Swapping

Attackers may fraudulently transfer the victim's phone number to another SIM card.

This allows attackers to receive MFA codes.

---

## SMS Interception

SMS messages may be intercepted during transmission.

---

## Best Practices

Applications should:

- Prefer authenticator apps
- Use hardware tokens for sensitive systems
- Enforce secure session handling
- Implement rate limiting for MFA codes
- Expire tokens quickly

---

## Key Takeaways

- MFA significantly improves authentication security.
- Poor implementation can still create vulnerabilities.
- Authenticator apps are generally more secure than SMS verification.

> [!IMPORTANT]
> True MFA requires multiple DIFFERENT authentication factors.

> [!TIP]
> Dedicated authenticator applications are usually more secure than SMS-based verification.