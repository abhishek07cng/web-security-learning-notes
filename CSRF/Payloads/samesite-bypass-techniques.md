# SameSite Bypass Techniques

## Purpose

Reusable Attack Notes

Documents common SameSite bypass strategies.

---

# Technique 1

## SameSite=Lax GET Navigation Bypass

Lax allows:

```text
GET
+
Top-Level Navigation
```

Cookies included.

---

### Example

```html
<script>
document.location =
"https://target.com/action";
</script>
```

---

### Related Lab

```text
Lab07
```

---

# Technique 2

## Method Override

Application supports:

```http
_method=POST
```

---

### Exploitation

```text
GET Request
        ↓
_method=POST
        ↓
Sensitive Action
```

---

### Related Lab

```text
Lab07
```

---

# Technique 3

## Client-Side Redirect Gadget

Application contains:

```javascript
window.location=
```

redirect.

---

### Exploitation

```text
Cross-Site Request
        ↓
Client Redirect
        ↓
Same-Site Request
        ↓
Cookie Included
```

---

### Related Lab

```text
Lab08
```

---

# Technique 4

## Path Traversal Redirect Abuse

User controls:

```text
postId
```

or similar parameter.

---

### Example

```text
../my-account/change-email
```

used inside redirect target.

---

### Related Lab

```text
Lab08
```

---

# Common Requirements

Most SameSite bypasses require:

- No CSRF token
- Cookie authentication
- Sensitive endpoint
- Weak request validation

---

# Key Takeaway

SameSite bypasses usually abuse browser behavior rather than directly attacking cookies.