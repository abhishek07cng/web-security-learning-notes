# Lab13 - Referer-Based Access Control

## Objective

Promote yourself to administrator.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Referer-Based Access Control |
| Difficulty | Practitioner |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application uses:

```http
Referer
```

to determine whether privileged actions are authorized.

---

# Analysis

## Step 1

Observe admin role modification request.

---

## Step 2

Replay request as:

```text
wiener
```

---

Response:

```http
403 Forbidden
```

---

## Step 3

Add:

```http
Referer:
/admin
```

---

## Step 4

Forward request.

---

Result:

```text
Role Updated
```

---

## Step 5

Access administrator functionality.

Lab solved.

---

# Full Payload Used

```http
Referer: /admin
```

---

# Why It Works

Application trusts:

```http
Referer
```

for authorization decisions.

---

# Attack Flow

```text
Modify Header
        ↓
Server Trusts Header
        ↓
Authorization Bypassed
```

---

# Personal Analysis & Testing Process

## Initial Observation

Request blocked.

---

## Key Thought

Headers are client-controlled.

---

## Test

Modified:

```http
Referer
```

header.

---

## Result

Authorization bypassed.

Lab solved.

---

# Mental Model

Whenever access depends on:

```http
Referer
Origin
Host
X-Forwarded-For
```

test header manipulation.

---

# Related Theory

- 12-referer-based-access-control.md

---

# Key Learnings

- Headers should never be trusted for authorization.
- Referer-based access control is fundamentally flawed.