# Lab04 - User Role Can Be Modified In User Profile

## Objective

Gain administrator privileges and delete:

```text
carlos
```

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Vertical Privilege Escalation |
| Difficulty | Practitioner |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application exposes role information through a profile update request.

Users can modify values that should be protected.

---

# Analysis

## Step 1

Log in.

---

## Step 2

Open:

```text
My Account
```

---

## Step 3

Update profile.

Intercept request.

---

## Step 4

Observed JSON:

```json
{
  "email":"wiener@normal-user.net",
  "roleid":1
}
```

---

## Step 5

Modify:

```json
{
  "email":"wiener@normal-user.net",
  "roleid":2
}
```

---

## Step 6

Forward request.

---

## Step 7

Access admin functionality.

Delete:

```text
carlos
```

Lab solved.

---

# Full Payload Used

## Original

```json
{
  "roleid":1
}
```

---

## Modified

```json
{
  "roleid":2
}
```

---

# Why It Works

Application accepts:

```text
Privilege Data
```

from user-controlled requests.

---

Execution Flow

```text
Modify Role ID
        ↓
Server Accepts Change
        ↓
Admin Role Assigned
```

---

# Personal Analysis & Testing Process

## Initial Observation

Profile update request contained:

```text
roleid
```

---

## Key Thought

Role information should never be user editable.

---

## Test

Changed:

```text
1
```

to:

```text
2
```

---

## Result

Administrator privileges granted.

Lab solved.

---

# Mental Model

Whenever profile updates contain:

```text
role
roleid
group
permission
isAdmin
```

attempt tampering.

---

# Mitigation

Ignore client-supplied privilege fields.

Validate role assignments server-side.

---

# Related Theory

- 03-vertical-access-controls.md
- 06-vertical-privilege-escalation.md

---

# Key Learnings

- Hidden fields are not secure.
- Role data must never be user-controlled.
- Privilege escalation often exists in profile update functionality.