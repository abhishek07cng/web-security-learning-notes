# Lab10 - Password Disclosure Via IDOR

## Objective

Obtain administrator credentials and delete:

```text
carlos
```

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Horizontal To Vertical Escalation |
| Difficulty | Practitioner |
| Platform | PortSwigger |

---

# Vulnerability Overview

An IDOR vulnerability exposes administrator credentials.

This allows:

```text
Horizontal Access
        ↓
Vertical Privilege Escalation
```

---

# Analysis

## Step 1

Login as:

```text
wiener
```

---

## Step 2

Access administrator profile.

---

## Step 3

Observe password disclosure.

---

## Finding

```text
administrator password exposed
```

---

## Step 4

Login as:

```text
administrator
```

---

## Step 5

Access:

```text
/admin
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

```text
/my-account?id=administrator
```

---

# Why It Works

Application exposes:

```text
Sensitive Credentials
```

through an IDOR vulnerability.

---

# Attack Flow

```text
IDOR
        ↓
Password Disclosure
        ↓
Admin Login
        ↓
Privilege Escalation
```

---

# Personal Analysis & Testing Process

## Initial Goal

Enumerate user profiles.

---

## Key Observation

Administrator profile contained sensitive information.

---

## Result

Password recovered.

Administrative access achieved.

Lab solved.

---

# Mental Model

Whenever an IDOR exists ask:

```text
Can Exposed Data
Lead To Privilege Escalation?
```

---

# Related Theory

- 08-horizontal-to-vertical-escalation.md
- 09-insecure-direct-object-references-idor.md

---

# Key Learnings

- IDOR impact often exceeds simple data disclosure.
- Sensitive information frequently enables privilege escalation.