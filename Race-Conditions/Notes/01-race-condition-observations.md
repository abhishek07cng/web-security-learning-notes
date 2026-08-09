# Race Condition Testing Checklist

## 1. Identify the Functionality

Look for functionality involving:

- Single-use actions
- Rate limits
- Account changes
- Password resets
- Email confirmation
- Registration
- Financial transactions
- Checkout
- Other security-sensitive state changes

---

## 2. Map the Application

Identify:

- Relevant endpoints
- Parameters
- Cookies
- Session state
- Requests that modify the same data
- Requests that read the same data

---

## 3. Predict a Collision

Ask:

```text
Can multiple requests interact with the same state?
```

Look for:

```text
Request A → State X
Request B → State X
```

This indicates potential collision.

---

## 4. Establish a Baseline

Send requests normally.

Record:

- Status codes
- Response lengths
- Response contents
- Response timing
- Application state

---

## 5. Send Requests Concurrently

Use Burp Repeater:

```text
Send group in parallel
```

For more complex timing:

```text
Turbo Intruder
```

---

## 6. Compare Results

Look for differences between sequential and parallel execution.

Potential indicators:

- Unexpected successful response
- Different response length
- Different response content
- Multiple successful operations
- Unexpected email
- Unexpected token
- Unexpected account state
- Unexpected cart state
- Unexpected authorization

---

## 7. Identify the Race Window

Determine the sequence of operations:

```text
Check
 ↓
Temporary State
 ↓
Update
```

The temporary state is the potential race window.

---

## 8. Reduce the Attack

Remove unnecessary requests.

Keep only the requests required to reproduce the behavior.

```text
Complex Attack
      ↓
Remove Noise
      ↓
Minimal Reproduction
```

---

## 9. Confirm Reproducibility

Repeat the minimal attack.

Record:

```text
Attempts
Successful attempts
Failure attempts
Success rate
```

---

## 10. Determine Impact

A race condition is more important when it affects:

- Authentication
- Authorization
- Account ownership
- Financial transactions
- Sensitive data
- Security controls
- Rate limits

---

# Quick Checklist

```text
☐ Map endpoints
☐ Identify shared state
☐ Identify collision potential
☐ Establish baseline
☐ Test sequentially
☐ Test in parallel
☐ Compare responses
☐ Identify race window
☐ Reduce requests
☐ Reproduce
☐ Confirm security impact
```

---

# Core Methodology

```text
PREDICT
   ↓
PROBE
   ↓
PROVE
```

This is the primary workflow for investigating race conditions.