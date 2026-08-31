# DOM-Based Vulnerabilities — Methodology

## Purpose

This methodology provides a structured workflow for identifying, tracing, validating, and documenting DOM-based vulnerabilities.

The central concept is:

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

# 1. Define Scope

Before testing:

```text
☐ Confirm authorization
☐ Identify in-scope application
☐ Identify allowed functionality
☐ Use authorized accounts
☐ Stay within testing boundaries
```

---

# 2. Identify Client-Side Functionality

Start by examining how the application processes data in the browser.

Inspect:

```text
☐ Page source
☐ JavaScript files
☐ Inline JavaScript
☐ DOM manipulation
☐ Event handlers
☐ URL processing
☐ Web Message handlers
☐ Cookie-related JavaScript
```

---

# 3. Identify Sources

Look for locations where attacker-controlled data can enter client-side JavaScript.

Common sources:

```text
URL parameters
URL fragment
document.URL
document.location
document.referrer
window.name
Web Messages
Cookies
Other browser-controlled data
```

Record:

```text
Source:
____________________________

File / Function:
____________________________

Attacker Controlled:
YES / NO
```

---

# 4. Identify Sinks

Search the JavaScript for operations that use source data.

Important categories:

```text
HTML / DOM Sinks
Location / Navigation Sinks
Web Message Handlers
Cookie Manipulation
Other DOM Sinks
DOM Clobbering-related functionality
```

Examples covered by the material include:

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

and:

```javascript
window.addEventListener("message", ...)
```

---

# 5. Trace Source → Sink

This is the most important part of the methodology.

```text
SOURCE
  ↓
Variable
  ↓
Function
  ↓
Processing
  ↓
SINK
```

Ask:

```text
Can attacker-controlled data reach the sink?
```

If yes:

```text
Continue
```

If no:

```text
Document the protection
Continue searching
```

---

# 6. Verify Attacker Control

A source is useful only if the attacker can influence it.

Examples:

```text
URL Parameter
      ↓
Attacker Controls Value
```

```text
URL Fragment
      ↓
Attacker Controls Value
```

```text
postMessage()
      ↓
Attacker Controls Message
```

Determine:

```text
☐ Input is attacker controlled
☐ Input reaches JavaScript
☐ Input reaches expected variable
```

---

# 7. Review Input Validation

Once a source is identified, inspect how the application processes the data.

Check:

```text
☐ Validation
☐ Encoding
☐ Sanitization
☐ Allowlisting
☐ Origin validation
☐ Type checking
```

Do not assume that the presence of a validation function means the input is safe.

Verify the actual behavior.

---

# 8. HTML / DOM Sink Analysis

When attacker-controlled data reaches an HTML-related sink:

```text
Source
  ↓
JavaScript
  ↓
HTML Sink
```

Relevant examples:

```javascript
element.innerHTML = value;
```

```javascript
document.write(value);
```

Determine:

```text
☐ Can attacker input reach sink?
☐ Is input interpreted as markup?
☐ Is input sanitized?
☐ Can dangerous DOM behavior occur?
```

---

# 9. DOM XSS Analysis

Potential flow:

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

Confirm the complete chain before classifying the issue as DOM XSS.

---

# 10. DOM Open Redirection Analysis

For location-related behavior:

```text
Source
  ↓
JavaScript
  ↓
Location Sink
  ↓
Browser Navigation
```

Determine:

```text
☐ Destination controlled by attacker
☐ Destination reaches navigation sink
☐ URL validation exists
☐ Validation can be bypassed or is insufficient
☐ Redirect behavior reproduced
```

---

# 11. Web Message Analysis

Search for:

```javascript
window.addEventListener("message", ...)
```

or:

```javascript
window.onmessage = ...
```

Then trace:

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

# 12. Validate Message Origin

Inspect whether the application checks:

```javascript
event.origin
```

Determine:

```text
☐ Origin validation exists
☐ Expected origin is defined
☐ Comparison is correct
☐ Unexpected origins are rejected
```

If origin validation is absent or insufficient, continue tracing the message data.

---

# 13. Validate Message Data

Even when the origin is checked, inspect:

```javascript
event.data
```

Determine:

```text
☐ Data is validated
☐ Data is sanitized where necessary
☐ Data reaches a sensitive sink
☐ Application behavior changes based on message
```

---

# 14. Cookie Manipulation Analysis

Search for:

```javascript
document.cookie
```

Trace:

```text
Source
  ↓
Cookie Value
  ↓
document.cookie
  ↓
Application Behavior
```

Determine:

```text
☐ Cookie can be influenced
☐ Cookie is security-sensitive
☐ Application trusts cookie value
☐ Manipulation produces meaningful behavior
```

---

# 15. Other DOM Sinks

If the sink is not one of the primary examples:

```text
Identify Sink
      ↓
Determine Browser Behavior
      ↓
Determine Source
      ↓
Trace Data Flow
      ↓
Assess Security Impact
```

The important question remains:

```text
Can attacker-controlled data reach a security-sensitive sink?
```

---

# 16. DOM Clobbering Analysis

Analyze whether attacker-controlled HTML can interfere with application assumptions about DOM elements or properties.

Conceptual flow:

```text
Attacker-Controlled HTML
        ↓
DOM Elements
        ↓
Property / Variable Resolution
        ↓
Application Logic
        ↓
Unexpected Behavior
```

Check:

```text
☐ Application relies on DOM-controlled properties
☐ Attacker can influence relevant HTML
☐ Property resolution changes
☐ Application consumes unexpected value
☐ Security impact is demonstrated
```

---

# 17. Exploitability Validation

Do not stop at identifying:

```text
Source
```

and:

```text
Sink
```

Confirm:

```text
Source is controllable
      ↓
Data reaches sink
      ↓
Sink produces relevant behavior
      ↓
Behavior is reproducible
```

---

# 18. Determine Vulnerability Class

Use the observed source-to-sink flow.

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
Attacker-Controlled Data
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

# 19. Build a Proof of Concept

Once the source-to-sink flow is confirmed:

```text
Identify Input
      ↓
Construct Controlled Input
      ↓
Trigger Client-Side Code
      ↓
Observe Sink
      ↓
Confirm Result
```

The PoC should demonstrate the smallest reproducible path to the observed impact.

---

# 20. Capture Evidence

Record:

```text
☐ Vulnerable page
☐ Source
☐ Relevant JavaScript
☐ Sink
☐ Input
☐ Data flow
☐ Browser behavior
☐ Result
☐ Security impact
```

A useful evidence chain is:

```text
Source
  ↓
Input
  ↓
JavaScript Function
  ↓
Sink
  ↓
Result
```

---

# 21. Reproduction Method

Use a simple sequence:

```text
1. Open affected functionality.
2. Identify source.
3. Supply attacker-controlled input.
4. Trigger the relevant JavaScript.
5. Follow the data flow.
6. Observe the sink behavior.
7. Confirm security impact.
```

Modify according to the specific vulnerability.

---

# 22. Impact Analysis

Determine the actual security consequence.

Potential categories include:

```text
DOM XSS
DOM Open Redirection
Web Message Vulnerability
Cookie Manipulation
DOM Clobbering
Other DOM-Based Security Impact
```

Record:

```text
Impact:
____________________________
```

---

# 23. Remediation Analysis

The appropriate remediation depends on the source and sink.

General principles:

```text
☐ Avoid dangerous DOM sinks where possible
☐ Validate attacker-controlled input
☐ Sanitize untrusted HTML where HTML is genuinely required
☐ Encode data appropriately for its context
☐ Validate message origins
☐ Validate message data
☐ Avoid trusting attacker-controlled client-side state
☐ Prevent unsafe client-side navigation
```

---

# 24. Reporting

Structure the final finding as:

```text
Title
  ↓
Affected Functionality
  ↓
Source
  ↓
Sink
  ↓
Data Flow
  ↓
Reproduction Steps
  ↓
Proof of Concept
  ↓
Observed Result
  ↓
Security Impact
  ↓
Remediation
```

---

# 25. Complete Methodology Flow

```text
START
  ↓
Confirm Scope
  ↓
Inspect Client-Side JavaScript
  ↓
Identify Sources
  ↓
Identify Sinks
  ↓
Trace Source → Sink
  ↓
Can Attacker Control Source?
  │
  ├── NO → Continue Analysis
  │
  └── YES
       ↓
Does Data Reach Sink?
       │
       ├── NO → Continue Analysis
       │
       └── YES
            ↓
       Review Validation
            ↓
       Review Sanitization
            ↓
       Determine Sink Behavior
            ↓
       Can Dangerous Behavior Occur?
            │
            ├── NO → Document
            │
            └── YES
                 ↓
           Confirm Reproduction
                 ↓
           Determine Impact
                 ↓
           Capture Evidence
                 ↓
           Write Report
```

---

# 26. Source → Sink Methodology

The core workflow can be remembered as:

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

Ask six questions:

```text
1. What is the source?
2. Can I control it?
3. Where does the data flow?
4. What is the sink?
5. What does the browser do?
6. What is the security impact?
```

---

# 27. Final Testing Checklist

```text
☐ Scope confirmed
☐ Client-side JavaScript inspected
☐ Sources identified
☐ Attacker control confirmed
☐ Sinks identified
☐ Source-to-sink flow traced
☐ Validation reviewed
☐ Sanitization reviewed
☐ HTML / DOM sinks reviewed
☐ Navigation sinks reviewed
☐ Web Message handlers reviewed
☐ event.origin validation reviewed
☐ event.data processing reviewed
☐ Cookie manipulation reviewed
☐ Other DOM sinks reviewed
☐ DOM clobbering reviewed
☐ Exploitability confirmed
☐ Impact confirmed
☐ Evidence captured
☐ Reproduction documented
☐ Remediation documented
☐ Report prepared
```

---

# Final Mental Model

```text
WHAT IS THE SOURCE?
        ↓
CAN I CONTROL IT?
        ↓
WHERE DOES THE DATA GO?
        ↓
WHAT IS THE SINK?
        ↓
WHAT DOES THE BROWSER DO?
        ↓
IS THERE SECURITY IMPACT?
        ↓
DOCUMENT + REPORT + REMEDIATE
```