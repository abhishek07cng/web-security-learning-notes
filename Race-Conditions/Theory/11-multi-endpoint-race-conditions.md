# Multi-Endpoint Race Conditions

## Overview

A **multi-endpoint race condition** occurs when requests to different endpoints interact with the same application state at the same time.

This is one of the most intuitive forms of race condition.

---

# Basic Example

Consider an online store:

```text
1. Add item to cart
2. Pay for the item
3. Confirm order
```

Normally:

```text
Add Item
   ↓
Payment
   ↓
Order Confirmation
```

---

# Race Variation

Suppose payment validation and order confirmation happen during the same request.

There may be a race window between:

```text
Payment Validated
       ↓
Race Window
       ↓
Order Confirmed
```

During this window, another request may modify the cart.

---

# Example Collision

```text
POST /cart
       │
       ├── Add expensive item
       │
       ▼
POST /cart/checkout
       │
       ├── Payment validated
       │
       │ ← Race Window
       │
       └── Order confirmed
```

A concurrent cart request may add additional items after payment validation but before the order is finalized.

---

# State Machine

Conceptually:

```text
Cart State
    │
    ▼
Payment Validation
    │
    ├──── Race Window ────┐
    │                     │
    ▼                     ▼
Order Confirmation    Cart Modification
```

The application may therefore finalize an order using a state that differs from the state that was originally validated.

---

# Identifying Multi-Endpoint Candidates

Use Burp Proxy history to identify endpoints that interact with the same functionality.

For example:

```text
POST /cart
POST /cart/checkout
```

These endpoints may operate on the same session-specific cart.

---

# Collision Potential

The supplied material recommends determining whether the relevant state is stored server-side.

For example, if the cart contents disappear when the session cookie is removed, this indicates that the cart state is associated with the session.

That suggests that multiple requests using the same session may interact with the same underlying state.

---

# Testing Workflow

```text
Identify Related Endpoints
          ↓
Determine Shared State
          ↓
Benchmark Requests
          ↓
Identify Potential Race Window
          ↓
Send Requests in Parallel
          ↓
Observe State Changes
          ↓
Confirm Impact
```

---

# Key Takeaways

- Multi-endpoint races involve different endpoints.
- The endpoints must interact with shared application state.
- Financial and workflow-related functionality can be particularly important to investigate.
- The critical race window may exist between validation and final state transition.