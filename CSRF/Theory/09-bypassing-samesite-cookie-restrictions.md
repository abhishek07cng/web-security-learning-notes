# Bypassing SameSite Cookie Restrictions

## Overview

SameSite is a browser security mechanism designed to reduce the risk of:

- Cross-Site Request Forgery (CSRF)
- Cross-Site Leaks (XS-Leaks)
- Some Cross-Origin attacks

It controls when cookies are included in cross-site requests.

---

# Why SameSite Exists

Before SameSite was introduced:

```text
Browser
    ↓
Always Sent Cookies
```

regardless of where the request originated.

This allowed attackers to abuse authenticated sessions using CSRF.

---

# SameSite Protection Levels

Browsers currently support:

```text
Strict
Lax
None
```

---

# Why SameSite Is Not Perfect

SameSite reduces risk but does not eliminate it.

Common bypasses include:

- GET-based navigation
- Method override
- Client-side redirects
- On-site gadgets
- Vulnerable sibling domains

---

# Chrome Default Behavior

Since Chrome 2021:

```text
No SameSite Attribute
        ↓
SameSite=Lax
```

applied automatically. :contentReference[oaicite:0]{index=0}

---

# Why Pentesters Must Understand SameSite

Modern applications often rely heavily on SameSite for CSRF protection.

Testing requires understanding:

- Site vs Origin
- Lax behavior
- Strict behavior
- Client-side redirect gadgets

---

# Related Theory

- `10-what-is-a-site-in-the-context-of-samesite-cookies.md`
- `11-how-does-samesite-work.md`

---

# Key Takeaways

- SameSite is browser-side protection.
- SameSite reduces but does not eliminate CSRF risk.
- Multiple bypass techniques exist.