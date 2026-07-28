# Command Injection Bug Bounty Checklist

## Reconnaissance

- Identify server-side functionality.
- Locate parameters used in system operations.
- Intercept requests using Burp Suite.

---

## Initial Testing

- Test visible command execution.
- Try different command separators.
- Observe server responses.

---

## Blind Testing

If output is hidden:

- Test time delays.
- Test output redirection.
- Test Burp Collaborator.
- Test out-of-band data exfiltration.

---

## Confirmation

Confirm command execution using one or more of the following:

- Visible output
- Response delay
- Generated output file
- DNS interaction
- Recovered command output

---

## Reconnaissance Commands

### Linux

```bash
whoami
uname -a
ifconfig
netstat -an
ps -ef
```

### Windows

```cmd
whoami
ver
ipconfig /all
netstat -an
tasklist
```

---

## Report

Include:

- Vulnerable endpoint
- Vulnerable parameter
- Payload used
- Evidence of successful execution
- Impact
- Suggested remediation

---

# Quick Checklist

- ☐ Identify injection point
- ☐ Test visible execution
- ☐ Test blind execution
- ☐ Confirm exploitation
- ☐ Gather evidence
- ☐ Assess impact
- ☐ Prepare report