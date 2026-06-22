# Lab08 - Password Reset Broken Logic

## Objective

Reset Carlos's password.

---

# Vulnerability Overview

Password reset workflow fails to validate user identity correctly.

---

# Analysis

## Step 1

Request password reset.

---

## Step 2

Observe:

```text
username
token
new-password
```

---

## Step 3

Manipulate request.

Replace:

```text
wiener
```

with:

```text
carlos
```

---

## Step 4

Submit request.

---

## Result

Carlos password reset.

Lab solved.

---

# Attack Flow

```text
Password Reset
        ↓
Weak Binding
        ↓
Account Takeover
```

---

# Related Theory

10-users-wont-always-follow-intended-sequence.md

---

# Key Learnings

Password reset logic must bind tokens to users.