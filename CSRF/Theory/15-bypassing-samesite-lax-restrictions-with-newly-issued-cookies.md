# Bypassing SameSite Lax Restrictions with Newly Issued Cookies

## Overview

SameSite=Lax normally prevents cookies from being included in cross-site POST requests.

However, modern browsers introduce an exception for newly issued cookies.

This behavior creates a short window in which CSRF attacks may still succeed.

---

# Chrome's Lax-by-Default Behavior

When a cookie is issued without a SameSite attribute:

```http
Set-Cookie:
session=abc123
```

Chrome automatically applies:

```text
SameSite=Lax
```

---

# The 120-Second Exception

For compatibility with Single Sign-On (SSO) systems:

```text
New Cookie
        ↓
120 Second Grace Period
        ↓
Cross-Site POST Allowed
```

---

# Why This Exists

Many authentication systems perform:

```text
Login
        ↓
Redirect
        ↓
POST Request
```

Immediately after authentication.

Without the grace period:

```text
SSO Systems Break
```

---

# Important Distinction

## Implicit Lax

```http
Set-Cookie:
session=abc123
```

Chrome applies:

```text
Lax + 120s Grace Period
```

---

## Explicit Lax

```http
Set-Cookie:
session=abc123;
SameSite=Lax
```

No grace period.

---

# Why Attackers Care

If an attacker can force:

```text
New Session Cookie
```

to be issued,

the attacker can reset the:

```text
120 Second Timer
```

on demand.

---

# Cookie Refresh Concept

```text
Old Session Cookie
        ↓
Authentication Flow
        ↓
New Session Cookie
        ↓
Fresh 120s Window
```

---

# Attack Requirements

Successful exploitation generally requires:

1. No CSRF token
2. Implicit SameSite=Lax
3. Cookie refresh mechanism
4. State-changing POST endpoint

---

# Typical Cookie Refresh Sources

- OAuth login flows
- SSO integrations
- Session renewal mechanisms
- Remember-me features

---

# Attack Flow

```text
Force Cookie Refresh
        ↓
New Session Cookie
        ↓
Grace Period Active
        ↓
Cross-Site POST
        ↓
CSRF Successful
```

---

# Related Theory

- `16-csrf-samesite-lax-bypass-via-oauth-cookie-refresh.md`

---

# Related Lab

- `lab10-samesite-lax-bypass-via-oauth-cookie-refresh.md`

---

# Key Takeaways

- Implicit SameSite=Lax is weaker than explicit SameSite=Lax.
- Newly issued cookies receive a temporary exception.
- Authentication flows can sometimes be abused to refresh cookies.
- OAuth systems frequently introduce cookie refresh opportunities.

> [!IMPORTANT]
> A freshly issued cookie may temporarily bypass the protections normally provided by SameSite=Lax.