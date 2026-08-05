# Timing-Based NoSQL Injection

## Overview

Sometimes NoSQL injection does not produce visible errors or response differences.

In these situations, timing-based techniques can be used to determine whether injected code is being executed.

The PortSwigger methodology relies on introducing a measurable delay in the server's response.

---

# Step 1 – Establish a Baseline

Load the application multiple times.

Measure the normal response time before testing any payloads.

---

# Step 2 – Inject a Timing Payload

Example payload:

```json
{
  "$where":"sleep(5000)"
}
```

This attempts to delay the response by approximately 5000 milliseconds.

---

# Step 3 – Observe the Response

If the application's response consistently takes longer than the baseline, this suggests that the injected code is being executed.

---

# Conditional Timing Payloads

The supplied material provides examples that introduce a delay only when a condition is true.

Example:

```text
admin'+function(x){if(x.password[0]==="a"){sleep(5000)};}(this)+'
```

Another example uses a loop that waits while a condition remains true.

Both approaches allow attackers to infer information by measuring response times.

---

# Why It Works

Instead of relying on visible output, timing-based attacks observe differences in server response time.

The delay acts as evidence that the injected expression has been evaluated.

---

# Key Takeaways

- Timing attacks are useful when no visible response differences exist.
- Baseline response times should be established before testing.
- Conditional delays enable blind extraction of information.