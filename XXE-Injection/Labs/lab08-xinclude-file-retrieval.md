# Lab 08 – Exploiting XInclude to Retrieve Files

## Objective

Exploit XInclude functionality to retrieve a local file when traditional XXE techniques cannot be used.

---

# Vulnerability

The application accepts user-controlled XML but does not allow a traditional:

```text
DOCTYPE
```

declaration.

However, the XML parser supports:

```text
XInclude
```

This provides an alternative way to reference external resources.

---

# Step 1 — Identify the XML Input

Intercept the XML request with Burp Suite.

Example:

```xml
<stockCheck>
    <productId>1</productId>
    <storeId>London</storeId>
</stockCheck>
```

Send the request to:

```text
Burp Repeater
```

---

# Step 2 — Test XInclude

Insert an XInclude element into an XML value that is processed by the application.

General structure:

```xml
<xi:include
    xmlns:xi="http://www.w3.org/2001/XInclude"
    href="RESOURCE"
    parse="text"/>
```

---

# Step 3 — Reference the Target Resource

Use the XInclude `href` attribute to reference the resource you want the server to process.

Conceptually:

```text
XInclude
    ↓
Local Resource
    ↓
XML Parser
    ↓
Included Content
```

---

# Step 4 — Send the Request

Send the modified request from Burp Repeater.

If XInclude is supported and the referenced resource is accessible, the content may be included in the application's response.

---

# Attack Flow

```text
Attacker XML
      ↓
XInclude
      ↓
Local Resource
      ↓
Parser
      ↓
Included Content
      ↓
Application Response
```

---

# Why It Works

Traditional XXE relies on:

```text
DOCTYPE
+
External Entity
```

XInclude uses a different XML mechanism:

```text
xi:include
```

Therefore, blocking `DOCTYPE` alone does not necessarily prevent all XML-related resource inclusion.

---

# Limitations

Successful exploitation depends on:

- XInclude support.
- Parser configuration.
- Location where attacker input is inserted.
- Access to the referenced resource.
- Whether included content is returned.

---

# Verification

A successful result is when the application response contains the contents of the referenced resource.

---

# Key Learning

When traditional XXE is blocked, investigate whether other XML features such as XInclude are still enabled.