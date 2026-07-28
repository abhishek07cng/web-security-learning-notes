# Command Injection Detection Methodology

## Overview

Detecting an OS Command Injection vulnerability involves identifying locations where user-controlled input is incorporated into operating system commands.

The PortSwigger material demonstrates different techniques depending on whether the application returns command output.

---

# Step 1 – Identify User Input

Locate parameters that influence server-side functionality.

Examples include:

- Product IDs
- Store IDs
- Feedback fields
- Email parameters

These inputs may be incorporated into operating system commands.

---

# Step 2 – Test for Visible Command Injection

Inject a harmless command that produces visible output.

Example:

```text
& echo aiwefwlguh &
```

If the application returns the supplied string, command execution has been confirmed.

---

# Step 3 – Determine Whether the Vulnerability is Blind

If no output is returned:

- The command may still execute.
- The application may simply suppress the output.

Continue testing using blind detection techniques.

---

# Step 4 – Test Time Delays

Inject a command that deliberately delays execution.

Example:

```text
ping -c 10 127.0.0.1
```

If the response is delayed by approximately ten seconds, the command likely executed.

---

# Step 5 – Test Output Redirection

If a writable web-accessible directory exists:

- Redirect command output into a file.
- Request the generated file through the browser.

This confirms execution without relying on the application's response.

---

# Step 6 – Test Out-of-Band (OAST)

If output cannot be viewed and files cannot be written:

- Trigger a DNS lookup.
- Monitor Burp Collaborator for interactions.

A successful interaction confirms command execution.

---

# Step 7 – Assess Impact

Once execution is confirmed, determine:

- Which operating system is running.
- Which user executes commands.
- Whether additional information can be obtained.

---

# Detection Workflow

```
Locate Input

↓

Inject echo

↓

Output Visible?

↓

Yes → Command Injection Confirmed

↓

No

↓

Time Delay

↓

Output Redirection

↓

OAST

↓

Confirm Execution

↓

Assess Impact
```

---

# Key Takeaways

- Begin with visible payloads whenever possible.
- If output is unavailable, switch to blind detection techniques.
- Use the simplest method that successfully confirms command execution.