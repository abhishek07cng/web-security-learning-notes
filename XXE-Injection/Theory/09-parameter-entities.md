# XML Parameter Entities

## Overview

Parameter entities are a special type of XML entity that can be referenced within a DTD.

They are especially important when testing **blind XXE**.

---

# Normal Entity

A normal entity can be referenced within XML document content:

```xml
&entity;
```

---

# Parameter Entity

A parameter entity is declared using:

```xml
<!ENTITY % entity "value">
```

It is referenced using:

```xml
%entity;
```

The `%` character distinguishes parameter entities from normal XML entities.

---

# Basic Example

```xml
<!DOCTYPE foo [
    <!ENTITY % example "test">
    %example;
]>
```

The parameter entity is processed as part of the DTD.

---

# Why Parameter Entities Matter

Parameter entities allow attackers to construct more complex DTD-based behavior.

They are useful when:

- The response does not directly contain entity values.
- An external DTD is involved.
- Additional entity declarations need to be dynamically constructed.
- OOB interaction is unavailable or insufficient.

---

# External DTD

A parameter entity can reference an external DTD.

Conceptually:

```text
XML
 ↓
Parameter Entity
 ↓
External DTD
 ↓
Additional Entity Definitions
```

This provides a way to move part of the attack logic outside the original XML document.

---

# Example Structure

```xml
<!DOCTYPE foo [
    <!ENTITY % xxe SYSTEM "YOUR-DTD-URL">
    %xxe;
]>
```

The parser attempts to retrieve and process the external DTD.

---

# Parameter Entity Flow

```text
DOCTYPE
   ↓
Parameter Entity
   ↓
External DTD
   ↓
Entity Declaration
   ↓
Entity Evaluation
```

---

# Blind XXE Usage

Parameter entities are particularly useful when the application does not reflect the result of a normal entity.

For example:

```text
Normal Entity
     ↓
No useful response
```

A parameter-entity technique may instead cause:

```text
Parameter Entity
     ↓
External DTD
     ↓
OOB Interaction
```

---

# Parameter Entities and Error-Based XXE

Parameter entities can also be used to dynamically construct entity declarations that trigger XML parser errors.

Conceptually:

```text
Parameter Entity
       ↓
Dynamic Entity Declaration
       ↓
Invalid Resource
       ↓
Parser Error
       ↓
Sensitive Data in Error
```

---

# Important Restriction

The XML specification treats parameter entities differently depending on whether declarations are inside an internal or external DTD.

Some techniques involving parameter entities within other parameter entity declarations are permitted in external DTDs but not normally in fully specified internal DTDs.

This is one reason external DTDs are important in advanced blind XXE techniques.

---

# Key Takeaways

- Parameter entities are declared using `%`.
- They are processed within DTDs.
- They can reference external DTDs.
- They are especially useful for blind XXE.
- They can support OOB and error-based techniques.
- External DTDs provide greater flexibility for complex parameter-entity attacks.