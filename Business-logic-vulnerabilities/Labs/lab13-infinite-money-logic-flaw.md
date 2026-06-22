# Lab13 - Infinite Money Logic Flaw

## Objective

Generate unlimited store credit.

---

# Vulnerability Overview

Gift cards and store credits interact incorrectly.

Repeated transactions create money.

---

# Analysis

## Step 1

Purchase gift card.

---

## Step 2

Redeem gift card.

---

## Step 3

Abuse discount logic.

---

## Step 4

Generate more credit than spent.

---

## Result

Infinite money created.

Lab solved.

---

# Attack Flow

```text
Buy Gift Card
        ↓
Redeem Credit
        ↓
Discount Applied
        ↓
Profit Generated
```

---

# Why It Works

Application violates:

```text
Conservation Of Value
```

---

# Personal Analysis & Testing Process

Whenever I see:

```text
Wallet
Store Credit
Gift Cards
Rewards
```

I test:

```text
Can Money Be Created?
```

---

# Related Theory

06-failing-to-handle-unconventional-input.md

11-domain-specific-flaws.md

---

# Key Learnings

Business logic bugs often involve financial calculations.