# Lab07 - Weak Isolation On Dual-Use Endpoint

## Objective

Gain unauthorized access to administrator functionality.

---

# Vulnerability Overview

The same endpoint serves both users and administrators.

Isolation between roles is insufficient.

---

# Analysis

## Step 1

Observe request:

```http
POST /account
```

---

## Step 2

Modify parameters.

---

## Step 3

Send administrator-related values.

---

## Result

Privileged functionality becomes accessible.

Lab solved.

---

# Why It Works

```text
Shared Endpoint
        ↓
Missing Separation
        ↓
Privilege Escalation
```

---

# Related Theory

08-users-wont-always-remain-trustworthy.md

---

# Key Learnings

Dual-use endpoints often lead to logic flaws.