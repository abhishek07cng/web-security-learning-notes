# Payload 10 – Race Condition Testing Methodology

## Phase 1 – Predict a Collision

Ask:

```text
What state is being changed?
```

Then:

```text
Which endpoints modify it?
```

Then:

```text
Can two requests access that state simultaneously?
```

---

## Phase 2 – Benchmark

First test normally.

```text
Request
Request
Request
```

Record:

```text
Status
Response length
Timing
State changes
Errors
```

This creates the baseline.

---

## Phase 3 – Introduce Concurrency

Send the same requests:

```text
in parallel
```

Compare the results with the baseline.

---

## Phase 4 – Identify the Race Window

Look for:

```text
Different response
Different response length
Unexpected success
Unexpected email
Unexpected account state
Unexpected cart state
Identical tokens
Unexpected authorization
```

---

## Phase 5 – Remove Noise

Remove unnecessary requests.

Keep only the requests needed to reproduce the behavior.

---

## Phase 6 – Prove the Concept

Repeat the minimal attack.

The goal is to demonstrate:

```text
Normal behavior
      ↓
Concurrent behavior
      ↓
Unexpected state
      ↓
Security impact
```

---

# Race Condition Checklist

## Single-Use Functionality

```text
☐ Coupons
☐ Gift cards
☐ CAPTCHA
☐ Email verification
☐ Password reset
☐ Registration
```

## Rate Limits

```text
☐ Login attempts
☐ OTP attempts
☐ Password reset requests
☐ API rate limits
```

## Financial Operations

```text
☐ Checkout
☐ Transfers
☐ Withdrawals
☐ Balance checks
```

## Account State

```text
☐ Email changes
☐ Password changes
☐ Role changes
☐ Account creation
☐ Verification
```

---

# Core Question

Whenever you encounter:

```text
CHECK
  ↓
TEMPORARY STATE
  ↓
UPDATE
```

ask:

> Can another request interact with the application during the temporary state?

That temporary period is the potential:

```text
RACE WINDOW
```

---

# Important Defensive Principle

Sensitive state transitions should be atomic.

The source recommends using datastore concurrency features and transactions so that sensitive checks and state changes happen as a single atomic operation. :contentReference[oaicite:16]{index=16}