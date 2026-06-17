# Insecure Direct Object References (IDOR)

## Overview

IDOR is a type of access control vulnerability where user-supplied identifiers are trusted without authorization checks.

---

# Example

Application:

```text
/account?id=1001
```

---

Attacker Changes:

```text
/account?id=1002
```

---

# Result

Another user's data exposed.

---

# Why It Happens

Application checks:

```text
User Is Logged In
```

but not:

```text
User Owns Resource
```

---

# Common Identifiers

## Numeric IDs

```text
?id=1
?id=2
?id=3
```

---

## Usernames

```text
?user=wiener
```

---

## GUIDs

```text
?id=ea7f8c91-34d2
```

---

## Filenames

```text
/report.pdf
```

↓

```text
/admin-report.pdf
```

---

# Testing Methodology

## Step 1

Find identifiers.

---

## Step 2

Modify identifier.

---

## Step 3

Observe response.

---

## Step 4

Check:

```text
Status Code
Data Changes
Authorization Errors
```

---

# Bug Bounty Mental Model

Ask:

```text
What Object
Am I Referencing?
```

---

# Related Labs

```text
Lab07
Lab08
Lab10
Lab11
```

---

# Key Takeaways

- IDOR is one of the most common access control bugs.
- GUIDs do not automatically provide security.
- Every object access requires authorization.