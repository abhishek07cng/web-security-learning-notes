# XXE File Retrieval

## Overview

One of the simplest XXE attack scenarios occurs when an XML parser resolves an external entity and the resulting value is returned in the application's response.

This can allow an attacker to retrieve arbitrary files accessible to the application.

---

# Basic Attack Concept

The attacker defines an external entity that references a local file.

Conceptually:

```text
XML Input
   ↓
External Entity
   ↓
Local File
   ↓
Entity Value
   ↓
Application Response
```

---

# Example

A vulnerable XML document can contain an external entity declaration such as:

```xml
<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "file:///etc/passwd">
]>
```

The entity can then be referenced inside XML data:

```xml
&xxe;
```

If the application returns the parsed value, the contents of the referenced file may appear in the response.

---

# Vulnerable Application Flow

Consider an application that accepts XML:

```xml
<stockCheck>
    <productId>1</productId>
    <storeId>London</storeId>
</stockCheck>
```

If the application parses this XML and returns entity values, an attacker may attempt to introduce an external entity.

---

# Basic Testing Method

### Step 1

Identify functionality that accepts XML.

Examples:

- Stock checking
- SOAP requests
- API requests
- XML-based forms

### Step 2

Intercept the request using Burp Suite.

### Step 3

Determine whether the application processes a `DOCTYPE` declaration.

### Step 4

Define an external entity referencing a known operating-system file.

### Step 5

Reference the entity in a value that is reflected in the response.

---

# Response-Based XXE

A successful response-based XXE may look conceptually like:

```text
Request
   ↓
XML Parser
   ↓
External Entity
   ↓
Local File
   ↓
Application
   ↓
Response contains file contents
```

---

# What to Look For

Look for:

- File contents in the response.
- Changes in response length.
- Parser behavior changes.
- XML parsing errors.
- Unexpected values appearing in reflected fields.

---

# Why File Retrieval Works

The vulnerability occurs because:

```text
Attacker controls XML
        +
Parser resolves external entities
        +
Entity value is returned
```

The application unintentionally becomes a mechanism for reading server-side resources.

---

# Impact

Depending on file permissions and application privileges, retrieved files could contain:

- Application configuration.
- Source code.
- Credentials.
- Environment information.
- Operating-system information.
- Other sensitive data.

---

# Limitations

File retrieval is not guaranteed.

It depends on:

- XML parser configuration.
- Whether external entities are enabled.
- File permissions.
- Whether the resulting entity value is reflected.
- Application-specific XML processing.

---

# Key Takeaways

- Response-based XXE can disclose local files.
- The external entity references a local resource.
- The entity must normally be used somewhere in the XML.
- The application must expose the resulting value or otherwise reveal it.
- Burp Suite can be used to intercept and modify XML requests.

Source material describes manual XXE testing as defining an external entity based on a well-known operating-system file and using that entity in data returned by the application. :contentReference[oaicite:0]{index=0}