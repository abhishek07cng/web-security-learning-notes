# CSRF Cheatsheet

## Core Concept

```text
CSRF forces authenticated users to perform unintended actions.
```

---

# 3 Required Conditions

| Condition | Description |
|---|---|
| Relevant Action | Sensitive state-changing functionality |
| Cookie-Based Authentication | Browser auto-attaches credentials |
| No Unpredictable Parameters | Attacker can fully craft request |

---

# Common Vulnerable Endpoints

```http
POST /change-email
POST /change-password
POST /transfer-funds
DELETE /account
```

---

# Common CSRF Protections

| Protection | Purpose |
|---|---|
| CSRF Tokens | Prevent forged requests |
| SameSite Cookies | Restrict cookie sending |
| Origin Validation | Verify request source |
| Referer Validation | Verify request origin |

---

# Common Authentication Mechanisms

| Mechanism | CSRF Risk |
|---|---|
| Session Cookies | Vulnerable |
| HTTP Basic Auth | Vulnerable |
| Client Certificates | Vulnerable |
| Bearer Tokens | Usually Safer |

---

# Basic CSRF PoC Template

```html
<form action="https://victim.com/change-email" method="POST">
    <input type="hidden" name="email" value="attacker@evil.com">
</form>

<script>
    document.forms[0].submit();
</script>
```

---

# Important Browser Behavior

```text
Browsers automatically attach cookies to requests.
```

---

# Common Attack Flow

```text
Victim Logs In
        ↓
Victim Visits Malicious Site
        ↓
Hidden Form Auto-Submits
        ↓
Browser Attaches Session Cookie
        ↓
Server Processes Request
```

---

# Common Burp Workflow

```text
Capture Request
        ↓
Generate CSRF PoC
        ↓
Host Payload
        ↓
Deliver to Victim
```

---

# Useful Burp Feature

```text
Engagement Tools → Generate CSRF PoC
```

---

# Related Theory

- `Theory/01-what-is-csrf.md`
- `Theory/03-how-csrf-works.md`

---

# Related Labs

- `Labs/lab01-basic-csrf.md`

---

# Key Takeaways

- CSRF exploits browser trust.
- Cookies are the core weakness.
- SameSite cookies reduce modern CSRF risk.

> [!IMPORTANT]
> CSRF attacks abuse automatic credential handling.