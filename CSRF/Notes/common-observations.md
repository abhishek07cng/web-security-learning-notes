# Common CSRF Observations

## Authentication Cookies Are Critical

CSRF almost always depends on:

```text
automatic cookie attachment
```

---

# Common Vulnerable Actions

| Action | Risk |
|---|---|
| Change Email | Account takeover |
| Change Password | Account compromise |
| Transfer Funds | Financial abuse |
| Delete Account | Data loss |

---

# Hidden Forms Are Common

Most CSRF attacks use:

```html
<input type="hidden">
```

fields.

---

# Auto-Submit Is Common

Most CSRF PoCs use:

```javascript
document.forms[0].submit();
```

to remove user interaction.

---

# SameSite Significantly Reduces CSRF

Modern browsers increasingly rely on:

```text
SameSite=Lax
```

to reduce attack success.

---

# Origin and Referer Validation Matter

Applications often use:

- Origin validation
- Referer validation

to verify legitimate requests.

---

# Common Testing Observation

```text
If cookies are automatically attached cross-site, investigate CSRF carefully.
```

---

# Burp PoC Generator Saves Time

Burp Suite Professional can automatically generate:

- HTML PoCs
- hidden forms
- auto-submit payloads

---

# Important Security Insight

```text
CSRF abuses trust rather than stealing credentials directly.
```

---

# Related Theory

- `Theory/01-what-is-csrf.md`
- `Theory/04-how-to-construct-a-csrf-attack.md`

---

# Related Labs

- `Labs/lab01-basic-csrf.md`

---

# Key Takeaways

- CSRF attacks are often extremely simple technically.
- Browser behavior is the real vulnerability.
- SameSite cookies are now a major defense layer.

> [!TIP]
> Always analyze whether sensitive requests rely solely on cookies for authentication.