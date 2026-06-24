# Lab02 - Hidden API Endpoint

## Objective

Purchase the jacket using the hidden API.

---

# Vulnerability Overview

The application exposes additional functionality through unsupported methods.

---

# Analysis

## Step 1

Observe endpoint:

```http
/api/products/1
```

---

## Step 2

Send:

```http
OPTIONS /api/products/1
```

---

## Step 3

Discover:

```text
PATCH
```

method.

---

## Step 4

Modify Content-Type.

---

## Step 5

Use hidden endpoint functionality.

---

## Result

Lab solved.

---

# Why It Works

```text
OPTIONS
        ↓
Hidden Method
        ↓
Additional Functionality
```

---

# Personal Analysis & Testing Process

Whenever I discover APIs I test:

```text
GET
POST
PUT
PATCH
DELETE
OPTIONS
```

---

# Related Theory

05-supported-http-methods.md

06-supported-content-types.md

---

# Key Learnings

Hidden methods often expose functionality.