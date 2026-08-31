# DOM-Based Vulnerabilities

## 1. Overview

DOM-based vulnerabilities occur when client-side JavaScript processes attacker-controlled data in an unsafe way.

The core model is:

```text
Attacker-Controlled Source
          ↓
      JavaScript
          ↓
          Sink
          ↓
    Browser Behavior
          ↓
    Security Impact
```

---

# 2. Sources

A **source** is a location from which attacker-controlled data can enter client-side JavaScript.

Common sources include:

```text
URL parameters
URL fragments
document.URL
document.location
document.referrer
window.name
Web Messages
Cookies
Other browser-controlled data
```

The important question is:

```text
Can an attacker control the value?
```

A source alone does not demonstrate a vulnerability.

---

# 3. Sinks

A **sink** is a client-side operation that processes data and may produce security-sensitive behavior.

Important categories include:

```text
HTML / DOM sinks
Location / navigation sinks
Web Message handlers
Cookie manipulation
Other DOM sinks
DOM Clobbering-related functionality
```

Examples include:

```javascript
innerHTML
```

```javascript
document.write()
```

```javascript
location
```

```javascript
document.cookie
```

---

# 4. Source-to-Sink Flow

The primary technique for finding DOM-based vulnerabilities is tracing data from its source to its sink.

```text
SOURCE
  ↓
Variable
  ↓
JavaScript Processing
  ↓
SINK
```

For every potential flow ask:

```text
Where does the data originate?
Can an attacker control it?
How is it processed?
Where does it end up?
What does the browser do with it?
```

---

# 5. DOM XSS

DOM XSS can occur when attacker-controlled data reaches an HTML-related DOM sink in an unsafe manner.

Conceptual flow:

```text
Attacker-Controlled Input
        ↓
DOM Source
        ↓
JavaScript
        ↓
HTML Sink
        ↓
DOM Modification
        ↓
Potential Script Execution
```

Examples of relevant sinks include:

```javascript
innerHTML
```

and:

```javascript
document.write()
```

The complete source-to-sink behavior must be demonstrated before confirming the vulnerability.

---

# 6. DOM Open Redirection

DOM-based open redirection occurs when attacker-controlled data influences client-side navigation.

Conceptual flow:

```text
Attacker-Controlled Input
        ↓
JavaScript
        ↓
Location Sink
        ↓
Browser Navigation
        ↓
Attacker-Controlled Destination
```

The analysis should determine:

```text
☐ Whether the destination is attacker controlled
☐ Where the value enters the application
☐ Which navigation sink receives it
☐ Whether destination validation is present
☐ Whether the behavior is reproducible
```

---

# 7. Web Message Vulnerabilities

Web applications can communicate between windows or frames using:

```javascript
postMessage()
```

A receiver may process messages using:

```javascript
window.addEventListener("message", ...)
```

or:

```javascript
window.onmessage = ...
```

The data flow is:

```text
postMessage()
      ↓
message Event
      ↓
event.data
      ↓
Application Logic
      ↓
Potential Sink
```

---

# 8. Web Message Origin Validation

A message handler should consider the origin of incoming messages.

The relevant property is:

```javascript
event.origin
```

During analysis determine:

```text
Is the origin checked?
Is the expected origin clearly defined?
Are unexpected origins rejected?
```

Lack of appropriate origin validation can become security-sensitive when attacker-controlled message data reaches important application functionality.

---

# 9. Web Message Data

Origin validation alone is not the only consideration.

Also inspect:

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

Determine whether message data is:

```text
Validated
Sanitized
Trusted
Used by a security-sensitive operation
```

---

# 10. Cookie Manipulation

Client-side JavaScript can interact with cookies using:

```javascript
document.cookie
```

Analyze:

```text
Source
  ↓
Cookie Value
  ↓
document.cookie
  ↓
Application Behavior
```

The important question is whether attacker-controlled data can influence a security-sensitive cookie or application state.

---

# 11. Other DOM Sinks

Not every DOM-based vulnerability fits neatly into the main categories.

When an unfamiliar sink is identified:

```text
Identify Source
      ↓
Identify Sink
      ↓
Trace Data
      ↓
Determine Browser Behavior
      ↓
Determine Security Impact
```

The presence of a DOM API alone does not establish a vulnerability.

---

# 12. DOM Clobbering

DOM clobbering involves situations where attacker-controlled HTML can interfere with how application code resolves DOM-related properties or variables.

Conceptual flow:

```text
Attacker-Controlled HTML
        ↓
DOM Elements
        ↓
Unexpected Property Resolution
        ↓
Application Logic
        ↓
Security-Sensitive Behavior
```

During analysis, determine whether the application relies on DOM-controlled properties and whether attacker-controlled markup can influence them.

---

# 13. Validation and Sanitization

For each source-to-sink flow, inspect the application's protection mechanisms.

Relevant controls include:

```text
Input Validation
Encoding
Sanitization
Allowlisting
Origin Validation
Type Checking
```

Do not assume that the presence of a protection function automatically makes the data safe.

The actual data flow and resulting browser behavior must be examined.

---

# 14. Exploitability

A potential DOM issue should be evaluated as a complete chain:

```text
Attacker Controls Source
        ↓
Input Reaches JavaScript
        ↓
Data Reaches Sink
        ↓
Sink Produces Relevant Behavior
        ↓
Behavior Is Reproducible
        ↓
Security Impact
```

Therefore:

```text
Source Found
    ≠
Vulnerability Confirmed
```

and:

```text
Sink Found
    ≠
Vulnerability Confirmed
```

---

# 15. Source → Sink Mental Model

The key questions are:

```text
1. What is the source?
2. Can I control it?
3. How does the data flow?
4. What is the sink?
5. What does the sink do?
6. Can the behavior be triggered?
7. What is the security impact?
```

---

# 16. Main Vulnerability Categories

The material covers several important DOM-based vulnerability classes:

```text
DOM XSS
DOM Open Redirection
Web Message Vulnerabilities
Cookie Manipulation
Other DOM Sinks
DOM Clobbering
```

Each should be analyzed by tracing:

```text
Source
  ↓
Data Flow
  ↓
Sink
  ↓
Browser Behavior
  ↓
Impact
```

---

# 17. Testing Workflow

```text
Inspect Client-Side JavaScript
          ↓
Identify Sources
          ↓
Identify Sinks
          ↓
Trace Source → Sink
          ↓
Confirm Attacker Control
          ↓
Review Validation
          ↓
Review Sanitization
          ↓
Trigger the Behavior
          ↓
Confirm Impact
          ↓
Document Finding
```

---

# 18. Key Takeaways

```text
• DOM vulnerabilities are primarily client-side issues.
• Sources provide attacker-controlled data.
• Sinks process that data.
• Source-to-sink tracing is central to detection.
• Not every source is exploitable.
• Not every sink is dangerous.
• Web Message handlers require origin and data analysis.
• Location-related sinks can produce DOM open redirection.
• HTML-related sinks can lead to DOM XSS.
• Cookies can participate in DOM-based security issues.
• DOM clobbering can interfere with application property resolution.
• Exploitability and impact must be demonstrated.
```

---

# Final Mental Model

```text
SOURCE
  ↓
ATTACKER CONTROL
  ↓
DATA FLOW
  ↓
SINK
  ↓
BROWSER BEHAVIOR
  ↓
SECURITY IMPACT
```