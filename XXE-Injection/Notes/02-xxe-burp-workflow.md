# XXE Burp Suite Workflow

## Overview

Burp Suite can be used to intercept, modify, and replay XML requests during authorized security testing.

---

# Step 1 — Intercept Request

Open:

```text
Burp Suite → Proxy → HTTP history
```

Find a request containing XML.

---

# Step 2 — Identify XML

Look for:

```http
Content-Type: application/xml
```

or:

```http
Content-Type: text/xml
```

Also inspect the request body for XML syntax.

---

# Step 3 — Send to Repeater

Right-click the request:

```text
Send to Repeater
```

---

# Step 4 — Establish Baseline

Send the original request.

Record:

```text
Status Code
Response Length
Response Body
Timing
Error Messages
```

---

# Step 5 — Test Basic XXE

Modify the XML to test external entity processing.

General structure:

```xml
<?xml version="1.0"?>

<!DOCTYPE foo [
    <!ENTITY xxe SYSTEM "RESOURCE">
]>

<foo>
    &xxe;
</foo>
```

Use an appropriate controlled resource for testing.

---

# Step 6 — Observe Response

Check whether the response changes.

Look for:

```text
File contents
Parser errors
Unexpected response
Entity value
```

---

# Step 7 — Test SSRF

If external entities appear to be processed, test whether the parser can make a request to a controlled URL.

```text
XML
 ↓
External Entity
 ↓
Controlled URL
 ↓
Server Interaction
```

---

# Step 8 — Blind XXE

If the entity value is not reflected:

```text
Use OOB detection
```

Generate a unique Burp Collaborator address and use it as the external resource.

---

# Step 9 — Monitor Collaborator

Check:

```text
Burp → Collaborator
```

Look for:

```text
DNS
HTTP
```

interactions.

---

# Step 10 — Parameter Entities

If appropriate, test parameter entities:

```xml
<!ENTITY % xxe SYSTEM "RESOURCE">
%xxe;
```

---

# Step 11 — External DTD

If the scenario requires a more complex DTD structure, test an external DTD in an authorized environment.

General structure:

```xml
<!DOCTYPE foo [
    <!ENTITY % xxe SYSTEM "YOUR-DTD-URL">
    %xxe;
]>
```

---

# Step 12 — Error-Based Testing

If detailed XML parser errors are exposed, inspect them for useful information.

```text
Request
 ↓
Parser
 ↓
Error
 ↓
Response
```

---

# Step 13 — XInclude

If traditional `DOCTYPE` processing is blocked, determine whether XInclude is supported.

```xml
<xi:include
    xmlns:xi="http://www.w3.org/2001/XInclude"
    href="RESOURCE"
    parse="text"/>
```

---

# Step 14 — File Upload Testing

For XML-based uploads:

```text
Proxy
 ↓
Upload Request
 ↓
Identify File Type
 ↓
Determine Processing
 ↓
Check XML Parser
```

SVG is particularly relevant because it is XML-based.

---

# Step 15 — Compare Results

Maintain a simple record:

| Test | Result |
|---|---|
| Normal XML | Baseline |
| External entity | |
| File reference | |
| URL reference | |
| OOB interaction | |
| Parameter entity | |
| External DTD | |
| Parser error | |
| XInclude | |
| SVG/XML upload | |

---

# Step 16 — Minimize the Request

Once behavior is confirmed:

```text
Remove unnecessary headers
Remove unnecessary XML
Remove unnecessary entities
Keep minimum reproduction
```

This makes the finding easier to understand and reproduce.

---

# Final Burp Workflow

```text
Proxy
  ↓
HTTP History
  ↓
Find XML Request
  ↓
Send to Repeater
  ↓
Baseline
  ↓
External Entity Test
  ↓
File / URL Test
  ↓
Blind XXE?
  ↓
OOB / Error-Based Testing
  ↓
XInclude / Upload Testing
  ↓
Confirm Impact
  ↓
Minimal Reproduction
```

---

# Important Rule

Only perform XXE testing against systems where you have explicit authorization.

Use controlled resources and lab environments when testing file access, SSRF, or out-of-band behavior.