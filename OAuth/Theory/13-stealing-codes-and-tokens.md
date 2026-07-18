# Stealing Authorization Codes and Access Tokens

## Overview

One of the most severe OAuth vulnerabilities occurs when an attacker can obtain another user's:

```text
Authorization Code

or

Access Token
```

Either can lead to complete account compromise depending on the OAuth implementation.

---

# Authorization Code Theft

Authorization Code Flow

```text
Victim

↓

Authorization Server

↓

Authorization Code

↓

Attacker

↓

Legitimate Callback

↓

Access Token
```

If an attacker obtains a valid authorization code before it is redeemed, they may complete the OAuth flow themselves.

---

# Access Token Theft

Implicit Flow

```text
Victim

↓

Access Token

↓

Browser

↓

Attacker
```

Unlike authorization codes, access tokens may immediately allow API access.

---

# Common Leak Sources

```text
Weak redirect_uri Validation

Open Redirects

Proxy Pages

JavaScript Gadgets

HTML Injection

XSS

Referer Headers
```

---

# Typical Attack Chain

```text
Weak redirect_uri

↓

Redirect To Attacker

↓

Victim Authorizes

↓

Token Or Code Leaks

↓

Account Takeover
```

---

# Authorization Code vs Access Token

Authorization Code

```text
Short Lifetime

Single Use

Backend Exchange Required
```

Access Token

```text
Immediately Usable

API Access

Resource Access
```

---

# Bug Bounty Questions

```text
Can I Leak The Authorization Code?

↓

Can I Leak The Access Token?

↓

Can I Replay Them?

↓

Can I Access /userinfo?

↓

Can I Login As Another User?
```

---

# Typical Impact

```text
Authentication Bypass

Account Takeover

Sensitive Data Disclosure

API Abuse
```

---

# Key Learnings

OAuth implementations must protect both authorization codes and access tokens. Exposure of either may allow attackers to impersonate users or access protected resources.