# Lab 02 – Blind OS Command Injection with Time Delays

## Lab Overview

**Objective**

Detect a Blind OS Command Injection vulnerability by introducing a deliberate delay in the server's response.

The application executes injected commands but does not display their output.

---

# Vulnerability

The feedback function sends submitted data using an operating system command.

Although commands execute successfully, their output is not returned to the browser.

---

# Reconnaissance

Open the feedback form.

Complete the required fields.

Intercept the submission request.

---

# Exploitation

Modify the email parameter.

Original:

```text
user@example.com
```

Modified:

```text
x||ping -c 10 127.0.0.1||
```

Forward the request.

---

# Successful Result

The server responds approximately **10 seconds** later.

The delay confirms that the injected command executed.

---

# Why It Works

The injected `ping` command occupies the server for approximately ten seconds.

Although no command output is returned, the increased response time proves successful execution.

---

# Impact

Blind Command Injection can still lead to complete system compromise despite the absence of visible output.

---

# Mitigation

- Avoid executing shell commands.
- Apply strict input validation.
- Reject unexpected shell metacharacters.

---

# Bug Bounty Methodology

1. Identify blind functionality.
2. Inject a time-delay payload.
3. Measure response time.
4. Repeat to confirm consistent behaviour.
5. Report successful command execution.

---

# Key Learnings

- Blind vulnerabilities require indirect confirmation techniques.
- Response timing can provide strong evidence of command execution.