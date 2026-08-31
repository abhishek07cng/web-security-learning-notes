# DOM-Based Vulnerabilities — Sources and Sinks

## 1. Overview

The fundamental concept behind DOM-based vulnerabilities is the flow of data from a **source** to a **sink**.

```text
SOURCE
  ↓
Attacker-Controlled Data
  ↓
JavaScript Processing
  ↓
SINK
  ↓
Browser Behavior
  ↓
Potential Security Impact
```

The primary task during DOM vulnerability testing is therefore to identify:

1. Where the data comes from
2. Whether the attacker can control it
3. How the application processes it
4. Where the data is eventually used

---

## 2. What Is a Source?

A **source** is a browser-side location from which data can enter client-side JavaScript.

Potential sources include:

- URL parameters
- URL fragments
- `document.URL`
- `document.location`
- `document.referrer`
- `window.name`
- Web Messages
- Cookies
- Other browser-controlled data

A source is important only when its value can be influenced by an attacker.

---

## 3. Source Example — URL Parameter

Consider:

```text
https://TARGET/page?name=test
```

The application may retrieve the value using JavaScript:

```javascript
const value = new URLSearchParams(location.search).get("name");
```

The flow becomes:

```text
URL Parameter
      ↓
JavaScript
      ↓
value
      ↓
Sink
```

The attacker controls:

```text
name=test
```

and can therefore influence the value processed by the application.

---

## 4. URL Fragment

A URL fragment appears after:

```text
#
```

Example:

```text
https://TARGET/page#test
```

Client-side JavaScript can access the fragment through browser location APIs.

Conceptual flow:

```text
URL Fragment
      ↓
Client-Side JavaScript
      ↓
Application Logic
      ↓
Sink
```

Because fragments are processed by the browser, they can be relevant to DOM-based vulnerabilities.

---

## 5. document.URL

JavaScript can access the current document URL through:

```javascript
document.URL
```

Conceptual flow:

```text
Current URL
      ↓
document.URL
      ↓
JavaScript
      ↓
Sink
```

If attacker-controlled URL content reaches a dangerous sink, further investigation is required.

---

## 6. document.location

Another important source is:

```javascript
document.location
```

It provides information about the current document location.

Conceptual flow:

```text
Attacker-Controlled URL
        ↓
document.location
        ↓
JavaScript
        ↓
Sink
```

Determine which component of the location is being consumed by the application.

---

## 7. document.referrer

The browser can expose the referring page through:

```javascript
document.referrer
```

Conceptual flow:

```text
Referring URL
      ↓
document.referrer
      ↓
JavaScript
      ↓
Sink
```

When reviewing this source, determine whether the value can be influenced in the relevant application context.

---

## 8. window.name

Another browser-controlled source is:

```javascript
window.name
```

Conceptually:

```text
Window Name
      ↓
JavaScript
      ↓
Application Logic
      ↓
Sink
```

If application logic trusts the value without appropriate validation, investigate the resulting source-to-sink flow.

---

## 9. Web Messages as Sources

Web applications can receive data from other windows or frames using:

```javascript
postMessage()
```

The receiving application may process:

```javascript
event.data
```

Conceptual flow:

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
```

Web messages therefore need to be analyzed as potential sources of attacker-controlled data.

---

## 10. Cookies as Sources

Client-side JavaScript can access cookies using:

```javascript
document.cookie
```

Conceptual flow:

```text
Cookie Value
      ↓
document.cookie
      ↓
JavaScript
      ↓
Sink
```

The security significance depends on whether the cookie value can be influenced and whether the application trusts it for security-sensitive behavior.

---

## 11. What Is a Sink?

A **sink** is an operation where data is used in a way that can produce a security-sensitive browser behavior.

Important sink categories include:

- HTML / DOM sinks
- Location / navigation sinks
- Web Message handling
- Cookie manipulation
- Other DOM sinks
- DOM Clobbering-related functionality

---

## 12. HTML / DOM Sinks

One important category is HTML manipulation.

Example:

```javascript
element.innerHTML = value;
```

The flow is:

```text
Attacker Input
      ↓
JavaScript
      ↓
innerHTML
      ↓
DOM Modification
```

If attacker-controlled data is interpreted as HTML in an unsafe way, this may lead to DOM XSS.

---

## 13. document.write()

Another relevant DOM sink is:

```javascript
document.write(value);
```

Conceptual flow:

```text
Attacker-Controlled Data
        ↓
JavaScript
        ↓
document.write()
        ↓
Document Modification
```

The security impact depends on how the supplied data is interpreted.

---

## 14. Location / Navigation Sink

Client-side navigation can also act as a sink.

Conceptual example:

```javascript
location = value;
```

The flow becomes:

```text
Attacker-Controlled Source
        ↓
JavaScript
        ↓
location
        ↓
Browser Navigation
```

If the destination can be controlled by an attacker, this may result in DOM-based open redirection.

---

## 15. Web Message Handler

A message receiver can act as part of a source-to-sink chain.

Example:

```javascript
window.addEventListener("message", function(event) {
    const value = event.data;
});
```

The flow is:

```text
postMessage()
      ↓
message event
      ↓
event.data
      ↓
Application Logic
      ↓
Potential Sink
```

The handler must therefore be analyzed for both:

- Origin Validation
- Data Validation

---

## 16. event.origin

When handling Web Messages, inspect:

```javascript
event.origin
```

The application should determine whether the message originated from an expected source.

Conceptual flow:

```text
Incoming Message
      ↓
event.origin
      ↓
Origin Validation
      ↓
Message Processing
```

The presence or absence of origin validation must be evaluated in the context of what the message controls.

---

## 17. event.data

The actual message contents are available through:

```javascript
event.data
```

Trace:

```text
event.data
    ↓
Application Processing
    ↓
Sink
```

Determine:

- Is the data attacker controlled?
- Is the data validated?
- Is the data sanitized?
- Does it reach a security-sensitive operation?

---

## 18. Cookie Manipulation as a Sink

Cookie-related JavaScript can also participate in a DOM-based vulnerability.

Example:

```javascript
document.cookie = value;
```

Conceptual flow:

```text
Attacker-Controlled Data
        ↓
JavaScript
        ↓
document.cookie
        ↓
Cookie State
        ↓
Application Behavior
```

Determine whether the resulting cookie state affects security-sensitive functionality.

---

## 19. Source vs Sink

The distinction is important.

### Source

A source is:

> Where data enters the application.

Examples:

```text
document.URL
document.location
document.referrer
window.name
event.data
document.cookie
```

### Sink

A sink is:

> Where data is used.

Examples:

```text
innerHTML
document.write()
location
document.cookie
Other DOM operations
```

---

## 20. Source-to-Sink Tracing

The practical workflow is:

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

For example:

```text
URL Parameter
      ↓
location.search
      ↓
JavaScript Variable
      ↓
Function
      ↓
innerHTML
      ↓
DOM Modification
```

---

## 21. Data Flow Does Not Equal Vulnerability

Finding:

```text
Source
```

and:

```text
Sink
```

does not automatically mean that the application is vulnerable.

You must establish:

```text
Source
  +
Attacker Control
  +
Data Reaches Sink
  +
Unsafe Processing
  +
Security-Relevant Behavior
```

---

## 22. Validation Between Source and Sink

Applications may process data before it reaches a sink.

Example:

```text
Source
  ↓
Validation
  ↓
Encoding
  ↓
Sanitization
  ↓
Sink
```

Determine whether those protections actually prevent the dangerous behavior.

---

## 23. Source-to-Sink Examples

### Example 1 — DOM XSS Candidate

```text
URL Parameter
      ↓
JavaScript
      ↓
innerHTML
      ↓
DOM Modification
```

Potential class:

```text
DOM XSS
```

### Example 2 — Open Redirection Candidate

```text
URL Parameter
      ↓
JavaScript
      ↓
location
      ↓
Navigation
```

Potential class:

```text
DOM Open Redirection
```

### Example 3 — Web Message Candidate

```text
postMessage()
      ↓
event.data
      ↓
JavaScript
      ↓
Dangerous Sink
```

Potential class:

```text
Web Message Vulnerability
```

### Example 4 — Cookie Candidate

```text
Attacker-Controlled Data
      ↓
document.cookie
      ↓
Application State
```

Potential class:

```text
Cookie Manipulation
```

---

## 24. DevTools Workflow

Browser DevTools can help trace DOM-based data flows.

Typical workflow:

```text
Open DevTools
      ↓
Sources
      ↓
Inspect JavaScript
      ↓
Search Source
      ↓
Search Sink
      ↓
Set Breakpoints
      ↓
Trigger Input
      ↓
Observe Data
```

Useful search terms include:

```text
document.URL
document.location
document.referrer
window.name
postMessage
message
event.data
event.origin
innerHTML
document.write
location
document.cookie
```

---

## 25. Burp Suite Workflow

Burp Suite can help identify the URLs and parameters that provide input to client-side code.

```text
Proxy
  ↓
HTTP History
  ↓
Identify Parameters
  ↓
Identify Relevant Page
  ↓
Open in Browser
  ↓
Inspect JavaScript
  ↓
Trace Source → Sink
```

---

## 26. Testing Questions

For every source-to-sink candidate, ask:

1. What is the source?
2. Can I control the source?
3. What value reaches JavaScript?
4. Where is the value stored?
5. Which functions process it?
6. What is the sink?
7. How does the sink interpret the value?
8. Is there validation?
9. Is there sanitization?
10. What security impact results?

---

## 27. Quick Source Reference

| Source | Example |
|---|---|
| URL parameter | `?value=test` |
| URL fragment | `#test` |
| `document.URL` | Current document URL |
| `document.location` | Current document location |
| `document.referrer` | Referring page |
| `window.name` | Window name |
| Web Message | `event.data` |
| Cookie | `document.cookie` |

---

## 28. Quick Sink Reference

| Sink / Behavior | Typical Analysis |
|---|---|
| `innerHTML` | HTML / DOM manipulation |
| `document.write()` | Document manipulation |
| `location` | Navigation |
| Message handler | Web Message processing |
| `document.cookie` | Cookie manipulation |
| Other DOM sinks | Analyze resulting browser behavior |
| DOM property resolution | DOM Clobbering analysis |

---

## 29. Core Detection Model

```text
SOURCE
  ↓
Can Attacker Control It?
  ↓
TRACE DATA
  ↓
SINK
  ↓
What Does Browser Do?
  ↓
Is Behavior Dangerous?
  ↓
Security Impact
```

---

## 30. Key Takeaways

- Sources are where attacker-controlled data enters client-side code.
- Sinks are where that data is used.
- Source-to-sink tracing is the foundation of DOM vulnerability analysis.
- URL-related browser properties can act as sources.
- Web Message data can act as a source.
- Cookies can provide client-side data.
- `innerHTML` and `document.write()` are important DOM sinks.
- `location` is important for navigation-related vulnerabilities.
- Web Message handlers require origin and data analysis.
- Finding a source and sink does not automatically prove a vulnerability.
- Validation and sanitization must be evaluated.
- The complete data flow and security impact must be demonstrated.

---

# Final Mental Model

```text
SOURCE
  ↓
ATTACKER CONTROL
  ↓
DATA FLOW
  ↓
PROCESSING
  ↓
SINK
  ↓
BROWSER BEHAVIOR
  ↓
SECURITY IMPACT
```

**Source → Control → Trace → Sink → Behavior → Impact**