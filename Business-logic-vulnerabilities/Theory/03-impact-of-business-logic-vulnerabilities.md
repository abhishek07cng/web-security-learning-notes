# Impact Of Business Logic Vulnerabilities

## Overview

Business logic flaws can have impacts ranging from low severity to complete compromise.

Impact depends on:

```text
Functionality Affected
Business Context
Attack Chain
```

---

# Authentication Logic

May Lead To:

```text
Authentication Bypass
Privilege Escalation
Account Takeover
```

---

# Financial Logic

May Lead To:

```text
Price Manipulation
Coupon Abuse
Infinite Money
Fraud
```

---

# Workflow Logic

May Lead To:

```text
Skipping Security Checks
Purchasing Without Payment
Unauthorized Actions
```

---

# Input Validation Logic

May Lead To:

```text
Negative Prices
Integer Overflow
Unexpected States
```

---

# Severity Ladder

```text
Information Disclosure
        ↓
Privilege Escalation
        ↓
Account Takeover
        ↓
Financial Fraud
        ↓
Authentication Bypass
```

---

# Why Minor Bugs Matter

Seemingly harmless quirks may become dangerous when chained with other vulnerabilities.

---

# Key Takeaways

Any unintended behavior should be investigated.