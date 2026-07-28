# Command Injection Interview Notes

## What is OS Command Injection?

OS Command Injection (Shell Injection) is a vulnerability that allows an attacker to execute operating system commands on the server by injecting malicious input into commands executed by the application.

---

## Why is it Dangerous?

It can allow an attacker to:

- Execute arbitrary operating system commands.
- Gather information about the server.
- Access sensitive data.
- Compromise the application.
- Potentially pivot to other systems within the organisation.

---

## How Can It Be Detected?

Visible Command Injection:

- Inject a harmless command such as:

```text
echo
```

Blind Command Injection:

- Time delays
- Output redirection
- OAST (Burp Collaborator)
- Out-of-band data exfiltration

---

## What Are Command Separators?

Common separators include:

```text
&
&&
|
||
;
```

Unix systems also support newline characters.

---

## What Is Inline Command Execution?

Unix-based shells support:

```text
`command`
```

and

```text
$(command)
```

These execute the enclosed command before continuing with the original shell command.

---

## Useful Reconnaissance Commands

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

## What Is OAST?

Out-of-Band Application Security Testing (OAST) confirms command execution by causing the server to interact with an external system, such as Burp Collaborator.

---

## How Does Out-of-Band Data Exfiltration Work?

The output of a command (for example, `whoami`) is embedded into a DNS request sent to Burp Collaborator, allowing the tester to recover the command output without relying on the application's HTTP response.

---

## How Can OS Command Injection Be Prevented?

- Avoid executing operating system commands whenever possible.
- Use platform APIs instead of shell commands.
- Apply strict allowlist-based input validation.
- Validate expected input types.
- Reject unexpected characters.
- Do not rely solely on escaping shell metacharacters.

---

# Interview Quick Answers

### What is the difference between visible and blind OS Command Injection?

Visible OS Command Injection returns the output of injected commands in the application's response.

Blind OS Command Injection executes commands successfully but hides their output, requiring indirect confirmation techniques such as time delays, output redirection, or OAST.

---

### Which tool is commonly used for OAST in PortSwigger Academy?

**Burp Collaborator**.

---

### What is the safest way to prevent OS Command Injection?

Avoid invoking operating system commands whenever possible and use native platform APIs instead.