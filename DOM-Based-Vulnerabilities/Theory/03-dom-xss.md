# DOM-Based Vulnerabilities — DOM XSS

## 1. Overview

DOM-based Cross-Site Scripting (DOM XSS) occurs when client-side JavaScript takes attacker-controlled data from a source and passes it to a dangerous sink in an unsafe way.

Unlike reflected or stored XSS, the vulnerable processing occurs in the browser through JavaScript.

The core model is:

```text
Attacker-Controlled Source
        ↓
JavaScript Processes Data
        ↓
Dangerous Sink
        ↓
DOM Modification / JavaScript Execution
```

The server does not necessarily need to receive or process the payload.

---

# 2. DOM XSS vs Other XSS

## Reflected XSS

```text
Attacker Input
      ↓
Server
      ↓
HTTP Response
      ↓
Browser
      ↓
JavaScript Execution
```

## Stored XSS

```text
Attacker Input
      ↓
Server
      ↓
Database / Storage
      ↓
Later Response
      ↓
Browser
      ↓
JavaScript Execution
```

## DOM XSS

```text
Attacker Input
      ↓
Browser
      ↓
Client-Side JavaScript
      ↓
Dangerous Sink
      ↓
JavaScript Execution
```

The key difference is that DOM XSS is primarily a **client-side source-to-sink problem**.

---

# 3. Sources

A source is where attacker-controlled data enters client-side JavaScript.

Common sources include:

```text
window.location
location.search
location.hash
location.pathname
document.URL
document.location
document.referrer
window.name
postMessage data
document.cookie
```

---

# 4. URL Sources

## location.search

Contains the query string.

Example:

```text
/search?q=test
```

Conceptual flow:

```text
?q=test
   ↓
location.search
   ↓
JavaScript
   ↓
Sink
```

---

## location.hash

Contains the URL fragment.

Example:

```text
/page#test
```

Conceptual flow:

```text
#test
   ↓
location.hash
   ↓
JavaScript
   ↓
Sink
```

---

## location.pathname

Contains the URL path.

Example:

```text
/products/test
```

Conceptual flow:

```text
URL Path
   ↓
location.pathname
   ↓
JavaScript
   ↓
Sink
```

---

# 5. Other Common Sources

## document.referrer

```javascript
document.referrer
```

Potential flow:

```text
Referring Page
      ↓
document.referrer
      ↓
JavaScript
      ↓
Sink
```

---

## window.name

```javascript
window.name
```

Potential flow:

```text
window.name
      ↓
JavaScript
      ↓
Application Logic
      ↓
Sink
```

---

## postMessage

Web applications can receive data from other windows and frames using Web Messages.

Conceptually:

```text
Attacker-Controlled Window
        ↓
postMessage()
        ↓
message event
        ↓
event.data
        ↓
JavaScript
        ↓
Sink
```

---

# 6. Sinks

A sink is a JavaScript operation where attacker-controlled data can cause a security-sensitive effect.

Important DOM XSS sinks include:

```text
document.write()
document.writeln()
document.domain
element.innerHTML
element.outerHTML
element.insertAdjacentHTML
element.onevent
```

Other JavaScript execution sinks include:

```text
eval()
setTimeout()
setInterval()
Function()
```

URL-related sinks include:

```text
location.href
location.assign()
src attributes
```

jQuery can also contain relevant sinks.

---

# 7. HTML / DOM Sinks

## innerHTML

Example:

```javascript
element.innerHTML = value;
```

Conceptual flow:

```text
Attacker Input
      ↓
JavaScript
      ↓
innerHTML
      ↓
Browser Parses HTML
      ↓
DOM Modification
      ↓
Potential Script Execution
```

---

## outerHTML

Example:

```javascript
element.outerHTML = value;
```

The value can replace the element's HTML representation.

Investigate whether attacker-controlled data can reach the sink.

---

## insertAdjacentHTML

Example:

```javascript
element.insertAdjacentHTML(position, value);
```

This can insert attacker-controlled HTML into the document if the value is not safely handled.

---

## document.write()

Example:

```javascript
document.write(value);
```

Potential flow:

```text
Attacker Input
      ↓
location.search
      ↓
document.write()
      ↓
HTML Added to Document
      ↓
Potential XSS
```

---

# 8. document.writeln()

Another related sink is:

```javascript
document.writeln(value);
```

Analyze it similarly to:

```javascript
document.write()
```

Determine:

```text
Source
  ↓
Data Flow
  ↓
Sink
  ↓
Browser Interpretation
```

---

# 9. Event Handler Sinks

DOM XSS can also occur when attacker-controlled data reaches event-handler properties.

Example:

```javascript
element.onclick = value;
```

Relevant sink category:

```text
element.onevent
```

Determine whether attacker-controlled data can influence the event handler in an executable context.

---

# 10. JavaScript Execution Sinks

Potentially dangerous JavaScript execution sinks include:

```javascript
eval(value);
```

```javascript
setTimeout(value);
```

```javascript
setInterval(value);
```

```javascript
Function(value);
```

Conceptual flow:

```text
Attacker Input
      ↓
JavaScript Processing
      ↓
Execution Sink
      ↓
JavaScript Execution
```

When encountering:

```text
eval()
```

inspect how the input is encoded and escaped before reaching the sink.

---

# 11. jQuery Sinks

The following jQuery functions can be relevant to DOM XSS:

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

The exact security impact depends on how attacker-controlled data reaches the function.

---

# 12. jQuery $() Selector Sink

A classic DOM XSS pattern involves the jQuery `$()` selector.

Example:

```javascript
$(window).on('hashchange', function() {
    var element = $(location.hash);
    element[0].scrollIntoView();
});
```

The source is:

```javascript
location.hash
```

The sink is:

```javascript
$()
```

The flow is:

```text
location.hash
      ↓
Attacker-Controlled Hash
      ↓
$()
      ↓
DOM Processing
      ↓
Potential XSS
```

More recent versions of jQuery have patched this particular vulnerability by preventing HTML injection into selectors when the input begins with `#`.

However, vulnerable code may still exist in real-world applications.

---

# 13. Triggering a Hashchange

A hashchange event can be triggered when the URL fragment changes.

Conceptual example:

```html
<iframe
    src="https://TARGET#"
    onload="this.src+='<img src=1 onerror=alert(1)>'">
</iframe>
```

The general concept is:

```text
Load Vulnerable Page
      ↓
Change Hash
      ↓
hashchange Event
      ↓
Vulnerable Handler
      ↓
$()
      ↓
Potential XSS
```

The exact technique depends on the vulnerable application and browser behavior.

---

# 14. DOM XSS in AngularJS

Frameworks can introduce their own DOM XSS patterns.

For AngularJS applications using:

```html
ng-app
```

AngularJS processes expressions inside:

```text
{{ }}
```

For example:

```text
{{7*7}}
```

If the expression evaluates:

```text
49
```

this indicates that AngularJS is processing the expression.

---

# 15. AngularJS Expression Injection

When angle brackets are HTML-encoded, an AngularJS expression may provide another client-side execution path in an affected application.

Conceptual flow:

```text
Attacker Input
      ↓
AngularJS Expression
      ↓
AngularJS Processing
      ↓
JavaScript Execution
```

The material's lab demonstrates an AngularJS expression-based DOM XSS technique.

---

# 16. DOM XSS Testing Methodology

## Step 1 — Identify a Potential Source

Start with a controllable value.

Example:

```text
/search?q=xss1337test
```

Use a unique alphanumeric marker:

```text
xss1337test
```

---

## Step 2 — Inject the Marker

Example:

```text
?q=xss1337test
```

The purpose is to determine where the value appears.

---

## Step 3 — Inspect the Live DOM

Use browser DevTools:

```text
DevTools
   ↓
Elements
   ↓
Ctrl + F
   ↓
Search xss1337test
```

Do not rely only on:

```text
View Source
```

because DOM XSS may modify the page after the original HTML has been loaded.

---

# 17. Why View Source Can Be Misleading

View Source shows the original HTML returned by the server.

DOM XSS often happens after JavaScript modifies the DOM.

Therefore:

```text
View Source
    ≠
Live DOM
```

For DOM-based testing, inspect:

```text
DevTools → Elements
```

to see the current DOM.

---

# 18. Identify the Context

After locating the marker, determine where it appears.

Possible contexts include:

```text
HTML text
HTML attribute
Inside a tag
Inside JavaScript
Inside a URL
Inside a JavaScript expression
```

Example:

```html
<img src="xss1337test">
```

The marker is inside:

```text
src attribute
```

The payload must therefore be designed for that specific context.

---

# 19. Context-Based Testing

The general process is:

```text
Inject Marker
      ↓
Find Marker in DOM
      ↓
Identify Context
      ↓
Determine Required Escape
      ↓
Test Appropriate Input
      ↓
Confirm Browser Behavior
```

Do not blindly use the same payload in every context.

---

# 20. Example — document.write + location.search

A vulnerable application may use:

```javascript
document.write(...)
```

with data from:

```javascript
location.search
```

Conceptual flow:

```text
Search Query
      ↓
location.search
      ↓
document.write()
      ↓
DOM
      ↓
Potential XSS
```

A unique marker can first be used to determine exactly where the input is inserted.

---

# 21. Example — innerHTML + location.search

A vulnerable pattern may look conceptually like:

```javascript
let query =
    new URLSearchParams(location.search).get('search');

document.getElementById('searchMessage').innerHTML =
    "You searched for: " + query;
```

Taint flow:

```text
/search?search=ATTACKER_INPUT
              ↓
        location.search
              ↓
   URLSearchParams.get()
              ↓
             query
              ↓
          innerHTML
              ↓
       Browser parses HTML
              ↓
        Potential XSS
```

---

# 22. Why `<script>` Is Not Always the Best Test

When testing an HTML sink, directly inserting:

```html
<script>alert(1)</script>
```

does not necessarily execute in every DOM insertion context.

Alternative HTML elements and event handlers can behave differently when inserted dynamically.

The correct approach is to:

```text
Identify Context
      ↓
Understand Sink
      ↓
Test Appropriate Input
```

---

# 23. DevTools JavaScript Analysis

For JavaScript execution sinks, use DevTools search.

Typical workflow:

```text
DevTools
   ↓
Sources
   ↓
Ctrl + Shift + F
   ↓
Search for source
   ↓
Locate JavaScript
   ↓
Set breakpoint
   ↓
Trigger source
   ↓
Trace value
```

Useful searches:

```text
location.search
location.hash
location.pathname
document.URL
document.referrer
window.name
postMessage
event.data
innerHTML
outerHTML
document.write
eval
setTimeout
setInterval
Function
```

---

# 24. Breakpoints and Taint Tracking

When a source is found:

```text
Set Breakpoint
      ↓
Trigger Source
      ↓
Inspect Variable
      ↓
Follow Assignments
      ↓
Follow Function Calls
      ↓
Find Sink
```

The value may be reassigned several times before reaching the sink.

Therefore, do not assume the source variable is directly passed to the sink.

---

# 25. DOM Invader

DOM Invader is a feature available in Burp's browser that can help automate DOM XSS source-to-sink analysis.

It can assist with:

```text
Source Identification
Taint Tracking
Sink Identification
```

It is particularly useful when JavaScript is:

```text
Minified
Obfuscated
Large
Complex
```

Manual verification should still be performed during testing.

---

# 26. URL Encoding Consideration

When testing:

```text
location.search
```

and:

```text
location.hash
```

be aware of URL encoding behavior.

Modern browsers may encode characters in these URL components before JavaScript reads them.

Conceptually:

```text
< > 
 ↓
%3C %3E
```

This can affect how the application processes attacker input.

Therefore:

```text
Payload Sent
      ≠
Value JavaScript Receives
```

Always inspect the actual value during debugging.

---

# 27. Stored DOM XSS

Not every DOM XSS source is directly supplied by the browser URL.

A stored DOM vulnerability can involve:

```text
Attacker Input
      ↓
Server
      ↓
Storage
      ↓
Later Response
      ↓
Client-Side JavaScript
      ↓
Dangerous Sink
      ↓
XSS
```

For example, a page may contain:

```javascript
element.innerHTML = comment.author;
```

If the stored value is attacker controlled and reaches an unsafe sink, investigate for stored DOM XSS.

---

# 28. Reflected / Stored Data + DOM XSS

Some DOM vulnerabilities combine client-side processing with data that originated from the server.

The important distinction is:

```text
Pure DOM XSS
    ↓
Data originates entirely from client-side source
```

versus:

```text
DOM XSS with Reflected / Stored Data
    ↓
Server-originated data
    ↓
Client-side JavaScript
    ↓
Dangerous Sink
```

The material covers both types of data flow.

---

# 29. DOM XSS and Taint Flow

The most important mental model is:

```text
SOURCE
   ↓
PROPAGATION
   ↓
SINK
```

Expanded:

```text
Attacker Input
      ↓
Source
      ↓
Variable
      ↓
Function
      ↓
Processing
      ↓
Sink
      ↓
Browser Behavior
      ↓
Security Impact
```

---

# 30. Testing Checklist

```text
☐ Identify client-side JavaScript
☐ Identify attacker-controlled sources
☐ Test URL parameters
☐ Test URL fragments
☐ Review document.URL
☐ Review document.location
☐ Review document.referrer
☐ Review window.name
☐ Review postMessage
☐ Review event.data
☐ Search for DOM sinks
☐ Search for JavaScript execution sinks
☐ Search for jQuery sinks
☐ Search for AngularJS expressions
☐ Trace source → propagation → sink
☐ Inspect live DOM
☐ Identify injection context
☐ Review validation and encoding
☐ Confirm browser behavior
☐ Confirm security impact
```

---

# 31. Common Sink Reference

## DOM / HTML

```text
document.write()
document.writeln()
element.innerHTML
element.outerHTML
element.insertAdjacentHTML
element.onevent
```

## JavaScript Execution

```text
eval()
setTimeout()
setInterval()
Function()
```

## URL / Navigation

```text
location.href
location.assign()
src
```

## jQuery

```text
$()
html()
append()
after()
before()
prepend()
replaceWith()
replaceAll()
insertAfter()
insertBefore()
wrap()
wrapInner()
wrapAll()
jQuery.parseHTML()
$.parseHTML()
```

---

# 32. Source Reference

```text
window.location
location.search
location.hash
location.pathname
document.URL
document.location
document.referrer
window.name
postMessage()
event.data
document.cookie
```

---

# 33. Complete DOM XSS Workflow

```text
START
  ↓
Inspect Client-Side JavaScript
  ↓
Identify Sources
  ↓
Identify Sinks
  ↓
Inject Unique Marker
  ↓
Find Marker in Live DOM / JavaScript
  ↓
Identify Context
  ↓
Trace Source → Propagation → Sink
  ↓
Check Validation / Encoding
  ↓
Determine Browser Interpretation
  ↓
Confirm Script Execution
  ↓
Confirm Security Impact
  ↓
Document Finding
```

---

# 34. Core Questions

When testing a DOM XSS candidate, ask:

```text
1. What is the source?
2. Can I control the source?
3. What exact value reaches JavaScript?
4. Where does the value go?
5. Is it transformed?
6. Is it decoded?
7. Is it validated?
8. Is it sanitized?
9. What is the sink?
10. How does the sink interpret the value?
11. Can JavaScript execute?
12. What is the security impact?
```

---

# 35. Final Mental Model

```text
SOURCE
  ↓
ATTACKER CONTROL
  ↓
TAINT PROPAGATION
  ↓
DANGEROUS SINK
  ↓
BROWSER INTERPRETATION
  ↓
SCRIPT EXECUTION
  ↓
SECURITY IMPACT
```

---

# Key Takeaways

- DOM XSS is primarily a client-side source-to-sink vulnerability.
- Common sources include URL components, `document.referrer`, `window.name`, Web Messages, and cookies.
- Important DOM sinks include `innerHTML`, `outerHTML`, `document.write()`, and `insertAdjacentHTML`.
- JavaScript execution sinks include `eval()`, `setTimeout()`, `setInterval()`, and `Function()`.
- jQuery functions can also act as DOM XSS sinks.
- AngularJS expressions can create framework-specific DOM XSS conditions.
- Use unique markers to locate attacker input in the live DOM.
- DevTools Elements is more useful than View Source for observing DOM changes.
- Always identify the exact injection context before testing.
- Trace the complete source → propagation → sink flow.
- DOM Invader can help automate source-to-sink analysis.
- URL encoding can change the value received by JavaScript.
- Stored or reflected server-side data can also participate in DOM XSS.
- Finding a source or sink alone does not prove a vulnerability.
- The complete source-to-sink behavior and security impact must be confirmed.

---

# Final Rule

```text
SOURCE
  +
ATTACKER CONTROL
  +
TAINT PROPAGATION
  +
DANGEROUS SINK
  +
UNSAFE INTERPRETATION
  +
SCRIPT EXECUTION
  +
SECURITY IMPACT
  =
CONFIRMED DOM XSS
```