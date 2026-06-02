# What Is A Site In The Context Of SameSite Cookies?

## Overview

To understand SameSite bypasses, you must understand the difference between:

```text
Site
Origin
```

These are NOT the same thing.

---

# What Is An Origin?

An Origin consists of:

```text
Scheme + Host + Port
```

Example:

```text
https://app.example.com
```

---

# Same-Origin Example

```text
https://app.example.com
https://app.example.com
```

Result:

```text
Same-Origin ✅
```

---

# Different Subdomains

```text
https://app.example.com
https://admin.example.com
```

Result:

```text
Same-Origin ❌
```

---

# What Is A Site?

A Site consists of:

```text
Scheme + eTLD+1
```

Examples:

```text
example.com
example.co.uk
```

---

# Same-Site Example

```text
https://app.example.com
https://admin.example.com
```

Result:

```text
Same-Site ✅
```

Even though:

```text
Same-Origin ❌
```

---

# Site vs Origin

| From | To | Same-Site | Same-Origin |
|--------|--------|--------|--------|
| example.com | example.com | ✅ | ✅ |
| app.example.com | admin.example.com | ✅ | ❌ |
| example.com | example.com:8080 | ✅ | ❌ |
| example.com | example.co.uk | ❌ | ❌ |

---

# Important Observation

A request can be:

```text
Same-Site ✅
Same-Origin ❌
```

but never:

```text
Same-Origin ✅
Same-Site ❌
```

---

# Why This Matters

Browsers evaluate:

```text
Same-Site
```

when deciding whether to send cookies.

This creates opportunities for SameSite bypasses. :contentReference[oaicite:1]{index=1}

---

# Memory Trick

```text
Origin = Exact Address

Site = Domain Family
```

---

# Key Takeaways

- Site and Origin are different concepts.
- SameSite uses Site, not Origin.
- This distinction is critical for advanced CSRF attacks.