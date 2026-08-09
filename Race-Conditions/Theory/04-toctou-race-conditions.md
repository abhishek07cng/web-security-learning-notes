# TOCTOU Race Conditions

## Overview

Limit overrun race conditions are a subtype of:

**Time-of-Check to Time-of-Use (TOCTOU)** vulnerabilities.

A TOCTOU race condition occurs when an application checks a condition and later uses the result, while another request can interact with the same state between those two operations.

---

# Basic Pattern

A vulnerable operation may follow this sequence:

```text
1. Check current state
        ↓
2. Perform operation
        ↓
3. Update state
```

The vulnerability exists when another request can reach the application between the check and the state update.

---

# Example

Consider a single-use discount code.

```text
Check:
"Has this code already been used?"
        ↓
Apply discount
        ↓
Mark code as used
```

If two requests arrive concurrently:

```text
Request A → Check: unused
Request B → Check: unused
Request A → Apply discount
Request B → Apply discount
Request A → Mark used
Request B → Mark used
```

Both requests may successfully use the same discount.

---

# Race Window

The vulnerable period is the time between:

```text
Time of Check
      ↓
Race Window
      ↓
Time of Use
```

This is where another request may cause a collision.

---

# Why TOCTOU Happens

The application treats the check and subsequent state change as separate operations.

If those operations are not atomic, concurrent requests may observe the same state.

---

# Common Examples

TOCTOU-style race conditions may affect:

- Single-use promotional codes
- Gift-card redemption
- Financial transactions
- CAPTCHA validation
- Rate limits

---

# Relationship to Limit Overruns

```text
Race Conditions
      │
      └── TOCTOU
            │
            └── Limit Overrun
```

Limit overrun race conditions are therefore a specific example of TOCTOU behavior.

---

# Key Takeaways

- TOCTOU means Time-of-Check to Time-of-Use.
- The vulnerability exists when checking and using a value are separated.
- Another request can interact with the same state during the race window.
- Limit overruns are a subtype of TOCTOU race conditions.