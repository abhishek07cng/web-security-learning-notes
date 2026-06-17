# Multi-Step Process Bypasses

## Overview

Many applications implement sensitive actions through multiple steps.

Example:

```text
Step 1
Choose Action
        ↓
Step 2
Review
        ↓
Step 3
Confirm
```

---

# Intended Security

The application expects users to follow:

```text
Correct Workflow
```

before reaching the final action.

---

# Vulnerability

Occurs when:

```text
Final Step
        ↓
Does Not Validate
Authorization
```

---

# Example

Role Change Process

```text
Step 1
Select User
        ↓
Step 2
Review Changes
        ↓
Step 3
Apply Changes
```

---

Attacker:

```text
Skips Step 1
Skips Step 2
        ↓
Directly Sends Step 3 Request
```

---

# Why It Happens

Developers assume:

```text
Previous Steps
Already Performed Validation
```

---

# Common Targets

```text
Role Changes
Checkout Processes
Refund Requests
Password Resets
Account Deletion
Approval Workflows
```

---

# Testing Methodology

## Step 1

Perform action normally.

---

## Step 2

Capture requests.

---

## Step 3

Identify:

```text
Final Request
```

---

## Step 4

Replay directly.

---

## Step 5

Check whether:

```text
Authorization
Still Happens
```

---

# Bug Bounty Mental Model

Ask:

```text
Can I Skip Earlier Steps
And Execute The Final Action?
```

---

# Related Labs

```text
Lab12
```

---

# Key Takeaways

- Every step must validate authorization.
- Never trust previous workflow stages.
- Multi-step processes often hide critical access control flaws.