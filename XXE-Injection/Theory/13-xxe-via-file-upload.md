# XXE via File Upload

## Overview

XXE vulnerabilities are not limited to endpoints that explicitly accept XML requests.

An application may process XML internally when handling an uploaded file.

This creates another potential XXE attack surface.

---

# How It Happens

A typical file-upload flow may look like:

```text
File Upload
    ↓
Application Processing
    ↓
XML Parser
    ↓
XML Content
```

If the uploaded file contains XML and the application parses it with unsafe XML configuration, XXE may be possible.

---

# Image Upload Example

Some image formats can contain XML-based content.

An example is:

```text
SVG
```

SVG files use XML syntax.

Therefore:

```text
SVG Upload
    ↓
XML Parser
    ↓
Potential XXE
```

---

# Attack Surface

When testing file uploads, determine:

- Which file formats are accepted?
- Is the uploaded file parsed?
- Is the file converted?
- Is metadata extracted?
- Is an XML-based format supported?
- Is the uploaded content processed by an XML parser?

---

# SVG and XML

An SVG document can contain XML declarations and elements.

Conceptually:

```xml
<?xml version="1.0"?>

<svg>
    ...
</svg>
```

Because SVG is XML-based, applications that process SVG files should be evaluated for unsafe XML processing.

---

# Testing Workflow

### Step 1 — Identify File Upload

Find functionality such as:

```text
Profile Picture
Image Upload
Document Upload
Import
Attachment
```

---

### Step 2 — Identify XML-Based Formats

Look for formats such as:

```text
SVG
XML
Other XML-based document formats
```

---

### Step 3 — Upload a Normal File

Establish the normal application behavior first.

Observe:

- Upload response.
- Processing behavior.
- File location.
- Whether the application transforms the file.

---

### Step 4 — Test XML Processing

Determine whether the application actually parses the uploaded XML.

If the file is simply stored without processing, the XXE attack surface may not exist.

---

### Step 5 — Test External Entity Processing

If the uploaded file is parsed as XML, investigate whether external entities are resolved.

---

# Content-Type Consideration

The application may restrict uploads based on:

```text
Filename
Content-Type
File extension
File contents
```

These controls may affect whether the XML-based file reaches the vulnerable parser.

---

# Example Flow

```text
Attacker
   ↓
Malicious XML-Based File
   ↓
Upload Endpoint
   ↓
Application Processing
   ↓
XML Parser
   ↓
External Entity Resolution
   ↓
Potential Impact
```

---

# Impact

Depending on the application's processing behavior, XXE through file upload may potentially lead to:

- Local file retrieval.
- SSRF.
- Out-of-band interaction.
- Information disclosure.

---

# Important Limitation

Uploading an XML-based file does **not** automatically mean the application is vulnerable.

The application must actually process the XML using a parser that permits the relevant external functionality.

---

# Testing Checklist

```text
☐ Identify upload functionality
☐ Identify accepted formats
☐ Identify XML-based formats
☐ Upload a normal file
☐ Determine whether the file is parsed
☐ Determine whether XML features are enabled
☐ Test safely for external entity processing
☐ Check application response
☐ Check observable side effects
☐ Assess impact
```

---

# Key Takeaways

- File uploads can provide an indirect XXE attack surface.
- XML-based formats such as SVG deserve attention.
- The important question is whether the application parses the uploaded XML.
- File extension and Content-Type controls can affect processing.
- Uploading a malicious file alone does not prove XXE.