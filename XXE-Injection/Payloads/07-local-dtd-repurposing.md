# Payload 07 – Local DTD Repurposing

## Purpose

Use an existing local DTD when an external malicious DTD cannot be loaded.

---

## Concept

```text
XML
 ↓
Local DTD
 ↓
Existing Entity
 ↓
Entity Repurposing
 ↓
Parser Behavior
 ↓
Possible Information Disclosure
```

---

## Generic Structure

The exact local DTD path and entity names depend on the target environment.

Conceptually:

```xml
<!DOCTYPE foo [
    <!ENTITY % local SYSTEM "file:///PATH/TO/LOCAL/DTD">
    %local;
]>
```

---

## Entity Repurposing

The goal is to identify an existing entity declaration inside the local DTD and construct XML that causes the parser to process that declaration in an unintended way.

```text
Local DTD
    ↓
Existing Entity
    ↓
Attacker-controlled Declaration
    ↓
Entity Collision / Repurposing
    ↓
Parser Error
```

---

## Error-Based Variant

If verbose parser errors are returned:

```text
Local DTD
   ↓
Repurposed Entity
   ↓
Parser Error
   ↓
Application Response
```

The error may disclose information derived from the processed resource.

---

## Requirements

```text
☐ Local DTD exists
☐ XML parser can access it
☐ DTD processing is enabled
☐ Useful entity declaration exists
☐ Parser behavior can be observed
```

---

## Limitations

This technique is highly environment-dependent.

The following may differ between targets:

- DTD location
- Entity names
- Parser implementation
- Operating system
- Installed software
- Error behavior

---

## Key Learning

Local DTD repurposing can provide an alternative to external DTDs when outbound DTD retrieval is unavailable.