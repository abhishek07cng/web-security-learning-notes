# XXE-Based SSRF

## Overview

XXE can sometimes be used to perform **Server-Side Request Forgery (SSRF)**.

Instead of using an external entity to reference a local file, the entity references a URL.

The vulnerable XML parser then causes the server to make a request to that URL.

---

# Basic Concept

```text
Attacker
   ↓
Malicious XML
   ↓
External Entity
   ↓
Internal URL
   ↓
Server makes request
```

The important difference is that the request originates from the vulnerable server rather than directly from the attacker.

---

# Example Structure

An external entity can reference a URL:

```xml
<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "http://internal-resource.example">
]>
```

The application parser may resolve the entity and cause a server-side request.

---

# Why This Is SSRF

Normally:

```text
Attacker → Target
```

With XXE-based SSRF:

```text
Attacker
   ↓
Vulnerable Application
   ↓
Internal / External Resource
```

The vulnerable application becomes the requester.

---

# Potential Targets

Depending on the environment, SSRF may allow interaction with:

- Internal applications.
- Internal APIs.
- Services not exposed to the public internet.
- Local network resources.
- Cloud infrastructure endpoints.

The actual impact depends on what the vulnerable server can access.

---

# Detection

A useful testing approach is to define an external entity based on a URL to a system you control.

Conceptually:

```text
XML Parser
     ↓
External Entity
     ↓
Your controlled server
     ↓
Observe interaction
```

The PortSwigger material specifically recommends using an out-of-band system such as Burp Collaborator when testing blind XXE. :contentReference[oaicite:1]{index=1}

---

# Blind XXE Connection

If the application does not return the external entity's value, the request may still occur.

For example:

```text
XML Parser
     ↓
External Entity
     ↓
HTTP Request
     ↓
Controlled Server
```

The application response itself may contain no useful information.

This becomes a **blind XXE** scenario.

---

# File Retrieval vs SSRF

### File Retrieval

```text
SYSTEM "file:///..."
        ↓
Local File
```

### SSRF

```text
SYSTEM "http://..."
        ↓
URL Request
```

Both rely on external entity resolution.

---

# Security Impact

Potential impact depends on the server's network access.

An XXE-based SSRF may allow an attacker to:

- Reach internal services.
- Discover accessible network resources.
- Interact with internal APIs.
- Access resources that trust requests originating from the vulnerable server.

---

# Important Limitation

An XXE-based SSRF does not automatically mean that every internal resource is accessible.

The result depends on:

- Network architecture.
- Firewall rules.
- Parser behavior.
- URL handling.
- Authentication requirements.
- Internal service configuration.

---

# Testing Workflow

```text
Identify XML Input
       ↓
Test External Entity Support
       ↓
Use Controlled URL
       ↓
Monitor for Server Interaction
       ↓
Confirm SSRF Behavior
       ↓
Assess Security Impact
```

---

# Key Takeaways

- XXE can act as an SSRF primitive.
- External entities can reference URLs.
- The vulnerable server makes the resulting request.
- Blind XXE can be detected through out-of-band interaction.
- Burp Collaborator is useful for detecting server-side interactions.
- The actual impact depends on the server's network access.

