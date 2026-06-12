# DOM XSS Interview Notes

## What Is DOM XSS?

DOM-Based XSS occurs when attacker-controlled input is processed entirely by client-side JavaScript and reaches a dangerous sink.

---

## Difference Between Reflected XSS And DOM XSS

### Reflected XSS

```text
Server Returns Payload
```

---

### DOM XSS

```text
Browser JavaScript Creates Payload
```

---

## What Is A Source?

Location where attacker-controlled data enters application.

Examples:

```javascript
location.search
location.hash
document.referrer
```

---

## What Is A Sink?

Location where data becomes dangerous.

Examples:

```javascript
innerHTML
eval()
document.write()
```

---

## Common DOM XSS Sources

```javascript
location.search
location.hash
window.name
document.cookie
postMessage
```

---

## Common DOM XSS Sinks

```javascript
innerHTML
outerHTML
document.write
eval
$()
.attr()
```

---

## How Do You Test DOM XSS?

```text
Find Source
        ↓
Inject Canary
        ↓
Locate Sink
        ↓
Determine Context
        ↓
Craft Payload
        ↓
Verify Execution
```

---

## What Tool Helps Most?

```text
DOM Invader
```

inside Burp Browser.

---

## AngularJS Detection Payload

```html
{{7*7}}
```

Expected:

```text
49
```

---

## Common Interview Question

### Why Is View Source Often Useless For DOM XSS?

Because DOM modifications occur:

```text
After Page Load
```

using JavaScript.

Use:

```text
Elements Tab
```

instead.

---

## Key Interview Takeaways

- DOM XSS is client-side.
- Source → Sink is the core concept.
- innerHTML and eval() are dangerous sinks.
- AngularJS and jQuery introduce framework-specific attack surfaces.