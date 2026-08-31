# DOM-Based Vulnerabilities — Web Message Origin Validation

## 1. Overview

When a web application receives messages using `postMessage()`, it should determine whether the message originated from a trusted source.

The sender's origin is exposed through:

```javascript
event.origin
```

The fundamental security model is:

```text
Incoming Web Message
        ↓
event.origin
        ↓
Origin Validation
        ↓
Message Data
        ↓
Application Logic
        ↓
Potential Sink
```

If the application accepts messages from untrusted origins and uses attacker-controlled data in a dangerous way, this can lead to DOM-based vulnerabilities.

---

## 2. What Is an Origin?

An origin is composed of:

```text
Scheme
Host
Port
```

For example:

```text
https://example.com
```

The origin identifies the security context from which the message was sent.

When testing Web Messages, the important question is:

```text
Does the application trust the actual sender origin?
```

---

## 3. `event.origin`

A message event provides the sender's origin through:

```javascript
event.origin
```

Example:

```javascript
window.addEventListener('message', function(event) {
    console.log(event.origin);
});
```

The application can use this value to determine whether the sender is trusted.

---

## 4. `event.data`

The contents of the message are available through:

```javascript
event.data
```

Example:

```javascript
window.addEventListener('message', function(event) {
    console.log(event.data);
});
```

The security analysis should consider both:

```text
event.origin
event.data
```

The origin determines **who sent the message**, while the data determines **what was sent**.

---

## 5. Secure Message Processing

A secure conceptual flow is:

```text
Incoming Message
      ↓
Check event.origin
      ↓
Trusted?
  ├── NO  → Reject
  └── YES
       ↓
Validate event.data
       ↓
Process Safely
       ↓
Safe Application Behavior
```

Both origin and message data should be considered when appropriate.

---

## 6. Missing Origin Validation

A vulnerable message handler may look like:

```javascript
window.addEventListener('message', function(event) {
    processMessage(event.data);
});
```

Notice that there is no check of:

```javascript
event.origin
```

The flow becomes:

```text
Any Sender
    ↓
postMessage()
    ↓
event.data
    ↓
Application Logic
```

If `processMessage()` performs a dangerous operation, an attacker may be able to influence the behavior.

---

## 7. Weak Origin Validation

An application may attempt to validate the origin using string matching.

Example:

```javascript
if (event.origin.endsWith('example.com')) {
    processMessage(event.data);
}
```

This can be dangerous because an attacker-controlled domain could contain the trusted string while still being a different origin.

Conceptually:

```text
Trusted String
      ↓
String Matching
      ↓
Unexpected Origin Accepted
```

The important lesson is:

```text
String Contains Trusted Text
        ≠
Trusted Origin
```

---

## 8. `startsWith()` Validation

Another weak pattern is:

```javascript
if (event.origin.startsWith('https://example.com')) {
    processMessage(event.data);
}
```

This should be carefully reviewed.

A validation mechanism should not merely determine whether the origin begins with a trusted string.

Instead, the application should verify the intended origin precisely.

---

## 9. `endsWith()` Validation

Similarly:

```javascript
if (event.origin.endsWith('example.com')) {
    processMessage(event.data);
}
```

can be problematic.

The string:

```text
example.com
```

could appear as part of another attacker-controlled hostname.

Therefore:

```text
endsWith()
    ↓
Potentially Ambiguous
```

---

## 10. Exact Origin Comparison

A stronger conceptual approach is to compare the complete expected origin.

For example:

```javascript
if (event.origin === 'https://example.com') {
    processMessage(event.data);
}
```

The model is:

```text
Incoming Origin
      ↓
Exact Comparison
      ↓
Expected Origin?
  ├── NO  → Reject
  └── YES → Process
```

The exact trusted origin should correspond to the application's legitimate communication requirements.

---

## 11. Why Origin Validation Matters

Consider:

```text
Attacker Page
      ↓
postMessage()
      ↓
Target Application
```

If the target accepts messages from any origin:

```text
Attacker Origin
      ↓
Accepted
      ↓
event.data
      ↓
Dangerous Sink
```

The attacker may be able to influence security-sensitive client-side behavior.

---

## 12. Origin Validation Is Not Enough

Even if the application validates:

```javascript
event.origin
```

the message contents should still be considered untrusted.

Secure conceptual flow:

```text
Trusted Origin
      ↓
Validate event.data
      ↓
Safe Processing
```

Therefore:

```text
Trusted Origin
    ≠
Automatically Trusted Data
```

---

## 13. Data Validation

Inspect how:

```javascript
event.data
```

is handled after origin validation.

Questions:

```text
☐ Is the expected data type checked?
☐ Is the structure validated?
☐ Are unexpected properties rejected?
☐ Is attacker-controlled content passed to a dangerous sink?
```

---

## 14. Origin + Data Flow

The complete Web Message analysis is:

```text
postMessage()
      ↓
event.origin
      ↓
Origin Validation
      ↓
event.data
      ↓
Data Validation
      ↓
Application Logic
      ↓
Sink
```

This is more useful than checking the origin in isolation.

---

## 15. Weak Validation Example

Consider:

```javascript
window.addEventListener('message', function(event) {
    if (event.origin.endsWith('normal-website.com')) {
        eval(event.data);
    }
});
```

The flow is:

```text
Attacker-Controlled Origin
          ↓
endsWith()
          ↓
Origin Accepted
          ↓
event.data
          ↓
eval()
          ↓
JavaScript Execution
```

This represents a potentially exploitable source-to-sink chain.

---

## 16. Testing Weak Origin Validation

When you find:

```javascript
event.origin
```

look for:

```text
startsWith()
endsWith()
includes()
indexOf()
substring()
```

These operations should be reviewed carefully when they are being used to determine whether a sender is trusted.

The objective is to determine whether an attacker-controlled origin can satisfy the validation logic.

---

## 17. Exact Origin Testing

Determine the expected origin used by the application.

Conceptually:

```text
Expected:
https://trusted.example

Received:
https://attacker.example
```

The application should distinguish these origins.

Do not assume that similar-looking hostnames represent the same origin.

---

## 18. Origin and Port

The port is part of an origin.

For example:

```text
https://example.com:443
```

and:

```text
https://example.com:8443
```

represent different origins.

Therefore, origin validation should account for the complete origin rather than only the hostname text.

---

## 19. Origin and Scheme

The scheme also matters.

For example:

```text
http://example.com
```

and:

```text
https://example.com
```

are different origins.

A validation mechanism should therefore avoid treating a hostname alone as sufficient trust.

---

## 20. Origin and Hostname

The hostname is another component of the origin.

These should not automatically be considered equivalent:

```text
example.com
sub.example.com
attackerexample.com
example.com.attacker.example
```

The application's trusted origin should be explicitly defined.

---

## 21. `targetOrigin`

The sender can specify a target origin when calling:

```javascript
postMessage(message, targetOrigin);
```

Example:

```javascript
targetWindow.postMessage(
    message,
    'https://example.com'
);
```

The `targetOrigin` argument controls where the message is intended to be delivered.

---

## 22. Wildcard `targetOrigin`

A sender may use:

```javascript
postMessage(message, '*');
```

The wildcard allows the message to be sent without restricting the target origin.

This can be dangerous when sensitive information is being sent.

When analyzing Web Messages, inspect:

```text
targetOrigin
event.origin
```

---

## 23. `targetOrigin` vs `event.origin`

These properties serve different purposes.

### `targetOrigin`

Controls where the sender intends to send the message:

```text
Sender
  ↓
targetOrigin
  ↓
Destination
```

### `event.origin`

Identifies the origin that sent the message:

```text
Sender
  ↓
postMessage()
  ↓
event.origin
  ↓
Receiver
```

Therefore:

```text
targetOrigin
    ≠
event.origin
```

Both can be relevant to Web Message security.

---

## 24. Testing `targetOrigin`

When reviewing:

```javascript
postMessage(message, targetOrigin);
```

ask:

```text
1. Is targetOrigin '*'
2. Is the target origin explicitly defined?
3. Is sensitive data being transmitted?
4. Is the receiving page expected to trust the sender?
```

The security significance depends on the application's communication model.

---

## 25. Web Message → DOM XSS

A weak origin check can become especially important when message data reaches a DOM XSS sink.

Example:

```javascript
window.addEventListener('message', function(event) {
    if (event.origin.endsWith('example.com')) {
        document.body.innerHTML = event.data;
    }
});
```

Flow:

```text
Attacker Origin
      ↓
Weak Origin Validation
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

## 26. Web Message → `eval()`

Another example:

```javascript
window.addEventListener('message', function(event) {
    if (event.origin.endsWith('example.com')) {
        eval(event.data);
    }
});
```

Flow:

```text
Attacker Origin
      ↓
Weak Origin Validation
      ↓
event.data
      ↓
eval()
      ↓
JavaScript Execution
```

The complete chain should be verified in an authorized testing environment.

---

## 27. Web Message → URL

A weakly validated message may also influence a URL.

Conceptual flow:

```text
Attacker Origin
      ↓
Origin Validation
      ↓
event.data
      ↓
URL Property
      ↓
Navigation / src
      ↓
Browser Behavior
```

Inspect both origin validation and destination validation.

---

## 28. Testing Methodology

### Step 1 — Find Message Handlers

Search JavaScript for:

```text
addEventListener('message'
```

and:

```text
onmessage
```

---

### Step 2 — Find Origin Checks

Search for:

```text
event.origin
```

Then determine how the value is compared.

---

### Step 3 — Identify Weak Comparisons

Look for:

```text
startsWith()
endsWith()
includes()
indexOf()
```

and similar string operations.

---

### Step 4 — Identify Message Data

Search for:

```text
event.data
```

Determine how the data is processed.

---

### Step 5 — Trace the Sink

Look for:

```text
eval()
innerHTML
document.write()
location
src
href
```

and other security-sensitive operations.

---

### Step 6 — Confirm the Flow

The objective is:

```text
Attacker-Controlled Origin
        ↓
Origin Validation
        ↓
event.data
        ↓
Dangerous Sink
        ↓
Security Impact
```

---

## 29. Browser DevTools Workflow

```text
Open DevTools
      ↓
Sources
      ↓
Search "message"
      ↓
Locate Message Handler
      ↓
Inspect event.origin
      ↓
Inspect event.data
      ↓
Review Validation
      ↓
Set Breakpoint
      ↓
Trigger Message
      ↓
Trace Data
      ↓
Identify Sink
```

---

## 30. Burp Suite Workflow

```text
Burp Proxy
      ↓
Identify Target Page
      ↓
Open Target in Browser
      ↓
Inspect Client-Side JavaScript
      ↓
Find Message Handler
      ↓
Find event.origin
      ↓
Analyze Origin Validation
      ↓
Find event.data
      ↓
Trace to Sink
      ↓
Confirm Behavior
```

---

## 31. Testing Questions

For every origin validation mechanism, ask:

```text
1. What origin does the application expect?
2. Is event.origin checked?
3. Is the comparison exact?
4. Is startsWith() used?
5. Is endsWith() used?
6. Is includes() used?
7. Is the scheme validated?
8. Is the hostname validated?
9. Is the port relevant?
10. Is event.data validated?
11. Where does event.data flow?
12. Does it reach a dangerous sink?
13. What browser behavior results?
14. What is the security impact?
```

---

## 32. Common Mistakes

### Mistake 1 — Trusting the Hostname Alone

Do not assume:

```text
Trusted hostname
    =
Trusted origin
```

Scheme and port are also relevant.

---

### Mistake 2 — Trusting `startsWith()`

A prefix check may accept an unintended origin.

Always determine the exact origin semantics of the validation.

---

### Mistake 3 — Trusting `endsWith()`

A suffix check may accept attacker-controlled domains containing the trusted hostname.

---

### Mistake 4 — Checking Only the Origin

Even a trusted origin does not automatically make:

```text
event.data
```

safe.

Data validation is still important.

---

### Mistake 5 — Assuming `targetOrigin` Protects the Receiver

`targetOrigin` is specified by the sender.

The receiver should still validate:

```text
event.origin
```

when trust decisions depend on the sender.

---

## 33. Secure vs Vulnerable Model

### Secure

```text
Incoming Message
      ↓
Exact Origin Validation
      ↓
Data Validation
      ↓
Safe Processing
      ↓
Safe Sink
```

### Potentially Vulnerable

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

## 34. Quick Reference

### Important Properties

```text
event.origin
event.data
targetOrigin
```

### Weak Validation Patterns

```text
startsWith()
endsWith()
includes()
indexOf()
```

### Common Sinks

```text
eval()
innerHTML
document.write()
location
src
href
```

---

## 35. Complete Testing Flow

```text
START
  ↓
Find message listener
  ↓
Identify event.origin
  ↓
Identify origin validation
  ↓
Determine whether validation is exact
  ↓
Identify event.data
  ↓
Review data validation
  ↓
Trace data flow
  ↓
Identify sink
  ↓
Determine browser behavior
  ↓
Confirm exploitability
  ↓
Assess security impact
  ↓
Document finding
```

---

## 36. Evidence Collection

Record:

```text
☐ Message listener
☐ event.origin
☐ Origin validation code
☐ Expected origin
☐ event.data
☐ Data validation
☐ Source-to-sink flow
☐ Sink
☐ Browser behavior
☐ Reproduction steps
☐ Security impact
```

---

## 37. Reporting Structure

A Web Message origin-validation finding should explain:

```text
Affected Functionality
        ↓
Message Source
        ↓
Sender Origin
        ↓
Origin Validation
        ↓
Message Data
        ↓
Sink
        ↓
Browser Behavior
        ↓
Security Impact
```

Include:

```text
Title
Affected URL
Origin Validation Issue
Message Structure
Source-to-Sink Flow
Reproduction Steps
Proof of Concept
Observed Result
Impact
Remediation
```

---

## 38. Remediation Principles

General defensive principles include:

```text
☐ Validate the complete expected origin
☐ Avoid weak substring-based origin checks
☐ Do not rely solely on hostname text
☐ Account for scheme and port
☐ Validate event.data
☐ Restrict accepted message structures
☐ Use an appropriate targetOrigin when sending messages
☐ Avoid dangerous sinks
☐ Treat all external messages as untrusted until validated
```

---

## 39. Final Checklist

```text
☐ Message handler identified
☐ event.origin identified
☐ Expected origin identified
☐ Origin comparison analyzed
☐ startsWith() reviewed
☐ endsWith() reviewed
☐ includes() reviewed
☐ indexOf() reviewed
☐ Scheme reviewed
☐ Host reviewed
☐ Port reviewed
☐ targetOrigin reviewed
☐ event.data identified
☐ Message data validation reviewed
☐ Source-to-sink flow traced
☐ Dangerous sink identified
☐ Browser behavior confirmed
☐ Exploitability confirmed
☐ Impact confirmed
☐ Evidence captured
☐ Remediation documented
```

---

# Final Mental Model

```text
ATTACKER
    ↓
postMessage()
    ↓
MESSAGE EVENT
    ↓
event.origin
    ↓
ORIGIN VALIDATION
    ↓
event.data
    ↓
DATA VALIDATION
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
WEB MESSAGE
      +
ATTACKER-CONTROLLED ORIGIN
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
CONFIRMED WEB MESSAGE ORIGIN-VALIDATION VULNERABILITY
```
```