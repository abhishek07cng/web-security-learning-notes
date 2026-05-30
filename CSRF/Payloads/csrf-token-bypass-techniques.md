# CSRF Token Bypass Techniques

## Purpose

Reusable Attack Notes

Contains common methods attackers use to bypass CSRF token validation.

---

# Technique 1

## Validation Depends On Request Method

Application validates:

```http
POST
```

but ignores:

```http
GET
```

---

### Exploitation

```text
POST
    ↓
GET
    ↓
Validation Bypassed
```

---

### Related Lab

```text
Lab02
```

---

# Technique 2

## Validation Depends On Token Presence

Application validates only if token exists.

---

### Exploitation

```text
Remove Token
        ↓
Validation Skipped
```

---

### Related Lab

```text
Lab03
```

---

# Technique 3

## Token Not Bound To Session

Application accepts tokens from other users.

---

### Exploitation

```text
Obtain Token
        ↓
Embed In PoC
        ↓
Victim Uses Token
```

---

### Related Lab

```text
Lab04
```

---

# Technique 4

## Token Bound To Non-Session Cookie

Token validation depends on:

```http
csrfKey
```

instead of:

```http
session
```

---

### Exploitation

```text
Inject Cookie
        ↓
Provide Matching Token
```

---

### Related Lab

```text
Lab05
```

---

# Technique 5

## Double Submit Cookie

Validation:

```text
Cookie == Parameter
```

---

### Exploitation

```text
Inject Fake Cookie
        ↓
Submit Fake Parameter
```

---

### Related Lab

```text
Lab06
```

---

# Key Takeaway

Always test HOW the token is validated, not merely whether a token exists.