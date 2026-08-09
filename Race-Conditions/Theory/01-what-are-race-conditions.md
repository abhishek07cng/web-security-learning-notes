# What Are Race Conditions?

## Overview

Race conditions are a type of vulnerability closely related to business logic flaws.

They occur when a website processes requests concurrently without adequate safeguards.

This can cause multiple threads to interact with the same data at the same time, resulting in a **collision** that produces unintended application behavior.

A race condition attack intentionally sends carefully timed requests to trigger these collisions.

---

# Basic Concept

A vulnerable application may process multiple requests concurrently:

```text
Request A ────────┐
                  ├──> Shared Data
Request B ────────┘
```

If the application does not properly synchronize these operations, both requests may interact with the same state before the first request has completed its security checks or updates.

---

# Race Window

The period during which a collision is possible is called the:

```text
Race Window
```

This can be extremely small.

For example:

```text
Check ─────── Race Window ─────── Update
```

The race window may only exist for a fraction of a second.

---

# Race Condition Attack

An attacker attempts to align multiple requests within the race window.

```text
Request 1 ──────────────┐
                        │
Request 2 ──────────────┼──> Collision
                        │
Request 3 ──────────────┘
```

If successful, the application may process multiple requests based on the same temporary state.

---

# Impact

The impact depends heavily on:

- The application
- The affected functionality
- The data being accessed
- The business logic involved

Possible consequences include:

- Exceeding usage limits
- Reusing single-use functionality
- Bypassing rate limits
- Multiple gift-card redemptions
- Multiple product ratings
- Excessive withdrawals or transfers
- Reusing a CAPTCHA solution

---

# Relationship to Business Logic

Race conditions are closely related to business logic vulnerabilities because they exploit the way an application transitions between different states.

A particularly important concept is the existence of **temporary sub-states**.

---

# Temporary Sub-State

A sensitive operation may temporarily enter a state before returning to its final state.

Example:

```text
Initial State
      │
      ▼
Temporary Sub-State
      │
      ▼
Final State
```

If another request reaches the application during the temporary sub-state, it may interact with data that has not yet been securely updated.

---

# Key Takeaways

- Race conditions occur when concurrent requests interact with shared data.
- A collision can produce unintended behavior.
- The exploitable period is called the race window.
- Race windows can be extremely short.
- Race conditions are closely related to business logic flaws.
- Exploitation relies on carefully timing multiple requests.