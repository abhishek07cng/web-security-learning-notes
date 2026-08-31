# DOM-Based Vulnerabilities — Quick Revision

## 1. Core Concept

A DOM-based vulnerability occurs when attacker-controlled data enters client-side JavaScript and reaches a security-sensitive operation in an unsafe way.

The core model is:

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
Security Impact
```

---

# 2. Source

A **source** is a location from which attacker-controlled data can enter client-side JavaScript.

Common sources:

```text
URL Parameters
URL Fragment
document.URL
document.location
document.referrer
window.name
Web Messages
Cookies
Other Browser-Controlled Data
```

Remember:

```text
Source Found
    ≠
Vulnerability Confirmed
```

The source must be controllable and must reach a relevant sink.

---

# 3. Sink

A **sink** is a client-side operation that uses the data.

Important sink categories:

```text
HTML / DOM Sinks
Location / Navigation Sinks
Web Message Handlers
Cookie Manipulation
Other DOM Sinks
DOM Clobbering-related Logic
```

Examples:

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

# 4. Source → Sink

The most important concept:

```text
Source
  ↓
Variable
  ↓
JavaScript Processing
  ↓
Sink
```

Ask:

```text
Can attacker-controlled data reach the sink?
```

If yes, continue testing.

---

# 5. DOM XSS

Typical flow:

```text
Attacker-Controlled Source
        ↓
JavaScript
        ↓
HTML / DOM Sink
        ↓
DOM Modification
        ↓
Potential Script Execution
```

Common HTML sinks include:

```javascript
innerHTML
```

and:

```javascript
document.write()
```

The important question is whether attacker-controlled input reaches the sink in a form that results in script execution.

---

# 6. DOM Open Redirection

Typical flow:

```text
Attacker-Controlled Input
        ↓
Client-Side JavaScript
        ↓
Location Sink
        ↓
Browser Navigation
        ↓
Attacker-Controlled Destination
```

Check:

```text
☐ Destination controlled by attacker
☐ Navigation sink identified
☐ URL validation reviewed
☐ Redirect behavior confirmed
```

---

# 7. Web Messages

Important API:

```javascript
window.addEventListener("message", ...)
```

or:

```javascript
window.onmessage = ...
```

Core flow:

```text
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

---

# 8. Web Message Security

Check:

```javascript
event.origin
```

and:

```javascript
event.data
```

Questions:

```text
Is the origin validated?
        ↓
Is the message data validated?
        ↓
Does message data reach a dangerous sink?
```

Remember:

```text
Message Received
    ≠
Vulnerability Confirmed
```

The complete source-to-sink behavior must be demonstrated.

---

# 9. Cookie Manipulation

Relevant API:

```javascript
document.cookie
```

Potential flow:

```text
Attacker-Controlled Data
      ↓
Cookie Manipulation
      ↓
Application State
      ↓
Security Impact
```

Check whether manipulating a cookie can influence security-sensitive application behavior.

---

# 10. Other DOM Sinks

When encountering an unfamiliar sink:

```text
Identify Sink
      ↓
Identify Source
      ↓
Trace Data
      ↓
Determine Browser Behavior
      ↓
Determine Security Impact
```

Do not assume every DOM sink is automatically exploitable.

---

# 11. DOM Clobbering

Core concept:

```text
Attacker-Controlled HTML
        ↓
DOM Elements
        ↓
Unexpected Property / Variable Resolution
        ↓
Application Logic
        ↓
Security Impact
```

Check whether application logic relies on DOM-controlled properties or element names.

---

# 12. Validation & Sanitization

For every source-to-sink flow, check:

```text
☐ Input validation
☐ Encoding
☐ Sanitization
☐ Allowlisting
☐ Origin validation
☐ Type checking
```

The important question is:

```text
Does the protection actually prevent
the dangerous behavior?
```

---

# 13. Exploitability

Do not stop after finding a source and sink.

Confirm:

```text
Attacker Controls Source
        ↓
Data Reaches Sink
        ↓
Sink Produces Relevant Behavior
        ↓
Behavior Is Reproducible
        ↓
Security Impact Confirmed
```

---

# 14. Classification

### DOM XSS

```text
Source
  ↓
HTML / DOM Sink
  ↓
Script Execution
```

### DOM Open Redirection

```text
Source
  ↓
Location Sink
  ↓
Attacker-Controlled Navigation
```

### Web Message Vulnerability

```text
postMessage()
  ↓
Message Handler
  ↓
Insufficient Validation
  ↓
Security-Sensitive Behavior
```

### Cookie Manipulation

```text
Attacker Input
  ↓
Cookie
  ↓
Application State
  ↓
Security Impact
```

### DOM Clobbering

```text
Attacker-Controlled DOM
  ↓
Unexpected Property Resolution
  ↓
Application Logic
  ↓
Security Impact
```

---

# 15. Fast Testing Methodology

```text
1. Inspect JavaScript
2. Find sources
3. Find sinks
4. Trace source → sink
5. Confirm attacker control
6. Review validation / sanitization
7. Determine browser behavior
8. Confirm exploitability
9. Determine impact
10. Document the complete chain
```

---

# 16. Burp + Browser Workflow

```text
Burp Suite
    ↓
Identify Target Functionality
    ↓
Inspect Requests / Responses
    ↓
Open Browser DevTools
    ↓
Inspect JavaScript
    ↓
Search Sources
    ↓
Search Sinks
    ↓
Trace Data Flow
    ↓
Test Controlled Input
    ↓
Observe Browser Behavior
```

---

# 17. Source Examples

```text
URL:
?parameter=value

Fragment:
#value

document.URL

document.location

document.referrer

window.name

postMessage()

document.cookie
```

---

# 18. Sink Examples

```text
innerHTML

document.write()

location

message handlers

document.cookie

Other DOM-related operations
```

---

# 19. Important Questions

When analyzing a DOM-based vulnerability, ask:

```text
1. What is the source?
2. Can I control it?
3. Where does the data flow?
4. What is the sink?
5. Is the sink security-sensitive?
6. Is the input validated?
7. Is the input sanitized?
8. What does the browser do?
9. Can I reproduce the behavior?
10. What is the security impact?
```

---

# 20. One-Minute Decision Tree

```text
SOURCE?
   ↓
Can I control it?
   ↓
SINK?
   ↓
Does data reach sink?
   ↓
Is sink dangerous?
   ↓
Can behavior be triggered?
   ↓
Security impact?
   ↓
Document / Report
```

---

# 21. Reporting

A good DOM vulnerability report should explain:

```text
Source
  ↓
Attacker-Controlled Input
  ↓
JavaScript Processing
  ↓
Sink
  ↓
Browser Behavior
  ↓
Security Impact
```

Include:

```text
☐ Affected functionality
☐ Source
☐ Sink
☐ Input
☐ Data flow
☐ Reproduction steps
☐ Proof of concept
☐ Observed result
☐ Impact
☐ Remediation
```

---

# 22. Remediation Principles

General defensive principles:

```text
☐ Avoid dangerous DOM sinks where possible
☐ Validate untrusted input
☐ Sanitize HTML when HTML is genuinely required
☐ Encode data for the correct context
☐ Validate Web Message origins
☐ Validate Web Message data
☐ Avoid trusting attacker-controlled client-side state
☐ Validate client-side navigation destinations
```

---

# 23. Core Mental Model

```text
SOURCE
  ↓
CONTROL
  ↓
TRACE
  ↓
SINK
  ↓
BEHAVIOR
  ↓
IMPACT
```

Memorize:

> **Source → Control → Trace → Sink → Behavior → Impact**

---

# Final Revision Checklist

```text
☐ Know what a DOM-based vulnerability is
☐ Know sources
☐ Know sinks
☐ Understand source-to-sink tracing
☐ Understand DOM XSS
☐ Understand DOM open redirection
☐ Understand Web Message vulnerabilities
☐ Understand event.origin
☐ Understand event.data
☐ Understand cookie manipulation
☐ Understand other DOM sinks
☐ Understand DOM clobbering
☐ Understand validation and sanitization
☐ Know how to confirm exploitability
☐ Know how to determine impact
☐ Know how to document a source-to-sink chain
```

---

# Final Rule

```text
SOURCE
  ≠
VULNERABILITY

SOURCE
  +
ATTACKER CONTROL
  +
DANGEROUS SINK
  +
EXPLOITABLE BEHAVIOR
  +
SECURITY IMPACT
  =
CONFIRMED DOM-BASED VULNERABILITY
```