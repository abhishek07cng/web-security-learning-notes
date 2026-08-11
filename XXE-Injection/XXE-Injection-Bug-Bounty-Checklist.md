# XXE Injection Bug Bounty Checklist

## XML Discovery

```text
☐ Find XML endpoints
☐ Find SOAP functionality
☐ Find XML imports
☐ Find XML-based APIs
☐ Find SVG processing
☐ Find XML-based file uploads
☐ Inspect application requests
```

---

# Request Analysis

```text
☐ Check Content-Type
☐ Check XML declaration
☐ Identify XML fields
☐ Identify reflected XML values
☐ Identify parser errors
☐ Identify file-processing functionality
```

---

# Basic XXE

```text
☐ Test DOCTYPE
☐ Test external entities
☐ Test local resource references
☐ Check response for entity values
```

---

# SSRF

```text
☐ Test URL-based external entities
☐ Use controlled destination
☐ Monitor server interaction
☐ Identify reachable resources
☐ Stay within authorized scope
```

---

# Blind XXE

```text
☐ Determine whether entity values are reflected
☐ If not, test OOB interaction
☐ Generate unique OOB address
☐ Monitor DNS
☐ Monitor HTTP
```

---

# Advanced Blind XXE

```text
☐ Parameter entities
☐ External DTD
☐ Error-based XXE
☐ Local DTD repurposing
```

---

# Alternative XML Features

```text
☐ XInclude
☐ SVG
☐ XML-based uploads
☐ Modified Content-Type
```

---

# Impact

```text
☐ Local file disclosure
☐ SSRF
☐ Internal service interaction
☐ OOB interaction
☐ Sensitive information disclosure
```

---

# Verification

```text
☐ Reproduce vulnerability
☐ Minimize request
☐ Confirm parser behavior
☐ Confirm security impact
☐ Avoid unnecessary destructive actions
```

---

# Reporting

```text
☐ Clear title
☐ Affected endpoint
☐ Parameter
☐ Reproduction steps
☐ Minimal request
☐ Evidence
☐ Impact
☐ Remediation
```

---

# Final Questions

```text
1. Does the application process XML?

2. Does the parser resolve external entities?

3. Can the parser access local resources?

4. Can the parser make network requests?

5. Is the behavior visible in the response?

6. If not, can it be observed out-of-band?

7. Can errors disclose useful information?

8. Are other XML features such as XInclude enabled?

9. Does file-upload functionality process XML-based formats?

10. What is the demonstrated security impact?
```