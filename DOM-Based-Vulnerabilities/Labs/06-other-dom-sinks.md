# Lab 06 — Other DOM-Based Sinks

## 1. Overview

Not every DOM-based vulnerability ends in:

```text
innerHTML
document.write()
location.href
document.cookie
```

Client-side JavaScript exposes many other operations that can become security-sensitive when attacker-controlled data reaches them.

The general model remains:

```text
Attacker-Controlled Source
        ↓
JavaScript Processing
        ↓
Other DOM / Browser Sink
        ↓
Browser Behavior
        ↓
Security Impact
```

The key rule is:

```text
SOURCE → TRACE DATA → SINK → OBSERVE BEHAVIOR → ASSESS IMPACT
```

Your source material lists several additional sink categories, including:

```text
eval()
document.domain
WebSocket()
element.src
postMessage()
setRequestHeader()
FileReader.readAsText()
ExecuteSql()
sessionStorage.setItem()
document.evaluate()
JSON.parse()
element.setAttribute()
RegExp()
```

:contentReference[oaicite:1]{index=1}

---

# 2. Important Principle

A sink is not automatically a vulnerability.

For example:

```javascript
JSON.parse(value);
```

does not automatically mean:

```text
JSON Injection
```

Likewise:

```javascript
new WebSocket(url);
```

does not automatically mean:

```text
WebSocket Vulnerability
```

You must establish:

```text
Source
  ↓
Attacker Control
  ↓
Data Flow
  ↓
Sink
  ↓
Unsafe Behavior
  ↓
Security Impact
```

Your source material explicitly emphasizes that finding a source and sink alone does not prove a vulnerability. :contentReference[oaicite:2]{index=2}

---

# 3. Sink Categories

The additional sink categories covered here are:

```text
1. JavaScript injection
2. Document-domain manipulation
3. WebSocket URL poisoning
4. Link manipulation
5. Web Message manipulation
6. Ajax request-header manipulation
7. Local file-path manipulation
8. Client-side SQL injection
9. HTML5 storage manipulation
10. Client-side XPath injection
11. Client-side JSON injection
12. DOM-data manipulation
13. Denial of service
```

---

# 4. JavaScript Injection — `eval()`

## Concept

The JavaScript execution sink:

```javascript
eval()
```

can become dangerous when attacker-controlled data reaches it.

Basic model:

```text
Attacker Input
      ↓
JavaScript Variable
      ↓
eval()
      ↓
JavaScript Execution
```

---

## Vulnerable Pattern

```javascript
eval(value);
```

If:

```text
value
```

is attacker-controlled, investigate the data flow.

---

## Testing

Search JavaScript for:

```text
eval(
```

Then trace backwards:

```text
eval()
  ↑
variable
  ↑
function
  ↑
source
```

Determine:

```text
Can attacker control the value?
Is the value transformed?
Is it validated?
Does it reach eval()?
```

---

## Important Testing Characters

When analyzing escaping around `eval()`, pay attention to:

```text
"
'
\
```

Your supplied notes specifically highlight these characters when testing JavaScript escaping around `eval()`. :contentReference[oaicite:3]{index=3}

---

# 5. Document-Domain Manipulation

## Sink

```javascript
document.domain
```

Historically, pages could modify:

```javascript
document.domain
```

to change the document's effective scripting domain.

The important testing question is:

```text
Can attacker-controlled data influence document.domain?
```

---

## Testing Flow

```text
Attacker-Controlled Source
        ↓
JavaScript
        ↓
document.domain
        ↓
Browser Origin / Domain Behavior
        ↓
Potential Security Impact
```

---

## Search Strategy

Search JavaScript for:

```text
document.domain
```

Especially:

```javascript
document.domain = value;
```

Then trace:

```text
value
  ↓
source
```

---

# 6. WebSocket URL Poisoning

## Sink

```javascript
new WebSocket(url)
```

The WebSocket constructor can become security-sensitive when its URL is attacker-controlled.

---

## Basic Flow

```text
Attacker-Controlled Source
        ↓
URL Construction
        ↓
WebSocket(url)
        ↓
Browser Connection
```

---

## Testing Questions

Ask:

```text
Where does the WebSocket URL come from?
Can attacker control it?
Which URL components are controllable?
Is the scheme validated?
Is the hostname validated?
Is the port controlled?
```

---

## Search Strategy

Search JavaScript for:

```text
new WebSocket(
```

and:

```text
WebSocket(
```

Then trace the URL argument backwards.

---

## Taint Flow

```text
location.search
      ↓
url
      ↓
new WebSocket(url)
      ↓
WebSocket Connection
```

The vulnerability depends on the resulting browser behavior and whether an attacker can meaningfully influence the destination.

---

# 7. Link Manipulation

## Sink

A DOM element's:

```javascript
element.src
```

can be security-sensitive when attacker-controlled data determines a resource URL.

Other related properties may include:

```text
href
src
action
```

---

## Basic Flow

```text
Attacker Input
      ↓
JavaScript
      ↓
element.src
      ↓
Resource Loading
```

---

## Testing

Search JavaScript for:

```text
.src =
.href =
.action =
```

Then determine:

```text
Where does the value come from?
What resource does the browser load?
Can the attacker control the destination?
```

---

# 8. Web Message Manipulation

## Sink / Mechanism

Web Messages use:

```javascript
postMessage()
```

The receiver processes:

```javascript
event.data
```

The security model is:

```text
Attacker-Controlled Window
      ↓
postMessage()
      ↓
event.data
      ↓
Application Logic
      ↓
Security-Sensitive Operation
```

---

## Testing

Search for:

```text
postMessage
addEventListener('message'
onmessage
event.data
event.origin
```

Review both:

```text
Origin Validation
Data Validation
```

Your source material specifically describes Web Message data as a potential source and requires origin and data analysis. :contentReference[oaicite:4]{index=4}

---

# 9. Ajax Request-Header Manipulation

## Sink

JavaScript can modify HTTP request headers using mechanisms such as:

```javascript
setRequestHeader()
```

The relevant sink from your source material is:

```text
setRequestHeader()
```

:contentReference[oaicite:5]{index=5}

---

## Flow

```text
Attacker-Controlled Input
        ↓
JavaScript
        ↓
setRequestHeader()
        ↓
HTTP Request
        ↓
Server
        ↓
Application Behavior
```

---

## Testing

Search for:

```text
setRequestHeader(
```

Then inspect:

```text
Header Name
Header Value
Source
Validation
Server-Side Consumption
```

The security impact depends on what the server does with the manipulated header.

---

# 10. Local File-Path Manipulation

## Sink

The source material identifies:

```javascript
FileReader.readAsText()
```

as a relevant sink. :contentReference[oaicite:6]{index=6}

---

## Basic Flow

```text
Attacker-Controlled Path
        ↓
JavaScript
        ↓
FileReader
        ↓
Local File Operation
```

---

## Testing

Search for:

```text
FileReader
readAsText
```

Then determine:

```text
Can the attacker control the file/path reference?
Does the browser permit the requested operation?
What data is returned?
Where does the result go?
```

Do not assume that a file-related API automatically allows arbitrary local-file access.

---

# 11. Client-Side SQL Injection

## Sink

The supplied source material lists:

```text
ExecuteSql()
```

as a client-side SQL injection sink. :contentReference[oaicite:7]{index=7}

---

## Flow

```text
Attacker Input
      ↓
Client-Side Variable
      ↓
SQL Construction
      ↓
ExecuteSql()
      ↓
Database Operation
```

---

## Testing

Search application code for:

```text
ExecuteSql
SQL
query
execute
```

Trace:

```text
Input
  ↓
SQL Query Construction
  ↓
ExecuteSql()
```

Determine whether attacker-controlled data changes the resulting query.

---

# 12. HTML5 Storage Manipulation

## Sink

The source material identifies:

```javascript
sessionStorage.setItem()
```

as a relevant sink. :contentReference[oaicite:8]{index=8}

Other client-side storage mechanisms include:

```text
localStorage
sessionStorage
IndexedDB
```

---

## Basic Flow

```text
Attacker-Controlled Input
        ↓
JavaScript
        ↓
sessionStorage.setItem()
        ↓
Stored Client-Side State
        ↓
Application Reads Value
        ↓
Security Impact
```

---

## Important Principle

Writing to storage is not automatically a vulnerability.

Find the consumer:

```text
Storage
   ↓
Application
   ↓
Security-Sensitive Operation
```

---

## Testing Questions

```text
What value is stored?
Can attacker control it?
Where is it later read?
Is it trusted?
Does it reach a dangerous sink?
```

---

# 13. Client-Side XPath Injection

## Sink

The supplied material identifies:

```javascript
document.evaluate()
```

as a client-side XPath injection sink. :contentReference[oaicite:9]{index=9}

---

## Flow

```text
Attacker Input
      ↓
XPath Construction
      ↓
document.evaluate()
      ↓
DOM Query
      ↓
Unexpected Result
```

---

## Testing

Search for:

```text
document.evaluate(
```

Then inspect:

```text
XPath String
Input Variables
Concatenation
Escaping
Validation
```

Determine whether attacker-controlled data can modify the XPath expression.

---

# 14. Client-Side JSON Injection

## Sink

The source material identifies:

```javascript
JSON.parse()
```

as a relevant sink category. :contentReference[oaicite:10]{index=10}

---

## Important Distinction

`JSON.parse()` is primarily a parser.

Therefore:

```text
JSON.parse()
      ≠
Automatic Code Execution
```

The security impact depends on what the parsed object is subsequently used for.

---

## Flow

```text
Attacker-Controlled JSON
        ↓
JSON.parse()
        ↓
JavaScript Object
        ↓
Application Logic
        ↓
Security-Sensitive Sink
```

---

## Testing

Search for:

```text
JSON.parse(
```

Then trace:

```text
Input
  ↓
JSON.parse()
  ↓
Parsed Property
  ↓
Sink
```

---

# 15. DOM-Data Manipulation

## Sink

The supplied source material identifies:

```javascript
element.setAttribute()
```

as a relevant sink. :contentReference[oaicite:11]{index=11}

---

## Basic Flow

```text
Attacker Input
      ↓
JavaScript
      ↓
setAttribute()
      ↓
DOM Attribute
      ↓
Browser Behavior
```

---

## Important Attributes

Pay attention to security-sensitive attributes such as:

```text
src
href
action
style
on*
```

The exact impact depends on:

```text
Attribute
Value
Browser Behavior
Application Context
```

---

## Testing

Search for:

```text
setAttribute(
```

Then determine:

```text
Which element?
Which attribute?
Which value?
Where does the value originate?
```

---

# 16. Denial of Service — `RegExp()`

## Sink

The supplied material identifies:

```javascript
RegExp()
```

as a possible denial-of-service sink. :contentReference[oaicite:12]{index=12}

---

## Basic Flow

```text
Attacker-Controlled Input
        ↓
Regular Expression Construction
        ↓
RegExp()
        ↓
Pattern Processing
        ↓
Excessive Resource Consumption
```

---

## Testing

Search for:

```text
new RegExp(
RegExp(
```

Determine whether attacker-controlled input influences the regular expression.

Then assess:

```text
Pattern Complexity
Input Length
Execution Time
Resource Consumption
```

Only classify the issue as a denial-of-service vulnerability when meaningful impact is demonstrated.

---

# 17. Generic Other-Sink Testing Workflow

Use this methodology whenever you discover an unfamiliar client-side sink.

```text
START
  ↓
Find Sink
  ↓
Identify Sink Argument
  ↓
Trace Argument Backwards
  ↓
Find Source
  ↓
Confirm Attacker Control
  ↓
Identify Transformations
  ↓
Identify Validation
  ↓
Determine Browser/API Behavior
  ↓
Determine Security Impact
```

---

# 18. DevTools Workflow

```text
DevTools
   ↓
Sources
   ↓
Ctrl + Shift + F
   ↓
Search Sink
   ↓
Find Sink Usage
   ↓
Set Breakpoint
   ↓
Trigger Functionality
   ↓
Inspect Arguments
   ↓
Trace Backwards
   ↓
Identify Source
   ↓
Observe Result
```

Your source material recommends using DevTools to inspect JavaScript, search sources and sinks, set breakpoints, trigger inputs, and observe the resulting data. :contentReference[oaicite:13]{index=13}

---

# 19. Burp Suite Workflow

```text
Burp Suite
      ↓
Proxy
      ↓
HTTP History
      ↓
Identify Relevant Pages
      ↓
Identify Parameters
      ↓
Open in Browser
      ↓
Inspect JavaScript
      ↓
Find Source
      ↓
Find Sink
      ↓
Trace Source → Sink
```

This follows the source material's recommended Burp workflow. :contentReference[oaicite:14]{index=14}

---

# 20. DOM Invader

Use DOM Invader to assist with:

```text
Source Discovery
Sink Discovery
Taint Tracking
```

The source material describes DOM Invader as particularly useful for automating taint tracking and analyzing minified or obfuscated JavaScript. :contentReference[oaicite:15]{index=15}

Use it as a discovery aid.

Always manually confirm:

```text
Source
Propagation
Sink
Impact
```

---

# 21. Source-to-Sink Tracing

The practical process is:

```text
Find Source
    ↓
Find Variable
    ↓
Follow Data
    ↓
Follow Function Calls
    ↓
Find Sink
    ↓
Determine Browser Behavior
```

This is the core methodology from your notes. :contentReference[oaicite:16]{index=16}

---

# 22. Example — WebSocket

```text
location.search
      ↓
url
      ↓
validate()
      ↓
new WebSocket(url)
      ↓
Browser Connection
```

Questions:

```text
☐ Is location.search attacker-controlled?
☐ Is url derived from it?
☐ Does validation actually restrict the destination?
☐ Does the browser establish the connection?
☐ Is the resulting behavior security-sensitive?
```

---

# 23. Example — Storage

```text
location.hash
      ↓
value
      ↓
sessionStorage.setItem()
      ↓
stored value
      ↓
application reads value
      ↓
dangerous operation
```

Questions:

```text
☐ Can the hash be controlled?
☐ Is the value stored?
☐ Where is it read?
☐ Is it trusted?
☐ Does it reach a security-sensitive sink?
```

---

# 24. Example — `setAttribute()`

```text
location.search
      ↓
url
      ↓
element.setAttribute("src", url)
      ↓
Resource Loading
```

Questions:

```text
☐ Is url attacker-controlled?
☐ Which attribute is modified?
☐ What element receives it?
☐ How does the browser interpret it?
☐ Can the destination be controlled?
```

---

# 25. Example — JSON.parse()

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

The important point is that the parser is only part of the chain.

The security-sensitive behavior occurs when:

```text
data.url
```

reaches:

```text
iframe.src
```

---

# 26. Example — `RegExp()`

```text
location.search
      ↓
pattern
      ↓
new RegExp(pattern)
      ↓
Regular Expression Processing
```

Questions:

```text
☐ Is pattern attacker-controlled?
☐ Can pattern complexity be controlled?
☐ Is execution expensive?
☐ Can repeated requests amplify the effect?
☐ Is measurable resource exhaustion demonstrated?
```

---

# 27. Sink Analysis Table

| Sink | Primary Behavior | What to Trace |
|---|---|---|
| `eval()` | JavaScript execution | Code string |
| `document.domain` | Domain behavior | Assigned value |
| `WebSocket()` | Network connection | URL |
| `element.src` | Resource loading | Source URL |
| `postMessage()` | Cross-window messaging | Message + origin |
| `setRequestHeader()` | HTTP header modification | Header value |
| `FileReader.readAsText()` | File reading | File input |
| `ExecuteSql()` | Database query | Query |
| `sessionStorage.setItem()` | Client-side storage | Stored value |
| `document.evaluate()` | XPath evaluation | XPath expression |
| `JSON.parse()` | JSON parsing | Parsed data |
| `setAttribute()` | DOM attribute manipulation | Attribute + value |
| `RegExp()` | Regular expression processing | Pattern |

The sink categories and examples are derived from the provided DOM-based vulnerability material. :contentReference[oaicite:17]{index=17}

---

# 28. Common Mistakes

## Mistake 1 — Assuming Every Sink Is Exploitable

```text
Sink found
      ≠
Vulnerability confirmed
```

---

## Mistake 2 — Ignoring the Argument

Always identify:

```text
What value reaches the sink?
```

---

## Mistake 3 — Ignoring Validation

The flow may be:

```text
Source
  ↓
Validation
  ↓
Sanitization
  ↓
Sink
```

Determine whether the controls actually prevent dangerous behavior.

Your source material explicitly requires validation and sanitization to be evaluated between source and sink. :contentReference[oaicite:18]{index=18}

---

## Mistake 4 — Ignoring the Consumer

Especially for:

```text
sessionStorage
cookies
WebSocket
JSON
```

follow the value beyond the immediate operation.

---

## Mistake 5 — Reporting Without Impact

A finding should demonstrate:

```text
Attacker Control
      ↓
Data Flow
      ↓
Sink
      ↓
Security-Relevant Behavior
```

---

# 29. Evidence Collection

Record:

```text
☐ Source
☐ Attacker-controlled input
☐ Variable
☐ Transformation
☐ Validation
☐ Sink
☐ Runtime value
☐ Browser/API behavior
☐ Security impact
☐ Reproduction steps
```

---

# 30. Lab Write-Up Template

```markdown
# Lab 06 — Other DOM-Based Sink

## Objective

Identify and demonstrate a security-sensitive data flow involving an additional DOM/browser sink.

## Source

```text
[Source]
```

## Sink

```text
[Sink]
```

## Vulnerable Code

```javascript
[Relevant code]
```

## Data Flow

```text
Source
  ↓
Variable
  ↓
Transformation
  ↓
Validation
  ↓
Sink
  ↓
Browser/API Behavior
  ↓
Impact
```

## Analysis

1. Identify the sink.
2. Identify the sink argument.
3. Trace the argument backwards.
4. Identify the source.
5. Confirm attacker control.
6. Review validation.
7. Observe browser/API behavior.
8. Confirm security impact.

## Result

[Document the confirmed behavior.]

## Key Lesson

A DOM sink must always be analyzed in the context of the data that reaches it and the behavior it causes.
```

---

# 31. Quick Revision — JavaScript Injection

```text
Source
  ↓
JavaScript
  ↓
eval()
  ↓
Execution
```

---

# 32. Quick Revision — WebSocket

```text
Source
  ↓
URL
  ↓
WebSocket()
  ↓
Connection
```

---

# 33. Quick Revision — Storage

```text
Source
  ↓
sessionStorage.setItem()
  ↓
Stored State
  ↓
Consumer
```

---

# 34. Quick Revision — XPath

```text
Source
  ↓
XPath Expression
  ↓
document.evaluate()
  ↓
DOM Query
```

---

# 35. Quick Revision — JSON

```text
Source
  ↓
JSON.parse()
  ↓
Parsed Object
  ↓
Consumer / Sink
```

---

# 36. Quick Revision — DOM Data

```text
Source
  ↓
Attribute / Value
  ↓
setAttribute()
  ↓
Browser Behavior
```

---

# 37. Quick Revision — RegExp

```text
Source
  ↓
Pattern
  ↓
RegExp()
  ↓
Resource Consumption
```

---

# 38. Master Checklist

```text
☐ Sink identified
☐ Sink argument identified
☐ Source identified
☐ Attacker control confirmed
☐ Data flow traced
☐ Function calls traced
☐ Transformations identified
☐ Encoding checked
☐ Decoding checked
☐ Validation checked
☐ Sanitization checked
☐ Browser/API behavior observed
☐ Security-sensitive behavior identified
☐ Impact confirmed
☐ Evidence captured
☐ Finding documented
```

---

# 39. Final Detection Model

```text
                 SOURCE
                    ↓
           CAN ATTACKER CONTROL?
                    ↓
                   YES
                    ↓
               TRACE DATA
                    ↓
             FIND THE SINK
                    ↓
          WHAT DOES IT DO?
                    ↓
         BROWSER / API BEHAVIOR
                    ↓
        IS THE BEHAVIOR DANGEROUS?
                    ↓
                   YES
                    ↓
            SECURITY IMPACT
```

---

# Final Rule

```text
OTHER DOM SINK
      +
ATTACKER-CONTROLLED DATA
      +
UNSAFE DATA FLOW
      +
SECURITY-SENSITIVE BEHAVIOR
      +
CONFIRMED IMPACT
      =
DOM-BASED TAINT-FLOW VULNERABILITY
```

The central principle remains:

```text
SOURCE
  ↓
ATTACKER CONTROL
  ↓
TRACE DATA
  ↓
SINK
  ↓
BROWSER BEHAVIOR
  ↓
SECURITY IMPACT
```

Finding a source or sink alone is **not enough**. The complete source-to-sink flow and resulting security impact must be demonstrated. :contentReference[oaicite:19]{index=19}