# DOM-Based Vulnerabilities — JavaScript Injection

## 1. Overview

JavaScript injection occurs when attacker-controlled data reaches a JavaScript execution sink and is interpreted as executable JavaScript.

The core taint-flow model is:

```text
Attacker-Controlled Source
        ↓
Client-Side JavaScript
        ↓
JavaScript Execution Sink
        ↓
JavaScript Execution
        ↓
Security Impact
```

A common JavaScript injection sink is:

```javascript
eval()
```

Other potentially dangerous execution sinks include:

```text
setTimeout()
setInterval()
Function()
```

The vulnerability depends on attacker-controlled data reaching the sink in an executable context.

---

## 2. JavaScript Injection vs DOM XSS

DOM XSS is a broad category of client-side vulnerabilities.

JavaScript injection is specifically concerned with attacker-controlled data being interpreted as JavaScript.

Conceptually:

```text
DOM-Based Vulnerabilities
        ↓
Source → Sink
        ↓
JavaScript Injection
        ↓
JavaScript Execution
```

The important question is:

```text
Can attacker-controlled data reach a JavaScript execution sink?
```

---

## 3. What Is a JavaScript Execution Sink?

A JavaScript execution sink is a function or operation that interprets supplied data as JavaScript.

Important examples include:

```javascript
eval()
```

```javascript
setTimeout()
```

```javascript
setInterval()
```

```javascript
Function()
```

These should be carefully reviewed when they receive data from an untrusted source.

---

## 4. `eval()`

The `eval()` function evaluates a string as JavaScript.

Example:

```javascript
eval(value);
```

The source-to-sink flow is:

```text
Attacker-Controlled Source
        ↓
value
        ↓
eval()
        ↓
JavaScript Execution
```

If an attacker can control the value passed to `eval()`, investigate for JavaScript injection.

---

## 5. Basic Vulnerable Pattern

Consider:

```javascript
const code = location.hash.slice(1);

eval(code);
```

The flow is:

```text
URL Fragment
      ↓
location.hash
      ↓
slice(1)
      ↓
code
      ↓
eval()
      ↓
JavaScript Execution
```

The fragment is attacker-controlled because an attacker can construct a URL containing a chosen fragment.

---

## 6. URL Fragment as a Source

A common source is:

```javascript
location.hash
```

Example:

```text
https://example.com/page#INPUT
```

Client-side JavaScript can access:

```javascript
location.hash
```

The flow becomes:

```text
URL Fragment
      ↓
location.hash
      ↓
JavaScript
      ↓
Execution Sink
```

---

## 7. URL Query String as a Source

Another potential source is:

```javascript
location.search
```

Example:

```text
https://example.com/page?code=INPUT
```

The application may extract:

```text
code
```

and pass it to JavaScript processing.

Conceptual flow:

```text
Query Parameter
      ↓
location.search
      ↓
JavaScript Variable
      ↓
Execution Sink
```

---

## 8. `setTimeout()`

`setTimeout()` can be dangerous when its argument is treated as executable code.

Example:

```javascript
setTimeout(value);
```

When analyzing legacy or unsafe code, determine whether attacker-controlled data reaches an execution-capable form of the API.

The flow is:

```text
Attacker Input
      ↓
JavaScript
      ↓
setTimeout()
      ↓
Potential JavaScript Execution
```

Prefer modern callback-based usage rather than evaluating strings as code.

---

## 9. `setInterval()`

Similarly:

```javascript
setInterval(value);
```

should be reviewed when the argument is derived from an untrusted source.

Conceptual flow:

```text
Attacker Input
      ↓
JavaScript
      ↓
setInterval()
      ↓
Potential JavaScript Execution
```

---

## 10. `Function()`

The `Function()` constructor can create executable JavaScript from a string.

Example:

```javascript
const fn = Function(value);
```

Potential flow:

```text
Attacker-Controlled Data
        ↓
Function()
        ↓
Generated Function
        ↓
JavaScript Execution
```

This should be treated as a dangerous execution sink when its input is attacker-controlled.

---

## 11. Source → Sink Analysis

The most important testing technique is to trace the complete data flow.

```text
SOURCE
  ↓
ATTACKER CONTROL
  ↓
VARIABLE
  ↓
FUNCTION
  ↓
PROCESSING
  ↓
EXECUTION SINK
  ↓
JAVASCRIPT EXECUTION
```

Finding only:

```text
location.hash
```

does not prove a vulnerability.

Finding only:

```text
eval()
```

does not prove a vulnerability.

The complete flow must be established.

---

## 12. Example Source-to-Sink Chain

Consider:

```javascript
const input = location.hash.slice(1);

eval(input);
```

The complete chain is:

```text
location.hash
      ↓
slice(1)
      ↓
input
      ↓
eval(input)
      ↓
JavaScript Execution
```

This is the fundamental JavaScript injection pattern.

---

## 13. Multiple Processing Steps

Real applications may process the input several times.

Example:

```text
Source
  ↓
decodeURIComponent()
  ↓
replace()
  ↓
Variable
  ↓
Function()
```

Therefore, testing should follow every transformation.

The important question is:

```text
What exact value reaches the execution sink?
```

---

## 14. Encoding and Decoding

Encoding can change the value received by JavaScript.

For example:

```text
Encoded Input
      ↓
decodeURIComponent()
      ↓
Decoded Input
      ↓
Execution Sink
```

When analyzing a potential vulnerability, determine whether the application:

```text
Encodes
Decodes
Escapes
Normalizes
Replaces
Filters
```

the input before it reaches the sink.

---

## 15. Why Transformations Matter

Suppose an application performs:

```javascript
const input = decodeURIComponent(location.hash.slice(1));
eval(input);
```

The flow is:

```text
URL Fragment
      ↓
location.hash
      ↓
slice(1)
      ↓
decodeURIComponent()
      ↓
eval()
```

A payload that appears encoded in the URL may become executable after decoding.

---

## 16. Testing Methodology

### Step 1 — Identify Sources

Search for:

```text
location.search
location.hash
location.pathname
document.URL
document.location
document.referrer
window.name
event.data
```

---

### Step 2 — Identify Execution Sinks

Search for:

```text
eval
setTimeout
setInterval
Function
```

---

### Step 3 — Trace the Data

Determine:

```text
Where does the value originate?
        ↓
Where is it stored?
        ↓
How is it transformed?
        ↓
Where is it passed?
        ↓
Does it reach an execution sink?
```

---

### Step 4 — Determine Context

Establish whether the value is:

```text
Directly executed
Decoded before execution
Concatenated into JavaScript
Passed into a generated function
Used in another executable context
```

---

### Step 5 — Confirm Behavior

Use an authorized lab or testing environment to confirm whether attacker-controlled input can cause the intended JavaScript behavior.

---

## 17. DevTools Workflow

```text
Open DevTools
      ↓
Sources
      ↓
Ctrl + Shift + F
      ↓
Search for execution sinks
      ↓
Find eval / Function / timers
      ↓
Trace input backwards
      ↓
Identify source
      ↓
Set breakpoint
      ↓
Trigger source
      ↓
Inspect value
      ↓
Confirm execution behavior
```

---

## 18. Search Terms

Useful JavaScript searches include:

```text
eval(
setTimeout(
setInterval(
Function(
location.search
location.hash
location.pathname
document.URL
document.location
document.referrer
window.name
event.data
decodeURIComponent
decodeURI
```

These searches can quickly reveal potential source-to-sink relationships.

---

## 19. Browser Debugger

When a sink is identified, place a breakpoint immediately before the dangerous operation.

For example:

```javascript
eval(input);
```

Pause execution and inspect:

```text
input
```

Determine:

```text
What is the exact value?
Where did it come from?
What transformations were applied?
```

---

## 20. Taint Tracking

The value may change variable names during execution.

Example:

```javascript
const a = location.hash;
const b = a.slice(1);
const c = decodeURIComponent(b);

eval(c);
```

The flow is:

```text
location.hash
      ↓
a
      ↓
b
      ↓
c
      ↓
eval()
```

The tester must follow the value rather than relying only on variable names.

---

## 21. DOM Invader

Burp's browser includes DOM Invader, which can assist with identifying DOM-based source-to-sink flows.

It can help with:

```text
Source Identification
Taint Tracking
Sink Identification
```

It is particularly useful for:

```text
Minified JavaScript
Large Applications
Complex Client-Side Code
Obfuscated Code
```

Manual verification remains important.

---

## 22. JavaScript Injection Through Web Messages

Web Messages can also provide attacker-controlled JavaScript.

Conceptual flow:

```text
Attacker-Controlled Window
        ↓
postMessage()
        ↓
event.data
        ↓
eval()
        ↓
JavaScript Execution
```

For example:

```javascript
window.addEventListener('message', function(event) {
    eval(event.data);
});
```

The message data is therefore the source, while `eval()` is the sink.

---

## 23. Web Message Origin Validation

When a Web Message reaches an execution sink, inspect:

```javascript
event.origin
```

A potentially dangerous pattern is:

```javascript
window.addEventListener('message', function(event) {
    eval(event.data);
});
```

with no origin validation.

The flow becomes:

```text
Attacker Origin
      ↓
postMessage()
      ↓
event.data
      ↓
eval()
      ↓
JavaScript Execution
```

Origin validation should be considered as part of the security analysis.

---

## 24. JavaScript URL as an Execution Context

A URL-related operation may also become a JavaScript execution path when an application allows attacker-controlled data to become a JavaScript URL.

Conceptually:

```text
Attacker Input
      ↓
URL Processing
      ↓
URL Sink
      ↓
JavaScript URL
      ↓
JavaScript Execution
```

This should be analyzed separately from direct `eval()`-based injection.

---

## 25. jQuery and JavaScript Execution

Some client-side libraries may transform or process attacker-controlled values in ways that eventually lead to execution.

When reviewing JavaScript-heavy applications, do not restrict searches to:

```text
eval()
```

Also inspect:

```text
jQuery
DOM APIs
URL APIs
Event Handlers
Dynamic Script Creation
```

Trace the actual data flow.

---

## 26. JavaScript Injection vs HTML Injection

These are different execution paths.

### HTML Injection

```text
Attacker Input
      ↓
HTML Sink
      ↓
HTML Parsing
      ↓
Potential JavaScript Execution
```

### JavaScript Injection

```text
Attacker Input
      ↓
JavaScript Processing
      ↓
JavaScript Execution Sink
      ↓
JavaScript Execution
```

The sink and context determine which technique is relevant.

---

## 27. JavaScript Injection vs DOM XSS

DOM XSS is the broader vulnerability category.

JavaScript injection can be one mechanism that produces DOM XSS.

Conceptually:

```text
DOM Vulnerability
      ↓
Source → Sink
      ↓
JavaScript Execution
      ↓
DOM XSS
```

The terminology depends on the exact source-to-sink flow.

---

## 28. Common Mistakes

### Mistake 1 — Finding `eval()` and Stopping

The presence of:

```javascript
eval()
```

does not automatically prove a vulnerability.

You must determine:

```text
Can attacker-controlled data reach it?
```

---

### Mistake 2 — Ignoring Data Transformations

Always inspect:

```text
decodeURIComponent()
replace()
substring()
slice()
JSON.parse()
```

and other processing functions.

---

### Mistake 3 — Testing Only One Source

Check multiple browser-controlled sources:

```text
location.search
location.hash
document.referrer
window.name
event.data
```

---

### Mistake 4 — Ignoring Framework Code

Large applications may route data through:

```text
Frameworks
Libraries
Utility Functions
Custom Wrappers
```

Follow the data through these layers.

---

### Mistake 5 — Assuming Encoded Input Is Safe

Encoded input may later be decoded.

Always inspect the value immediately before the sink.

---

## 29. Testing Questions

Ask:

```text
1. What is the source?
2. Can I control it?
3. What exact value enters JavaScript?
4. Is the value decoded?
5. Is it transformed?
6. Is it concatenated?
7. Does it reach eval()?
8. Does it reach Function()?
9. Does it reach setTimeout()?
10. Does it reach setInterval()?
11. Is there another execution sink?
12. Does JavaScript execute?
13. What security impact results?
```

---

## 30. Evidence Collection

Capture:

```text
☐ Source
☐ Attacker-controlled input
☐ JavaScript processing
☐ Variable/value at sink
☐ Execution sink
☐ Browser behavior
☐ Reproduction steps
☐ Security impact
```

The strongest evidence shows:

```text
Attacker Input
      ↓
Source
      ↓
Propagation
      ↓
Execution Sink
      ↓
JavaScript Execution
```

---

## 31. Reporting Structure

A report should contain:

```text
Title
Affected Functionality
Source
Sink
Data Flow
Reproduction Steps
Proof of Concept
Observed Behavior
Security Impact
Remediation
```

Example:

```text
URL Fragment
      ↓
location.hash
      ↓
decodeURIComponent()
      ↓
eval()
      ↓
JavaScript Execution
```

---

## 32. Remediation

General defensive principles include:

```text
☐ Avoid eval()
☐ Avoid dynamically evaluating strings as JavaScript
☐ Avoid string-based setTimeout()
☐ Avoid string-based setInterval()
☐ Avoid Function() with untrusted data
☐ Validate untrusted input
☐ Use allowlists where appropriate
☐ Use safe APIs that do not interpret strings as code
☐ Validate Web Message origins
☐ Validate Web Message data
```

The safest approach is generally to avoid dynamically executing untrusted data altogether.

---

## 33. Quick Reference

### Sources

```text
location.search
location.hash
location.pathname
document.URL
document.location
document.referrer
window.name
event.data
```

### Execution Sinks

```text
eval()
setTimeout()
setInterval()
Function()
```

### Useful Transformations to Review

```text
decodeURIComponent()
decodeURI()
replace()
slice()
substring()
JSON.parse()
```

---

## 34. Complete Testing Workflow

```text
START
  ↓
Identify Client-Side JavaScript
  ↓
Find Sources
  ↓
Find Execution Sinks
  ↓
Confirm Attacker Control
  ↓
Trace Data Flow
  ↓
Identify Transformations
  ↓
Inspect Value at Sink
  ↓
Determine Execution Context
  ↓
Confirm JavaScript Execution
  ↓
Assess Security Impact
  ↓
Document Finding
```

---

## 35. Final Checklist

```text
☐ Client-side JavaScript identified
☐ Sources identified
☐ Attacker control confirmed
☐ eval() searched
☐ setTimeout() searched
☐ setInterval() searched
☐ Function() searched
☐ Web Message handlers checked
☐ event.origin checked
☐ event.data checked
☐ Data transformations identified
☐ Decoding identified
☐ Sink identified
☐ Exact value at sink inspected
☐ JavaScript execution confirmed
☐ Security impact confirmed
☐ Evidence captured
☐ Remediation documented
```

---

# Final Mental Model

```text
ATTACKER-CONTROLLED SOURCE
          ↓
CLIENT-SIDE JAVASCRIPT
          ↓
DATA PROPAGATION
          ↓
TRANSFORMATION / DECODING
          ↓
JAVASCRIPT EXECUTION SINK
          ↓
JAVASCRIPT EXECUTION
          ↓
SECURITY IMPACT
```

---

# Final Rule

```text
SOURCE
  +
ATTACKER CONTROL
  +
DATA PROPAGATION
  +
EXECUTION SINK
  +
UNSAFE INTERPRETATION
  +
REPRODUCIBLE JAVASCRIPT EXECUTION
  +
SECURITY IMPACT
  =
CONFIRMED JAVASCRIPT INJECTION
```