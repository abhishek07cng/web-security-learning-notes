# Lab09 - User ID Controlled By Request Parameter With Data Leakage In Redirect

## Objective

Obtain the API key for:

```text
carlos
```

by exploiting information leakage during a redirect.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Horizontal Privilege Escalation |
| Difficulty | Practitioner |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application attempts to prevent unauthorized access by redirecting users.

However:

```text
Sensitive Data
        ↓
Still Included
        ↓
In Redirect Response
```

before the redirect occurs.

---

# Analysis

## Step 1

Login as:

```text
wiener
```

---

## Step 2

Access:

```text
/my-account?id=carlos
```

---

## Step 3

Application responds:

```http
302 Found
Location: /login
```

---

## Step 4

Observe response body.

---

## Finding

Carlos's account information appears before redirect.

---

## Step 5

Use Burp Repeater.

---

## Step 6

Disable redirect following.

---

## Step 7

Extract:

```text
Carlos API Key
```

Lab solved.

---

# Full Payload Used

```text
/my-account?id=carlos
```

---

# Why It Works

Application performs:

```text
Generate Response
        ↓
Add Sensitive Data
        ↓
Redirect User
```

instead of:

```text
Authorization Check
        ↓
Redirect
```

---

# Personal Analysis & Testing Process

## Initial Observation

Access redirected.

---

## Key Thought

Redirects sometimes leak data.

---

## Strategy

Inspect raw response before browser follows redirect.

---

## Result

Sensitive data exposed.

Lab solved.

---

# Mental Model

Whenever you see:

```http
301
302
303
307
308
```

check:

```text
Response Body
Response Headers
```

for leaked information.

---

# Mitigation

Perform authorization checks before generating content.

---

# Related Theory

- 07-horizontal-privilege-escalation.md
- 09-insecure-direct-object-references-idor.md

---

# Key Learnings

- Redirects do not automatically protect data.
- Always inspect raw responses.
- Sensitive data should never be included before redirects.