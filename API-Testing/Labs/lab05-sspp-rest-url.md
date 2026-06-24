# Lab05 - Server-Side Parameter Pollution In REST Paths

## Objective

Reset Carlos's password.

---

# Vulnerability Overview

User-controlled values influence internal REST URLs.

---

# Analysis

## Step 1

Observe:

```text
/api/user/wiener
```

---

## Step 2

Manipulate path.

Examples:

```text
../
```

---

## Step 3

Reach hidden functionality.

---

## Step 4

Extract reset information.

---

## Result

Carlos password reset.

Lab solved.

---

# Attack Flow

```text
Path Input
        ↓
Internal REST URL
        ↓
Unexpected Endpoint
```

---

# Personal Analysis & Testing Process

Whenever I see:

```text
REST APIs
Path Parameters
```

I ask:

```text
Can Path Construction Be Influenced?
```

---

# Related Theory

09-server-side-parameter-pollution.md

11-sspp-in-rest-paths.md

---

# Key Learnings

REST path construction should never trust user input.