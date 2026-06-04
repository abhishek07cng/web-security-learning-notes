# Referer Interview Notes

## What Is Referer?

HTTP header indicating the URL that initiated a request.

Example:

```http
Referer:
https://target.com/profile
```

---

## Why Is It Used?

- Analytics
- Logging
- CSRF Protection

---

## Why Is It Weak?

### Reason 1

Header can be removed.

---

### Reason 2

Browser privacy settings affect it.

---

### Reason 3

Developers often validate incorrectly.

---

## Common Referer Vulnerabilities

### Validation Depends On Presence

```text
Referer Missing
↓
Request Accepted
```

---

### Substring Matching

```text
Contains target.com
```

instead of:

```text
Host == target.com
```

---

## Difference Between Origin And Referer

### Origin

```text
Scheme
Host
Port
```

---

### Referer

```text
Full URL
```

including path.

---

## Better CSRF Defenses

```text
CSRF Tokens
Origin Validation
SameSite
```

---

# Common Interview Question

### Should Referer Validation Be Used Alone?

Answer:

```text
No

It should be an additional defence,
not the primary CSRF protection mechanism.
```