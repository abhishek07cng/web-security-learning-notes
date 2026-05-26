# 22 - Authentication Best Practices

## Overview

Authentication best practices help reduce the risk of:

- account compromise
- brute-force attacks
- credential theft
- session hijacking
- authentication bypass

Secure authentication requires both:

- strong security controls
- secure implementation logic

---

# Secure Authentication Best Practices

---

## 1. Enforce HTTPS Everywhere

Applications should:

- redirect HTTP to HTTPS
- use secure TLS configurations
- prevent insecure authentication traffic

---

## 2. Use Strong Password Policies

Applications should encourage:

- long passwords
- unpredictable passwords
- password uniqueness

Avoid relying only on:

- minimum length
- special character requirements

---

## 3. Hash Passwords Securely

Passwords should NEVER be stored in plaintext.

Applications should use secure hashing algorithms such as:

- bcrypt
- Argon2
- PBKDF2

---

## 4. Implement Multi-Factor Authentication

Applications should:

- use authenticator apps
- support hardware tokens
- protect sensitive accounts with MFA

---

## 5. Prevent Username Enumeration

Applications should:

- use generic error messages
- normalize response timing
- avoid exposing usernames publicly

---

## 6. Implement Rate Limiting

Applications should restrict:

- login attempts
- MFA verification attempts
- password reset requests

---

## 7. Use Secure Session Management

Applications should:

- generate random session tokens
- expire sessions properly
- invalidate sessions after logout
- use secure cookie attributes

Example:

```http
HttpOnly
Secure
SameSite
```

---

## 8. Secure Password Reset Functionality

Applications should:

- use random reset tokens
- expire tokens quickly
- validate tokens server-side
- prevent token reuse

---

## 9. Monitor Authentication Activity

Applications should detect:

- brute-force attacks
- credential stuffing
- suspicious login locations
- unusual authentication behavior

---

## 10. Require Re-Authentication for Sensitive Actions

Applications should request password confirmation before:

- password changes
- email updates
- MFA modifications
- account deletion

---

## 11. Protect Against Credential Stuffing

Applications should:

- detect leaked credentials
- block automated attacks
- monitor suspicious login patterns

---

## 12. Use High-Entropy Tokens

All authentication-related tokens should be:

- random
- unpredictable
- time-limited

This includes:

- session IDs
- reset tokens
- remember-me cookies
- MFA tokens

---

# Common Authentication Mistakes

| Mistake | Risk |
|---|---|
| Weak Password Policies | Easy brute-force attacks |
| No MFA | Credential compromise |
| Predictable Tokens | Account takeover |
| Weak Session Management | Session hijacking |
| Inconsistent Errors | Username enumeration |
| Missing Rate Limiting | Automated attacks |

---

# Secure Authentication Checklist

| Security Measure | Recommended |
|---|---|
| HTTPS | Yes |
| MFA | Yes |
| CAPTCHA | Yes |
| Rate Limiting | Yes |
| Secure Password Hashing | Yes |
| Secure Session Cookies | Yes |
| Generic Error Messages | Yes |
| Login Monitoring | Yes |

---

# Key Takeaways

- Authentication security requires multiple defensive layers.
- Strong passwords alone are insufficient.
- Proper implementation logic is critical.
- MFA significantly improves protection when implemented securely.

> [!IMPORTANT]
> Authentication systems should always assume attackers will automate authentication attacks.

> [!TIP]
> Always secure supplementary authentication functionality such as password reset and remember-me mechanisms.