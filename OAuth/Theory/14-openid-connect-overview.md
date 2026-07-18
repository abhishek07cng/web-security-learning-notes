# OpenID Connect (OIDC) Overview

## What is OpenID Connect?

OpenID Connect (OIDC) is an identity layer built on top of OAuth 2.0.

OAuth provides:

```text
Authorization
```

OIDC provides:

```text
Authentication
```

---

# OAuth vs OpenID Connect

OAuth

```text
Can this application access this resource?
```

OIDC

```text
Who is this user?
```

---

# Additional OIDC Components

```text
ID Token

Nonce

Discovery Endpoint

JWKS Endpoint

UserInfo Endpoint
```

---

# ID Token

Unlike an access token, an ID Token contains identity information.

Usually implemented as a JWT.

Example claims:

```json
{
  "sub":"123456",

  "email":"user@example.com",

  "name":"John Doe"
}
```

---

# Standard Scopes

```text
openid

profile

email

phone

address
```

---

# Discovery Endpoint

Most providers expose:

```text
/.well-known/openid-configuration
```

Useful information includes:

```text
Issuer

JWKS URI

Authorization Endpoint

Token Endpoint

Supported Algorithms
```

---

# Bug Bounty Perspective

Review:

```text
ID Token Validation

Nonce Validation

JWKS Configuration

Issuer Validation

Audience Validation
```

---

# Common Risks

```text
Improper ID Token Validation

JWT Validation Errors

Nonce Bypass

Authentication Bypass
```

---

# Key Learnings

OpenID Connect extends OAuth by providing standardized identity information. Incorrect validation of ID Tokens or OIDC metadata can result in authentication vulnerabilities.