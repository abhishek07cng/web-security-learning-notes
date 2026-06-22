# What Are Business Logic Vulnerabilities?

## Overview

Business Logic Vulnerabilities are flaws in the design or implementation of an application that allow attackers to trigger unintended behavior.

These vulnerabilities allow attackers to abuse legitimate functionality to achieve malicious goals.

---

# Business Logic

Business logic represents the rules that define how an application should behave.

Examples:

```text
Order Processing
Authentication
Discounts
Password Reset
Coupon Systems
2FA
Role Management
```

---

# Root Cause

Developers make assumptions about:

```text
User Behavior
Application State
Workflow Sequence
Input Values
```

Attackers violate these assumptions.

---

# Why Logic Flaws Are Difficult

Logic flaws:

```text
Depend On Context
Require Human Understanding
Are Difficult To Automate
Often Unique
```

---

# Typical Attack Flow

```text
Understand Business Rules
        ↓
Find Assumption
        ↓
Break Assumption
        ↓
Trigger Unexpected State
        ↓
Abuse Functionality
```

---

# Examples

```text
Price Manipulation
2FA Bypass
Coupon Abuse
Workflow Bypass
Infinite Money
Password Reset Flaws
Authentication State Machine Bugs
```

---

# Key Takeaways

- Logic flaws abuse intended functionality.
- These bugs are difficult for scanners to detect.
- Manual testing is essential.