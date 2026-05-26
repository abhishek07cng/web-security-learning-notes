# 06 - Brute-Force Attacks

## Overview

A brute-force attack is an automated attack in which attackers repeatedly attempt different username and password combinations until valid credentials are discovered.

Attackers commonly use:

- Wordlists
- Credential databases
- Automation tools
- Password spraying techniques

---

## Common Brute-Force Targets

- Login forms
- Password reset endpoints
- API authentication endpoints
- HTTP Basic Authentication

---

## Attack Workflow

1. Identify authentication functionality
2. Capture requests using Burp Suite
3. Send requests to Burp Intruder
4. Configure payload positions
5. Load username/password wordlists
6. Analyze responses
7. Identify successful authentication

---

## Common Tools

| Tool | Purpose |
|---|---|
| Burp Intruder | Automated login attacks |
| ffuf | Fast brute-forcing |
| Hydra | Authentication attacks |
| Turbo Intruder | High-speed brute force |

---

## Indicators of Successful Login

Attackers commonly analyze:

- HTTP status codes
- Response length
- Redirect behavior
- Authentication cookies
- Response messages

---

## Common Weaknesses

Applications become vulnerable when they lack:

- Rate limiting
- CAPTCHA protection
- Account lockout
- MFA
- Login monitoring

---

## Mitigation

Applications should:

- Implement rate limiting
- Use CAPTCHA
- Enforce MFA
- Detect suspicious login attempts
- Monitor failed authentications

---

## Key Takeaways

- Brute-force attacks are highly automatable.
- Weak login protection significantly increases risk.
- Response analysis is critical during testing.

> [!TIP]
> During testing, compare response lengths and status codes carefully.