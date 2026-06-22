# Lab02 - Broken 2FA Logic

## Objective

Access Carlos's account.

---

# Vulnerability Overview

The 2FA mechanism does not properly bind verification to the authenticated user.

---

# Analysis

## Step 1

Login using:

```text
wiener:peter
```

---

## Step 2

Observe:

```text
/login2
```

---

## Step 3

Change:

```http
verify=carlos
```

or modify cookies/session values.

---

## Step 4

Submit code.

---

Result:

Carlos account accessible.

Lab solved.

---

# Why It Works

```text
Session State
        ↓
Incorrect User Binding
        ↓
2FA Broken
```

---

# Related Theory

07-making-flawed-assumptions-about-user-behavior.md

---

# Key Learnings

2FA should be tied to the authenticated session.