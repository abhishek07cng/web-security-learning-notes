# Out-of-Band XXE and OAST

## Overview

Out-of-band (OOB) XXE occurs when the vulnerable XML parser makes a network interaction that is observable outside the application's normal response.

This technique is particularly useful for **blind XXE**.

---

# Basic Flow

```text
Attacker
   ↓
Malicious XML
   ↓
Vulnerable XML Parser
   ↓
External Entity
   ↓
Controlled Server
   ↓
Interaction Detected
```

---

# Why OOB Is Useful

In a blind XXE vulnerability:

```text
HTTP Response
      ↓
No useful entity value
```

Therefore, the attacker needs another way to determine whether the entity was processed.

OOB interaction provides that signal.

---

# OAST

**Out-of-band Application Security Testing (OAST)** involves detecting vulnerabilities through interactions that occur outside the original HTTP response.

For XXE testing, an OAST service can monitor whether the vulnerable application attempts to resolve an external resource.

---

# Burp Collaborator

Burp Collaborator can be used to generate a unique external address.

The tester places the address into an external entity.

Conceptually:

```text
External Entity
       ↓
Unique Collaborator Address
       ↓
XML Parser
       ↓
Network Interaction
       ↓
Collaborator Records Interaction
```

---

# Detection Example

The general structure is:

```xml
<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "YOUR-CONTROLLED-URL">
]>
```

The entity can then be referenced within the XML document.

If the parser resolves external entities, the application may contact the controlled destination.

---

# Types of Interaction

Depending on the environment, OOB testing may reveal:

```text
DNS Interaction
HTTP Interaction
```

The exact interaction depends on:

- XML parser.
- Network configuration.
- URL handling.
- Firewall rules.
- Protocol support.

---

# Blind XXE Workflow

```text
Find XML Endpoint
       ↓
Inject External Entity
       ↓
Use Controlled OOB Address
       ↓
Send Request
       ↓
Monitor Interaction
       ↓
Interaction?
    /      \
  YES       NO
   ↓         ↓
Confirm     Investigate
XXE         Parser / Network
```

---

# OOB Does Not Automatically Mean Data Exfiltration

Detecting an interaction proves that the server attempted to resolve the external resource.

It does not automatically mean that sensitive local files can be retrieved.

Further testing is required to determine the actual impact.

---

# Important Considerations

When testing blind XXE:

- Use a unique OOB identifier.
- Record the time of the request.
- Compare the interaction with your test request.
- Check both DNS and HTTP interactions where appropriate.
- Consider whether outbound traffic is restricted.

---

# Key Takeaways

- OOB techniques are useful for blind XXE.
- Burp Collaborator can detect external interactions.
- OAST provides visibility when the application response does not.
- An OOB interaction confirms server-side processing of the external resource.
- OOB detection and data exfiltration are separate concepts.