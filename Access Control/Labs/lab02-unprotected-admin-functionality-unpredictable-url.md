# Lab02 - Unprotected Admin Functionality With Unpredictable URL

## Objective

Access the administrator panel and delete:

```text
carlos
```

to solve the lab.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Vertical Privilege Escalation |
| Difficulty | Apprentice |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application hides admin functionality behind an unpredictable URL.

Developers assume:

```text
Secret URL
=
Security
```

---

# Analysis

## Step 1

Browse application.

No visible admin links.

---

## Step 2

Inspect JavaScript files.

Example:

```html
<script src="/resources/js/lab.js">
```

---

## Step 3

Review JavaScript source.

Found:

```javascript
var isAdmin = false;

if(isAdmin){
    window.location='/admin-zx81';
}
```

---

## Step 4

Navigate directly to:

```text
/admin-zx81
```

---

## Step 5

Delete:

```text
carlos
```

Lab solved.

---

# Full Request Used

```http
GET /admin-zx81 HTTP/2
```

---

# Why It Works

Application relies on:

```text
Security Through Obscurity
```

instead of authorization.

---

Execution Flow

```text
JavaScript Reveals URL
        ↓
Direct Access
        ↓
No Authorization Check
        ↓
Admin Access
```

---

# Personal Analysis & Testing Process

## Initial Observation

No admin functionality visible.

---

## Key Thought

Developers frequently hide endpoints in:

```text
JavaScript
```

---

## Discovery

Admin path revealed inside source code.

---

## Result

Admin panel accessible without restrictions.

Lab solved.

---

# Mental Model

Always inspect:

```text
JavaScript Files
Comments
Source Code
```

for:

```text
Admin Endpoints
API Routes
Hidden Functionality
```

---

# Mitigation

Protect endpoints using:

```text
Server-Side Authorization
```

---

Do not rely on:

```text
Secret URLs
```

---

# Related Theory

- 03-vertical-access-controls.md
- 06-vertical-privilege-escalation.md

---

# Key Learnings

- Security through obscurity fails.
- JavaScript often leaks sensitive paths.
- Every admin endpoint requires authorization.