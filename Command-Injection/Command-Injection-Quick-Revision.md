# Command Injection Quick Revision

## Definition

OS Command Injection (Shell Injection) allows attackers to execute operating system commands through user-controlled input.

---

# Common Indicators

- User input reaches shell commands.
- Shell metacharacters are accepted.
- Unexpected command execution.

---

# Command Separators

Cross-platform:

```text
&
&&
|
||
```

Unix:

```text
;
Newline
```

Inline execution:

```text
`command`
```

```text
$(command)
```

---

# Detection Methods

### Visible

```text
echo
```

### Blind

- Time Delay
- Output Redirection
- OAST
- Data Exfiltration

---

# Useful Commands

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

# OAST

Use Burp Collaborator to:

- Confirm execution
- Recover command output

---

# Prevention

- Avoid shell commands.
- Use platform APIs.
- Validate input.
- Use allowlists.
- Reject unexpected characters.

---

# Exam Tips

Remember this order:

```
Visible

↓

Time Delay

↓

Output Redirection

↓

OAST

↓

Data Exfiltration

↓

Recon
```

---

# One-Minute Summary

OS Command Injection occurs when user input is incorporated into operating system commands without proper validation. Depending on the application's behaviour, successful exploitation may be confirmed through visible output, response delays, output redirection, or Out-of-Band (OAST) techniques using Burp Collaborator. Effective prevention focuses on avoiding shell commands and applying strict input validation.