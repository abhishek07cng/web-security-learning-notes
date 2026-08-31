# DOM Clobbering Payloads

## 1. Purpose

Payloads for testing DOM Clobbering through attacker-controlled HTML.

The core model is:

```text
Attacker HTML
      ↓
id / name
      ↓
Named DOM Property
      ↓
JavaScript Property
      ↓
Application Logic
```

---

# 2. Basic `id` Clobber

```html
<a id="test"></a>
```

Then inspect:

```javascript
window.test
```

---

# 3. Basic `name` Clobber

```html
<form name="test"></form>
```

Then inspect:

```javascript
window.test
```

---

# 4. Anchor Element

```html
<a id="config"></a>
```

Useful when application code references:

```javascript
window.config
```

---

# 5. Anchor with `href`

```html
<a id="config" href="https://example.com"></a>
```

Useful when application logic reads:

```javascript
window.config.href
```

---

# 6. Form Element

```html
<form id="config"></form>
```

or:

```html
<form name="config"></form>
```

Useful for testing named properties.

---

# 7. Input Element

```html
<input id="config">
```

Use when testing whether:

```javascript
window.config
```

can be influenced.

---

# 8. Property Collision Test

If application code contains:

```javascript
window.config
```

test:

```html
<a id="config"></a>
```

Then inspect:

```javascript
window.config
```

---

# 9. Fallback Test

For code such as:

```javascript
let config = window.config || defaultConfig;
```

test whether:

```html
<a id="config"></a>
```

causes:

```text
window.config
```

to become truthy.

---

# 10. URL Property Test

If code accesses:

```javascript
window.url
```

test:

```html
<a id="url" href="https://example.com"></a>
```

Then inspect:

```javascript
window.url
```

and:

```javascript
window.url.href
```

---

# 11. Multiple Element Testing

Where the application expects nested properties, investigate whether multiple named elements can create the required DOM property structure.

Start with harmless values:

```html
<a id="config"></a>
<a id="url" href="https://example.com"></a>
```

Then inspect the actual runtime object in DevTools.

---

# 12. Script Configuration Testing

If application code uses:

```javascript
window.scriptURL
```

test:

```html
<a id="scriptURL" href="https://example.com"></a>
```

Then determine how the application consumes the property.

---

# 13. Redirect Configuration Testing

If code uses:

```javascript
window.redirectURL
```

test:

```html
<a id="redirectURL" href="https://example.com"></a>
```

Then trace:

```text
window.redirectURL
      ↓
Consumer
      ↓
Navigation
```

---

# 14. Attribute Testing

Potentially relevant attributes:

```text
id
name
href
```

Start with:

```html
<a id="test"></a>
```

before attempting more complex structures.

---

# 15. Harmless Marker

Use:

```text
clobber123
```

as a property identifier when testing application behavior.

---

# 16. DOM Property Verification

Use:

```javascript
window.test
```

```javascript
typeof window.test
```

and:

```javascript
window.test === document.getElementById("test")
```

to understand the resulting DOM property.

---

# 17. Consumer Testing

After creating a property, find:

```text
Where is it used?
```

Trace:

```text
DOM Element
      ↓
Named Property
      ↓
Application Variable
      ↓
Consumer
      ↓
Sink
```

---

# 18. DOM Clobbering Checklist

```text
☐ HTML injection confirmed
☐ Sanitization reviewed
☐ id tested
☐ name tested
☐ Named property created
☐ window property identified
☐ Fallback logic checked
☐ Consumer identified
☐ Sink identified
☐ Security impact confirmed
```

---

# Quick Payload List

```html
<a id="test"></a>
```

```html
<form name="test"></form>
```

```html
<a id="config"></a>
```

```html
<a id="url" href="https://example.com"></a>
```

```html
<a id="redirectURL" href="https://example.com"></a>
```

```html
<a id="scriptURL" href="https://example.com"></a>
```

---

# Final Rule

```text
HTML
 ↓
id / name
 ↓
NAMED DOM PROPERTY
 ↓
JAVASCRIPT
 ↓
CONSUMER
 ↓
SECURITY IMPACT
```

Creating a named property alone is **not** enough to establish a vulnerability.