# Lab10 - Insufficient Workflow Validation

## Objective

Bypass workflow restrictions.

---

# Vulnerability Overview

The application assumes users follow:

```text
Step 1
Step 2
Step 3
```

Attackers can skip intermediate steps.

---

# Analysis

## Step 1

Observe entire workflow.

---

## Step 2

Capture requests.

---

## Step 3

Replay final request directly.

---

## Result

Action executes successfully.

Lab solved.

---

# Attack Flow

```text
Skip Step
        ↓
Replay Final Request
        ↓
Logic Broken
```

---

# Why It Works

Developers assume:

```text
Previous Steps Already Happened
```

---

# Personal Analysis & Testing Process

Whenever I see:

```text
Wizard
Checkout
Password Reset
Approval Flow
```

I test:

```text
Can Final Request Be Called Directly?
```

---

# Related Theory

10-users-wont-always-follow-intended-sequence.md

---

# Key Learnings

Workflow assumptions are dangerous.