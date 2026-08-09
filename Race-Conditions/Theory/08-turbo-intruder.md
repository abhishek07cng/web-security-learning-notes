# Turbo Intruder for Race Conditions

## Overview

**Turbo Intruder** is a Burp Suite extension that can be used to test race conditions.

The PortSwigger methodology recommends it as an alternative to Burp Repeater when sending groups of requests in parallel.

---

# When to Use Turbo Intruder

Turbo Intruder can be useful when:

- Many requests need to be sent.
- Custom request timing is required.
- The default Repeater workflow is insufficient.
- A short client-side delay is needed.

---

# Basic Workflow

```text
Identify Target
      ↓
Capture Request
      ↓
Send to Turbo Intruder
      ↓
Configure Requests
      ↓
Send Concurrently
      ↓
Observe Behavior
```

---

# Parallel Testing

The PortSwigger material describes Turbo Intruder as an alternative to Repeater's parallel request functionality.

It can be used to investigate whether multiple requests interact with the same data concurrently.

---

# Client-Side Delay

Turbo Intruder can introduce a short delay between requests.

However, the supplied material highlights an important limitation:

Using a client-side delay splits the actual attack requests across multiple TCP packets.

Therefore:

```text
Client-side delay
      ↓
Multiple TCP packets
      ↓
Single-packet attack unavailable
```

On high-jitter targets, the attack may therefore be unreliable regardless of the selected delay.

---

# Alternative Approach

If connection warming does not solve timing issues, the PortSwigger material describes intentionally triggering server-side rate or resource limits.

Sending many dummy requests may cause the server to introduce a processing delay.

This can make the single-packet technique viable when delayed execution is required.

---

# Repeater vs Turbo Intruder

| Burp Repeater | Turbo Intruder |
|---|---|
| Built-in Burp functionality | Burp extension |
| Request grouping | Custom request handling |
| Parallel requests | Parallel/custom timing |
| Easy initial testing | Useful for more specialized testing |

---

# Key Takeaways

- Turbo Intruder can assist with race condition testing.
- It is useful when custom timing or many requests are required.
- Client-side delays can interfere with single-packet synchronization.
- High network jitter can reduce reliability.