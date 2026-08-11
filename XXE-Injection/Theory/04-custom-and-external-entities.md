# Custom and External XML Entities

## Overview

XML allows applications to define custom entities.

These entities can contain:

- Static values.
- External resources.

External entities are particularly important when studying XXE because the XML parser may resolve resources specified by the entity.

---

# Custom Entities

A custom entity can be defined inside a DTD.

Example:

```xml
<!DOCTYPE foo [
    <!ENTITY myentity "my entity value">
]>
```

The entity can then be referenced with:

```xml
&myentity;
```

The parser replaces the entity reference with its defined value.

---

# External Entities

An external entity references a resource outside the XML document.

Example:

```xml
<!DOCTYPE foo [
    <!ENTITY ext SYSTEM "http://example.com">
]>
```

The external resource is referenced using the:

```text
SYSTEM
```

keyword.

---

# File-Based External Entity

An external entity can reference a local file.

Example:

```xml
<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "file:///path/to/file">
]>
```

When the entity is referenced:

```xml
&xxe;
```

the XML parser may attempt to read the specified resource.

---

# External Entity Flow

```text
DOCTYPE
   ↓
External Entity Definition
   ↓
Entity Reference
   ↓
XML Parser
   ↓
External Resource
```

---

# HTTP-Based External Entity

External entities can also reference URLs:

```xml
<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "http://example.com">
]>
```

This behavior is important because it can cause the vulnerable server to make a request to the specified URL.

This forms the basis of **XXE-based SSRF**.

---

# Entity Resolution

A vulnerable processing flow may look like:

```text
Attacker-controlled XML
          ↓
DOCTYPE
          ↓
External Entity
          ↓
Entity Reference
          ↓
Parser resolves entity
          ↓
File / URL accessed
```

---

# Security Impact

Depending on parser behavior and application functionality, external entity resolution can result in:

```text
Local File Retrieval
        │
        ├── Sensitive File Disclosure
        │
        └── Configuration / Credential Exposure

URL Resolution
        │
        └── SSRF
```

---

# Important Distinction

A custom entity itself is not necessarily dangerous.

For example:

```xml
<!ENTITY greeting "Hello">
```

contains only a static value.

The security concern arises when attacker-controlled XML can cause the parser to resolve external resources.

---

# Key Takeaways

- Custom entities can contain application-defined values.
- External entities reference resources outside the XML document.
- The `SYSTEM` keyword is used to define external entities.
- External entities can reference files or URLs.
- External entity resolution is central to many XXE attacks.