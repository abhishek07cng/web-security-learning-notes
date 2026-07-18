# OAuth Observations

## Overview

This document contains practical observations gathered while solving OAuth labs and performing bug bounty reconnaissance.

---

# General Observations

## OAuth Is an Authorization Framework

OAuth was designed for:

```
Authorization
```

not authentication.

Many applications incorrectly use OAuth as an authentication mechanism, leading to implementation flaws.

---

## Most OAuth Bugs Are Implementation Bugs

The OAuth specification is generally secure.

Common issues arise from:

- Missing state validation
- Weak redirect_uri validation
- Token leakage
- Open redirects
- Incorrect ID Token validation
- Insecure callback pages

---

## The redirect_uri Parameter Is Critical

Always inspect:

```
redirect_uri
```

Testing should include:

- Exact matching
- Wildcards
- Prefix/suffix validation
- Open redirects
- Directory traversal

---

## state Is OAuth's CSRF Protection

Missing or improperly validated `state` values often result in:

- Login CSRF
- Forced account linking
- Account takeover

---

## Implicit Flow Has a Larger Attack Surface

Because the access token is delivered to the browser, additional risks include:

- XSS
- postMessage()
- Browser history
- Referer leakage
- Open redirects

Whenever possible, prefer Authorization Code Flow with PKCE.

---

## Recon Strategy

When testing an application:

1. Identify OAuth providers.
2. Capture the authorization request.
3. Record all parameters.
4. Inspect callback endpoints.
5. Search for token exposure.
6. Review OIDC metadata when available.

---

## Personal Notes

- Always inspect every OAuth parameter individually.
- Small client-side issues can become critical when combined with OAuth.
- Chaining vulnerabilities often leads to account takeover.