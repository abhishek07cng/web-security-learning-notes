# Lab05 - Inconsistent Handling Of Exceptional Input

## Objective

Bypass restrictions and purchase the jacket.

---

# Vulnerability Overview

Different parts of the application handle unusual inputs differently.

---

# Analysis

## Step 1

Observe normal behavior.

---

## Step 2

Supply:

```text
Long Strings
Special Characters
Unexpected Values
```

---

## Step 3

Application components disagree.

---

## Step 4

Restrictions bypassed.

Lab solved.

---

# Attack Flow

```text
Input
        ↓
Different Components
        ↓
Different Interpretation
        ↓
Logic Flaw
```

---

# Why It Works

Validation and processing behave inconsistently.

---

# Related Theory

06-failing-to-handle-unconventional-input.md

13-email-address-parser-discrepancies.md

---

# Key Learnings

Parser inconsistencies frequently cause logic flaws.