# Lab11 - Authentication Bypass Via Flawed State Machine

## Objective

Access Carlos's account without completing all authentication steps.

---

# Vulnerability Overview

The application incorrectly manages authentication states.

It assumes users follow the intended sequence.

---

# Analysis

## Normal Flow

```text
Login
        ↓
2FA
        ↓
Authenticated Session
```

---

## Actual Flow

```text
Login
        ↓
Session Created
        ↓
User Access Granted
        ↓
2FA Pending
```

---

## Step 1

Login normally.

---

## Step 2

Observe requests.

---

## Step 3

Directly access protected functionality.

---

## Result

Access granted before authentication completed.

Lab solved.

---

# Why It Works

```text
State Machine Broken
        ↓
Session Active Too Early
        ↓
Authentication Bypass
```

---

# Personal Analysis & Testing Process

Whenever I see:

```text
Login
OTP
Email Verification
Password Reset
```

I ask:

```text
When Is The Session Actually Created?
```

---

# Related Theory

10-users-wont-always-follow-intended-sequence.md

---

# Key Learnings

Authentication states should transition correctly.