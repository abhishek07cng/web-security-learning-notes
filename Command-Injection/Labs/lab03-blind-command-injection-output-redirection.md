# Lab 03 – Blind OS Command Injection with Output Redirection

## Lab Overview

**Objective**

Retrieve the output of a blind command injection by redirecting it into a web-accessible file.

---

# Vulnerability

The application executes injected commands but suppresses their output.

However, it contains a writable directory that is accessible through the web server.

---

# Reconnaissance

Intercept the feedback request.

Identify the vulnerable email parameter.

---

# Exploitation

Modify the email value:

```text
||whoami>/var/www/images/output.txt||
```

Submit the request.

---

# Retrieve Output

Request:

```text
/output.txt
```

The browser displays the contents of the generated file.

---

# Successful Result

The returned file contains the output of:

```bash
whoami
```

confirming successful command execution.

---

# Why It Works

The shell redirects the command output into a file.

Because the directory is web-accessible, the attacker can retrieve the output through a normal HTTP request.

---

# Impact

Attackers can recover command output even when the application suppresses it.

---

# Mitigation

- Prevent execution of OS commands.
- Restrict write access to web-accessible directories.
- Validate all user input.

---

# Bug Bounty Methodology

1. Confirm blind injection.
2. Identify writable directories.
3. Redirect output to a file.
4. Retrieve the file.
5. Verify command execution.

---

# Key Learnings

- Output redirection is an effective technique for blind OS Command Injection.
- Web-accessible directories increase the impact of the vulnerability.