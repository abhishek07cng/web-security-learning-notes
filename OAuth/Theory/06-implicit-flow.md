# OAuth Implicit Grant Flow

## Overview

The Implicit Flow was designed for browser-based applications that cannot safely store a client secret.

Unlike the Authorization Code Flow, the OAuth provider returns the **access token directly to the browser**.

---

# Flow Overview

```text
User

↓

Authorization Server

↓

Access Token

↓

Browser

↓

Client Application
```

---

# Step 1 — Authorization Request

Example:

```http
GET /authorization

response_type=token
```

Notice:

```text
response_type=token
```

instead of:

```text
response_type=code
```

---

# Step 2 — User Authentication

The user authenticates with the OAuth provider.

---

# Step 3 — User Consent

Requested scopes are displayed.

---

# Step 4 — Access Token Returned

Instead of an authorization code:

```http
GET /callback

#access_token=TOKEN
```

The token appears inside the URL fragment.

---

# Step 5 — JavaScript Reads Token

The browser extracts:

```text
window.location.hash
```

The client stores:

```text
Access Token

User Information
```

---

# Step 6 — Resource Request

API request:

```http
Authorization: Bearer ACCESS_TOKEN
```

---

# Why It's Less Secure

The access token travels through:

```text
Browser

History

JavaScript

Fragments

Potential Redirects
```

This increases exposure.

---

# Typical Vulnerabilities

```text
Access Token Leakage

Open Redirect

Token Theft

Improper Validation

Account Takeover
```

---

# Authorization Code vs Implicit

```text
Authorization Code

↓

Authorization Code

↓

Backend Exchange

↓

Access Token

-------------------------

Implicit

↓

Access Token

↓

Browser
```

---

# Bug Bounty Perspective

Always inspect:

```text
window.location.hash

Authorization Header

Browser Storage

JavaScript

Callback Page
```

---

# Questions To Ask

```text
Can The Token Leak?

Can JavaScript Read It?

Can An Open Redirect Forward It?

Can Another Page Access The Fragment?
```

---

# Key Learnings

The Implicit Flow is easier to implement but exposes access tokens to the browser, making it significantly more susceptible to token leakage and client-side attacks.