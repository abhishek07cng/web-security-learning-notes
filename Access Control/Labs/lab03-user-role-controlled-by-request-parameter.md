# Lab03 - User Role Controlled By Request Parameter

## Objective

Access the admin panel and delete:

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

The application stores role information inside a client-controlled cookie.

---

# Analysis

## Step 1

Log in as normal user.

---

## Step 2

Intercept request using Burp.

Found:

```http
Cookie:
Admin=false
```

---

## Step 3

Modify cookie:

```http
Admin=true
```

---

## Step 4

Forward request.

---

## Step 5

Access:

```text
/administrator-panel
```

---

## Step 6

Delete:

```text
carlos
```

Lab solved.

---

# Full Payload Used

## Original

```http
Admin=false
```

---

## Modified

```http
Admin=true
```

---

# Why It Works

Application trusts:

```text
Client-Controlled Cookie
```

for authorization.

---

Execution Flow

```text
Modify Cookie
        ↓
Server Trusts Cookie
        ↓
Admin Privileges Granted
```

---

# Personal Analysis & Testing Process

## Initial Observation

Role data present in cookie.

---

## Key Thought

Never trust:

```text
Client-Side Authorization
```

---

## Test

Changed:

```http
false
```

to:

```http
true
```

---

## Result

Admin access granted immediately.

Lab solved.

---

# Mental Model

Whenever you see:

```text
admin
role
isAdmin
privilege
```

inside:

```text
Cookies
Headers
Parameters
```

try modifying them.

---

# Mitigation

Store authorization data:

```text
Server Side
```

only.

---

# Related Theory

- 03-vertical-access-controls.md
- 06-vertical-privilege-escalation.md

---

# Key Learnings

- Client-controlled roles are dangerous.
- Authorization must never rely on cookies.