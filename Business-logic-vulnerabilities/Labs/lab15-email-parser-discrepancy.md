# Lab15 - Email Address Parser Discrepancy

## Objective

Bypass email-based restrictions.

---

# Vulnerability Overview

Different components interpret email addresses differently.

---

# Analysis

## Step 1

Observe registration restrictions.

Example:

```text
Only company emails allowed
```

---

## Step 2

Supply unusual email format.

---

## Step 3

Validation layer accepts one interpretation.

Backend accepts another.

---

## Result

Restriction bypassed.

Lab solved.

---

# Attack Flow

```text
Input Email
        ↓
Different Parsers
        ↓
Different Interpretations
        ↓
Restriction Bypassed
```

---

# Why It Works

Different systems apply different parsing rules.

---

# Personal Analysis & Testing Process

Whenever I see:

```text
Email Restrictions
Internal Access
Whitelists
```

I test:

```text
Encoding
Separators
Alternative Formats
```

---

# Related Theory

13-email-address-parser-discrepancies.md

---

# Key Learnings

Parser inconsistencies frequently create logic flaws.