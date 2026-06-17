# Referer-Based Access Control

## Overview

Some applications make authorization decisions using:

```http
Referer
```

headers.

---

# Example

Application expects:

```http
Referer:
/admin
```

before allowing sensitive actions.

---

# Intended Logic

```text
User Came From Admin Page
        ↓
Allow Request
```

---

# Problem

Attackers fully control:

```http
Referer
```

headers.

---

# Example

Blocked Request:

```http
POST /admin/delete-user
```

---

Attacker Adds:

```http
Referer:
/admin
```

---

Request succeeds.

---

# Why It Happens

Application trusts:

```text
Client-Supplied Data
```

for authorization.

---

# Testing Methodology

## Step 1

Identify sensitive request.

---

## Step 2

Remove Referer.

---

## Step 3

Modify Referer.

---

## Step 4

Observe behavior.

---

# Common Indicators

```text
403 Without Referer
200 With Referer
```

---

# Bug Bounty Mental Model

Ask:

```text
Is Authorization
Based On Headers?
```

---

# Related Labs

```text
Lab13
```

---

# Key Takeaways

- Referer is not a security control.
- Headers are attacker-controlled.
- Authorization must be server-side.