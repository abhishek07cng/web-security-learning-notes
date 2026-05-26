# 05 - Password-Based Authentication

## Overview

Password-based authentication is the most common authentication mechanism used by modern web applications.

Users authenticate by providing:

- Username or email
- Secret password

The application verifies these credentials before granting access.

---

## Security Risks

Password-based authentication becomes vulnerable when attackers can:

- Guess passwords
- Reuse leaked credentials
- Steal session cookies
- Enumerate valid usernames

---

## Common Weaknesses

| Weakness | Description |
|---|---|
| Weak Passwords | Easily guessable passwords |
| Password Reuse | Same password across services |
| No Rate Limiting | Unlimited login attempts |
| Predictable Usernames | Easy user enumeration |

---

## Common Attack Types

### Brute Force

Attackers repeatedly try different password combinations until valid credentials are discovered.

---

### Credential Stuffing

Attackers use leaked username-password pairs obtained from previous data breaches.

---

### Password Spraying

Attackers attempt common passwords across many accounts.

Example:

```text
Password123
Welcome123
Summer2024
```

---

## Password Security Best Practices

Applications should:

- Enforce strong passwords
- Hash passwords securely
- Implement MFA
- Prevent brute-force attacks
- Monitor suspicious login activity

---

## Key Takeaways

- Password-based authentication remains widely used.
- Weak passwords are a major security risk.
- Proper brute-force protection is essential.

> [!IMPORTANT]
> Password reuse significantly increases the impact of credential leaks.