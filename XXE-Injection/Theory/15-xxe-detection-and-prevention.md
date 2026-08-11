# XXE Detection and Prevention

## Detection

XXE testing begins by identifying functionality that processes XML.

Potential sources include:

- XML APIs.
- SOAP requests.
- XML-based forms.
- File uploads.
- SVG processing.
- XML imports.
- Other XML-based document formats.

---

# Step 1 — Identify XML Processing

Look for:

```text
Content-Type: application/xml
Content-Type: text/xml
```

Also inspect requests whose bodies contain:

```xml
<?xml ... ?>
```

or XML elements.

---

# Step 2 — Test XML Parser Behavior

Determine whether the application:

- Parses XML.
- Supports DTDs.
- Resolves external entities.
- Supports XInclude.
- Generates detailed parser errors.

---

# Step 3 — Identify the XXE Type

### Response-Based

```text
Entity
 ↓
File
 ↓
Response
```

### SSRF

```text
Entity
 ↓
URL
 ↓
Server Request
```

### Blind XXE

```text
Entity
 ↓
External Interaction
 ↓
No Useful Response
```

### Error-Based

```text
Entity
 ↓
Parser Error
 ↓
Information Disclosure
```

---

# Step 4 — Check Out-of-Band Interaction

For blind XXE, determine whether the server can make an external interaction.

Conceptually:

```text
XML Parser
     ↓
Controlled Destination
     ↓
Interaction
```

An observed interaction can confirm that external entity resolution is occurring.

---

# Step 5 — Investigate Alternative Attack Surfaces

If direct XXE testing is unsuccessful, consider whether the application processes XML through:

```text
File Upload
SVG
XInclude
Modified Content-Type
External DTD
```

---

# Prevention

## 1. Disable External Entity Processing

The most important defense is to disable XML external entity functionality when it is not required.

Conceptually:

```text
XML Parser
     ↓
External Entities Disabled
```

This prevents attacker-controlled XML from resolving arbitrary external resources.

---

# 2. Disable DTD Processing Where Possible

If the application does not require DTD functionality, disable it.

This reduces the available attack surface.

---

# 3. Use Secure Parser Configuration

XML parsers should be configured according to the security recommendations of the specific language and library.

Security-sensitive options should be explicitly configured rather than relying on potentially unsafe defaults.

---

# 4. Validate Input

Application input should be validated according to the expected XML structure.

Validation should not be considered a replacement for secure parser configuration.

---

# 5. Restrict External Network Access

Applications should have appropriate network controls.

Even if a parser is accidentally configured unsafely, network restrictions can reduce the impact of SSRF-style attacks.

---

# 6. Restrict File Access

The application should operate with the minimum filesystem permissions required.

This limits the impact if a parser is abused to access local resources.

---

# 7. Secure File Upload Processing

For XML-based file uploads:

```text
Validate Format
      ↓
Validate Content
      ↓
Secure Parser
      ↓
Restrict Processing
```

Applications should not blindly parse uploaded XML using unsafe parser configurations.

---

# 8. Avoid Detailed Parser Errors

Do not expose unnecessary internal XML parser errors to users.

Instead of:

```text
Detailed internal parser error
```

return a generic application error.

---

# Prevention Checklist

```text
☐ Disable external entities
☐ Disable DTD processing when unnecessary
☐ Use secure XML parser configuration
☐ Validate XML structure
☐ Restrict outbound network access
☐ Restrict filesystem permissions
☐ Secure XML-based file uploads
☐ Avoid detailed parser errors
☐ Keep XML libraries updated
```

---

# Secure Architecture

A safer processing flow is:

```text
User XML
   ↓
Input Validation
   ↓
Secure XML Parser
   ↓
External Entities Disabled
   ↓
Application
```

---

# Vulnerable Architecture

```text
User XML
   ↓
XML Parser
   ↓
External Entity Resolution
   ↓
File / Network Resource
   ↓
Sensitive Information
```

---

# Final Takeaway

The most effective defense against XXE is to prevent untrusted XML from resolving external entities or unnecessary DTD functionality.

The application should use a secure parser configuration and apply appropriate filesystem and network restrictions as additional layers of defense.