# Lab04 - Low-Level Logic Flaw

## Objective

Purchase products without sufficient balance.

---

# Vulnerability Overview

Arithmetic assumptions break due to integer handling.

---

# Analysis

## Step 1

Add many products.

---

## Step 2

Observe total value.

---

## Step 3

Trigger:

```text
Integer Overflow
```

or abnormal calculations.

---

## Step 4

Checkout succeeds.

Lab solved.

---

# Why It Works

```text
Large Values
        ↓
Overflow
        ↓
Unexpected Total
```

---

# Related Theory

06-failing-to-handle-unconventional-input.md

---

# Key Learnings

Boundary conditions often produce logic flaws.