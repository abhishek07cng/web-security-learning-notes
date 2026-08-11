# Lab 09 – XXE via Image File Upload

## Objective

Exploit XXE through an image upload feature.

The application accepts image files and processes SVG content using an XML parser.

The objective is to demonstrate that XML-based file formats can introduce an XXE attack surface.

---

# Vulnerability

SVG is an XML-based image format.

Therefore:

```text
SVG Upload
     ↓
XML Processing
     ↓
XML Parser
     ↓
Potential XXE
```

If the parser resolves external entities, an uploaded SVG can potentially trigger XXE behavior.

---

# Step 1 — Identify the Upload Functionality

Find the application's image upload feature.

Examples:

```text
Profile Picture
Avatar
Image Upload
```

---

# Step 2 — Understand Normal Processing

Upload a normal image first.

Observe:

- Accepted file types.
- Content-Type.
- File extension.
- Server response.
- Whether the application transforms the image.

---

# Step 3 — Identify SVG Support

Determine whether:

```text
image/svg+xml
```

or another SVG representation is accepted.

---

# Step 4 — Prepare an XML-Based Image

SVG files contain XML.

Basic structure:

```xml
<?xml version="1.0"?>

<svg xmlns="http://www.w3.org/2000/svg">
    <text>Test</text>
</svg>
```

The SVG can then be investigated for unsafe XML processing.

---

# Step 5 — Test XML Parser Behavior

Determine whether the application parses the SVG using an XML parser that permits external entity processing.

The important question is:

```text
Does the server parse the uploaded SVG as XML?
```

rather than simply storing the file.

---

# Attack Flow

```text
Malicious SVG
      ↓
Upload Endpoint
      ↓
Image Processing
      ↓
XML Parser
      ↓
External Entity Resolution
      ↓
Potential Impact
```

---

# Possible Impact

Depending on the application's processing behavior:

```text
XXE
 ↓
File Retrieval
```

or:

```text
XXE
 ↓
SSRF
```

or:

```text
XXE
 ↓
Out-of-Band Interaction
```

may be possible.

---

# File Upload Validation

Investigate how the application validates:

```text
Filename
Extension
Content-Type
File Signature
Actual File Contents
```

Do not assume that a file is safe merely because its extension indicates an image.

---

# Verification

A successful vulnerability requires evidence that:

```text
Uploaded SVG
      ↓
XML Parser
      ↓
Unsafe XML Feature
      ↓
Observable Security Impact
```

Simply uploading an SVG does not prove XXE.

---

# Testing Checklist

```text
☐ Find image upload
☐ Upload normal image
☐ Identify accepted formats
☐ Test SVG support
☐ Determine whether SVG is parsed
☐ Investigate XML parser behavior
☐ Test safely for external entity processing
☐ Observe response / OOB interaction
☐ Confirm impact
```

---

# Key Learning

File uploads can introduce XXE vulnerabilities even when the application's normal API does not accept XML directly.

XML-based formats such as SVG should therefore be included when assessing XML parser attack surfaces.