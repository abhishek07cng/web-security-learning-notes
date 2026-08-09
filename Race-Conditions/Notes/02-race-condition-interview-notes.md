# Race Condition Burp Suite Workflow

## Burp Repeater

Burp Repeater is useful for manually investigating race conditions.

---

## Step 1 — Find the Request

Use:

```text
Proxy → HTTP history
```

Find the request associated with the functionality being tested.

---

## Step 2 — Send to Repeater

Right-click:

```text
Send to Repeater
```

---

## Step 3 — Create a Request Group

Duplicate the request as necessary.

Group related requests together.

Examples:

```text
POST /cart/coupon
POST /cart/coupon
POST /cart/coupon
```

or:

```text
POST /cart
POST /cart/checkout
```

---

## Step 4 — Establish Baseline

Send requests sequentially.

Observe:

```text
Status
Length
Response
Timing
```

---

## Step 5 — Parallel Testing

Use:

```text
Send group in parallel
```

Compare the results against the sequential baseline.

---

# Connection Warming

If requests have noticeably different response times, try adding a harmless request before the attack requests.

Example:

```http
GET /
```

Then:

```text
GET /
POST /cart
POST /cart/checkout
```

This can reduce timing differences caused by backend connection setup.

---

# Turbo Intruder

Use Turbo Intruder when:

- Many requests are required.
- The race window is very small.
- Burp Repeater is insufficient.
- You need custom request scheduling.
- You need gates for synchronization.

---

# Gate Concept

Requests can be queued using a common gate:

```python
engine.queue(request, gate='1')
```

Then released:

```python
engine.openGate('1')
```

Conceptually:

```text
Queue
 ↓
Queue
 ↓
Queue
 ↓
openGate()
 ↓
Requests released
```

---

# Single-Packet Technique

The source describes using:

```text
HTTP/2
Engine.BURP2
concurrentConnections=1
```

to minimize network jitter.

This is useful when the race window is extremely small.

---

# Important Observation

Do not rely only on immediate responses.

Race conditions can produce second-order effects.

Check:

```text
Email
Account state
Cart
Tokens
Authorization
Database-backed behavior
```

---

# Workflow Summary

```text
Proxy
 ↓
HTTP History
 ↓
Send to Repeater
 ↓
Create Group
 ↓
Sequential Baseline
 ↓
Parallel Test
 ↓
Observe Collision
 ↓
Turbo Intruder if Necessary
 ↓
Minimize Attack
 ↓
Confirm Impact
```