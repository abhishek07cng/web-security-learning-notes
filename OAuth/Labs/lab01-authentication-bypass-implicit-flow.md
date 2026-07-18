# Lab 01 - Authentication Bypass via OAuth Implicit Flow

## Lab Information

**Difficulty:** Apprentice

**Vulnerability Class**

OAuth Authentication

Improper Implicit Flow Validation

Authentication Bypass

---

# Objective

Login as:

```
Carlos
```

without knowing his password.

---

# Vulnerability

The client application trusts user-controlled information returned from the browser.

During the OAuth login process it sends:

```
Email

Access Token
```

to its own authentication endpoint.

The server **fails to verify that the access token actually belongs to the submitted email address.**

---

# Root Cause

Server trusts browser data.

Instead of validating:

```
Access Token

↓

OAuth Provider

↓

Returned User
```

it simply accepts:

```
Email

+

Access Token
```

from the client.

---

# Attack Flow

```
OAuth Login

↓

Receive Access Token

↓

POST /authenticate

↓

Modify Email

↓

Carlos

↓

Authenticated As Carlos
```

---

# OAuth Flow

```
Browser

↓

OAuth Provider

↓

Access Token

↓

POST /authenticate

↓

Client Creates Session
```

---

# Burp Analysis

Capture OAuth login.

Observe:

```
GET /auth
```

↓

OAuth Flow

↓

```
POST /authenticate
```

Request:

```http
POST /authenticate

email=wiener@...

access_token=xxxxxxxx
```

---

# Exploitation

Send request to Burp Repeater.

Replace

```
email=wiener@...
```

with

```
email=carlos@carlos-montoya.net
```

Leave access token unchanged.

Forward request.

Open request in browser.

Authenticated as Carlos.

---

# Why It Works

The application verifies:

```
Access Token Exists
```

instead of

```
Access Token

↓

Belongs To Carlos
```

---

# Impact

Complete Authentication Bypass

↓

Account Takeover

---

# Mitigation

Always retrieve user information from:

```
/userinfo
```

using the supplied access token.

Never trust:

```
Email

Username

User ID

Role
```

submitted by the browser.

---

# Bug Bounty Indicators

Look for:

```
POST /authenticate

POST /oauth-login

POST /login/social
```

Questions:

```
Can Email Be Modified?

Can Username Be Modified?

Does Access Token Match User?
```

---

# Personal Learning

OAuth authentication must never trust browser-supplied identity information.

The access token should always be validated against the OAuth provider before creating a local session.

---

# PortSwigger Skills Learned

- OAuth Flow
- Burp Proxy
- Burp Repeater
- Authentication Bypass
- Access Token Validation