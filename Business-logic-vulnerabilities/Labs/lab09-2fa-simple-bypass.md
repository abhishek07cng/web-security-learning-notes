# Lab09 - 2FA Simple Bypass

## Objective

Access Carlos's account without completing 2FA.

---

# Vulnerability Overview

2FA is enforced only through the UI.

Server trusts navigation sequence.

---

# Analysis

## Step 1

Login.

---

## Step 2

Before submitting 2FA code, manually visit:

```text
/my-account
```

---

## Result

Authenticated session established.

2FA bypassed.

Lab solved.

---

# Why It Works

```text
Login
        ↓
Session Created
        ↓
2FA Skipped
        ↓
Access Granted
```

---

# Related Theory

10-users-wont-always-follow-intended-sequence.md

---

# Key Learnings

Every stage should verify authentication state.