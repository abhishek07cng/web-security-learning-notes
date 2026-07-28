# Command Injection Checklist

## Detection

- Test visible output (`echo`)
- Test command separators
- Identify blind behaviour
- Test time delays
- Test output redirection
- Test OAST
- Test out-of-band data exfiltration

---

## Confirmation

- Command output returned
- Response delay observed
- Output file created
- DNS interaction received
- Command output recovered

---

## Reconnaissance

### Linux

- `whoami`
- `uname -a`
- `ifconfig`
- `netstat -an`
- `ps -ef`

### Windows

- `whoami`
- `ver`
- `ipconfig /all`
- `netstat -an`
- `tasklist`

---

## Prevention

- Avoid OS commands.
- Use platform APIs.
- Apply strict allowlist validation.
- Validate expected input types.
- Reject unexpected characters.

---

# One-Minute Workflow

```
Identify Input

↓

Inject echo

↓

Visible?

↓

Yes → Confirm

↓

No

↓

Time Delay

↓

Output Redirection

↓

OAST

↓

Data Exfiltration

↓

Assess Impact
```