# XXE Injection — Quick Revision

## Definition

XXE, or XML External Entity injection, occurs when attacker-controlled XML causes an XML parser to process external entities or resources in an unsafe way.

---

# Core Components

```text
XML
 ↓
DOCTYPE / DTD
 ↓
Entity
 ↓
External Resource
 ↓
Parser
```

---

# XML Entity

Normal entity:

```xml
<!ENTITY name "value">
```

Reference:

```xml
&name;
```

---

# External Entity

General structure:

```xml
<!ENTITY xxe SYSTEM "RESOURCE">
```

Reference:

```xml
&xxe;
```

---

# Basic XXE

```text
XML
 ↓
External Entity
 ↓
Local File
 ↓
Application Response
```

Potential result:

```text
Local File Disclosure
```

---

# XXE SSRF

```text
XML
 ↓
External Entity
 ↓
URL
 ↓
Server-Side Request
```

Potential result:

```text
Internal Resource Access
```

---

# Blind XXE

```text
External Entity
      ↓
No Useful Response
```

Use indirect observation such as:

```text
OOB Interaction
Error Message
External DTD
Local DTD
```

---

# OOB XXE

```text
XML Parser
     ↓
Controlled Address
     ↓
DNS / HTTP Interaction
```

Useful for detecting blind XXE.

---

# Parameter Entity

Declaration:

```xml
<!ENTITY % name "value">
```

Reference:

```xml
%name;
```

Parameter entities are processed within DTDs.

---

# External DTD

```text
XML
 ↓
External DTD
 ↓
Entity Definitions
 ↓
Additional Processing
```

Useful for advanced blind XXE techniques.

---

# Error-Based XXE

```text
Resource
   ↓
Entity
   ↓
Parser Error
   ↓
Application Response
```

Detailed errors may disclose useful information.

---

# Local DTD Repurposing

Used when an external DTD cannot be retrieved.

```text
Local DTD
   ↓
Existing Entity
   ↓
Repurposing
   ↓
Parser Behavior
```

Environment-dependent.

---

# XInclude

Alternative XML inclusion mechanism:

```xml
<xi:include
    xmlns:xi="http://www.w3.org/2001/XInclude"
    href="RESOURCE"
    parse="text"/>
```

Useful to investigate when traditional `DOCTYPE`-based XXE is blocked.

---

# File Upload XXE

XML-based formats can introduce an XXE attack surface.

Example:

```text
SVG
 ↓
XML Parser
 ↓
External Entity
 ↓
Potential XXE
```

---

# Modified Content-Type

Do not assume:

```text
application/xml
```

is the only way an application can process XML.

Investigate the application's actual parsing behavior.

---

# Testing Methodology

```text
IDENTIFY
   ↓
BASELINE
   ↓
TEST ENTITY PROCESSING
   ↓
FILE RETRIEVAL
   ↓
SSRF
   ↓
BLIND XXE
   ↓
OOB
   ↓
PARAMETER ENTITIES
   ↓
EXTERNAL DTD
   ↓
ERROR-BASED
   ↓
LOCAL DTD
   ↓
XINCLUDE
   ↓
FILE UPLOAD
   ↓
CONFIRM
   ↓
IMPACT
```

---

# Detection Checklist

```text
☐ XML endpoint
☐ XML input
☐ DOCTYPE processing
☐ External entity processing
☐ File retrieval
☐ SSRF
☐ Blind XXE
☐ OOB interaction
☐ Parameter entities
☐ External DTD
☐ Error messages
☐ Local DTD
☐ XInclude
☐ XML-based file upload
```

---

# Prevention

```text
Disable external entities
Disable unnecessary DTD processing
Use secure XML parser configuration
Restrict filesystem permissions
Restrict outbound network access
Secure XML-based uploads
Avoid verbose parser errors
Keep XML libraries updated
```

---

# One-Minute Summary

```text
XXE
 ↓
Attacker-Controlled XML
 ↓
Unsafe XML Parser
 ↓
External Resource
```

Main attack categories:

```text
File Retrieval
SSRF
Blind XXE
OOB XXE
Error-Based XXE
XInclude
File Upload XXE
```

Core question:

```text
Can attacker-controlled XML cause the parser
to access an external resource?
```

If yes, determine exactly what access is possible and what security impact can be demonstrated.