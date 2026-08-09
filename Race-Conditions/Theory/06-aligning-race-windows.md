# Aligning Race Windows

## Overview

Successfully exploiting a race condition requires requests to overlap within the vulnerable race window.

The PortSwigger material highlights synchronization as one of the primary challenges when testing race conditions.

---

# The Problem

Suppose the vulnerable operation lasts only a few milliseconds:

```text
Request A
       ├──────── Race Window ────────┤

Request B
              ├──────── Race Window ────────┤
```

If the windows do not overlap, no collision occurs.

---

# Desired Result

The goal is:

```text
Request A
       ├───────────────┤
       │ Race Window   │
       ├───────────────┤

Request B
       ├───────────────┤
       │ Race Window   │
       ├───────────────┤
```

The vulnerable portions overlap.

---

# Network Jitter

Network jitter introduces uncertainty in when requests arrive at the server.

Even if requests are sent simultaneously:

```text
Client
 ├── Request A
 └── Request B

        ↓

Network

        ↓

Server
 ├── Request A arrives
 └────── Request B arrives later
```

The requests may no longer overlap correctly.

---

# Burp Repeater

The PortSwigger material describes enhanced Burp Repeater functionality for sending groups of requests in parallel.

Burp automatically selects an appropriate synchronization technique based on the HTTP version supported by the server.

---

# HTTP/1 Synchronization

For HTTP/1, Burp uses:

```text
Last-byte synchronization
```

This technique helps hold requests until they are ready to be completed, improving the chance that their processing overlaps.

---

# HTTP/2 Synchronization

For HTTP/2, Burp uses the:

```text
Single-packet attack
```

The PortSwigger material describes this technique as being designed to greatly reduce interference from network jitter.

---

# Single-Packet Attack

The single-packet technique can cause many requests to be completed simultaneously.

The supplied material notes that approximately:

```text
20–30 requests
```

can be completed using a single TCP packet in the described attack technique.

---

# Why Send Many Requests?

Although an exploit may require only two requests, sending more requests can help reduce the impact of internal server-side latency.

For example:

```text
Request 1 ──┐
Request 2 ──┤
Request 3 ──┤
Request 4 ──┤
Request 5 ──┤──> Race Window
Request 6 ──┤
Request 7 ──┘
```

This can improve reliability during the discovery phase.

---

# Synchronization Workflow

```text
Identify Race Window
        ↓
Prepare Parallel Requests
        ↓
Determine HTTP Version
        ↓
Use Appropriate Synchronization
        ↓
Send Requests
        ↓
Observe Collision
        ↓
Repeat to Confirm
```

---

# Key Takeaways

- Race-window alignment is critical for exploitation.
- Network jitter can prevent simultaneous processing.
- Burp Repeater provides synchronization techniques.
- HTTP/1 uses last-byte synchronization.
- HTTP/2 can use the single-packet attack.
- Sending multiple requests can improve initial detection reliability.