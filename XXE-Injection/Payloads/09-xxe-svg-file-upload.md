# Payload 09 – XXE Through SVG File Upload

## Purpose

Test XML processing through an uploaded SVG file.

SVG is an XML-based image format and may therefore reach an XML parser during application processing.

---

## Basic SVG

```xml
<?xml version="1.0"?>

<svg xmlns="http://www.w3.org/2000/svg">
    <text>Test</text>
</svg>
```

---

## XXE Test Structure

In an authorized lab, an SVG can be constructed to test whether the application's XML parser resolves external entities.

Conceptually:

```xml
<?xml version="1.0"?>

<!DOCTYPE svg [
    <!ENTITY xxe SYSTEM "RESOURCE">
]>

<svg xmlns="http://www.w3.org/2000/svg">
    <text>&xxe;</text>
</svg>
```

---

## Upload Flow

```text
SVG
 ↓
Upload Endpoint
 ↓
File Validation
 ↓
Image Processing
 ↓
XML Parser
 ↓
External Entity Processing
 ↓
Potential Impact
```

---

## Test Points

Check:

```text
Filename
Extension
Content-Type
File contents
Image processing library
XML parser
```

---

## OOB Variant

If the application does not return the entity value, a controlled external resource can be used to determine whether the parser attempts an external interaction.

---

## Verification

Do not consider an upload successful merely because:

```text
SVG accepted
```

Confirm that:

```text
SVG
 ↓
XML Parser
 ↓
External Entity Resolution
 ↓
Observable Effect
```

actually occurs.

---

## Key Learning

XML-based file formats can introduce XXE attack surfaces even when the main application API does not explicitly accept XML.