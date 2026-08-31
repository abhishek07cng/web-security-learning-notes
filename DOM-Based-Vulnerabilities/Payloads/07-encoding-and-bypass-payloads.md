# Encoding and Validation Testing Payloads

## 1. Purpose

Reference values for testing:

```text
Encoding
Decoding
Filtering
Validation
Sanitization
Context Changes
```

The key model is:

```text
INPUT
  ↓
ENCODING
  ↓
DECODING
  ↓
VALIDATION
  ↓
SINK
```

---

# 2. Marker

Always begin with:

```text
encodetest123
```

---

# 3. HTML Encoding

Characters:

```text
<
>
"
'
&
```

HTML entities:

```text
&lt;
&gt;
&quot;
&#39;
&amp;
```

---

# 4. URL Encoding

Examples:

```text
%3C
%3E
%22
%27
%26
```

Combined:

```text
%3Cimg%20src=x%20onerror=print()%3E
```

---

# 5. Double URL Encoding

Example:

```text
%253C
```

This represents an encoded:

```text
%3C
```

Use only when the application performs multiple decoding steps.

---

# 6. JavaScript Escape Characters

Test:

```text
'
```

```text
"
```

```text
\
```

```text
`
```

Relevant when input reaches:

```text
JavaScript strings
Template literals
eval()
```

---

# 7. Null / Empty Values

Test:

```text
""
```

```text
null
```

```text
undefined
```

where the application's data type permits them.

---

# 8. Whitespace Testing

Test:

```text
space
tab
newline
carriage return
```

Useful for identifying weak validation.

---

# 9. Case Variation

If the application checks:

```text
javascript:
```

test the exact behavior of case normalization rather than assuming case-insensitivity.

---

# 10. Prefix Validation Testing

If code uses:

```javascript
startsWith()
```

test:

```text
ExpectedPrefix
ExpectedPrefix + controlled suffix
```

Determine whether the validation checks the complete value.

---

# 11. Suffix Validation Testing

If code uses:

```javascript
endsWith()
```

test:

```text
controlled prefix + ExpectedSuffix
```

Determine whether the validation is actually validating the intended component.

---

# 12. Substring Validation

If code uses:

```javascript
includes()
```

or:

```javascript
indexOf()
```

test:

```text
trusted-string + attacker-controlled-data
```

The goal is to determine whether a substring check is being incorrectly used as a security boundary.

---

# 13. Regex Validation

Record:

```text
Regex
Input
Match
Expected Result
Actual Result
```

Test boundary conditions rather than blindly generating random strings.

---

# 14. URL Component Testing

Break a URL into:

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

Then determine which component the validation actually checks.

---

# 15. Encoding Chain

Test:

```text
Raw Input
    ↓
URL Encoding
    ↓
Application Decoding
    ↓
DOM Sink
```

Record the value at every stage.

---

# 16. Decoding Functions

Search for:

```text
decodeURI()
decodeURIComponent()
atob()
unescape()
```

Also inspect custom decoding functions.

---

# 17. Encoding Functions

Search for:

```text
encodeURI()
encodeURIComponent()
btoa()
escape()
```

Determine whether encoding occurs:

```text
Before Sink
```

or:

```text
After Sink
```

---

# 18. Sanitizer Testing

Identify:

```text
Allowed Characters
Removed Characters
Encoded Characters
Allowed Tags
Allowed Attributes
```

Use:

```text
encodetest123
```

before testing security-sensitive syntax.

---

# 19. Context-Boundary Testing

Test based on where the input lands:

```text
HTML
Attribute
JavaScript
URL
CSS
JSON
DOM Property
```

The same encoded value may behave differently in each context.

---

# 20. Bypass Analysis Checklist

```text
☐ Encoding identified
☐ Decoding identified
☐ Number of decoding passes identified
☐ Validation identified
☐ Validation order identified
☐ Sanitization identified
☐ Context identified
☐ Browser interpretation identified
☐ Final sink identified
☐ Impact confirmed
```

---

# Quick Reference

```text
<   → %3C
>   → %3E
"   → %22
'   → %27
&   → %26
```

JavaScript-sensitive:

```text
'
"
\
`
```

URL-sensitive:

```text
:
/
?
#
&
=
```

---

# Final Rule

```text
NEVER TEST ONLY THE RAW PAYLOAD.

RAW
 ↓
ENCODED
 ↓
DECODED
 ↓
VALIDATED
 ↓
SANITIZED
 ↓
SINK
```