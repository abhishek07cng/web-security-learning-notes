# DOM Vulnerability Testing Methodology

## 1. Reconnaissance

Map:

- Application functionality
- JavaScript files
- URL parameters
- URL fragments
- Forms
- Web Messages
- Client-side storage

## 2. Find Sources

Search JavaScript for:

```javascript
location.search
location.hash
location.pathname
document.URL
document.referrer
window.name
document.cookie
event.data
localStorage
sessionStorage
```

## 3. Find Sinks

Search for:

```javascript
innerHTML
outerHTML
document.write
eval
Function
setTimeout
location
location.href
location.assign
location.replace
window.open
setAttribute
document.cookie
```

## 4. Marker-First Testing

Use:

```text
domtest123
```

Trace where it appears.

Do not start with complex payloads.

## 5. Identify Context

Determine whether the value enters:

- HTML
- Attribute
- JavaScript
- URL
- JSON
- DOM property

## 6. Trace the Data

Use:

`Source → Variable → Function → Transformation → Validation → Sanitization → Sink`

## 7. Use DevTools

### Elements
Inspect the live DOM.

### Sources
Search JavaScript and set breakpoints.

### Console
Inspect runtime values.

### Network
Inspect requests and responses.

### Application
Inspect cookies and storage.

## 8. Verify

Confirm:

```text
[ ] Attacker control
[ ] Source
[ ] Sink
[ ] Context
[ ] Data flow
[ ] Validation
[ ] Sanitization
[ ] Runtime behavior
[ ] Security impact
```

## 9. Final Rule

`Find → Trace → Understand → Test → Verify → Document`

Never report a source or sink alone as a confirmed vulnerability.
