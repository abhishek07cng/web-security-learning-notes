# Time Delay Payloads

## Purpose

Use response delays to confirm Blind OS Command Injection.

---

## Example Payload

```text
ping -c 10 127.0.0.1
```

---

## Expected Result

The application responds approximately ten seconds later.

---

## Why It Works

The injected command forces the server to wait before completing the request.

---

# Key Takeaways

Time delays provide reliable evidence of command execution when output is unavailable.