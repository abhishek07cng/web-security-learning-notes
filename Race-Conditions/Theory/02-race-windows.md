# Race Windows

## Overview

A **race window** is the period during which concurrent requests can interact with an application in an unintended way.

The smaller the race window, the more difficult exploitation becomes.

---

# Example

Consider a one-time promotional code.

The application performs:

```text
1. Check whether code has already been used
2. Apply discount
3. Update database
4. Mark code as used
```

Normally:

```text
Request
   │
   ▼
Check code
   │
   ▼
Apply discount
   │
   ▼
Mark code as used
```

A second request should only be processed after the first request has completed.

---

# Race Window

The vulnerable period occurs between the validation and database update:

```text
Check
  │
  │
  │  ← Race Window
  │
Update
```

During this period, another request may also pass the initial validation.

---

# Concurrent Requests

An attacker attempts to send requests so that they overlap inside the race window.

```text
Request A:
Check ─────────────── Update

Request B:
      Check ─────────────── Update
```

Both requests may observe the same initial state.

---

# Why Timing Matters

The race window may be extremely short.

The supplied PortSwigger material notes that it can sometimes be only milliseconds or even shorter.

Even when requests are sent at exactly the same time, external factors can affect when the server actually processes them.

These factors are referred to as:

```text
Network Jitter
Server-Side Jitter
```

---

# Aligning Race Windows

The objective is to make multiple requests overlap during the vulnerable period.

Conceptually:

```text
Request A      ────────┐
                       │
                       ├── Race Window
                       │
Request B      ────────┘
```

Successful alignment creates a collision.

---

# Burp Suite Support

The PortSwigger material describes newer Burp Repeater capabilities for sending groups of requests in parallel.

For HTTP/1:

```text
Last-byte synchronization
```

For HTTP/2:

```text
Single-packet attack
```

The single-packet technique can send many requests together in a way that greatly reduces the impact of network jitter.

---

# Key Takeaways

- The race window is the vulnerable period between application state transitions.
- Race windows may be extremely short.
- Multiple requests must overlap within this period.
- Network and server-side jitter can make alignment difficult.
- Burp Suite provides techniques for improving request synchronization.