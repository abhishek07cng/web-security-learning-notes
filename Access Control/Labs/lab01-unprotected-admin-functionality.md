# Lab01 - Unprotected Admin Functionality

## Objective

Access the administrator panel and delete the user:

```text
carlos
```

to solve the lab.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Vertical Privilege Escalation |
| Difficulty | Apprentice |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application contains administrator functionality that is not protected by access controls.

Normal users should not be able to access:

```text
/admin
```

---

# Analysis

## Step 1

Browse the application normally.

---

## Step 2

Inspect:

```text
robots.txt
```

---

Found:

```text
Disallow: /administrator-panel
```

---

## Step 3

Navigate directly to:

```text
/administrator-panel
```

---

Result:

```text
Admin Panel Accessible
```

---

## Step 4

Locate user:

```text
carlos
```

---

## Step 5

Delete the account.

Lab solved.

---

# Full Request Used

```http
GET /administrator-panel HTTP/2
```

---

# Why It Works

Application relies on:

```text
Hidden URL
```

instead of:

```text
Authorization Checks
```

---

Execution Flow

```text
Admin URL Discovered
        ↓
No Authorization Check
        ↓
Admin Panel Access
        ↓
Delete User
```

---

# Personal Analysis & Testing Process

## Initial Observation

Admin functionality not visible.

---

## Key Thought

Many applications expose sensitive paths through:

```text
robots.txt
```

---

## Discovery

Found:

```text
/administrator-panel
```

inside robots file.

---

## Result

Direct access granted.

No authorization validation existed.

Lab solved.

---

# Mental Model

Whenever you find:

```text
robots.txt
sitemap.xml
backup files
```

always check for:

```text
Admin URLs
Hidden Functionality
```

---

# Mitigation

Implement:

```text
Server-Side Authorization Checks
```

for all admin functionality.

---

Never rely on:

```text
Hidden URLs
```

for security.

---

# Related Theory

- 03-vertical-access-controls.md
- 06-vertical-privilege-escalation.md

---

# Key Learnings

- Hidden functionality is not security.
- robots.txt often leaks sensitive endpoints.
- Authorization must be enforced server-side.