# Browser Behavior Notes

## Automatic Credential Attachment

Browsers automatically attach credentials such as:

- session cookies
- HTTP Basic Auth
- client certificates

to outgoing requests.

This is the core behavior CSRF exploits.

---

# Important Browser Behavior

```text
The browser does NOT care which site initiated the request.
```

If credentials exist for the target domain, they are automatically included.

---

# Same-Origin Policy (SOP)

The Same-Origin Policy:

- blocks cross-origin RESPONSE reading
- does NOT block REQUEST sending

---

# Important CSRF Insight

```text
CSRF exploits SOP limitations rather than bypassing SOP itself.
```

---

# Why CSRF Works

The server sees:

- valid cookies
- valid session
- normal request format

and assumes the request is legitimate.

---

# Browser Credential Comparison

| Mechanism | Automatically Attached? | CSRF Risk |
|---|---|
| Session Cookies | Yes | Vulnerable |
| HTTP Basic Auth | Yes | Vulnerable |
| Bearer Tokens | No | Usually Safer |

---

# SameSite Cookie Behavior

## SameSite=Strict

Cookies NOT sent cross-site.

Strongest protection.

---

## SameSite=Lax

Cookies restricted on many cross-site requests.

Modern default.

---

## SameSite=None

Cookies sent normally cross-site.

Most vulnerable.

---

# Important Security Insight

```text
Bearer tokens resist CSRF because JavaScript must manually attach them.
```

Cross-site pages cannot easily do this due to browser security restrictions.

---

# Related Theory

- `Theory/01-what-is-csrf.md`
- `Theory/03-how-csrf-works.md`

---

# Key Takeaways

- Browser automation is the foundation of CSRF.
- SOP prevents reading responses, not sending requests.
- SameSite cookies significantly reduce CSRF risk.

> [!IMPORTANT]
> Understanding browser behavior is critical for understanding CSRF.