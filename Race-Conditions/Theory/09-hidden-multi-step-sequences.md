# Hidden Multi-Step Sequences

## Overview

Not all race conditions involve simple limit overruns.

Applications can contain **hidden multi-step sequences** inside a single HTTP request.

These sequences may transition through temporary sub-states that are normally invisible to the user.

---

# Temporary Sub-States

A request may internally perform multiple operations:

```text
Request
  │
  ├── Step 1
  │
  ├── Temporary Sub-State
  │
  ├── Step 2
  │
  └── Final State
```

The temporary sub-state may create a race window.

---

# Example: MFA Workflow

The supplied material gives an example of an MFA implementation:

```text
session['userid'] = user.userid

if user.mfa_enabled:
    session['enforce_mfa'] = True

# generate and send MFA code
# redirect to MFA form
```

There is potentially a temporary state where:

```text
User is logged in
        +
MFA is not yet enforced
```

An attacker could potentially attempt to collide a login request with a request to a sensitive authenticated endpoint.

---

# Why This Matters

The vulnerability is not necessarily visible as a traditional:

```text
Check → Use
```

pattern.

Instead, the request itself may contain several hidden state transitions.

---

# Finding Hidden Sequences

The PortSwigger methodology recommends looking for endpoints that:

- Affect security-critical functionality.
- Operate on the same records.
- Perform multiple internal operations.
- Transition through temporary states.

---

# Predict → Probe → Prove

The methodology can be summarized as:

```text
PREDICT
   ↓
Identify potential collisions
   ↓
PROBE
   ↓
Benchmark and send requests concurrently
   ↓
PROVE
   ↓
Remove unnecessary requests and reproduce
```

---

# Predict Potential Collisions

Testing every endpoint is impractical.

Prioritize endpoints by asking:

### Is the endpoint security-critical?

If it does not affect important functionality, it may not be worth prioritizing.

### Is there collision potential?

A successful collision generally requires two or more requests that operate on the same record.

---

# Probe for Clues

First establish normal behavior.

In Burp Repeater:

```text
Send group in sequence
```

Then send the same requests concurrently:

```text
Send group in parallel
```

Compare the results.

---

# What Counts as a Clue?

Any deviation from normal behavior may be significant.

Examples include:

- Different HTTP responses
- Different response contents
- Different email contents
- Unexpected state changes
- Visible changes in application behavior

---

# Prove the Concept

Once a potential race condition is identified:

1. Understand what is happening.
2. Remove unnecessary requests.
3. Reduce the attack to the essential requests.
4. Confirm that the behavior remains reproducible.

---

# Structural Weakness

Advanced race conditions may produce unusual exploitation primitives.

Instead of treating the issue as an isolated bug, consider it a:

```text
Structural weakness in the application's state machine
```

This perspective can help identify the path toward maximum impact.

---

# Key Takeaways

- Race conditions can exist inside apparently single-step requests.
- Temporary sub-states can create hidden race windows.
- Multi-step sequences may affect authentication and other security-critical functionality.
- Use the **Predict → Probe → Prove** methodology.
- Focus on endpoints with both security impact and collision potential.