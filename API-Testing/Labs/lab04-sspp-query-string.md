# Lab04 - Server-Side Parameter Pollution In Query Strings

## Objective

Reset Carlos's password.

---

# Vulnerability Overview

User input is concatenated into internal API requests.

---

# Analysis

## Step 1

Observe request:

```text
username=wiener
```

---

## Step 2

Inject:

```text
&
#
```

characters.

---

## Step 3

Manipulate internal request construction.

---

## Step 4

Discover reset token.

---

## Result

Password reset achieved.

Lab solved.

---

# Why It Works

```text
User Input
        ↓
Internal Request
        ↓
Parameter Injection
        ↓
Unexpected Behavior
```

---

# Personal Analysis & Testing Process

Whenever input becomes part of:

```text
URLs
Query Strings
```

I test:

```text
&
#
=
?
```

---

# Related Theory

09-server-side-parameter-pollution.md

10-sspp-in-query-strings.md

---

# Key Learnings

Internal APIs often trust user input too much.