# Partial Construction Race Conditions

## Overview

A **partial construction race condition** occurs when an application temporarily creates or modifies an object before the object reaches its final state.

During this temporary state, another concurrent request may interact with the partially constructed data.

---

# Basic Concept

An application may construct data in multiple stages:

```text
Step 1
  ↓
Partial Object
  ↓
Step 2
  ↓
Completed Object
```

The partial object may contain information or behavior that should not be externally accessible.

---

# Race Window

The vulnerable period exists while the object is only partially constructed:

```text
Create
  │
  ▼
Partial Construction
  │
  │ ← Race Window
  │
  ▼
Completed Object
```

A concurrent request attempts to access the object during this window.

---

# Why This Matters

Applications may assume that an object is either:

```text
Not Created
```

or:

```text
Fully Created
```

But internally, it may temporarily exist in an intermediate state.

An attacker can attempt to access this intermediate state using a concurrent request.

---

# Testing Methodology

### Step 1 — Identify State Creation

Look for functionality that creates or modifies:

- Accounts
- Sessions
- Tokens
- Orders
- Other security-sensitive records

---

### Step 2 — Identify Related Requests

Determine whether another endpoint can access the same object while it is being created.

---

### Step 3 — Benchmark Normal Behavior

Send the requests sequentially.

Observe:

- Response timing
- Response contents
- Application state

---

### Step 4 — Send in Parallel

Use Burp Repeater or Turbo Intruder.

```text
Request A ───────┐
                 ├──> Partial Object
Request B ───────┘
```

---

### Step 5 — Look for Unexpected State

Check whether the second request observes data that should only exist after construction is complete.

---

# Relationship to Hidden Multi-Step Sequences

Partial construction is closely related to hidden multi-step sequences.

Both rely on temporary application states.

```text
Initial State
     ↓
Temporary State
     ↓
Final State
```

The race condition occurs when another request interacts with the temporary state.

---

# Predict → Probe → Prove

Use the same methodology:

```text
Predict
  ↓
Identify possible shared state
  ↓
Probe
  ↓
Send concurrent requests
  ↓
Prove
  ↓
Reproduce the unexpected behavior
```

---

# Key Takeaways

- Applications may expose partially constructed objects.
- Temporary construction states can create race windows.
- A concurrent request may interact with the object before construction is complete.
- Testing requires identifying shared state and overlapping requests.
```

---

# `Theory/15-prevention.md`

````md
# Preventing Race Conditions

## Overview

Race conditions occur when concurrent requests can interact with application state in an unsafe way.

Preventing them requires ensuring that security-sensitive state transitions cannot be manipulated through concurrent execution.

---

# Main Principle

The vulnerable sequence should not allow another request to observe or modify an unsafe intermediate state.

Conceptually:

```text
Unsafe:

Check
  ↓
Race Window
  ↓
Update
```

A safer design ensures that the relevant operation is handled atomically.

---

# Atomic Operations

Security-sensitive operations should ideally be performed as an atomic transaction.

Instead of:

```text
Check
  ↓
Use
  ↓
Update
```

the application should ensure that another concurrent request cannot interfere between these operations.

---

# Avoid Exposed Temporary States

Applications should avoid allowing security-sensitive temporary states to be accessed by concurrent requests.

For example:

```text
Initial
   ↓
Secure Atomic Operation
   ↓
Final
```

rather than exposing:

```text
Initial
   ↓
Temporary Vulnerable State
   ↓
Final
```

---

# Protect Shared State

When multiple requests can access the same record or session state, the application should ensure that concurrent operations cannot produce inconsistent results.

This is particularly important for:

- Authentication
- Password resets
- Financial transactions
- Rate limits
- Single-use functionality
- Account changes

---

# Rate and Resource Limits

Rate limits can sometimes interact with race conditions in unexpected ways.

Security-sensitive operations should be designed so that sending many requests concurrently cannot bypass the intended restriction.

---

# Testing as a Defensive Measure

Developers should test security-critical workflows under concurrent requests.

Testing should include:

- Parallel requests
- Multiple simultaneous users
- Repeated single-use operations
- Concurrent state changes

---

# State Machine Review

Review workflows as state machines:

```text
Initial State
      ↓
Intermediate State
      ↓
Final State
```

Ask:

- Can another request access the intermediate state?
- Can two requests modify the same record?
- Are check and update operations separated?
- Can requests reach security-sensitive functionality concurrently?

---

# Prevention Checklist

☐ Protect shared application state.

☐ Make security-sensitive operations atomic where appropriate.

☐ Prevent access to unsafe intermediate states.

☐ Ensure single-use functionality cannot be reused concurrently.

☐ Ensure rate limits cannot be bypassed through parallel requests.

☐ Review multi-step workflows for race windows.

☐ Test security-critical endpoints under concurrent requests.

---

# Key Takeaways

- Race conditions are fundamentally problems involving concurrent state changes.
- Security-sensitive operations should be protected from unsafe interleaving.
- Temporary states should not expose security-sensitive behavior.
- Atomic handling of critical operations reduces race-condition risk.
- Developers should test workflows using concurrent requests.