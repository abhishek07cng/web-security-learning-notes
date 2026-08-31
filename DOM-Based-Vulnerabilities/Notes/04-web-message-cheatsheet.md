# Web Message Vulnerabilities — Quick Revision

## 1. Core Concept

Web Messages use `postMessage()` to communicate data between browsing contexts.

Typical flow:

`postMessage() → message event → event.data → Application Logic → Sink`

## 2. Important APIs

Sender:

```javascript
targetWindow.postMessage(message, targetOrigin);
```

Receiver:

```javascript
window.addEventListener("message", function(event) {
    console.log(event.data);
});
```

Important properties:

```javascript
event.data
event.origin
event.source
```

## 3. Security Checks

A receiver should validate the message origin before trusting sensitive data:

```javascript
if (event.origin === "https://trusted.example") {
    // process message
}
```

Be cautious with:

```javascript
event.origin.includes("trusted.example")
event.origin.startsWith("https://trusted.example")
event.origin.endsWith("trusted.example")
```

## 4. Data Flow

Trace:

`event.data → Variable → Parsing → Validation → Sink`

Example:

```javascript
const data = JSON.parse(event.data);
iframe.src = data.url;
```

## 5. Testing

Start with:

```text
dommsg123
```

Then determine:

- Where `event.data` is used.
- Whether `event.origin` is checked.
- Whether the message is parsed.
- Whether attacker-controlled properties reach a sink.

## 6. Common Sinks

```javascript
element.innerHTML = event.data
location = event.data
iframe.src = event.data
window.open(event.data)
eval(event.data)
```

## 7. Checklist

```text
[ ] Message receiver found
[ ] event.data identified
[ ] event.origin checked
[ ] Origin validation verified
[ ] Message format understood
[ ] Data flow traced
[ ] Sink identified
[ ] Browser behavior confirmed
[ ] Security impact confirmed
```

## 8. Remember

`Untrusted Message + Weak Origin Validation + Dangerous Sink = Potential Web Message Vulnerability`
