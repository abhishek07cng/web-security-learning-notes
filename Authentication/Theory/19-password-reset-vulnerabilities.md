# 19 - Password Reset Vulnerabilities

## Overview

Password reset functionality is one of the most sensitive authentication features in web applications.

Since users are not authenticated during the reset process, applications must rely on alternative verification mechanisms.

Improper implementation may allow attackers to completely compromise accounts.

---

## Common Password Reset Methods

Applications commonly use:

- Email reset links
- Temporary reset tokens
- SMS verification codes
- Security questions

---

## Why Password Reset Is Dangerous

Password reset workflows temporarily replace normal authentication mechanisms.

Weak validation may allow attackers to:

- reset arbitrary passwords
- steal reset tokens
- bypass verification
- compromise accounts

---

## Insecure Password Reset Approaches

---

## 1. Sending Passwords via Email

Some applications send:

- current passwords
- temporary passwords

through email.

This is highly insecure.

---

## Why This Is Dangerous

Email is not designed for secure credential storage.

Risks include:

- inbox compromise
- email interception
- insecure synchronization
- persistent credential exposure

---

## 2. Predictable Reset URLs

Weak implementations may use URLs such as:

```text
/reset-password?user=carlos
```

Attackers can simply modify the username parameter to target other users.

---

## Secure Reset Token Design

Applications should instead generate:

- high-entropy
- random
- temporary

reset tokens.

Example:

```text
/reset-password?token=a0ba0d1cb3b63d13822572fcff1a2418
```

---

## Token Validation Weaknesses

Some applications:

- validate tokens during page load
- but fail to validate tokens again during form submission

Attackers may:

1. Open reset form
2. Remove token
3. Modify username
4. Submit new password

This may reset arbitrary accounts.

---

## Password Reset Poisoning

Applications that dynamically generate reset URLs may become vulnerable to:

```text
Password Reset Poisoning
```

Attackers manipulate headers such as:

```http
X-Forwarded-Host
```

to generate malicious reset links pointing to attacker-controlled servers.

Victims may unknowingly leak reset tokens.

---

## Common Testing Methodology

During testing, analyze:

- reset token generation
- token expiration
- parameter validation
- header trust assumptions
- reset URL construction

---

## Real-World Risks

Weak password reset functionality may allow attackers to:

- take over accounts
- bypass authentication
- steal reset tokens
- compromise administrator accounts

---

## Prevention

Applications should:

- Use high-entropy reset tokens
- Expire tokens quickly
- Validate tokens server-side
- Prevent token reuse
- Avoid exposing usernames
- Protect against header injection

---

## Secure Password Reset Principles

Applications should:

- require token validation during ALL reset stages
- invalidate tokens after usage
- monitor suspicious reset activity
- use HTTPS exclusively

---

## Key Takeaways

- Password reset functionality is a high-value attack surface.
- Weak token validation may completely compromise accounts.
- Reset links must be generated and validated securely.

> [!WARNING]
> Improper password reset logic can allow complete account takeover.

> [!IMPORTANT]
> Reset tokens should always be random, temporary, single-use, and validated server-side.