# DOM-Based Vulnerabilities — Web Message Vulnerabilities

## 1. Overview

Web Messages can act as a source of attacker-controlled data in DOM-based vulnerabilities.

Web applications can communicate between windows, frames, and other browsing contexts using:

```javascript
postMessage()
```

The receiving page can process the message using a message event listener.

The fundamental flow is:

```text
Attacker-Controlled Window
        ↓
postMessage()
        ↓
message Event
        ↓
event.data
        ↓
Application Logic
        ↓
Sink
        ↓
Security Impact
```

---

## 2. What Is a Web Message?

The `postMessage()` API allows one browsing context to send data to another.

Conceptually:

```javascript
targetWindow.postMessage(message, targetOrigin);
```

The receiving page can listen for the message:

```javascript
window.addEventListener('message', function(event) {
    // process event.data
});
```

The received message is exposed through:

```javascript
event.data
```

The sender's origin is available through:

```javascript
event.origin
```

---

## 3. Why Web Messages Matter

A page may trust incoming messages and pass their contents to another function or DOM sink.

Potential flow:

```text
Attacker-Controlled Window
        ↓
postMessage()
        ↓
Vulnerable Message Handler
        ↓
event.data
        ↓
Application Logic
        ↓
Dangerous Sink
```

If the destination page does not adequately verify the sender or message data, attacker-controlled input may reach a dangerous sink.

---

## 4. Basic Vulnerable Pattern

Consider:

```javascript
window.addEventListener('message', function(e) {
    eval(e.data);
});
```

The flow is:

```text
Attacker-Controlled Message
        ↓
event.data
        ↓
eval()
        ↓
JavaScript Execution
```

This is dangerous because `eval()` processes its argument as JavaScript.

---

## 5. Constructing a Message Source

An attacker can potentially host a malicious page containing an iframe pointing to the vulnerable page.

Conceptual example:

```html
<iframe
    src="//vulnerable-website"
    onload="this.contentWindow.postMessage('print()','*')">
</iframe>
```

The flow becomes:

```text
Attacker Page
      ↓
iframe
      ↓
Vulnerable Page
      ↓
postMessage()
      ↓
event.data
      ↓
eval()
      ↓
JavaScript Execution
```

The exact payload and sink depend on the vulnerable application.

---

## 6. The `targetOrigin` Argument

The second argument to `postMessage()` specifies the intended target origin.

Example:

```javascript
postMessage('data', '*');
```

The wildcard:

```text
*
```

allows the message to be sent without restricting the target origin.

This becomes particularly important when the receiving application also fails to verify the sender's origin.

---

## 7. `event.origin`

The receiving page can inspect:

```javascript
event.origin
```

This identifies the origin of the document that sent the message.

Conceptual security flow:

```text
Incoming Message
      ↓
event.origin
      ↓
Origin Verification
      ↓
Message Processing
```

A secure implementation should verify that the sender is an expected origin before trusting the message.

---

## 8. `event.data`

The message contents are available through:

```javascript
event.data
```

Potential flow:

```text
Attacker-Controlled Message
        ↓
event.data
        ↓
Application Processing
        ↓
Sink
```

The application should not automatically trust the contents of `event.data`.

---

## 9. Origin Validation

When reviewing a message handler, ask:

- Is `event.origin` checked?
- Is the expected origin explicitly defined?
- Is the comparison exact?
- Are unexpected origins rejected?

A missing origin check can allow an attacker-controlled page to send messages to the vulnerable application.

---

## 10. Weak Origin Validation

Some applications attempt to validate origins using string methods.

Example:

```javascript
if (e.origin.endsWith('normal-website.com')) {
    eval(e.data);
}
```

This type of validation can be unsafe because an attacker-controlled origin such as:

```text
http://www.malicious-websitenormal-website.com
```

could satisfy the `endsWith()` condition.

The important lesson is:

```text
Origin Validation
      ↓
Must Validate the Actual Expected Origin
```

Do not rely on weak substring-based origin checks.

---

## 11. `startsWith()` and `endsWith()`

Be cautious when code uses:

```javascript
origin.startsWith(...)
```

or:

```javascript
origin.endsWith(...)
```

when validating origins.

For example:

```javascript
if (e.origin.endsWith('normal-website.com')) {
    ...
}
```

The validation may accept an attacker-controlled domain that merely contains the trusted string.

Therefore:

```text
String Matching
      ≠
Reliable Origin Validation
```

---

## 12. Exact Origin Validation

The expected origin should be validated as an origin rather than merely searching for a trusted string.

Conceptually:

```text
Incoming Origin
      ↓
Compare Against Expected Origin
      ↓
Match?
  ├── NO  → Reject
  └── YES → Process
```

The exact implementation should follow the application's legitimate communication requirements.

---

## 13. Message Handler as a Source

A message event listener can act as a source for a DOM-based vulnerability.

Example:

```javascript
window.addEventListener('message', function(event) {
    const value = event.data;

    // application logic
});
```

The source is:

```javascript
event.data
```

The flow is:

```text
postMessage()
      ↓
event.data
      ↓
JavaScript
      ↓
Sink
```

---

## 14. Message Handler as a Sink Chain

The message handler itself is not necessarily the vulnerability.

Instead:

```text
Web Message
      ↓
Message Handler
      ↓
Application Function
      ↓
Dangerous Sink
```

Any dangerous operation performed using attacker-controlled message data should be investigated.

---

## 15. Web Message → `eval()`

Example:

```javascript
window.addEventListener('message', function(e) {
    eval(e.data);
});
```

Taint flow:

```text
postMessage()
      ↓
event.data
      ↓
eval()
      ↓
JavaScript Execution
```

Potential impact:

```text
DOM XSS
```

when the attacker can successfully cause the vulnerable page to process the malicious message.

---

## 16. Web Message → HTML Sink

A message can also reach an HTML sink.

Example pattern:

```javascript
window.addEventListener('message', function(e) {
    document.getElementById('ads').innerHTML = e.data;
});
```

Flow:

```text
postMessage()
      ↓
event.data
      ↓
innerHTML
      ↓
DOM Modification
      ↓
Potential XSS
```

---

## 17. Web Message → JavaScript URL

A message can potentially influence a URL-bearing sink.

Conceptual flow:

```text
postMessage()
      ↓
event.data
      ↓
URL / src
      ↓
JavaScript URL
      ↓
Script Execution
```

This is especially relevant when the application accepts attacker-controlled message properties as URLs.

---

## 18. Web Message → `JSON.parse()`

Some applications expect messages in JSON format.

Example:

```javascript
window.addEventListener('message', function(event) {
    const data = JSON.parse(event.data);
});
```

The flow is:

```text
postMessage()
      ↓
event.data
      ↓
JSON.parse()
      ↓
JavaScript Object
      ↓
Application Logic
      ↓
Potential Sink
```

`JSON.parse()` itself does not execute JavaScript. The security issue depends on how the resulting object is subsequently used.

---

## 19. JSON Message Structure

An application may expect a message containing a property such as:

```json
{
    "type": "load-channel",
    "url": "..."
}
```

The message handler may then use:

```javascript
data.url
```

in another operation.

Conceptual flow:

```text
JSON Message
      ↓
JSON.parse()
      ↓
data.type
      ↓
Application Branch
      ↓
data.url
      ↓
Sink
```

The security analysis must therefore follow the complete flow.

---

## 20. Web Message + iframe

A common testing structure is:

```text
Attacker Page
      ↓
iframe
      ↓
Target Page
      ↓
postMessage()
      ↓
Target Message Handler
      ↓
Sink
```

The iframe provides a browsing context whose `contentWindow` can be used to send a message to the target.

---

## 21. `contentWindow`

When a target is loaded inside an iframe:

```javascript
iframe.contentWindow
```

can represent the window of the framed document.

Conceptually:

```javascript
iframe.contentWindow.postMessage(message, targetOrigin);
```

This can be used to test whether the target page accepts messages from an unexpected origin.

---

## 22. Web Message DOM XSS Lab Pattern

A vulnerable page may contain a handler that takes incoming message content and inserts it into a DOM element.

Conceptually:

```javascript
window.addEventListener('message', function(event) {
    document.getElementById('ads').innerHTML = event.data;
});
```

The flow is:

```text
Attacker Page
      ↓
postMessage()
      ↓
event.data
      ↓
innerHTML
      ↓
DOM
      ↓
Potential XSS
```

This pattern is demonstrated in the PortSwigger Web Security Academy material.

---

## 23. Lab: DOM XSS Using Web Messages

The lab demonstrates a simple Web Message vulnerability.

The vulnerable application listens for a Web Message and inserts the message content into a page element.

The testing concept is:

```text
1. Identify the message listener.
2. Determine how event.data is processed.
3. Identify the sink.
4. Construct an authorized exploit page.
5. Send the message to the target.
6. Confirm the resulting browser behavior.
```

The supplied material's lab uses an iframe and `postMessage()` to deliver the test input.

---

## 24. Lab: Web Messages and a JavaScript URL

Another lab uses Web Messages together with JSON parsing.

The vulnerable flow is:

```text
Attacker Page
      ↓
iframe
      ↓
postMessage()
      ↓
JSON.parse()
      ↓
Message Type
      ↓
URL Property
      ↓
iframe src
      ↓
JavaScript URL
      ↓
JavaScript Execution
```

The lab demonstrates how a message property can eventually reach a URL-bearing sink.

---

## 25. Web Message Vulnerability Impact

The impact depends on how the destination document processes the incoming message.

Potential outcomes include:

```text
DOM XSS
Unexpected DOM Modification
JavaScript Execution
Navigation
Other Security-Sensitive Client-Side Behavior
```

The important point is:

```text
Web Message Source
      +
Unsafe Sink
      ↓
Potential Security Impact
```

---

## 26. Which Sinks Can Be Reached?

Any sink used by the incoming message handler may become relevant if the message source is not adequately trusted or validated.

Examples include:

```text
eval()
innerHTML
document.write()
location
URL / src attributes
JavaScript execution functions
Other DOM sinks
```

Always trace the specific application flow.

---

## 27. Testing Methodology

### Step 1 — Search for Message Handlers

Search JavaScript for:

```text
addEventListener('message'
```

and:

```text
onmessage
```

---

### Step 2 — Identify `event.data`

Look for:

```javascript
event.data
```

Determine where the message contents are stored and processed.

---

### Step 3 — Identify `event.origin`

Look for:

```javascript
event.origin
```

Determine whether the application validates the sender.

---

### Step 4 — Follow the Data

Trace:

```text
event.data
      ↓
Variable
      ↓
Function
      ↓
Sink
```

---

### Step 5 — Identify the Sink

Search for:

```text
eval
innerHTML
document.write
location
src
href
```

and other relevant operations.

---

### Step 6 — Confirm the Behavior

Use an authorized test environment and confirm whether the message produces the expected security-sensitive behavior.

---

## 28. DevTools Workflow

```text
Open DevTools
      ↓
Sources
      ↓
Search for "message"
      ↓
Find Event Listener
      ↓
Inspect event.data
      ↓
Inspect event.origin
      ↓
Set Breakpoint
      ↓
Send Test Message
      ↓
Follow Data
      ↓
Identify Sink
```

---

## 29. Burp Suite Workflow

```text
Burp Proxy
      ↓
Identify Target Page
      ↓
Open in Browser
      ↓
Inspect JavaScript
      ↓
Find Message Handler
      ↓
Identify event.data
      ↓
Identify Sink
      ↓
Test Authorized Message Source
      ↓
Confirm Behavior
```

---

## 30. Testing Questions

For every Web Message handler, ask:

```text
1. Does the page listen for messages?
2. What does event.data contain?
3. Is event.origin checked?
4. How is the origin checked?
5. Is the check exact?
6. Is the message data validated?
7. Is JSON.parse() used?
8. Which properties of the message are trusted?
9. Where does the data flow?
10. What sink receives the data?
11. What browser behavior results?
12. What is the security impact?
```

---

## 31. Common Mistakes

### Mistake 1 — Only Looking for `postMessage()`

Finding:

```javascript
postMessage()
```

does not automatically mean the target is vulnerable.

The receiving page must be analyzed.

---

### Mistake 2 — Ignoring `event.origin`

Always inspect:

```javascript
event.origin
```

when analyzing a message handler.

---

### Mistake 3 — Assuming `JSON.parse()` Is the Sink

`JSON.parse()` parses JSON.

It does not by itself execute JavaScript.

The important question is:

```text
What happens to the parsed object afterward?
```

---

### Mistake 4 — Trusting Weak Origin Checks

Be careful with:

```javascript
startsWith()
```

and:

```javascript
endsWith()
```

when used to validate origins.

---

### Mistake 5 — Stopping at the Message Handler

The message handler is usually part of the source-to-sink chain.

Continue tracing:

```text
event.data
      ↓
Application Logic
      ↓
Sink
```

---

## 32. Source → Sink Examples

### Example 1 — `eval()`

```text
postMessage()
      ↓
event.data
      ↓
eval()
      ↓
JavaScript Execution
```

### Example 2 — `innerHTML`

```text
postMessage()
      ↓
event.data
      ↓
innerHTML
      ↓
DOM Modification
      ↓
Potential XSS
```

### Example 3 — JavaScript URL

```text
postMessage()
      ↓
event.data
      ↓
url Property
      ↓
iframe src
      ↓
JavaScript URL
      ↓
Execution
```

### Example 4 — Navigation

```text
postMessage()
      ↓
event.data
      ↓
location
      ↓
Browser Navigation
```

---

## 33. Complete Web Message Testing Flow

```text
START
  ↓
Find message listener
  ↓
Identify event.data
  ↓
Identify event.origin
  ↓
Review origin validation
  ↓
Review data validation
  ↓
Trace event.data
  ↓
Find sink
  ↓
Determine browser behavior
  ↓
Confirm exploitability
  ↓
Determine impact
  ↓
Document finding
```

---

## 34. Security Model

The secure conceptual model is:

```text
Incoming Message
      ↓
Verify Trusted Origin
      ↓
Validate Message Data
      ↓
Process Data Safely
      ↓
Use Safe Sink
```

The vulnerable model is:

```text
Incoming Message
      ↓
No / Weak Origin Validation
      ↓
Untrusted event.data
      ↓
Dangerous Sink
      ↓
Security Impact
```

---

## 35. Quick Reference

### Sources

```text
postMessage()
event.data
```

### Security Properties

```text
event.origin
targetOrigin
```

### Common Sinks

```text
eval()
innerHTML
document.write()
location
src
href
Other DOM sinks
```

### Common Processing

```text
JSON.parse()
```

---

## 36. Final Checklist

```text
☐ Message listener identified
☐ event.data identified
☐ event.origin identified
☐ Origin validation reviewed
☐ Weak string-based validation reviewed
☐ Message data validation reviewed
☐ JSON.parse() reviewed
☐ Message properties traced
☐ Source-to-sink flow identified
☐ Dangerous sink identified
☐ Browser behavior confirmed
☐ Exploitability confirmed
☐ Security impact confirmed
☐ Evidence captured
☐ Reproduction documented
☐ Remediation documented
```

---

# Final Mental Model

```text
ATTACKER WINDOW
      ↓
postMessage()
      ↓
MESSAGE EVENT
      ↓
event.origin ──→ Origin Validation
      ↓
event.data
      ↓
APPLICATION LOGIC
      ↓
DANGEROUS SINK
      ↓
BROWSER BEHAVIOR
      ↓
SECURITY IMPACT
```

---

# Final Rule

```text
WEB MESSAGE SOURCE
        +
INSUFFICIENT ORIGIN VALIDATION
        +
ATTACKER-CONTROLLED DATA
        +
DANGEROUS SINK
        +
REPRODUCIBLE BEHAVIOR
        +
SECURITY IMPACT
        =
CONFIRMED WEB MESSAGE VULNERABILITY
```