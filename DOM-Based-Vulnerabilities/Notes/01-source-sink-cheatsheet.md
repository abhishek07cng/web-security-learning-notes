# DOM-Based Vulnerabilities — Source & Sink Cheat Sheet

## 1. Core Model

A DOM vulnerability usually follows:

`Source → Attacker-Controlled Data → JavaScript Processing → Sink → Browser Behavior`

Ask:
- Can I control the source?
- How does the data flow?
- What transformations occur?
- What is the final sink?
- What security impact results?

## 2. Common Sources

| Source | Purpose |
|---|---|
| `location.search` | Query string |
| `location.hash` | URL fragment |
| `location.pathname` | URL path |
| `document.URL` | Current URL |
| `document.referrer` | Referring URL |
| `window.name` | Window name |
| `document.cookie` | JS-accessible cookies |
| `event.data` | Web Message data |

## 3. Common Sinks

### HTML / DOM
```javascript
document.write(value)
element.innerHTML = value
element.outerHTML = value
element.insertAdjacentHTML("beforeend", value)
```

### JavaScript Execution
```javascript
eval(value)
Function(value)
setTimeout(value)
setInterval(value)
```

### Navigation
```javascript
location = value
location.href = value
location.assign(value)
location.replace(value)
window.open(value)
```

### Other
```javascript
element.setAttribute(attribute, value)
document.cookie = value
new WebSocket(value)
XMLHttpRequest.open(method, value)
```

## 4. Web Messages

Source:

```javascript
window.addEventListener("message", function(event) {
    console.log(event.data);
});
```

Always inspect:

```javascript
event.data
event.origin
```

Prefer exact origin validation:

```javascript
if (event.origin === "https://trusted.example") {
    // process message
}
```

Be cautious with weak checks such as `includes()`, `startsWith()`, or `endsWith()`.

## 5. Marker-First Testing

Start with a unique harmless marker:

```text
domtest123
```

Example:

```text
https://target.example/page#domtest123
```

Then find the marker in DevTools.

Workflow:

`Marker → Reflection → Context → Source/Sink → Data Flow → Validation → Payload`

## 6. Context Identification

Determine whether the input reaches:

- HTML text
- HTML attribute
- JavaScript string
- JavaScript expression
- URL
- JSON
- DOM property

The payload must match the context.

## 7. Basic Authorized-Lab Tests

HTML:

```html
<b>domtest123</b>
```

Event-handler test:

```html
<img src=x onerror=print()>
```

SVG:

```html
<svg onload=print()>
```

JavaScript execution sink:

```javascript
print()
```

URL sink:

```text
https://example.com
```

Only use execution payloads against systems you are authorized to test.

## 8. Encoding / Decoding

Look for:

```javascript
encodeURI()
encodeURIComponent()
decodeURI()
decodeURIComponent()
```

Also inspect:

- `replace()`
- custom sanitizers
- regular expressions
- HTML encoding
- URL encoding

Trace the value that actually reaches the sink.

## 9. DevTools Workflow

Use:

- **Elements** — inspect the live DOM and attributes
- **Sources** — search JavaScript and set breakpoints
- **Console** — inspect sources and runtime values
- **Network** — inspect requests and responses
- **Application** — inspect cookies and browser storage

Useful checks:

```javascript
location.search
location.hash
location.pathname
document.URL
document.referrer
document.cookie
```

## 10. DOM Invader

Use DOM Invader to help identify:

- Sources
- Sinks
- Data flow / taint
- Web Message issues

Always manually verify automated findings.

## 11. Source-to-Sink Checklist

```text
[ ] Source identified
[ ] Attacker control confirmed
[ ] Marker traced
[ ] Context identified
[ ] Sink identified
[ ] Data flow traced
[ ] Encoding/decoding checked
[ ] Validation checked
[ ] Sanitization checked
[ ] Runtime behavior confirmed
[ ] Security impact confirmed
```

## 12. Quick Revision

**Source:** Where does attacker-controlled data enter?

**Sink:** Where is the data finally used?

**Context:** How does the browser interpret it?

**Data flow:** What happens between source and sink?

**Impact:** What security consequence can be reproduced?

### Golden Rule

`Don't hunt for payloads first. Find the source, find the sink, trace the data, understand the context, then test the appropriate behavior.`
