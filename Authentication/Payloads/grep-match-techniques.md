# Grep Match Techniques

## Overview

Grep Match is one of the most powerful Burp Intruder features.

It helps identify:

- successful logins
- valid usernames
- session creation
- hidden behavior changes

during automated attacks.

---

# Why Grep Match Matters

Without Grep Match:

- analyzing thousands of responses becomes difficult

With Grep Match:

- successful responses become easy to identify

---

# Common Authentication Indicators

| Indicator | Meaning |
|---|---|
| 302 Found | Successful login |
| Set-Cookie | Session creation |
| Logout | Authenticated state |
| /my-account | Account access |
| Welcome | Successful authentication |

---

# Common Username Enumeration Indicators

## Different Error Messages

### Invalid Username

```text
Invalid username or password
```

### Valid Username

```text
Incorrect password
```

---

# Common Grep Match Strings

```text
Incorrect password
Too many login attempts
Set-Cookie
/my-account
Logout
```

---

# Grep Match During Brute Force

## Successful Login Indicators

| Indicator | Purpose |
|---|---|
| HTTP 302 | Redirect after login |
| Session Cookie | Authenticated state |
| Different Response Length | Behavioral change |
| Dashboard Access | Successful authentication |

---

# Response Length Analysis

One of the BEST enumeration techniques.

---

## Example

| Username | Response Length |
|---|---|
| invaliduser | 2145 |
| carlos | 2198 |

The anomaly may indicate a valid account.

---

# MFA Testing Indicators

During MFA testing, useful grep matches include:

```text
Invalid verification code
Too many attempts
Verification successful
```

---

# Password Reset Testing Indicators

Useful grep values:

```text
Invalid token
Token expired
Password reset successful
```

---

# Cookie Analysis Indicators

Useful authentication cookies:

```text
session
remember-me
stay-logged-in
auth-token
```

---

# Redirect Analysis

Redirects often reveal authentication success.

---

## Common Successful Redirects

```text
/my-account
/dashboard
/admin
```

---

# Grep Extract Usage

Useful for extracting:

- CSRF tokens
- reset tokens
- session identifiers
- usernames

---

# Common Testing Workflow

```text
Capture Request
        ↓
Send to Intruder
        ↓
Configure Grep Match
        ↓
Launch Attack
        ↓
Sort Responses
        ↓
Identify Anomalies
```

---

# Best Practices

- Use response length sorting
- Combine Grep Match with status codes
- Monitor cookies carefully
- Compare redirects
- Watch for timing differences

---

# Common Mistakes

| Mistake | Problem |
|---|---|
| Ignoring Small Differences | Missed vulnerabilities |
| Only Watching Status Codes | Hidden anomalies missed |
| No Grep Match Setup | Slower analysis |
| Ignoring Cookies | Missed authentication state |

---

# Key Takeaways

- Grep Match dramatically improves attack analysis.
- Small differences often reveal vulnerabilities.
- Response length analysis is extremely valuable.

> [!TIP]
> Always sort Intruder responses by length during authentication testing.

> [!IMPORTANT]
> Authentication success often appears through redirects and cookies rather than visible messages.