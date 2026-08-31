# Lab 04 — Web Message Origin Validation

## 1. Lab Overview

Web Messages allow different browser windows, tabs, and iframes to communicate using:

```javascript
postMessage()
```

A receiving page can process the message using:

```javascript
window.addEventListener('message', function(event) {
    ...
});
```

The security problem occurs when the receiver trusts messages without properly verifying:

```javascript
event.origin
```

The fundamental model is:

```text
Attacker-Controlled Window
        ↓
postMessage()
        ↓
Message Event
        ↓
event.origin
        ↓
Origin Validation
        ↓
event.data
        ↓
Security-Sensitive Sink
        ↓
Impact
```

---

# 2. What Is Origin Validation?

The browser provides the sender's origin through:

```javascript
event.origin
```

An origin consists conceptually of:

```text
scheme + host + port
```

For example:

```text
https://example.com
```

A secure application should verify that the message came from the expected origin.

---

# 3. Why Origin Validation Matters

Suppose an application contains:

```javascript
window.addEventListener('message', function(event) {
    eval(event.data);
});
```

If there is no origin validation:

```text
Attacker Website
      ↓
postMessage()
      ↓
Victim Page
      ↓
event.data
      ↓
eval()
```

The attacker may be able to control the message.

The source material explains that when a page handles incoming Web Messages unsafely and fails to verify the origin correctly, properties and functions used by the event listener can become sinks. :contentReference[oaicite:1]{index=1}

---

# 4. Basic Secure Pattern

A basic pattern is:

```javascript
window.addEventListener('message', function(event) {

    if (event.origin !== 'https://trusted.example') {
        return;
    }

    // Process event.data
});
```

The important property is the exact origin comparison:

```javascript
event.origin === 'https://trusted.example'
```

---

# 5. Vulnerable Pattern — `indexOf()`

A common mistake is:

```javascript
if (event.origin.indexOf('normal-website.com') > -1) {
    eval(event.data);
}
```

This does not verify that the origin **is**:

```text
normal-website.com
```

It only checks whether the string appears somewhere in the origin.

The supplied material identifies this exact flaw. :contentReference[oaicite:2]{index=2}

---

# 6. `indexOf()` Bypass

The vulnerable check:

```javascript
event.origin.indexOf('normal-website.com') > -1
```

could accept an origin such as:

```text
http://www.normal-website.com.evil.net
```

because:

```text
normal-website.com
```

appears inside the attacker-controlled origin.

Conceptually:

```text
Attacker Origin
      ↓
http://www.normal-website.com.evil.net
      ↓
Contains "normal-website.com"
      ↓
Validation Passes
```

The source material explicitly gives this example. :contentReference[oaicite:3]{index=3}

---

# 7. Vulnerable Pattern — `startsWith()`

Another common pattern is:

```javascript
if (event.origin.startsWith('https://normal-website.com')) {
    // process message
}
```

This can be unsafe if the expected origin is not compared carefully.

For example:

```text
https://normal-website.com.evil.net
```

starts with:

```text
https://normal-website.com
```

but the actual host is:

```text
normal-website.com.evil.net
```

not:

```text
normal-website.com
```

---

# 8. Vulnerable Pattern — `endsWith()`

The supplied material gives this example:

```javascript
if (e.origin.endsWith('normal-website.com')) {
    eval(e.data);
}
```

An origin such as:

```text
http://www.malicious-websitenormal-website.com
```

could satisfy the suffix check. :contentReference[oaicite:4]{index=4}

The lesson is:

```text
String Matching
      ≠
Origin Validation
```

---

# 9. Exact Origin Comparison

A safer approach is:

```javascript
if (event.origin !== 'https://normal-website.com') {
    return;
}
```

This checks the complete origin rather than searching for a substring.

The validation should correspond to the exact origin the application expects.

---

# 10. Origin vs Hostname

Remember that:

```text
Origin
```

and:

```text
Hostname
```

are not identical.

For example:

```text
Origin:
https://example.com:8443

Hostname:
example.com
```

The scheme and port can be security-relevant.

Therefore, avoid casually stripping components unless the application's security model explicitly requires it.

---

# 11. Origin vs URL

A complete URL may contain:

```text
https://example.com/path?x=1
```

The origin is:

```text
https://example.com
```

The path and query are not part of the origin.

When validating:

```javascript
event.origin
```

compare it against the intended origin, not an arbitrary substring of a URL.

---

# 12. Lab Objective

The objective of this class of lab is to:

```text
Identify a Web Message listener
        ↓
Identify flawed origin validation
        ↓
Find an attacker-controlled origin that passes
        ↓
Send a controlled Web Message
        ↓
Reach the vulnerable sink
        ↓
Confirm the impact
```

---

# 13. Step 1 — Find the Message Listener

Search the application's JavaScript for:

```javascript
addEventListener('message'
```

Also search for:

```text
onmessage
postMessage
event.data
event.origin
```

---

# 14. Step 2 — Inspect the Event Handler

Example:

```javascript
window.addEventListener('message', function(e) {

    if (e.origin.indexOf('normal-website.com') > -1) {
        eval(e.data);
    }

});
```

Identify:

```text
Source:
e.data

Origin:
e.origin

Validation:
indexOf()

Sink:
eval()
```

---

# 15. Step 3 — Identify the Validation Function

Look for:

```text
indexOf()
includes()
startsWith()
endsWith()
match()
test()
```

Then determine exactly what the function validates.

---

# 16. Step 4 — Understand the Validation

For:

```javascript
e.origin.indexOf('normal-website.com') > -1
```

the application is effectively asking:

```text
Does the string contain "normal-website.com"?
```

It is not asking:

```text
Is the complete origin exactly "https://normal-website.com"?
```

This distinction is the vulnerability.

---

# 17. Step 5 — Construct an Attacker Origin

A test origin should be constructed so that:

```text
Attacker-Controlled Origin
        ↓
Contains the trusted domain string
        ↓
Validation passes
```

Example from the supplied material:

```text
http://www.normal-website.com.evil.net
```

:contentReference[oaicite:5]{index=5}

---

# 18. Step 6 — Create the Sending Page

Use an authorized lab/exploit-server environment.

The basic structure is:

```html
<script>
window.addEventListener('load', function() {

    const target = window.open('https://TARGET-LAB/');

    target.postMessage(
        'TEST-MESSAGE',
        '*'
    );

});
</script>
```

The exact message must match the vulnerable application's expected format.

---

# 19. Step 7 — Trigger the Message

The attacker-controlled page sends:

```javascript
target.postMessage(message, '*');
```

The vulnerable page receives:

```javascript
event.data
```

and evaluates:

```javascript
event.origin
```

---

# 20. Step 8 — Confirm the Origin

At the vulnerable page, inspect:

```javascript
event.origin
```

with DevTools.

Confirm that it is:

```text
Attacker-Controlled Origin
```

while still satisfying the application's flawed validation.

---

# 21. Step 9 — Trace to the Sink

Once the validation is bypassed:

```text
Attacker Origin
      ↓
postMessage()
      ↓
event.data
      ↓
Origin Validation
      ↓
Validation Bypass
      ↓
Sink
```

The final sink may be:

```text
eval()
innerHTML
location
iframe.src
document.write()
```

or another security-sensitive operation.

---

# 22. Source → Sink Example

Consider:

```javascript
window.addEventListener('message', function(e) {

    if (e.origin.indexOf('normal-website.com') > -1) {
        eval(e.data);
    }

});
```

The flow is:

```text
Attacker-Controlled Window
        ↓
postMessage()
        ↓
event.origin
        ↓
indexOf()
        ↓
Validation Bypass
        ↓
event.data
        ↓
eval()
        ↓
JavaScript Execution
```

---

# 23. `startsWith()` Example

Vulnerable:

```javascript
if (e.origin.startsWith('https://normal-website.com')) {
    eval(e.data);
}
```

Potentially accepted:

```text
https://normal-website.com.evil.net
```

because the attacker-controlled origin begins with:

```text
https://normal-website.com
```

The important question is:

```text
Does the check validate the complete origin?
```

---

# 24. `endsWith()` Example

Vulnerable:

```javascript
if (e.origin.endsWith('normal-website.com')) {
    eval(e.data);
}
```

Potentially accepted:

```text
https://evilnormal-website.com
```

because the trusted string occurs at the end.

The supplied material demonstrates this class of bypass. :contentReference[oaicite:6]{index=6}

---

# 25. `includes()` Example

A similar problem exists with:

```javascript
if (e.origin.includes('normal-website.com')) {
    ...
}
```

Possible attacker-controlled origin:

```text
https://evil.example/...
```

The exact bypass depends on the resulting origin string and what substring the application checks.

The principle remains:

```text
Substring Matching
        ≠
Exact Origin Validation
```

---

# 26. Regex Validation

Regex-based validation can also be flawed.

Example:

```javascript
/^https:\/\/.*\.trusted.example$/
```

When reviewing regex validation, check:

```text
Anchors
Dots
Subdomains
Ports
Schemes
Unexpected characters
```

Do not assume that a regex is safe simply because it exists.

---

# 27. Message Validation vs Origin Validation

There are two separate questions:

```text
1. Who sent the message?
2. What does the message contain?
```

Therefore, secure Web Message handling should consider both:

```text
Origin Validation
+
Message/Data Validation
```

---

# 28. Message Structure Validation

If the application expects:

```json
{
    "type": "load-channel",
    "url": "https://example.com"
}
```

it should validate:

```text
type
url
data types
allowed values
```

Even if the origin is trusted, the message data may still require validation.

---

# 29. `targetOrigin` Is Not Enough

A sender may use:

```javascript
postMessage(message, 'https://trusted.example');
```

This does not automatically make the message trusted.

The receiver must still verify:

```javascript
event.origin
```

because the receiver is responsible for deciding whether the sender is trusted.

---

# 30. Common Sink Categories

Web Message vulnerabilities can lead to different impacts depending on the sink.

### DOM XSS

```text
event.data
      ↓
innerHTML
```

### JavaScript Execution

```text
event.data
      ↓
eval()
```

### Navigation

```text
event.data
      ↓
location.href
```

### Resource Loading

```text
event.data
      ↓
iframe.src
```

The supplied material emphasizes that any sink used by an unsafe message handler can potentially become part of a DOM-based Web Message vulnerability. :contentReference[oaicite:7]{index=7}

---

# 31. DevTools Testing Workflow

```text
DevTools
   ↓
Sources
   ↓
Search:
   message
   postMessage
   event.origin
   event.data
   ↓
Find Listener
   ↓
Set Breakpoint
   ↓
Trigger Message
   ↓
Inspect event.origin
   ↓
Inspect event.data
   ↓
Inspect Validation
   ↓
Inspect Sink
```

---

# 32. Console Checks

When analyzing a validation condition, test the behavior independently.

For example:

```javascript
let origin =
    "http://www.normal-website.com.evil.net";

origin.indexOf("normal-website.com");
```

If the result is greater than:

```text
-1
```

the substring exists.

This demonstrates why the check is not equivalent to exact origin comparison.

---

# 33. Burp Suite Workflow

```text
Burp Suite
      ↓
Burp Browser
      ↓
Open Lab
      ↓
HTTP History
      ↓
Inspect JavaScript
      ↓
Find message listener
      ↓
Find event.origin
      ↓
Identify validation
      ↓
Find event.data usage
      ↓
Find sink
      ↓
Build authorized exploit
      ↓
Confirm impact
```

---

# 34. DOM Invader

Use DOM Invader when available to help identify:

```text
Web Message Sources
Message Event Handlers
DOM Sinks
Taint Flow
```

Your notes describe DOM Invader as a way to automate taint tracking between sources and sinks, especially useful for minified or obfuscated JavaScript. :contentReference[oaicite:8]{index=8}

---

# 35. Testing Methodology

```text
START
  ↓
Find message listener
  ↓
Identify event.origin
  ↓
Identify validation
  ↓
Determine exact validation semantics
  ↓
Identify event.data
  ↓
Find sink
  ↓
Determine attacker control
  ↓
Construct controlled origin
  ↓
Bypass flawed validation
  ↓
Send controlled message
  ↓
Confirm source → sink flow
  ↓
Assess impact
```

---

# 36. Common Mistakes

## Mistake 1 — Assuming `event.origin` Exists Means Secure

The application may read:

```javascript
event.origin
```

but validate it incorrectly.

---

## Mistake 2 — Trusting `indexOf()`

```javascript
origin.indexOf("trusted")
```

is a substring search.

It is not an exact origin comparison.

---

## Mistake 3 — Trusting `startsWith()`

```javascript
origin.startsWith("https://trusted.example")
```

may accept:

```text
https://trusted.example.evil.net
```

depending on the exact validation.

---

## Mistake 4 — Trusting `endsWith()`

```javascript
origin.endsWith("trusted.example")
```

may accept an attacker-controlled host whose name happens to end with the trusted string.

---

## Mistake 5 — Ignoring the Sink

An origin validation flaw becomes security-relevant when attacker-controlled message data can reach a dangerous operation.

Always trace:

```text
Origin
  ↓
Message
  ↓
Data
  ↓
Sink
```

---

# 37. Secure Implementation

A safer basic pattern is:

```javascript
window.addEventListener('message', function(event) {

    if (event.origin !== 'https://trusted.example') {
        return;
    }

    // Validate message structure.
    // Validate expected values.
    // Process data safely.
});
```

The key principles are:

```text
Exact Origin
+
Expected Message Structure
+
Safe Sink
```

---

# 38. Defense Checklist

```text
☐ Use exact origin comparison
☐ Validate event.origin
☐ Validate event.data
☐ Validate message structure
☐ Allow only expected message types
☐ Allow only expected values
☐ Avoid eval()
☐ Avoid unsafe HTML sinks
☐ Validate URLs before navigation
☐ Avoid javascript: URLs
☐ Use safe DOM APIs
```

---

# 39. Lab Write-Up Template

```markdown
# Lab 04 — Web Message Origin Validation

## Objective

Identify and bypass flawed origin validation in a Web Message handler.

## Message Source

```text
postMessage()
```

## Receiver

```text
message event
```

## Origin

```text
event.origin
```

## Validation

```javascript
[insert vulnerable validation]
```

## Message Data

```text
event.data
```

## Sink

```text
[insert sink]
```

## Validation Bypass

```text
[insert authorized lab origin]
```

## Taint Flow

```text
Attacker Origin
      ↓
postMessage()
      ↓
event.origin
      ↓
Flawed Validation
      ↓
event.data
      ↓
Sink
      ↓
Security Impact
```

## Result

[Describe the confirmed lab behavior.]

## Key Lesson

Never treat substring-based origin checks as equivalent to exact origin validation.
```

---

# 40. Quick Revision

## Dangerous Checks

```javascript
origin.indexOf("trusted")
```

```javascript
origin.includes("trusted")
```

```javascript
origin.startsWith("trusted")
```

```javascript
origin.endsWith("trusted")
```

---

## Preferred Concept

```javascript
event.origin === "https://trusted.example"
```

---

# 41. One-Line Mental Model

```text
event.origin → flawed string validation → attacker origin accepted → event.data → dangerous sink
```

---

# 42. Master Checklist

```text
☐ Message listener found
☐ event.origin identified
☐ Origin validation identified
☐ Validation function understood
☐ Exact origin requirement understood
☐ indexOf() checked
☐ includes() checked
☐ startsWith() checked
☐ endsWith() checked
☐ Regex checked
☐ event.data identified
☐ Message structure identified
☐ Sink identified
☐ Attacker origin controlled
☐ Validation bypass confirmed
☐ Message delivered
☐ Source → sink flow confirmed
☐ Security impact confirmed
☐ Evidence captured
☐ Remediation documented
```

---

# 43. Final Mental Model

```text
                 ATTACKER
                    ↓
            ATTACKER ORIGIN
                    ↓
               postMessage()
                    ↓
              MESSAGE EVENT
                    ↓
              event.origin
                    ↓
          ┌──────────────────┐
          │ FLAWED VALIDATION │
          │                  │
          │ indexOf()        │
          │ includes()       │
          │ startsWith()     │
          │ endsWith()       │
          └────────┬─────────┘
                   ↓
             VALIDATION PASS
                   ↓
               event.data
                   ↓
             APPLICATION
                 LOGIC
                   ↓
                 SINK
                   ↓
            SECURITY IMPACT
```

---

# Final Rule

```text
UNTRUSTED WEB MESSAGE
        +
IMPROPER ORIGIN VALIDATION
        +
ATTACKER-CONTROLLED MESSAGE DATA
        +
SECURITY-SENSITIVE SINK
        =
WEB MESSAGE VULNERABILITY
```

And the most important rule to remember:

```text
STRING MATCHING
      ≠
EXACT ORIGIN VALIDATION
```