# Brute-Force Methodology

## Overview

Brute-force attacks attempt to discover valid credentials through repeated authentication attempts.

Attackers commonly automate these attacks using:

- Burp Intruder
- Hydra
- ffuf
- Turbo Intruder

---

# Standard Authentication Testing Workflow

```text
Reconnaissance
        ↓
Username Enumeration
        ↓
Password Brute Force
        ↓
MFA Analysis
        ↓
Session Testing
        ↓
Privilege Analysis
```

---

# Phase 1 - Reconnaissance

## Goals

Identify:

- login endpoints
- authentication parameters
- session cookies
- redirects
- MFA workflows

---

# Common Authentication Endpoints

```text
/login
/signin
/auth
/login2
/my-account
```

---

# Phase 2 - Username Enumeration

## Purpose

Identify valid usernames before password attacks.

---

## Common Enumeration Indicators

| Indicator | Purpose |
|---|---|
| Response Length | Detect valid users |
| Error Messages | Reveal usernames |
| Timing Differences | Backend validation |
| Lockout Behavior | Existing accounts |

---

## Typical Enumeration Request

```http
username=§payload§&password=test
```

---

# Phase 3 - Password Brute Force

After identifying valid users:

- brute-force passwords
- analyze responses
- monitor authentication indicators

---

## Typical Password Attack

```http
username=carlos&password=§payload§
```

---

# Common Authentication Success Indicators

| Indicator | Meaning |
|---|---|
| HTTP 302 | Successful login |
| Set-Cookie | Session created |
| Redirects | Authenticated state |
| Longer Responses | Behavioral change |

---

# Phase 4 - MFA Analysis

## Common MFA Weaknesses

- missing validation
- short MFA codes
- no rate limiting
- weak session handling

---

## Typical MFA Workflow

```text
Login
        ↓
Intercept MFA Request
        ↓
Test Validation Logic
        ↓
Attempt Forced Browsing
```

---

# Phase 5 - Session Analysis

## Analyze

- session cookies
- remember-me functionality
- token predictability
- session expiration

---

# Common Cookie Names

```text
session
remember-me
stay-logged-in
auth-token
```

---

# Phase 6 - Password Reset Testing

## Analyze

- reset tokens
- URL generation
- parameter trust
- header injection

---

# Common Password Reset Vulnerabilities

| Vulnerability | Risk |
|---|---|
| Weak Tokens | Token brute force |
| Header Trust | Reset poisoning |
| Client-Side Trust | Account takeover |

---

# Common Attack Types

| Attack Type | Purpose |
|---|---|
| Sniper | Single parameter |
| Pitchfork | Credential stuffing |
| Cluster Bomb | Full brute force |

---

# Common Tools

| Tool | Purpose |
|---|---|
| Burp Intruder | Automated attacks |
| Hydra | Login brute force |
| Turbo Intruder | High-speed testing |
| ffuf | Fuzzing |

---

# Common Wordlists

## Usernames

```text
admin
administrator
carlos
support
```

---

## Passwords

```text
password123
welcome123
qwerty
letmein
```

---

# Common Mistakes

| Mistake | Problem |
|---|---|
| No Enumeration First | Slower attacks |
| Ignoring Cookies | Missed auth state |
| Missing Response Analysis | Hidden success indicators |
| No Rate Limit Awareness | IP bans |

---

# Key Takeaways

- Enumeration significantly improves brute-force efficiency.
- Response analysis is critical during authentication attacks.
- Session handling flaws are extremely dangerous.

> [!TIP]
> Always enumerate usernames before password attacks.

> [!IMPORTANT]
> Successful authentication is often identified through redirects and cookies.