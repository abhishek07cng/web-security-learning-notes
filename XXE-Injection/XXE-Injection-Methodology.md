# XXE Injection Testing Methodology

## Overview

XXE testing focuses on identifying XML-processing functionality and determining whether attacker-controlled XML can cause the parser to resolve external resources.

The core methodology is:

```text
IDENTIFY → TEST → ESCALATE → CONFIRM → REPORT
```

---

# Phase 1 — Identify

## 1. Find XML Processing

Look for:

- XML API endpoints
- SOAP requests
- XML-based forms
- XML imports
- SVG processing
- XML-based file uploads
- Requests containing XML bodies

Check for:

```http
Content-Type: application/xml
Content-Type: text/xml
```

Also inspect request bodies for XML declarations and XML elements.

---

## 2. Understand the Application

Determine:

- Where XML enters the application.
- Which endpoint processes it.
- Whether the XML is reflected.
- Whether errors are returned.
- Whether uploaded XML is parsed.
- Whether XML is transformed or converted.

---

# Phase 2 — Establish a Baseline

Send the original request without modifications.

Record:

```text
Status Code
Response Length
Response Body
Timing
Parser Errors
Application Behavior
```

The baseline provides a comparison for later tests.

---

# Phase 3 — Test External Entity Processing

Determine whether the parser processes:

```text
DOCTYPE
External Entities
```

A basic test can determine whether the application resolves an external resource.

---

# Phase 4 — Test Response-Based XXE

If entity values are reflected in the response, investigate whether an external entity can reference a local resource.

Flow:

```text
XML
 ↓
External Entity
 ↓
Local Resource
 ↓
Application
 ↓
Response
```

---

# Phase 5 — Test XXE-Based SSRF

If URL-based external entities are processed, determine whether the server can make a request to a controlled destination.

Flow:

```text
XML
 ↓
External Entity
 ↓
URL
 ↓
Server
 ↓
Controlled Destination
```

If confirmed, assess the reachable resources only within the authorized scope.

---

# Phase 6 — Test Blind XXE

If the application does not return the entity value:

```text
Normal XXE
     ↓
No Useful Response
     ↓
Blind XXE
```

Move to indirect detection.

---

# Phase 7 — OOB Detection

Use a controlled OAST destination.

```text
External Entity
       ↓
Controlled Address
       ↓
XML Parser
       ↓
DNS / HTTP Interaction
```

Observe whether an interaction occurs.

---

# Phase 8 — Parameter Entities

If normal entities are insufficient, investigate parameter entities.

```text
Parameter Entity
       ↓
External DTD
       ↓
Additional Processing
```

Parameter entities are particularly useful in blind XXE scenarios.

---

# Phase 9 — External DTD

Determine whether the application can retrieve an external DTD.

Conceptually:

```text
XML
 ↓
External DTD
 ↓
Entity Definitions
 ↓
Additional XML Processing
```

External DTDs can provide greater flexibility for advanced blind XXE techniques.

---

# Phase 10 — Error-Based XXE

If the application exposes detailed XML parser errors, determine whether they can reveal useful information.

Flow:

```text
Entity
 ↓
Parser Condition
 ↓
Error
 ↓
Application Response
```

Look for:

- File paths
- Entity information
- Resource names
- Parser details
- Sensitive information

---

# Phase 11 — Local DTD Repurposing

If external DTD access is unavailable:

```text
External DTD
      ↓
Blocked
```

investigate whether an appropriate local DTD exists.

Conceptually:

```text
Local DTD
 ↓
Existing Entity
 ↓
Repurposing
 ↓
Parser Behavior
```

This technique is highly environment-dependent.

---

# Phase 12 — XInclude

If traditional `DOCTYPE`-based XXE is blocked, determine whether XInclude is supported.

```text
DOCTYPE Blocked
       ↓
Test XInclude
       ↓
Referenced Resource
       ↓
Included Content
```

---

# Phase 13 — File Uploads

Investigate XML-based file formats.

Examples:

```text
SVG
XML
Other XML-based formats
```

Determine whether the application actually parses the uploaded content.

---

# Phase 14 — Modified Content-Type

Do not assume that XML processing only occurs when the request is explicitly labeled:

```http
Content-Type: application/xml
```

Investigate whether the application continues to process XML when the declared Content-Type changes.

---

# Phase 15 — Confirm

Once potential XXE behavior is identified:

1. Reproduce the behavior.
2. Remove unnecessary request components.
3. Create a minimal proof of concept.
4. Confirm the security impact.
5. Verify that the behavior is repeatable.

---

# Phase 16 — Assess Impact

Determine whether the vulnerability provides:

```text
Local File Disclosure
        ↓
SSRF
        ↓
Internal Resource Access
        ↓
Out-of-Band Interaction
        ↓
Sensitive Information Disclosure
```

Do not assume maximum impact without evidence.

---

# Phase 17 — Report

A good XXE report should contain:

```text
Title
Endpoint
Parameter
Vulnerability Description
Reproduction Steps
Request
Response
Impact
Evidence
Remediation
```

---

# Complete Methodology

```text
IDENTIFY
   ↓
XML Processing
   ↓
BASELINE
   ↓
External Entity Test
   ↓
Response-Based XXE
   ↓
SSRF
   ↓
Blind XXE
   ↓
OOB
   ↓
Parameter Entities
   ↓
External DTD
   ↓
Error-Based XXE
   ↓
Local DTD
   ↓
XInclude
   ↓
File Upload
   ↓
Content-Type Testing
   ↓
CONFIRM
   ↓
IMPACT
   ↓
REPORT
```

---

# Core Principle

The most important question during XXE testing is:

```text
Can attacker-controlled XML cause the server's XML parser
to access an external resource?
```

If yes, determine exactly what resource access is possible and what security impact it creates.