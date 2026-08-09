# Burp Repeater — Sending Requests in Parallel

## Overview

Race condition testing requires multiple requests to be processed concurrently.

Burp Suite Repeater provides functionality for grouping requests and sending them in parallel.

---

# Creating a Request Group

A typical workflow is:

1. Send relevant requests to Burp Repeater.
2. Add the requests to a tab group.
3. Benchmark them under normal conditions.
4. Send the group in parallel.
5. Compare the results.

---

# Sequential Benchmark

Before testing for a race condition, establish how the requests behave normally.

Use:

```text
Send group in sequence
```

This provides a baseline for:

- Response times
- Response contents
- Application behavior

---

# Parallel Testing

After establishing the baseline, use:

```text
Send group in parallel
```

This attempts to align the requests within the race window.

---

# Synchronization

Burp can automatically use synchronization techniques based on the HTTP version.

For HTTP/1:

```text
Last-byte synchronization
```

For HTTP/2:

```text
Single-packet attack
```

---

# Why Parallel Requests Matter

Sequential processing:

```text
Request A → Complete
              ↓
Request B → Complete
```

Parallel processing:

```text
Request A ───────┐
                 ├──> Collision
Request B ───────┘
```

The second approach is necessary when the vulnerability depends on concurrent state changes.

---

# What to Observe

Do not only examine HTTP responses.

Look for:

- Response differences
- Changed application behavior
- Different email contents
- Unexpected state changes
- Other second-order effects

---

# Key Takeaways

- Establish a sequential baseline first.
- Group related requests in Repeater.
- Send the same requests in parallel.
- Compare both direct and second-order effects.