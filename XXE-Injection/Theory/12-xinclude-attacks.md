# XInclude Attacks

## Overview

**XInclude** is an XML feature that allows an XML document to include content from another resource.

In some situations, an application may accept XML data but prevent or restrict direct `DOCTYPE` declarations.

If XInclude processing is enabled, it may provide another way to cause the server to access local resources.

---

# Why XInclude Matters

A traditional XXE attack often relies on:

```xml
<!DOCTYPE ...>
```

If the application blocks this syntax, the traditional approach may fail.

However, an application may still process XInclude directives.

Conceptually:

```text
XML Input
   ↓
XInclude
   ↓
External Resource
   ↓
Included Content
```

---

# Basic XInclude Structure

A simplified XInclude element uses:

```xml
<xi:include
    xmlns:xi="http://www.w3.org/2001/XInclude"
    href="..."
    parse="text"/>
```

The important attributes are:

```text
href
parse
```

---

# File Retrieval Concept

An attacker may attempt to use XInclude to reference a local file.

Conceptually:

```text
XInclude
    ↓
Local File
    ↓
Included Content
    ↓
Application Response
```

If the application returns the processed XML, the file contents may become visible.

---

# XInclude vs Traditional XXE

### Traditional XXE

```text
DOCTYPE
   ↓
External Entity
   ↓
Resource
```

### XInclude

```text
xi:include
   ↓
Resource
```

XInclude therefore provides an alternative XML processing mechanism.

---

# Testing Workflow

### Step 1

Identify an endpoint that accepts XML.

### Step 2

Determine whether:

```text
DOCTYPE
```

is blocked.

### Step 3

Check whether the application supports XInclude.

### Step 4

Insert an XInclude element into a suitable XML value.

### Step 5

Observe whether referenced content is processed.

---

# Example Structure

A vulnerable application may process an XML field such as:

```xml
<productId>1</productId>
```

An attacker may attempt to introduce an XInclude element in a location where the XML parser accepts it.

Conceptually:

```xml
<productId>
    <xi:include
        xmlns:xi="http://www.w3.org/2001/XInclude"
        href="RESOURCE"
        parse="text"/>
</productId>
```

---

# Requirements

XInclude exploitation depends on:

- XML parser behavior.
- XInclude support.
- Application configuration.
- Where the attacker-controlled XML is inserted.
- Whether the resulting content is returned.

---

# Limitations

XInclude is not automatically enabled in every XML parser.

Also, an application may:

- Disable XInclude.
- Validate XML structure.
- Restrict the accepted XML elements.
- Sanitize or reject namespace declarations.
- Prevent local-resource access.

---

# Testing Flow

```text
XML Endpoint
     ↓
DOCTYPE Blocked?
     ↓
YES
     ↓
Test XInclude
     ↓
XInclude Processed?
     ↓
YES
     ↓
Test Controlled Resource
     ↓
Assess Impact
```

---

# Key Takeaways

- XInclude is an XML inclusion mechanism.
- It can sometimes provide an alternative to traditional XXE.
- It is particularly interesting when `DOCTYPE` is blocked.
- Exploitation depends on parser and application configuration.
- XInclude can potentially be used for local resource retrieval.