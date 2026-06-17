# Lab11 - Insecure Direct Object Reference

## Objective

Retrieve the contents of:

```text
carlos secret file
```

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | IDOR |
| Difficulty | Apprentice |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application references files directly using predictable identifiers.

No authorization checks exist.

---

# Analysis

## Step 1

Download your own transcript.

---

Example:

```text
/static/121.txt
```

---

## Step 2

Modify filename.

---

Original:

```text
/static/121.txt
```

---

Modified:

```text
/static/122.txt
```

---

## Step 3

Observe another user's file.

---

## Step 4

Enumerate until:

```text
carlos.txt
```

or corresponding file.

---

## Step 5

Open file.

Lab solved.

---

# Full Payload Used

```text
/static/121.txt
```

↓

```text
/static/122.txt
```

---

# Why It Works

Application trusts:

```text
User Supplied File Identifier
```

without ownership validation.

---

# Attack Flow

```text
File Identifier
        ↓
Modified
        ↓
No Access Check
        ↓
Sensitive File Exposed
```

---

# Personal Analysis & Testing Process

## Initial Observation

Files accessed directly through URL.

---

## Key Thought

Predictable filenames often indicate IDOR.

---

## Result

Sensitive file retrieved.

Lab solved.

---

# Mental Model

Whenever you see:

```text
.pdf
.txt
.csv
.docx
```

check:

```text
Can Filename Be Changed?
```

---

# Related Theory

- 09-insecure-direct-object-references-idor.md

---

# Key Learnings

- Files require authorization checks.
- Predictable identifiers create IDOR opportunities.