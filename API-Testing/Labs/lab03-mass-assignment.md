# Lab03 - Mass Assignment Vulnerability

## Objective

Purchase the jacket using hidden object properties.

---

# Vulnerability Overview

The API automatically binds user-controlled JSON data to internal object properties.

---

# Analysis

## Step 1

Observe response.

Visible fields:

```json
{
 "name":"jacket",
 "price":1337
}
```

---

## Step 2

Inspect hidden object structure.

Discover:

```text
discount
chosen_discount
```

---

## Step 3

Add hidden properties.

---

## Step 4

Send modified request.

---

## Result

Price reduced.

Lab solved.

---

# Attack Flow

```text
Hidden Property
        ↓
Automatic Binding
        ↓
Business Logic Abuse
```

---

# Personal Analysis & Testing Process

Whenever I see JSON APIs I ask:

```text
What Properties Exist Internally?
```

---

# Related Theory

07-hidden-parameters.md

08-mass-assignment-vulnerabilities.md

---

# Key Learnings

Object properties may exist even when hidden from the UI.