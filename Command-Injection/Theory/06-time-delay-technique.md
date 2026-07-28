# Detecting Blind OS Command Injection Using Time Delays

## Overview

When command output is not returned by the application, one method of confirming execution is to introduce a deliberate delay.

If the server responds noticeably later than expected, this indicates that the injected command was executed.

---

# Using Ping

The PortSwigger material uses the `ping` command because it allows control over how long the command runs.

Example payload:

```bash
& ping -c 10 127.0.0.1 &
```

---

# How It Works

The injected command causes the server to ping its loopback interface.

Because the command runs for approximately ten seconds, the application's response is delayed by the same amount.

---

# Lab Example

The feedback function accepts an email parameter.

Modified value:

```text
email=x||ping+-c+10+127.0.0.1||
```

After submitting the request, the application's response takes approximately **10 seconds** to return.

This delay confirms that the injected command executed.

---

# Detection Workflow

```
Inject Ping Command

↓

Server Executes Ping

↓

Response Delayed

↓

Execution Confirmed
```

---

# Why It Works

Although the application hides command output, it cannot hide the additional processing time required to execute the injected command.

The delay itself becomes evidence of successful execution.

---

# Advantages

- Does not require command output.
- Easy to observe.
- Effective for blind vulnerabilities.

---

# Limitations

- Relies on measurable response delays.
- Asynchronous execution may reduce the effectiveness of this technique.

---

# Key Takeaways

- Time delays are an effective way to detect blind Command Injection.
- The PortSwigger material demonstrates using `ping` to introduce a controlled delay.
- A significant response delay indicates that the injected command executed successfully.