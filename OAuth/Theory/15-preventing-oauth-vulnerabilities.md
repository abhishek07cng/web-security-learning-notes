# Preventing OAuth Vulnerabilities

## Overview

OAuth security depends on both:

```text
OAuth Provider

↓

Client Application
```

A secure provider cannot compensate for an insecure client implementation.

---

# For OAuth Providers

## Validate redirect_uri

Always perform:

```text
Exact Match

↓

Approved Callback
```

Never rely on:

```text
Prefix Matching

Wildcard Matching

Regex Shortcuts
```

---

## Enforce state

Every authorization request should include:

```text
state
```

The value should be:

```text
Random

Unique

Bound To Session
```

---

## Validate Client Identity

Ensure:

```text
client_id

↓

Authorized redirect_uri

↓

Correct Client
```

---

## Validate Scope

Never issue permissions beyond those approved by the user.

---

## Validate Access Tokens

Ensure:

```text
Correct Client

Correct Scope

Valid Lifetime
```

---

# For Client Applications

Always use:

```text
state
```

Validate:

```text
Authorization Code

Access Token

ID Token

Nonce
```

---

## Protect Authorization Codes

Never expose them via:

```text
Referer Headers

JavaScript

Logs

URLs
```

---

## Secure Callback Pages

Avoid:

```text
Open Redirects

XSS

HTML Injection

Unsafe JavaScript
```

---

## PKCE

Public clients should implement:

```text
PKCE
```

to reduce authorization code interception attacks.

---

# Bug Bounty Perspective

When reviewing an OAuth implementation, verify:

- Exact `redirect_uri` validation
- Proper `state` generation and validation
- Secure callback handling
- Correct scope enforcement
- Token validation
- PKCE support where appropriate
- OIDC validation (`issuer`, `audience`, `nonce`, `ID Token`)

---

# Security Checklist

```text
✔ Exact redirect_uri Matching

✔ Session-Bound state

✔ Scope Validation

✔ Token Validation

✔ PKCE

✔ OIDC Validation

✔ Secure Callback Pages
```

---

# Key Learnings

OAuth security is achieved through careful validation and secure implementation rather than relying on the protocol alone. Most real-world vulnerabilities stem from implementation mistakes rather than flaws in the OAuth specification.