# Authentication Testing Cheatsheet

## Authentication Testing Workflow

```text
Identify Authentication Functionality
            ↓
Capture Requests
            ↓
Analyze Responses
            ↓
Username Enumeration
            ↓
Password Brute Force
            ↓
MFA Testing
            ↓
Session Analysis
            ↓
Password Reset Testing
            ↓
Authorization Checks
```

---

# Common Authentication Attack Types

| Attack Type | Purpose |
|---|---|
| Username Enumeration | Identify valid users |
| Brute Force | Guess passwords |
| Credential Stuffing | Reuse leaked credentials |
| Password Spraying | Common passwords across many users |
| MFA Bypass | Skip second authentication factor |
| Session Hijacking | Steal authenticated sessions |

---

# Common Authentication Endpoints

```text
/login
/signin
/auth
/login2
/my-account
/forgot-password
/change-password
```

---

# Burp Suite Workflow

## Proxy

Used for:

- intercepting requests
- modifying requests
- analyzing responses

---

## Repeater

Used for:

- manual testing
- parameter manipulation
- response analysis

---

## Intruder

Used for:

- brute force
- fuzzing
- enumeration
- automation

---

# Common Response Indicators

| Indicator | Meaning |
|---|---|
| HTTP 302 | Successful authentication |
| Set-Cookie | Session creation |
| Different Response Length | Behavioral difference |
| Redirect to /my-account | Successful login |
| Response Timing Difference | Username enumeration |

---

# Common Username Enumeration Indicators

Applications may reveal valid usernames through:

- error messages
- response size
- timing differences
- redirects
- lockout behavior

---

# Common Password Attack Workflow

```text
Enumerate Username
        ↓
Identify Valid Account
        ↓
Brute-Force Password
        ↓
Analyze Responses
        ↓
Gain Authenticated Access
```

---

# Common MFA Testing Workflow

```text
Login with Valid Credentials
        ↓
Intercept MFA Request
        ↓
Analyze Session State
        ↓
Attempt Forced Browsing
        ↓
Test MFA Validation
```

---

# Common Password Reset Testing Workflow

```text
Request Password Reset
        ↓
Analyze Reset Link
        ↓
Inspect Tokens
        ↓
Test Parameter Manipulation
        ↓
Analyze Header Trust
```

---

# Common Authentication Weaknesses

| Weakness | Risk |
|---|---|
| Generic Logic Flaws | Authentication bypass |
| Weak Session Handling | Unauthorized access |
| Missing Rate Limiting | Brute-force attacks |
| Weak Remember-Me Tokens | Persistent compromise |
| Predictable Reset Tokens | Account takeover |

---

# Common HTTP Headers During Testing

```http
Authorization
Cookie
Set-Cookie
Host
X-Forwarded-Host
Referer
Origin
```

---

# Useful Burp Features

| Feature | Purpose |
|---|---|
| Grep Match | Identify successful responses |
| Grep Extract | Extract tokens/data |
| Resource Pools | Control attack speed |
| Comparer | Analyze response differences |
| Decoder | Decode Base64/Hashes |

---

# Common Authentication Cookies

```text
session
PHPSESSID
JSESSIONID
remember-me
stay-logged-in
auth-token
```

---

# Authentication Security Checklist

| Security Control | Recommended |
|---|---|
| HTTPS | Yes |
| MFA | Yes |
| Rate Limiting | Yes |
| CAPTCHA | Yes |
| Generic Errors | Yes |
| Secure Session Cookies | Yes |
| Secure Reset Tokens | Yes |

---

# Common Authentication Tools

| Tool | Purpose |
|---|---|
| Burp Suite | Web testing |
| ffuf | Fuzzing |
| Hydra | Brute force |
| Hashcat | Offline cracking |
| CyberChef | Encoding/Decoding |
| Turbo Intruder | High-speed attacks |

---

# Common Testing Observations

- Different response lengths often indicate valid usernames.
- Redirects commonly indicate successful authentication.
- Session cookies usually appear after successful login.
- Base64 encoding is NOT encryption.
- Weak remember-me cookies may expose credentials.
- MFA systems often fail due to weak session validation.

---

# Common Attack Indicators

## Successful Login

```text
302 Redirect
Set-Cookie
/my-account
Dashboard Access
```

---

## Username Enumeration

```text
Different Errors
Timing Differences
Length Changes
Lockout Behavior
```

---

## Password Reset Poisoning

```text
Host Header Reflection
X-Forwarded-Host Trust
External Reset Links
```

---

# Common Authentication Security Principles

Applications should:

- validate all authentication server-side
- prevent enumeration
- normalize responses
- secure session management
- use MFA correctly
- protect reset workflows
- avoid trusting client-side data

---

# Important Notes

> [!IMPORTANT]
> Authentication logic flaws are often more dangerous than weak passwords.

> [!TIP]
> Always compare response length, redirects, and cookies during testing.

> [!WARNING]
> Weak authentication implementations may allow complete application compromise.