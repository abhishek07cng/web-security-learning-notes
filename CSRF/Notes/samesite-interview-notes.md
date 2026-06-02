# SameSite Interview Notes

## What Is SameSite?

Browser security mechanism controlling when cookies are sent in cross-site requests.

---

## Why Was SameSite Introduced?

To reduce:

- CSRF
- Cross-Site Leaks
- Certain CORS attacks

---

## SameSite Modes

### Strict

```text
Never send cookies cross-site
```

---

### Lax

```text
Send cookies only during:

GET
+
Top-Level Navigation
```

---

### None

```text
Always send cookies
```

Requires:

```http
Secure
```

---

## What Is A Site?

```text
Scheme + eTLD+1
```

Example:

```text
app.example.com
admin.example.com
```

Same-Site.

---

## What Is An Origin?

```text
Scheme + Host + Port
```

Example:

```text
https://app.example.com:443
```

---

## Difference Between Site And Origin?

```text
Site
    ↓
Domain Family

Origin
    ↓
Exact Address
```

---

## Can A Request Be:

Same-Site ✅

Same-Origin ❌

Answer:

```text
YES
```

Example:

```text
app.example.com
admin.example.com
```

---

## Common SameSite Bypasses

### Lax

```text
GET Navigation
```

### Strict

```text
Client-Side Redirect Gadget
```

---

## Why Is SameSite Not Complete CSRF Protection?

Because:

- GET requests may still include cookies
- Client-side redirects may create same-site requests
- Applications often contain logic flaws

---

## Best Defence Strategy

```text
CSRF Tokens
+
SameSite
+
Origin Validation
```

---

# Important Interview Point

SameSite should be viewed as:

```text
Additional Protection
```

not the primary CSRF defence.