# Blind Command Injection Payloads

## Overview

Blind OS Command Injection does not return command output.

Alternative techniques are required to confirm execution.

---

## Example Payload

```text
echo test
```

If output is not visible, move to blind detection techniques.

---

## Detection Options

- Time delays
- Output redirection
- OAST
- Out-of-band data exfiltration

---

# Key Takeaways

Blind vulnerabilities require indirect methods to verify command execution.