# Lab12 - Multi-Step Process With No Access Control On One Step

## Objective

Promote yourself to administrator.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Context-Dependent Access Control |
| Difficulty | Practitioner |
| Platform | PortSwigger |

---

# Vulnerability Overview

The role modification workflow contains multiple steps.

One critical step lacks authorization validation.

---

# Analysis

## Step 1

Login as administrator.

---

## Step 2

Capture role change workflow.

---

## Step 3

Identify final request.

Example:

```http
POST /admin/roles
```

---

## Step 4

Login as:

```text
wiener
```

---

## Step 5

Replay final request.

---

## Result

Role changed successfully.

---

## Step 6

Access admin functionality.

Lab solved.

---

# Full Request Used

```http
POST /admin/roles

username=wiener
&action=upgrade
```

---

# Why It Works

Application validates:

```text
Earlier Steps
```

but not:

```text
Final Step
```

---

# Attack Flow

```text
Skip Workflow
        ↓
Direct Final Request
        ↓
Authorization Missing
        ↓
Admin Role Granted
```

---

# Personal Analysis & Testing Process

## Key Observation

Multi-step workflows often assume previous validation.

---

## Strategy

Replay final request directly.

---

## Result

Privilege escalation achieved.

Lab solved.

---

# Mental Model

Whenever you see:

```text
Wizard
Approval Flow
Checkout Process
Role Change Process
```

test:

```text
Can Final Request Be Called Directly?
```

---

# Related Theory

- 05-context-dependent-access-controls.md
- 11-multi-step-process-bypasses.md

---

# Key Learnings

- Every workflow step requires authorization.
- Multi-step processes frequently contain bypasses.