# Predict, Probe, Prove Methodology

## Overview

PortSwigger recommends a three-stage methodology for efficiently identifying and exploiting advanced race conditions:

```text
Predict → Probe → Prove
```

This approach helps reduce the number of endpoints that need to be tested and makes it easier to distinguish genuine race conditions from normal application behavior.

---

# Phase 1 — Predict Potential Collisions

Testing every endpoint is impractical.

After mapping the target normally, prioritize endpoints using two questions:

### 1. Is the endpoint security-critical?

Focus on functionality that affects:

- Authentication
- Authorization
- Sensitive account operations
- Financial operations
- Other critical business logic

Endpoints that do not affect important functionality are lower priority.

---

### 2. Is There Collision Potential?

A successful collision generally requires two or more requests to interact with the same record.

For example:

```text
Request A → Record X
Request B → Record X
```

has collision potential.

Whereas:

```text
Request A → Record X
Request B → Record Y
```

is less likely to produce a useful collision.

---

# Phase 2 — Probe for Clues

First establish a baseline under normal conditions.

In Burp Repeater:

```text
Send group in sequence
```

Observe:

- Response times
- Response contents
- Application behavior

---

# Parallel Testing

Next, send the same request group concurrently.

Use:

```text
Send group in parallel
```

This attempts to minimize network jitter and align the requests within the race window.

Turbo Intruder can also be used as an alternative.

---

# What Counts as a Clue?

Any deviation from the normal baseline can be significant.

Look for:

- Changed responses
- Different response contents
- Different email contents
- Unexpected application behavior
- Changes that only become visible after the requests complete

These later effects are examples of **second-order effects**.

---

# Phase 3 — Prove the Concept

Once a potential collision has been identified:

1. Understand what is happening.
2. Remove unnecessary requests.
3. Reduce the attack to the essential requests.
4. Repeat the attack.
5. Confirm that the behavior remains reproducible.

---

# Why This Matters

Advanced race conditions can produce unusual exploitation primitives.

The objective is not simply to identify a strange response.

You should understand the underlying state transition and determine whether it represents a genuine security weakness.

---

# Methodology Flow

```text
Map Application
      ↓
Identify Security-Critical Endpoints
      ↓
Identify Collision Potential
      ↓
Benchmark Normal Behavior
      ↓
Send Requests in Parallel
      ↓
Look for Deviations
      ↓
Understand the Collision
      ↓
Remove Superfluous Requests
      ↓
Reproduce
      ↓
Prove Impact
```

---

# Key Takeaways

- **Predict** which endpoints are worth testing.
- **Probe** them for deviations from normal behavior.
- **Prove** the race condition by simplifying and reproducing it.
- Prioritize security-critical functionality.
- Look for requests that operate on the same record.