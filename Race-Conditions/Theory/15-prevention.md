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