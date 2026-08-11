# What is XML External Entity Injection (XXE)?

## Overview

XML External Entity injection, commonly known as **XXE**, is a web security vulnerability that allows an attacker to interfere with an application's processing of XML data.

Depending on the application's XML parser and configuration, XXE can allow an attacker to:

- Read files from the application server.
- Interact with back-end systems.
- Perform SSRF attacks.
- Trigger out-of-band network interactions.
- Potentially compromise underlying infrastructure.

---

# How XXE Vulnerabilities Arise

Applications sometimes use XML to transmit data between the client and server.

The server then uses an XML parser or standard library to process the submitted XML.

XML supports several features that can become dangerous when they are enabled unnecessarily.

A vulnerable flow can look like:

```text
User Input
    ↓
XML Document
    ↓
XML Parser
    ↓
Application
```

If the parser supports external entities and the application allows attacker-controlled XML, the attacker may be able to influence how external entities are resolved.

---

# What Can XXE Lead To?

Common XXE attack types include:

### 1. File Retrieval

An external entity can reference a file on the server.

```text
XML
 ↓
External Entity
 ↓
Local File
 ↓
Application Response
```

---

### 2. SSRF

An external entity can reference a URL.

```text
XML
 ↓
External Entity
 ↓
Internal URL
 ↓
Server-side Request
```

This can allow interaction with systems that are accessible from the vulnerable server.

---

### 3. Blind XXE

The application may process the external entity without returning its value in the response.

In this situation, attackers can use:

- Out-of-band interactions.
- Error messages.
- External DTDs.
- Other indirect techniques.

---

# Why XXE Exists

The XML specification provides features such as:

- Entities
- DTDs
- External entities
- XInclude

XML parsers may support these features by default even when the application does not need them.

This creates unnecessary attack surface.

---

# Basic Vulnerable Flow

```text
Attacker
   ↓
Malicious XML
   ↓
Application
   ↓
XML Parser
   ↓
External Entity Resolution
   ↓
File / URL / Internal Resource
```

---

# Security Impact

The impact depends on the parser and application behavior.

Possible consequences include:

```text
Local File Disclosure
        ↓
SSRF
        ↓
Internal Service Access
        ↓
Sensitive Information Disclosure
```

In some situations, XXE can be leveraged to compromise underlying infrastructure.

---

# Detection

When testing XML functionality, investigate whether:

- The application accepts XML input.
- A `DOCTYPE` declaration is processed.
- External entities are resolved.
- XML parser errors reveal useful information.
- The application makes unexpected outbound requests.

---

# Key Takeaways

- XXE affects applications that process attacker-controlled XML.
- XML entities and DTDs are central to understanding XXE.
- External entities can reference files or URLs.
- XXE can result in file retrieval or SSRF.
- Blind XXE requires indirect detection or exploitation techniques.
- Disabling unnecessary XML features is an important defense.

Source: PortSwigger Web Security Academy XXE material. :contentReference[oaicite:0]{index=0}