# Limit Overrun Race Conditions

## Overview

A **limit overrun race condition** is one of the most well-known forms of race condition.

It occurs when an attacker exceeds a limit imposed by the application's business logic.

---

# Example: One-Time Discount

Imagine an online store that provides a promotional code that should only be used once.

The application may perform these steps:

```text
1. Check that the code has not already been used
2. Apply the discount
3. Update the database
4. Mark the code as used
```

Under normal circumstances, attempting to reuse the code should fail.

---

# Vulnerable Scenario

Suppose two requests are sent almost simultaneously.

```text
Request A
   │
   ├── Check: unused
   │
   ├── Apply discount
   │
   └── Update database

Request B
   │
   ├── Check: unused
   │
   ├── Apply discount
   │
   └── Update database
```

If both requests reach the validation step before the database is updated, both may pass the check.

---

# Temporary Sub-State

The application temporarily enters a sub-state during request processing.

```text
Initial State
     │
     ▼
Processing Request
     │
     ▼
Temporary Sub-State
     │
     ▼
Database Updated
     │
     ▼
Final State
```

The race window exists during this temporary sub-state.

---

# Possible Variations

The supplied material gives several examples of limit-overrun attacks:

- Redeeming a gift card multiple times
- Rating a product multiple times
- Withdrawing or transferring cash beyond an account balance
- Reusing a single CAPTCHA solution
- Bypassing an anti-brute-force rate limit

---

# Relationship to TOCTOU

Limit overrun race conditions are a subtype of:

```text
Time-of-Check to Time-of-Use (TOCTOU)
```

The problem occurs because the application's security check and subsequent state-changing operation are separated in time.

---

# Detection Methodology

The PortSwigger methodology recommends:

### Step 1 — Identify the Endpoint

Find a:

- Single-use endpoint
- Rate-limited endpoint
- Security-sensitive endpoint
- Functionality with a useful business impact

---

### Step 2 — Send Multiple Requests

Issue multiple requests in quick succession.

```text
Request 1 ──┐
Request 2 ──┤
Request 3 ──┤──> Target Endpoint
Request 4 ──┘
```

---

### Step 3 — Look for an Overrun

Determine whether the application's limit can be exceeded.

---

# Main Challenge

The primary challenge is timing.

At least two requests must overlap inside the race window.

The window may be only milliseconds long.

---

# Burp Repeater

Burp Repeater can be used to send requests in parallel.

The PortSwigger material explains that newer Burp versions automatically adapt the synchronization technique depending on the HTTP version.

```text
HTTP/1  → Last-byte synchronization
HTTP/2  → Single-packet attack
```

---

# Key Takeaways

- Limit overruns exploit business-logic limits.
- The attack relies on concurrent requests.
- Both requests may pass the same validation before the state is updated.
- Limit overruns are a subtype of TOCTOU flaws.
- Burp Repeater can help align parallel requests.