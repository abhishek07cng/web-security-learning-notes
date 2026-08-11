# XXE Testing Checklist

## 1. Identify XML Processing

Look for:

- XML API endpoints
- SOAP requests
- XML-based forms
- XML imports
- SVG uploads
- XML-based document processing
- Requests containing XML bodies

Check headers such as:

```http
Content-Type: application/xml
Content-Type: text/xml
```

---

# 2. Establish Baseline

Before testing, send the normal request.

Record:

- Status code
- Response length
- Response content
- XML parser behavior
- Error messages
- Application state

---

# 3. Test External Entity Processing

Determine whether the parser accepts:

```text
DOCTYPE
External entities
```

Test in an authorized lab or target only.

---

# 4. Test Response-Based XXE

Check whether an external entity referencing a local resource produces content in the response.

```text
XML
 ↓
External Entity
 ↓
Local Resource
 ↓
Response
```

---

# 5. Test XXE-Based SSRF

Determine whether external entities can reference URLs.

```text
XML
 ↓
External Entity
 ↓
URL
 ↓
Server-Side Request
```

Use a controlled destination where appropriate.

---

# 6. Test Blind XXE

If the response does not contain the entity value:

```text
Normal XXE
      ↓
No useful response
      ↓
Test OOB interaction
```

---

# 7. OOB Testing

Use a controlled OAST destination.

Check for:

```text
☐ DNS interaction
☐ HTTP interaction
```

Record:

- Timestamp
- Unique identifier
- Request source
- Interaction type

---

# 8. Parameter Entities

If normal entity testing is unsuccessful, investigate parameter entities:

```xml
<!ENTITY % name "value">
```

Reference:

```xml
%name;
```

---

# 9. External DTD

Determine whether the parser can retrieve an external DTD.

Conceptually:

```text
XML
 ↓
External DTD
 ↓
Additional Entity Definitions
```

---

# 10. Error-Based XXE

Check whether detailed XML parser errors are returned.

Look for:

```text
☐ File paths
☐ Entity names
☐ Resource names
☐ Parser details
☐ Information derived from processed resources
```

---

# 11. Local DTD

If external DTD access is unavailable, investigate whether a suitable local DTD exists.

Consider:

```text
Local DTD
 ↓
Existing Entity
 ↓
Entity Repurposing
```

This technique is environment-dependent.

---

# 12. XInclude

If `DOCTYPE`-based XXE is blocked, determine whether XInclude is supported.

Look for:

```xml
<xi:include
    xmlns:xi="http://www.w3.org/2001/XInclude"
    href="RESOURCE"
    parse="text"/>
```

---

# 13. File Uploads

Check XML-based file formats.

Examples:

```text
SVG
XML
Other XML-based formats
```

Determine whether uploaded content is actually parsed as XML.

---

# 14. Content-Type Testing

Record the normal:

```http
Content-Type
```

Then determine whether the application continues to parse XML when the request format changes.

---

# 15. Impact Assessment

Determine whether the vulnerability can result in:

```text
☐ Local file disclosure
☐ SSRF
☐ Internal service interaction
☐ OOB interaction
☐ Information disclosure
☐ Other security impact
```

---

# 16. Verification

Do not rely on a single successful response.

Confirm:

```text
☐ Behavior is reproducible
☐ Parser behavior is confirmed
☐ Security impact is understood
☐ Unnecessary requests are removed
☐ Minimal reproduction is documented
```

---

# 17. Prevention Review

Check whether the application:

```text
☐ Disables external entities
☐ Disables unnecessary DTD processing
☐ Uses secure XML parser configuration
☐ Restricts filesystem access
☐ Restricts outbound network access
☐ Avoids verbose parser errors
☐ Securely processes XML-based uploads
```

---

# Quick Checklist

```text
☐ Find XML
☐ Baseline
☐ Test DTD
☐ Test external entities
☐ Test file retrieval
☐ Test SSRF
☐ Test blind XXE
☐ Test OOB
☐ Test parameter entities
☐ Test external DTD
☐ Test error-based behavior
☐ Consider local DTD
☐ Test XInclude
☐ Check XML file uploads
☐ Check Content-Type handling
☐ Confirm impact
☐ Document findings
```