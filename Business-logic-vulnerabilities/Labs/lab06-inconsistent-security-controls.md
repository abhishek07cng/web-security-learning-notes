# Lab06 - Inconsistent Security Controls

## Objective

Access functionality reserved for internal users.

---

# Vulnerability Overview

The application applies different security controls to different components.

One component performs validation while another trusts the input.

---

# Analysis

## Step 1

Observe email restrictions.

Application expects:

```text
@dontwannacry.com
```

---

## Step 2

Attempt registration using unconventional email formats.

---

## Step 3

Different components interpret email differently.

---

## Result

Internal-only restrictions bypassed.

Lab solved.

---

# Why It Works

```text
Validation Layer
        ↓
Parser Difference
        ↓
Bypass Restriction
```

---

# Personal Analysis & Testing Process

Whenever restrictions depend on:

```text
Email Domain
Phone Number
Username
```

I test parser discrepancies.

---

# Related Theory

13-email-address-parser-discrepancies.md

---

# Key Learnings

Different components may interpret input differently.