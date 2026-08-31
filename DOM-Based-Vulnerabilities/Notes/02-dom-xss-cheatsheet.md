# DOM XSS — Quick Revision

## 1. What Is DOM XSS?

DOM-based Cross-Site Scripting occurs when client-side JavaScript takes attacker-controlled data and uses it in a dangerous DOM or JavaScript sink.

Core flow:

`Source → Data Flow → Sink → Browser Interpretation → JavaScript Execution`

## 2. Common Sources

```javascript
location.search
location.hash
location.pathname
document.URL
document.referrer
window.name
event.data
```

## 3. Common DOM XSS Sinks

```javascript
document.write(value)
document.writeln(value)
element.innerHTML = value
element.outerHTML = value
element.insertAdjacentHTML("beforeend", value)
```

Other potentially dangerous sinks:

```javascript
eval(value)
Function(value)
setTimeout(value)
setInterval(value)
```

## 4. Basic Testing

Start with a harmless marker:

```text
domtest123
```

Then try HTML in an authorized lab:

```html
<b>domtest123</b>
```

If HTML is interpreted, test execution:

```html
<img src=x onerror=print()>
```

Alternative:

```html
<svg onload=print()>
```

## 5. Context Matters

Identify where the input lands:

- HTML body
- HTML attribute
- JavaScript string
- JavaScript expression
- URL
- DOM property

Never use the same payload blindly in every context.

## 6. Source-to-Sink Analysis

Trace:

`Source → Variable → Transformation → Validation → Sanitization → Sink`

Check for:

```javascript
encodeURI()
encodeURIComponent()
decodeURI()
decodeURIComponent()
replace()
```

## 7. DevTools

### Elements
Inspect the live DOM and injected values.

### Sources
Search JavaScript and set breakpoints.

### Console
Check:

```javascript
location.search
location.hash
document.URL
document.referrer
```

### Network
Inspect requests and responses.

## 8. Verification Checklist

```text
[ ] Source identified
[ ] Attacker control confirmed
[ ] Input traced
[ ] Context identified
[ ] Sink identified
[ ] Encoding/decoding checked
[ ] Validation checked
[ ] Sanitization checked
[ ] Execution confirmed
[ ] Security impact confirmed
```

## 9. Common Mistakes

- Finding a source and assuming it is vulnerable.
- Finding `innerHTML` and assuming DOM XSS.
- Ignoring the injection context.
- Ignoring encoding/decoding.
- Using payloads before understanding the data flow.
- Reporting without demonstrating security impact.

## 10. Remember

`Source + Attacker Control + Unsafe Sink + Successful Execution = Confirmed DOM XSS`

The most important skill is **tracing attacker-controlled data from source to sink**.
