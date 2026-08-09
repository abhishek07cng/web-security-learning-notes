# Connection Warming

## Overview

Connection warming is a technique used when different requests have noticeably different response times.

These differences may be caused by the backend network architecture rather than the actual processing time of the endpoints.

---

# The Problem

Suppose two requests are sent sequentially:

```text
Request A → Slow
Request B → Fast
```

If this difference is caused by connection setup or backend network behavior, it can interfere with attempts to align the race windows.

---

# Benchmarking

In Burp Repeater:

1. Group the relevant requests.
2. Send them in sequence.
3. Observe their response times.

Example:

```text
Request A: ███████████
Request B: ███
```

---

# Warming the Connection

The PortSwigger material demonstrates adding an additional request to the beginning of the request group.

For example:

```text
GET /
POST /cart
POST /cart/checkout
```

Send them sequentially over the same connection.

---

# Effect

After warming the connection, the later requests may complete within a much smaller time window.

Conceptually:

### Before warming

```text
Request A ───────────────
Request B ─────
```

### After warming

```text
Warm-up ─────
Request A ───────
Request B ───────
```

The requests are now more closely aligned.

---

# Why It Works

The PortSwigger material explains that the initial delay can be caused by the backend network architecture rather than the processing time of the individual endpoints.

Once the connection has been warmed, this delay may no longer interfere significantly with the attack.

---

# Example Workflow

```text
Identify Requests
       ↓
Send Sequentially
       ↓
Observe Timing Difference
       ↓
Add Warm-Up Request
       ↓
Send Sequentially Again
       ↓
Compare Timing
       ↓
Remove Warm-Up Request
       ↓
Attempt Parallel Attack
```

---

# When Connection Warming Doesn't Help

If warming the connection does not sufficiently align the requests, other techniques may be considered.

The supplied material discusses:

- Turbo Intruder client-side delays
- Server-side delays caused by rate/resource limits

However, client-side delays can split attack requests across multiple TCP packets and therefore prevent use of the single-packet attack.

---

# Key Takeaways

- Connection warming can reduce timing differences caused by backend network behavior.
- Benchmark request timing before attempting exploitation.
- A warm-up request can make subsequent requests complete within a smaller window.
- If warming does not help, other synchronization strategies may be necessary.
```

---

## ✅ Theory Progress

Completed:

- ✅ 01 — What Are Race Conditions?
- ✅ 02 — Race Windows
- ✅ 03 — Limit Overrun Race Conditions
- ✅ 04 — TOCTOU Race Conditions
- ✅ 05 — Detecting Limit Overruns
- ✅ 06 — Aligning Race Windows
- ✅ 07 — Burp Repeater Parallel Requests
- ✅ 08 — Turbo Intruder
- ✅ 09 — Hidden Multi-Step Sequences
- ✅ 10 — Predict, Probe, Prove Methodology
- ✅ 11 — Multi-Endpoint Race Conditions
- ✅ 12 — Connection Warming

### Remaining Theory

- ⏳ **13 — Single-Endpoint Race Conditions**
- ⏳ **14 — Partial Construction Race Conditions**
- ⏳ **15 — Prevention**

After those three, the **Theory section will be 15/15 complete**.