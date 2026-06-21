# File Upload Observations

## Observation 1

Validation usually fails because:

```text
User Input Is Trusted
```

---

## Observation 2

Blacklists are unreliable.

---

## Observation 3

Content-Type headers are attacker-controlled.

---

## Observation 4

Storage location determines severity.

---

## Observation 5

Execution is worse than upload.

---

## Observation 6

Polyglot files bypass magic-byte checks.

---

## Observation 7

Race conditions are timing vulnerabilities.

---

## Personal Formula

```text
Upload
        ↓
Store
        ↓
Execute
```