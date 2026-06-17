# Lab08 - User ID Controlled By Request Parameter With GUID

## Objective

Retrieve the API key for:

```text
carlos
```

using a GUID-based identifier.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Horizontal Privilege Escalation |
| Difficulty | Practitioner |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application uses GUIDs instead of usernames.

Developers assume GUIDs provide security.

---

# Analysis

## Step 1

Login as:

```text
wiener
```

---

## Step 2

Visit:

```text
/my-account?id=<guid>
```

---

## Step 3

Search site for:

```text
carlos
```

---

## Step 4

Open blog post authored by:

```text
carlos
```

---

## Step 5

Observe URL.

Found:

```text
carlos GUID
```

---

## Step 6

Replace your GUID with Carlos GUID.

---

## Step 7

Load page.

---

Result:

```text
Carlos Profile Accessible
```

---

## Step 8

Retrieve API key.

Lab solved.

---

# Full Payload Used

```text
/my-account?id=<carlos-guid>
```

---

# Why It Works

GUIDs are:

```text
Identifiers
```

not:

```text
Authorization Controls
```

---

Execution Flow

```text
GUID Leaked
        ↓
GUID Reused
        ↓
Ownership Check Missing
        ↓
Data Exposed
```

---

# Personal Analysis & Testing Process

## Initial Observation

Numeric IDs absent.

---

## Key Thought

GUIDs often create a false sense of security.

---

## Strategy

Find GUID elsewhere in application.

---

## Discovery

Carlos GUID leaked via blog author profile.

---

## Result

Profile and API key exposed.

Lab solved.

---

# Mental Model

Never assume:

```text
GUID
=
Secure
```

Always ask:

```text
Can I Obtain Another User's GUID?
```

---

# Related Theory

- 07-horizontal-privilege-escalation.md
- 09-insecure-direct-object-references-idor.md

---

# Key Learnings

- GUIDs are not authorization.
- Information disclosure often leads to IDOR.
- Always search for leaked identifiers.