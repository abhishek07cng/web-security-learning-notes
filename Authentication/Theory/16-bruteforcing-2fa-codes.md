# 16 - Bruteforcing 2FA Codes

## Overview

Many Two-Factor Authentication systems use short numeric verification codes.

Without proper protections, attackers may brute-force these codes using automation tools.

---

## Why 2FA Codes Are Vulnerable

Verification codes are often:

```text
4-digit
6-digit
```

numeric values.

This creates a relatively small search space.

Example:

```text
000000 → 999999
```

Without strong protections, attackers can automate attempts until valid codes are discovered.

---

## Common Weaknesses

| Weakness | Description |
|---|---|
| No Rate Limiting | Unlimited verification attempts |
| Short Verification Codes | Small brute-force space |
| Long Expiration Windows | More time for attacks |
| Weak Session Validation | Reusable authentication state |
| No Account Monitoring | Automated attacks undetected |

---

## Typical Attack Workflow

1. Authenticate using valid username/password
2. Reach MFA verification stage
3. Intercept verification request
4. Send request to Burp Intruder
5. Brute-force MFA code payloads
6. Analyze successful responses

---

## Example Verification Request

```http
POST /login2 HTTP/1.1

mfa-code=123456
```

Attackers automate requests by replacing:

```text
123456
```

with payload lists.

---

## Common Tools Used

| Tool | Purpose |
|---|---|
| Burp Intruder | Automated MFA brute force |
| Turbo Intruder | High-speed attacks |
| ffuf | Fast request automation |

---

## Session Handling Weaknesses

Applications sometimes fail to:

- invalidate sessions after failed attempts
- expire temporary MFA states
- detect automation patterns

This allows attackers to continue brute-forcing verification codes.

---

## Automation Using Burp Intruder

Attackers commonly:

1. Intercept MFA request
2. Add payload position to verification code
3. Load numeric payload list
4. Launch attack
5. Analyze:
   - response length
   - redirects
   - status codes
   - authentication cookies

---

## Common Indicators of Success

Successful verification attempts may produce:

- HTTP 302 redirects
- Larger response lengths
- Session cookie changes
- Access to authenticated pages

---

## Real-World Risks

Weak MFA brute-force protection may allow attackers to:

- Bypass MFA protections
- Access sensitive accounts
- Compromise administrator accounts

---

## Mitigation

Applications should:

- Implement strict rate limiting
- Expire MFA tokens quickly
- Lock verification attempts
- Detect automation behavior
- Require re-authentication
- Monitor suspicious login activity

---

## Best Practices

Applications should:

- Use short-lived MFA tokens
- Limit verification attempts
- Enforce IP-based protections
- Use CAPTCHA after repeated failures
- Prefer authenticator apps

---

## Key Takeaways

- Short MFA codes are vulnerable without proper protections.
- Automated brute-force attacks are highly effective against weak implementations.
- Rate limiting is essential for MFA security.

> [!IMPORTANT]
> MFA systems must implement brute-force protections just like password authentication systems.

> [!TIP]
> During testing, carefully compare response behavior for successful and failed MFA attempts.