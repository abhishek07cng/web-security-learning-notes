# Detecting Limit Overrun Race Conditions

## Overview

The PortSwigger methodology describes a relatively straightforward process for detecting limit overrun race conditions.

The main difficulty is synchronizing requests so that they overlap within the race window.

---

# Step 1 — Identify a Suitable Endpoint

Look for endpoints that have:

- Single-use functionality
- Rate limits
- Business-logic restrictions
- Security-sensitive operations

Examples include:

```text
Promotional codes
Gift cards
CAPTCHA verification
Rate-limited login functionality
Financial operations
```

---

# Step 2 — Understand the Normal Workflow

Determine what the application normally does.

For example:

```text
Request
   ↓
Check limit
   ↓
Perform operation
   ↓
Update state
```

Understanding this sequence helps identify where a race condition may occur.

---

# Step 3 — Send Multiple Requests

Send several requests to the same endpoint in quick succession.

Conceptually:

```text
Request 1 ──┐
Request 2 ──┤
Request 3 ──┤──> Target
Request 4 ──┘
```

The goal is to cause multiple requests to enter the vulnerable state simultaneously.

---

# Step 4 — Observe the Result

Look for behavior that exceeds the intended limit.

Examples:

```text
Single-use code
      ↓
Used multiple times
```

or:

```text
Rate limit
      ↓
More requests accepted than expected
```

---

# Main Challenge

The race window may only last a few milliseconds.

Simply sending requests one after another may not trigger the vulnerability.

---

# Network Jitter

Even if requests are sent at approximately the same time, network conditions can affect when they reach the server.

This is known as:

```text
Network Jitter
```

---

# Server-Side Jitter

The server itself may also process requests at slightly different times.

This can make it difficult to align requests inside the race window.

---

# Burp Repeater

Burp Repeater provides functionality for sending multiple requests in parallel.

The PortSwigger material describes:

### HTTP/1

Burp uses:

```text
Last-byte synchronization
```

### HTTP/2

Burp can use:

```text
Single-packet attack
```

This helps reduce the impact of network jitter.

---

# Increasing the Number of Requests

Although two requests may sometimes be enough, sending a larger number of requests can help compensate for internal server-side latency.

This can be useful during the initial discovery phase.

---

# Testing Workflow

```text
Identify Endpoint
       ↓
Understand State Changes
       ↓
Identify Potential Race Window
       ↓
Send Parallel Requests
       ↓
Observe Responses
       ↓
Check for Limit Overrun
       ↓
Repeat if Necessary
```

---

# Key Takeaways

- Start with single-use or rate-limited functionality.
- Understand the normal state transition.
- Send multiple requests concurrently.
- Network and server-side jitter can affect results.
- Burp Repeater helps synchronize requests.
- A successful overrun confirms the race condition.
```

---

# `Theory/06-aligning-race-windows.md`

````md
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