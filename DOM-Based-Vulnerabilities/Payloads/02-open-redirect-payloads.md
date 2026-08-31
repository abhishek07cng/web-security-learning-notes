# DOM Open Redirect Payloads

## 1. Purpose

Payloads for testing DOM-based open redirection.

The core flow is:

```text
Attacker-Controlled URL
        ↓
DOM Source
        ↓
URL Processing
        ↓
Navigation Sink
        ↓
External Destination
```

---

# 2. Basic External URL

```text
https://example.com
```

Use a domain you control during authorized testing.

---

# 3. HTTP Destination

```text
http://example.com
```

Useful when testing:

```text
http:
```

acceptance.

---

# 4. HTTPS Destination

```text
https://example.com
```

Useful for testing:

```text
https:
```

validation.

---

# 5. Fragment-Based Redirect

Example:

```text
https://target.example/page#https://example.com
```

Relevant when JavaScript reads:

```javascript
location.hash
```

---

# 6. Query-Parameter Redirect

Example:

```text
https://target.example/page?url=https://example.com
```

Relevant when JavaScript reads:

```javascript
location.search
```

---

# 7. `location.href`

If the application contains:

```javascript
location.href = value;
```

test:

```text
https://example.com
```

---

# 8. `location.assign()`

For:

```javascript
location.assign(value);
```

test:

```text
https://example.com
```

---

# 9. `location.replace()`

For:

```javascript
location.replace(value);
```

test:

```text
https://example.com
```

---

# 10. `window.open()`

For:

```javascript
window.open(value);
```

test:

```text
https://example.com
```

---

# 11. JavaScript URL

For URL-sensitive sinks, test in an authorized lab:

```text
javascript:print()
```

This determines whether the sink permits a JavaScript URL.

---

# 12. Protocol Validation Testing

If validation uses:

```javascript
url.startsWith("https:")
```

test an external HTTPS destination:

```text
https://attacker.example
```

The important question is whether the application validates:

```text
Destination
```

or merely:

```text
Protocol Prefix
```

---

# 13. Trusted-Domain Validation Testing

If code uses:

```javascript
url.includes("trusted.example")
```

test the validation semantics with benign controlled domains.

Conceptual test:

```text
https://trusted.example.attacker.example
```

Determine whether the application is checking:

```text
Actual Host
```

or:

```text
Substring
```

---

# 14. `startsWith()` Testing

If code checks:

```javascript
url.startsWith("https://trusted.example")
```

inspect whether a URL such as:

```text
https://trusted.example.attacker.example
```

is accepted.

---

# 15. `endsWith()` Testing

If code checks:

```javascript
url.endsWith("trusted.example")
```

inspect whether an attacker-controlled hostname ending in that string is accepted.

Example:

```text
https://attackertrusted.example
```

---

# 16. URL Component Testing

When testing redirects, inspect:

```text
Scheme
Username
Password
Hostname
Port
Path
Query
Fragment
```

Do not rely only on string matching.

---

# 17. Redirect Testing Checklist

```text
☐ Source identified
☐ URL parameter identified
☐ Navigation sink identified
☐ External URL tested
☐ HTTP tested
☐ HTTPS tested
☐ Fragment tested
☐ Query parameter tested
☐ Protocol validation reviewed
☐ Host validation reviewed
☐ startsWith() reviewed
☐ endsWith() reviewed
☐ includes() reviewed
☐ Final destination confirmed
```

---

# 18. Quick Payload List

```text
https://example.com
```

```text
http://example.com
```

```text
javascript:print()
```

```text
#https://example.com
```

```text
?url=https://example.com
```

---

# Final Rule

```text
SOURCE
  ↓
URL
  ↓
VALIDATION
  ↓
NAVIGATION SINK
  ↓
EXTERNAL DOMAIN
```

A redirect is confirmed only after the browser actually reaches the attacker-controlled destination.