# Race Conditions Testing Methodology

## Overview

Race condition testing focuses on identifying situations where multiple requests can interact with the same application state during a temporary or inconsistent state.

The core methodology is:

```text
PREDICT → PROBE → PROVE
```

---

# Phase 1 — Predict

## 1. Map the Application

Identify:

- Security-critical endpoints
- Authentication functionality
- Account-management functionality
- Financial operations
- Single-use functionality
- Rate-limited functionality
- Requests that modify shared state

---

## 2. Identify Collision Potential

Ask:

```text
Can two or more requests interact with the same record?
```

Example:

```text
Request A → Account X
Request B → Account X
```

This has collision potential.

---

## 3. Identify Temporary States

Look for workflows such as:

```text
CHECK
  ↓
TEMPORARY STATE
  ↓
UPDATE
```

The temporary state may represent a race window.

---

# Phase 2 — Probe

## 1. Establish a Baseline

Send requests normally.

Record:

- HTTP status
- Response length
- Response content
- Response timing
- Application state

---

## 2. Send Requests Sequentially

Use Burp Repeater to establish normal behavior.

---

## 3. Send Requests in Parallel

Use:

```text
Send group in parallel
```

Compare the result with the sequential baseline.

---

## 4. Look for Deviations

Potential indicators:

- Unexpected successful responses
- Multiple successful operations
- Different response lengths
- Unexpected email contents
- Unexpected tokens
- Unexpected account state
- Unexpected authorization
- Unexpected cart state

---

# Phase 3 — Prove

Once a potential race condition is discovered:

1. Understand the collision.
2. Remove unnecessary requests.
3. Keep only the essential requests.
4. Repeat the attack.
5. Confirm reproducibility.
6. Demonstrate security impact.

---

# Race Condition Categories

## Limit Overrun

```text
Single-use restriction
        ↓
Concurrent requests
        ↓
Restriction exceeded
```

---

## TOCTOU

```text
Time of Check
      ↓
Race Window
      ↓
Time of Use
```

---

## Multi-Endpoint

```text
Endpoint A ──┐
             ├── Shared State
Endpoint B ──┘
```

---

## Single-Endpoint

```text
Request A ──┐
Request B ──┤
Request C ──┘
     ↓
Same Endpoint
```

---

## Partial Construction

```text
Object Creation
      ↓
Partial State
      ↓
Completed State
```

A concurrent request may interact with the object during the partial state.

---

# Synchronization

If timing is inconsistent:

### Connection Warming

Use a preliminary request to reduce connection-related timing differences.

### Burp Repeater

Use parallel request groups.

### Turbo Intruder

Use when:

- Many requests are required.
- The race window is very small.
- Custom synchronization is required.

### Single-Packet Attack

For HTTP/2 testing, the source describes the single-packet technique as a way to reduce network jitter.

---

# Final Workflow

```text
Map
 ↓
Predict
 ↓
Benchmark
 ↓
Probe
 ↓
Synchronize
 ↓
Identify Race Window
 ↓
Reduce Requests
 ↓
Reproduce
 ↓
Prove Impact
```