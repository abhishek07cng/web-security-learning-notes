# Lab12 - Discount Logic Flaw

## Objective

Purchase items at an unintended discount.

---

# Vulnerability Overview

Coupon and discount logic can be abused because the application makes incorrect assumptions.

---

# Analysis

## Step 1

Apply discount.

---

## Step 2

Observe:

```text
Coupon
Quantity
Total Price
```

---

## Step 3

Reuse coupon multiple times.

---

## Result

Total price reduced unexpectedly.

Lab solved.

---

# Attack Flow

```text
Coupon Applied
        ↓
Coupon Reused
        ↓
Unexpected Discount
```

---

# Why It Works

Business rules fail to enforce:

```text
Single Use
Maximum Discount
```

---

# Personal Analysis & Testing Process

Whenever I see:

```text
Coupons
Gift Cards
Rewards
Promo Codes
```

I test:

```text
Reuse
Replay
Multiple Applications
```

---

# Related Theory

08-users-wont-always-remain-trustworthy.md

11-domain-specific-flaws.md

---

# Key Learnings

Financial logic requires strict validation.