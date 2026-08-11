# Document Type Definition (DTD)

## Overview

A **Document Type Definition (DTD)** contains declarations that define aspects of an XML document.

A DTD can define:

- The structure of an XML document.
- Types of data values it can contain.
- XML entities.
- Other XML-related declarations.

---

# DOCTYPE

A DTD is declared using the optional:

```xml
<!DOCTYPE ...>
```

element.

Example:

```xml
<!DOCTYPE foo [
    ...
]>
```

The declarations between the square brackets form the internal DTD.

---

# Internal DTD

An internal DTD is completely contained within the XML document.

Example:

```xml
<?xml version="1.0"?>

<!DOCTYPE foo [
    <!ENTITY myentity "example">
]>

<foo>
    &myentity;
</foo>
```

The entity definition exists directly inside the XML document.

---

# External DTD

A DTD can also be loaded from another location.

This is called an **external DTD**.

Conceptually:

```text
XML Document
     ↓
DOCTYPE
     ↓
External DTD
     ↓
DTD Declarations
```

External DTDs are particularly relevant to blind XXE techniques.

---

# Hybrid DTD

A DTD can also combine declarations from:

```text
Internal DTD
+
External DTD
```

This is sometimes referred to as a hybrid DTD.

---

# Entity Declaration Inside a DTD

A custom entity can be defined inside the DTD:

```xml
<!DOCTYPE foo [
    <!ENTITY myentity "my value">
]>
```

The XML document can then reference:

```xml
&myentity;
```

---

# External Entity Declaration

An external entity can be declared using:

```xml
<!ENTITY ext SYSTEM "http://example.com">
```

or:

```xml
<!ENTITY ext SYSTEM "file:///path/to/file">
```

The parser may attempt to resolve the referenced resource.

---

# DTD and XXE

A simplified XXE structure is:

```text
XML Document
     ↓
DOCTYPE
     ↓
Entity Definition
     ↓
External Resource
```

For example:

```xml
<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "file:///path/to/file">
]>
```

Then:

```xml
&xxe;
```

references the external entity.

---

# Parameter Entities

XML also supports **parameter entities**.

These are a special type of entity that can be referenced within the DTD itself.

They are particularly important when testing blind XXE.

Conceptually:

```text
DTD
 ↓
Parameter Entity
 ↓
External DTD / Entity
```

---

# Why DTDs Matter in XXE Testing

Understanding DTDs is essential for:

- Basic XXE.
- External entity attacks.
- Blind XXE.
- Parameter-entity techniques.
- External malicious DTDs.
- Local DTD repurposing.
- Error-based XXE.

---

# DTD Structure

A simplified structure is:

```xml
<!DOCTYPE root [
    declarations
]>
```

The declarations may define:

```text
Entities
Element structure
Other XML declarations
```

---

# Security Perspective

DTD support is not inherently a vulnerability.

The security problem occurs when an application processes attacker-controlled XML while allowing dangerous XML features that the application does not require.

---

# Key Takeaways

- DTD stands for Document Type Definition.
- DTDs are declared using `DOCTYPE`.
- DTDs can be internal, external, or hybrid.
- Custom entities can be defined inside DTDs.
- External entities are central to XXE.
- Parameter entities are important for blind XXE techniques.
- Unnecessary DTD/external-entity functionality should be disabled where possible.

Source: PortSwigger Web Security Academy XXE material. :contentReference[oaicite:2]{index=2}