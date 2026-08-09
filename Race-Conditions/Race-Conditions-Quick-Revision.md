# Race Conditions — Quick Revision

## Definition

A race condition occurs when concurrent requests interact with shared application state in an unintended way.

---

# Race Window

The temporary period during which requests can collide.

```text
CHECK
 ↓
RACE WINDOW
 ↓
UPDATE
```

---

# Main Types

## 1. Limit Overrun

Allows an attacker to exceed an intended limit.

Examples:

```text
Coupon reuse
Gift-card reuse
Rate-limit bypass
```

---

## 2. TOCTOU

```text
Time of Check
      ↓
Race Window
      ↓
Time of Use
```

---

## 3. Multi-Endpoint

Different endpoints interact with shared state.

```text
/cart
   +
/cart/checkout
```

---

## 4. Single-Endpoint

Multiple requests target the same endpoint.

```text
/change-email
/change-email
```

---

## 5. Partial Construction

Another request interacts with an object while it is still being constructed.

```text
Create
 ↓
Partial State
 ↓
Complete
```

---

# Detection

Start with:

```text
PREDICT
```

Identify possible collisions.

Then:

```text
PROBE
```

Compare sequential and parallel requests.

Finally:

```text
PROVE
```

Reduce the attack and reproduce it.

---

# Burp Repeater

Basic workflow:

```text
Proxy History
     ↓
Send to Repeater
     ↓
Create Request Group
     ↓
Sequential Baseline
     ↓
Parallel Requests
     ↓
Compare Results
```

---

# Turbo Intruder

Useful when:

- Many requests are required.
- The race window is very small.
- Custom synchronization is needed.

---

# Connection Warming

Useful when requests have different timing because of connection setup.

Concept:

```text
Warm Connection
      ↓
Attack Requests
      ↓
Better Alignment
```

---

# Single-Packet Attack

For HTTP/2:

```text
Engine.BURP2
concurrentConnections=1
```

The technique attempts to reduce network jitter.

---

# Important Indicators

Look for:

```text
Multiple successful operations
Unexpected response
Unexpected response length
Unexpected email
Unexpected token
Unexpected account state
Unexpected authorization
Unexpected cart state
```

---

# Testing Workflow

```text
Map
 ↓
Predict
 ↓
Benchmark
 ↓
Probe
 ↓
Parallelize
 ↓
Identify Race Window
 ↓
Reduce
 ↓
Reproduce
 ↓
Prove Impact
```

---

# Prevention

The key defensive principle is:

```text
Make security-sensitive state transitions atomic.
```

Use appropriate datastore concurrency controls and transactions where required.

---

# One-Minute Summary

Race conditions exploit concurrent processing of shared state.

The attacker looks for:

```text
Check
 ↓
Temporary State
 ↓
Update
```

and attempts to send another request during the temporary state.

The core methodology is:

```text
PREDICT → PROBE → PROVE
```