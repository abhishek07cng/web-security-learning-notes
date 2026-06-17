# Lab06 - Method-Based Access Control Bypass

## Objective

Promote yourself to administrator and delete:

```text
carlos
```

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Vertical Privilege Escalation |
| Difficulty | Practitioner |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application restricts privileged functionality based on:

```http
HTTP Method
```

instead of proper authorization.

---

# Analysis

## Step 1

Login as administrator.

---

## Step 2

Observe role upgrade request.

Example:

```http
POST /admin-roles
```

---

## Step 3

Log in as:

```text
wiener
```

---

## Step 4

Replay admin request.

Response:

```http
401
```

or

```http
403
```

---

## Step 5

Change:

```http
POST
```

to:

```http
GET
```

or

```http
POST
```

to:

```http
PATCH
```

(depending on lab version)

---

## Step 6

Forward request.

---

Result:

```text
Role Updated Successfully
```

---

## Step 7

Delete:

```text
carlos
```

Lab solved.

---

# Full Payload Used

## Original

```http
POST /admin-roles
```

---

## Modified

```http
GET /admin-roles
```

---

# Why It Works

Application validates:

```text
POST Requests
```

but ignores:

```text
GET Requests
```

---

Execution Flow

```text
Method Changed
        ↓
Authorization Check Skipped
        ↓
Admin Action Executed
```

---

# Personal Analysis & Testing Process

## Initial Observation

Admin action blocked.

---

## Key Thought

Some applications implement authorization differently across methods.

---

## Test

Modified HTTP method.

---

## Result

Authorization bypassed.

Lab solved.

---

# Mental Model

Whenever a request fails:

```http
POST
```

try:

```http
GET
PUT
PATCH
OPTIONS
```

---

# Mitigation

Authorization must be:

```text
Independent Of HTTP Method
```

---

# Related Theory

- 06-vertical-privilege-escalation.md

---

# Key Learnings

- Authorization inconsistencies are common.
- HTTP methods can reveal hidden attack paths.