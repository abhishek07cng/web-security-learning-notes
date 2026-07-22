# OAST and Burp Collaborator

## Overview

Out-of-Band Application Security Testing (OAST) is the primary technique for detecting Blind SSRF vulnerabilities.

Since Blind SSRF does not return the server's response to the attacker, OAST relies on monitoring interactions with a server that you control.

Burp Collaborator is the most commonly used OAST tool for this purpose.

---

# What is Burp Collaborator?

Burp Collaborator generates unique domains that can receive:

- DNS requests
- HTTP requests
- SMTP interactions

If the vulnerable application attempts to access one of these domains, Burp Collaborator records the interaction.

---

# How OAST Works

```
Attacker

↓

Insert Collaborator Payload

↓

Application

↓

Burp Collaborator Server

↓

DNS / HTTP Request

↓

Interaction Logged
```

---

# Typical Workflow

1. Generate a Burp Collaborator payload.
2. Insert the payload into a vulnerable parameter.
3. Send the request.
4. Poll Burp Collaborator for interactions.
5. Review any DNS or HTTP requests made by the application.

---

# Example

Referer header:

```http
Referer: http://abcd1234.burpcollaborator.net
```

If the application fetches the supplied URL, Burp Collaborator records the interaction.

---

# DNS vs HTTP Interactions

### DNS Only

The application resolved the domain name but could not establish an HTTP connection.

Possible reason:

- Outbound HTTP traffic is blocked.
- Only DNS requests are permitted.

---

### DNS + HTTP

The application successfully contacted the external server.

This provides stronger evidence of Blind SSRF.

---

# Why OAST Matters

Blind SSRF often provides no visible response.

OAST confirms that the server made the outbound request, allowing attackers to detect vulnerabilities that would otherwise remain invisible.

---

# Bug Bounty Perspective

Whenever you suspect Blind SSRF:

- Generate a Burp Collaborator payload.
- Insert it into URL-based parameters.
- Test headers such as Referer.
- Poll for DNS and HTTP interactions.

---

# Key Learnings

Burp Collaborator enables reliable detection of Blind SSRF by recording outbound interactions initiated by the vulnerable application.