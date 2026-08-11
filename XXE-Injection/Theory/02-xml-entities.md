# XML Entities

## Overview

XML entities provide a way to represent data within an XML document without placing the data directly into the document.

XML defines several built-in entities.

For example:

```xml
&lt;
&gt;
```

represent:

```text
<
>
```

These characters have special meaning in XML and therefore need to be represented appropriately when used as data.

---

# Built-in XML Entities

Common examples include:

```text
&lt;   → <
&gt;   → >
&amp;  → &
&quot; → "
&apos; → '
```

---

# Custom XML Entities

XML also allows custom entities to be defined inside a DTD.

Example:

```xml
<!DOCTYPE foo [
    <!ENTITY myentity "my entity value">
]>
```

Once defined, the entity can be referenced using:

```xml
&myentity;
```

The parser replaces the entity reference with its defined value.

Conceptually:

```text
&myentity;
     ↓
"my entity value"
```

---

# Why Entities Matter for XXE

Entities become security-relevant when their values are loaded from external resources.

A normal custom entity might contain a fixed value:

```xml
<!ENTITY example "hello">
```

An external entity can instead reference a resource outside the XML document.

---

# External Entities

An external entity uses the:

```text
SYSTEM
```

keyword.

Example:

```xml
<!DOCTYPE foo [
    <!ENTITY ext SYSTEM "http://normal-website.com">
]>
```

The entity's value is loaded from the specified resource.

---

# File-Based External Entity

External entities can also use the `file://` protocol.

Example:

```xml
<!DOCTYPE foo [
    <!ENTITY ext SYSTEM "file:///path/to/file">
]>
```

This behavior is one of the primary mechanisms behind XXE attacks.

---

# Entity Reference

After defining an entity:

```xml
<!ENTITY ext SYSTEM "file:///path/to/file">
```

the entity can be referenced as:

```xml
&ext;
```

The XML parser attempts to resolve the external resource.

---

# Entity Flow

```text
DOCTYPE
   ↓
Entity Definition
   ↓
Entity Reference
   ↓
XML Parser
   ↓
Entity Resolution
   ↓
External Resource
```

---

# Security Perspective

The important distinction is:

### Internal Entity

```text
ENTITY
  ↓
Static Value
```

### External Entity

```text
ENTITY
  ↓
External Resource
```

External resources may include:

```text
Files
URLs
Internal services
```

This is why external entity resolution is security-sensitive.

---

# Key Takeaways

- XML entities represent data inside XML.
- Entities can be built-in or custom.
- Custom entities can be declared inside a DTD.
- External entities use the `SYSTEM` keyword.
- External entities can reference URLs or files.
- External entity resolution is a core component of XXE.

Source: PortSwigger Web Security Academy XXE material. :contentReference[oaicite:1]{index=1}