# CSRF - SameSite Lax Bypass via OAuth Cookie Refresh

## Overview

This attack abuses an OAuth authentication flow to force the victim's browser to receive a new session cookie.

The newly issued cookie triggers Chrome's:

```text
120 Second Lax Grace Period
```

allowing a cross-site POST request that would normally be blocked.

---

# OAuth Refresher

OAuth login flow:

```text
Target Site
        ↓
OAuth Provider
        ↓
OAuth Callback
        ↓
New Session Cookie
```

---

# Vulnerable Scenario

The application:

- Uses OAuth login
- Does not use CSRF tokens
- Sets session cookies without SameSite attribute

Example:

```http
Set-Cookie:
session=abc123;
HttpOnly;
Path=/
```

No SameSite value present.

---

# Why OAuth Matters

Every OAuth completion may issue:

```text
New Session Cookie
```

even when the user is already logged in.

---

# OAuth Refresh Gadget

Example endpoint:

```text
/social-login
```

Visiting it:

```text
OAuth Flow
        ↓
New Session Cookie
```

without requiring credentials again.

---

# Browser Challenge

The attacker wants:

```text
Refresh Cookie
        ↓
Launch CSRF
```

but:

```javascript
window.open()
```

is often blocked.

---

# Popup Blockers

Browsers allow:

```javascript
window.open()
```

only when triggered by:

```text
User Interaction
```

such as:

```text
Click
```

---

# Working Solution

```javascript
window.onclick = () => {
    window.open('/social-login');
}
```

Browser treats this as:

```text
User Gesture
```

and allows the popup.

---

# Full Attack Flow

```text
Victim Visits Exploit Page
        ↓
Victim Clicks Page
        ↓
OAuth Refresh Triggered
        ↓
New Session Cookie Issued
        ↓
120 Second Timer Resets
        ↓
CSRF Form Submitted
        ↓
Email Changed
```

---

# Why The Attack Works

The application relies on:

```text
SameSite=Lax
```

instead of:

```text
CSRF Token Validation
```

The attacker refreshes the victim's cookie immediately before sending the malicious POST request.

---

# Common Indicators

Look for:

```text
/oidc/login
/oauth/login
/social-login
/auth/callback
```

and observe whether new cookies are issued repeatedly.

---

# Related Lab

- `lab10-samesite-lax-bypass-via-oauth-cookie-refresh.md`

---

# Related Payloads

- `oauth-cookie-refresh-notes.md`

---

# Key Takeaways

- OAuth can unintentionally refresh session cookies.
- Cookie refreshes can reset Chrome's Lax grace period.
- SameSite protections should never replace CSRF tokens.

> [!WARNING]
> If an attacker can refresh a session cookie on demand, SameSite=Lax may provide far less protection than expected.