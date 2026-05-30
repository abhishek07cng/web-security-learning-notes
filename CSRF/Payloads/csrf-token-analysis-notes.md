# CSRF Token Analysis Notes

## Purpose

Revision Notes

Used during CSRF testing to determine whether a token implementation is secure.

---

# What Is A Secure Token?

A secure CSRF token should be:

- Unique
- Secret
- Unpredictable
- Session Bound

---

# Common Places Tokens Appear

## Hidden Form Fields

```html
<input type="hidden" name="csrf" value="TOKEN">
```

---

## Request Parameters

```http
csrf=TOKEN
```

---

## Request Headers

```http
X-CSRF-Token: TOKEN
```

---

# Questions To Ask During Testing

## 1. Is The Token Required?

Remove token completely.

Observe:

```text
Request Accepted?
Request Rejected?
```

---

## 2. Is The Token Validated?

Modify token value.

Observe:

```text
Request Accepted?
Request Rejected?
```

---

## 3. Is Token Bound To Session?

Use token from another account.

Observe:

```text
Request Accepted?
```

---

## 4. Is Token Bound To Cookie?

Replace:

```http
csrfKey
```

and retest.

---

## 5. Is Double Submit Used?

Compare:

```http
Cookie: csrf=
```

with:

```http
Body: csrf=
```

---

# Common Weak Implementations

- Token only checked for POST
- Token only checked if present
- Token not session-bound
- Token tied to wrong cookie
- Double submit cookie

---

# Related Labs

- Lab02
- Lab03
- Lab04
- Lab05
- Lab06

---

# Key Takeaway

Never assume a token is secure simply because it exists.