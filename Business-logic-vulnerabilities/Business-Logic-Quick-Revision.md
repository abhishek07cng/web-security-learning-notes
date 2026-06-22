# Business Logic Quick Revision

## Root Cause

```text
Bad Assumptions
```

---

## Formula

```text
Assumption
        ↓
Violation
        ↓
Unexpected State
        ↓
Impact
```

---

## Common Targets

```text
Checkout
Coupons
Gift Cards
Wallets
Password Reset
2FA
Registration
```

---

## Common Tests

### Negative Values

```text
-1
0
999999999
```

---

### Parameter Removal

```text
coupon=
token=
email=
```

---

### Workflow Bypass

```text
Skip Steps
Replay Requests
```

---

### State Machine

```text
Session Created Too Early
```

---

### Financial Abuse

```text
Infinite Money
Coupon Reuse
```

---

### Parser Discrepancies

```text
Email Validation
Encoding
```

---

## Severity Ladder

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

# Top Lessons From PortSwigger

1. Business logic bugs exploit assumptions.

2. Users do not follow intended workflows.

3. Authentication ≠ Trust.

4. Financial functionality deserves special attention.

5. State machines are frequently broken.

6. Scanners rarely find business logic bugs.

7. Ask:

```text
Should This Be Possible?
```

instead of:

```text
Can I Do This?
```

---

# Personal Business Logic Formula

```text
Understand Feature
        ↓
Find Assumptions
        ↓
Break Assumptions
        ↓
Unexpected State
        ↓
Impact
```