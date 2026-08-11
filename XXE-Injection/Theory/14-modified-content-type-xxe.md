# XXE via Modified Content Type

## Overview

Some applications accept XML only when a request uses a specific Content-Type.

For example:

```http
Content-Type: application/xml
```

However, the underlying application may still parse XML when the request is submitted using another Content-Type.

This can create an XXE attack surface that is not immediately obvious.

---

# Typical Scenario

An application may normally receive:

```http
POST /stockCheck
Content-Type: application/xml
```

with XML content such as:

```xml
<stockCheck>
    <productId>1</productId>
    <storeId>London</storeId>
</stockCheck>
```

The application processes the XML.

---

# Testing Content-Type Handling

When an endpoint appears to accept structured input, examine:

```text
Content-Type
Request Body
Parser Behavior
```

Do not assume that the declared Content-Type completely determines how the server processes the body.

---

# Potential Test

A request that normally uses:

```http
Content-Type: application/xml
```

may be tested with another supported request format if the application's behavior suggests that the same body is still passed to an XML parser.

For example:

```http
Content-Type: application/x-www-form-urlencoded
```

with XML data embedded in a parameter.

---

# Why This Matters

An application may have:

```text
Request Validation
       ↓
Content-Type Check
       ↓
Application Processing
       ↓
XML Parser
```

If validation and parsing are handled differently, an attacker may be able to reach the XML parser through an unexpected request format.

---

# Detection Workflow

```text
Identify XML Endpoint
       ↓
Observe Normal Content-Type
       ↓
Modify Content-Type
       ↓
Observe Parser Behavior
       ↓
Does XML Still Get Processed?
       ↓
YES
       ↓
Investigate XXE
```

---

# Burp Suite Workflow

1. Intercept the XML request.
2. Send it to Repeater.
3. Record the normal Content-Type.
4. Test how the application reacts to alternative request formats.
5. Observe whether XML parsing still occurs.
6. If XML processing remains active, investigate the endpoint for XXE.

---

# Indicators

Useful indicators include:

- XML parser errors.
- Same application response after changing Content-Type.
- XML-specific validation errors.
- Changes in response length.
- Successful processing of XML data despite an unexpected Content-Type.

---

# Important Limitation

Changing Content-Type does not itself create an XXE vulnerability.

The application must still:

```text
Accept the request
      +
Process the XML
      +
Allow dangerous XML functionality
```

---

# Relationship to File Uploads

The same principle applies to file-upload functionality.

Applications may validate:

```text
Filename
Extension
Content-Type
```

while later processing the actual file contents.

Therefore, testing should consider both:

```text
Declared Type
```

and:

```text
Actual Processing
```

---

# Key Takeaways

- Content-Type handling can affect the XML attack surface.
- Do not assume XML parsing is limited to requests explicitly labeled `application/xml`.
- Burp Repeater is useful for testing alternate request formats.
- XML parser behavior is more important than the declared Content-Type alone.
- A modified Content-Type is only useful if the application continues to process the body as XML.