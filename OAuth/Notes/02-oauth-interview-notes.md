# OAuth Interview Notes

## What Is OAuth?

OAuth 2.0 is an authorization framework that allows third-party applications to access user resources without sharing passwords.

---

## OAuth vs Authentication

OAuth

```
Authorization
```

OpenID Connect

```
Authentication
```

---

## Main Components

- Resource Owner
- Client
- Authorization Server
- Resource Server

---

## OAuth Flows

- Authorization Code
- Authorization Code + PKCE
- Implicit
- Client Credentials
- Device Code
- Refresh Token

---

## What Is PKCE?

Proof Key for Code Exchange.

Protects public clients against authorization code interception.

---

## What Is state?

Used as a CSRF protection mechanism.

Should be:

- Random
- Session-bound
- Validated

---

## What Is redirect_uri?

The callback endpoint used after user authorization.

Weak validation can lead to:

- Authorization code theft
- Access token theft
- Account takeover

---

## Common OAuth Vulnerabilities

- Missing state
- Weak redirect_uri validation
- Open redirects
- Token leakage
- ID Token validation flaws
- Scope validation issues

---

## Bug Bounty Questions

- Can I modify redirect_uri?
- Is state validated?
- Is PKCE used?
- Can tokens leak?
- Can callback pages be abused?

---

## Best Practices

- Use Authorization Code Flow with PKCE.
- Validate redirect_uri exactly.
- Validate state and nonce.
- Protect callback pages.
- Avoid the Implicit Flow in new applications.