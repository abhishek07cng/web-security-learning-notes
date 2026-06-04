# CSRF Referer Cheatsheet

## What Is Referer?

Header indicating:

```text
Where Request Originated
```

---

## Common Uses

- Analytics
- Logging
- CSRF Protection

---

# Common Flaws

## Missing Referer Accepted

```text
Referer Missing
↓
Request Accepted
```

---

## Substring Validation

```text
Contains target.com
```

instead of:

```text
Host == target.com
```

---

# Useful Payloads

## Missing Referer

```html
<meta name="referrer"
content="no-referrer">
```

---

## Full Referer

```html
<meta name="referrer"
content="unsafe-url">
```

---

## Query String Injection

```http
https://evil.com?target.com
```

---

## Subdomain Injection

```http
https://target.com.evil.com
```

---

## Path Injection

```http
https://evil.com/target.com
```

---

# Interview Question

### Why Is Referer Validation Weak?

Answer:

```text
Referer Can Be Removed
Modified
Suppressed
Or Validated Incorrectly
```

---

# Best Defence

```text
CSRF Token
+
Origin Validation
+
SameSite
```

---

# Related Labs

- Lab11
- Lab12