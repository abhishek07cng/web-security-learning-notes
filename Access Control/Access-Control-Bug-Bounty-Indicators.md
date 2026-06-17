# Access Control Bug Bounty Indicators

## Purpose

Connect:

```text
Observation
        ↓
Potential Vulnerability
        ↓
Testing Strategy
```

---

# Scenario 1

## Hidden Admin Functionality

### Observation

```text
/admin
/admin-panel
/manage
```

---

### Test

Direct access.

---

### Related Labs

```text
Lab01
Lab02
```

---

# Scenario 2

## Role Information In Requests

### Observation

```text
role
roleid
admin
isAdmin
```

---

### Test

Modify values.

---

### Related Labs

```text
Lab03
Lab04
```

---

# Scenario 3

## 403 Forbidden Response

### Test Headers

```http
X-Original-URL
X-Rewrite-URL
```

---

### Related Lab

```text
Lab05
```

---

# Scenario 4

## Sensitive Action Uses POST

### Test

```http
GET
PUT
PATCH
```

---

### Related Lab

```text
Lab06
```

---

# Scenario 5

## User Identifier In URL

### Observation

```text
id=
user=
account=
```

---

### Test

Replace identifier.

---

### Related Labs

```text
Lab07
Lab08
Lab09
```

---

# Scenario 6

## Access To Other User Data

### Ask

```text
Can This Lead To Admin Access?
```

---

### Related Lab

```text
Lab10
```

---

# Scenario 7

## Direct File Access

### Observation

```text
.pdf
.txt
.csv
```

---

### Test

Modify filename.

---

### Related Lab

```text
Lab11
```

---

# Scenario 8

## Multi-Step Workflow

### Test

Skip earlier steps.

Replay final request.

---

### Related Lab

```text
Lab12
```

---

# Scenario 9

## Referer Required

### Test

Modify:

```http
Referer
```

---

### Related Lab

```text
Lab13
```

---

# Access Control Testing Formula

```text
URL
        ↓
Method
        ↓
Headers
        ↓
Parameters
        ↓
Workflow
```

---

# Severity Guide

```text
Data Disclosure
        ↓
Account Modification
        ↓
Account Takeover
        ↓
Admin Access
```

---

# Personal Bug Bounty Reminder

Never ask:

```text
Can I Access This?
```

Ask:

```text
Should I Be Able To Access This?
```

That mindset finds most access control vulnerabilities.