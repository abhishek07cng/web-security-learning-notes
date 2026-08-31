# DOM-Based Vulnerabilities — Decision Tree

## Purpose

A practical decision tree for analyzing DOM-based vulnerabilities by tracing data from a controllable **source** to a dangerous **sink**, then determining whether the data can be manipulated to produce a security impact.

---

# 1. Start

```text
START
  ↓
Identify DOM-Based Functionality
  ↓
Inspect Client-Side JavaScript
  ↓
Identify Sources
  ↓
Identify Sinks
  ↓
Trace Data Flow
```

---

# 2. Identify a Source

A DOM vulnerability generally begins with attacker-controllable data entering the browser.

Common source categories include:

```text
URL
URL Parameters
URL Fragment
document.location
document.URL
document.referrer
window.name
Web Messages
Cookies
Other Browser-Controlled Data
```

Decision:

```text
Attacker-Controlled Source Found?
          │
      ┌───┴───┐
      │       │
     NO      YES
      │       │
      ▼       ▼
Continue    Trace
source      data
analysis    flow
```

---

# 3. Identify the Sink

Look for JavaScript functionality that uses the source value.

Important sink categories covered in the material include:

```text
innerHTML
document.write()
location
Web Message Handlers
Cookie Manipulation
Other DOM Sinks
DOM Clobbering-related functionality
```

Decision:

```text
Potential Sink Found?
          │
      ┌───┴───┐
      │       │
     NO      YES
      │       │
      ▼       ▼
Continue    Trace
analysis    source → sink
```

---

# 4. Trace the Data Flow

The central DOM-security model is:

```text
SOURCE
  ↓
Data
  ↓
JavaScript Processing
  ↓
SINK
  ↓
Browser Behavior
```

Ask:

```text
Can attacker-controlled data reach the sink?
```

If:

```text
Source → Sink
```

exists, continue testing.

If the data is safely transformed or validated before reaching the sink, document the protection and continue looking for another flow.

---

# 5. Can the Source Be Controlled?

```text
Can attacker influence source?
          │
      ┌───┴───┐
      │       │
     NO      YES
      │       │
      ▼       ▼
Usually    Continue
not        testing
exploitable
```

Examples:

```text
URL parameter
URL fragment
window.name
postMessage data
referrer
```

---

# 6. Determine the Sink Type

```text
What type of sink?
       │
 ┌─────┼───────────────┐
 ↓     ↓       ↓       ↓
HTML  URL    Message  Cookie
Sink  Sink   Sink     Sink
```

Then follow the corresponding branch.

---

# 7. HTML Sink

Potentially dangerous DOM operations include:

```javascript
element.innerHTML = value;
```

and:

```javascript
document.write(value);
```

Decision:

```text
Attacker Data
      ↓
HTML Sink
      ↓
Can Data Become Executable HTML?
          │
      ┌───┴───┐
      │       │
     NO      YES
      │       │
      ▼       ▼
Continue    Potential
analysis    DOM XSS
```

---

# 8. DOM XSS Flow

```text
Attacker-Controlled Source
          ↓
JavaScript
          ↓
HTML Sink
          ↓
Attacker-Controlled Markup
          ↓
Script Execution
```

The source material demonstrates DOM XSS through vulnerable DOM processing.

---

# 9. Location / Open Redirection

If attacker-controlled data reaches a navigation-related sink:

```text
Source
  ↓
location
  ↓
Browser Navigation
```

Determine whether the attacker can control the destination.

Decision:

```text
Can attacker control destination?
          │
      ┌───┴───┐
      │       │
     NO      YES
      │       │
      ▼       ▼
Continue    Potential
analysis    DOM Open
            Redirection
```

---

# 10. DOM Open Redirection

Conceptual flow:

```text
Attacker-Controlled Input
        ↓
Client-Side JavaScript
        ↓
Location Sink
        ↓
Attacker-Controlled URL
        ↓
Browser Redirect
```

Test whether the application restricts or validates the destination.

---

# 11. Web Message Vulnerabilities

Check for:

```javascript
window.addEventListener("message", ...)
```

or:

```javascript
window.onmessage = ...
```

The important flow is:

```text
postMessage()
     ↓
message event
     ↓
Message Handler
     ↓
Application Logic
```

---

# 12. Web Message Decision

```text
Message Handler Found?
          │
      ┌───┴───┐
      │       │
     NO      YES
      │       │
      ▼       ▼
Continue    Inspect
analysis    Handler
```

Then determine:

```text
Is origin validated?
Is message data validated?
Is message data used by a dangerous sink?
```

---

# 13. Web Message Origin Validation

Check whether the application validates:

```text
event.origin
```

Decision:

```text
Origin Validation?
          │
      ┌───┴───┐
      │       │
     YES      NO
      │       │
      ▼       ▼
Review      Potential
validation  Web Message
            Vulnerability
```

---

# 14. Web Message Data Flow

Trace:

```text
Attacker Window
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

If attacker-controlled `event.data` reaches a dangerous sink, continue the analysis.

---

# 15. Cookie Manipulation

Check whether client-side JavaScript reads or writes cookies.

Relevant functionality:

```javascript
document.cookie
```

Trace:

```text
Attacker-Controlled Data
      ↓
Cookie Manipulation
      ↓
Application State
```

Determine whether manipulating the cookie can affect security-sensitive application behavior.

---

# 16. Cookie Decision

```text
Can attacker influence cookie value?
          │
      ┌───┴───┐
      │       │
     NO      YES
      │       │
      ▼       ▼
Continue    Determine
analysis    security
            impact
```

---

# 17. Other DOM Sinks

If the source does not fit the primary examples:

```text
Identify Sink
      ↓
Determine Browser Behavior
      ↓
Determine Whether Data Is Dangerous
      ↓
Test Attacker Control
```

Do not assume that every DOM sink is exploitable.

---

# 18. DOM Clobbering

Check whether application code relies on DOM elements or properties that can be influenced through attacker-controlled HTML.

Conceptual flow:

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

---

# 19. DOM Clobbering Decision

```text
Application relies on DOM-controlled properties?
          │
      ┌───┴───┐
      │       │
     NO      YES
      │       │
      ▼       ▼
Continue    Analyze
analysis    property
            resolution
```

---

# 20. Is the Data Sanitized?

Once a source and sink are identified:

```text
Source
  ↓
Validation / Encoding / Sanitization
  ↓
Sink
```

Determine whether the protection actually prevents the dangerous behavior.

```text
Protection Effective?
          │
      ┌───┴───┐
      │       │
     YES      NO
      │       │
      ▼       ▼
Document    Continue
protection  exploitation
```

---

# 21. Can the Vulnerability Be Triggered?

A source-to-sink flow alone does not automatically prove exploitability.

Ask:

```text
Can attacker control the source?
        ↓
Can controlled data reach the sink?
        ↓
Can the sink produce the dangerous behavior?
        ↓
Can the behavior be reproduced?
```

---

# 22. Determine Impact

Potential outcomes depend on the vulnerability class.

```text
DOM XSS
    ↓
Script Execution

DOM Open Redirection
    ↓
Attacker-Controlled Navigation

Web Message Vulnerability
    ↓
Unexpected Client-Side Behavior

Cookie Manipulation
    ↓
Application State Manipulation

DOM Clobbering
    ↓
Unexpected Application Logic
```

---

# 23. Confirm the Complete Chain

The minimum mental model is:

```text
SOURCE
  ↓
ATTACKER CONTROL
  ↓
DATA FLOW
  ↓
SINK
  ↓
DANGEROUS BEHAVIOR
  ↓
SECURITY IMPACT
```

---

# 24. Final Decision

```text
Source Identified
      ↓
Attacker Controls Source?
      │
   ┌──┴──┐
   NO    YES
   │      │
   ▼      ▼
Continue  Identify Sink
          ↓
       Data Reaches Sink?
          │
       ┌──┴──┐
       NO    YES
       │      │
       ▼      ▼
    Stop /   Analyze
    Continue Sink
              ↓
       Dangerous Behavior?
          │
       ┌──┴──┐
       NO    YES
       │      │
       ▼      ▼
    Document  Validate
              Impact
                ↓
             Report
```

---

# 25. Complete DOM-Based Vulnerability Decision Tree

```text
START
  │
  ▼
Inspect Client-Side JavaScript
  │
  ▼
Identify Source
  │
  ├── URL / Parameter / Fragment
  ├── document.location
  ├── document.URL
  ├── document.referrer
  ├── window.name
  ├── Web Message
  └── Cookie / Other Browser Data
  │
  ▼
Identify Sink
  │
  ├── HTML / DOM Sink
  ├── Location Sink
  ├── Message Handler
  ├── Cookie Manipulation
  ├── Other DOM Sink
  └── DOM Clobbering
  │
  ▼
Trace Source → Sink
  │
  ▼
Can Attacker Control Source?
  │
  ├── NO → Document / Continue
  │
  └── YES
       │
       ▼
Does Data Reach Sink?
       │
       ├── NO → Stop
       │
       └── YES
            │
            ▼
       Is Sink Dangerous?
            │
       ├── NO → Document
       │
       └── YES
            │
            ▼
       Can Behavior Be Triggered?
            │
       ├── NO → Continue Analysis
       │
       └── YES
            │
            ▼
       Validate Security Impact
            │
            ▼
       Document Evidence
            │
            ▼
       Recommend Remediation
```

---

# 26. Quick Source → Sink Reference

| Source | Potential Sink / Behavior |
|---|---|
| URL parameters | DOM HTML / navigation |
| URL fragment | DOM HTML / client-side logic |
| `document.location` | DOM manipulation / navigation |
| `document.URL` | DOM manipulation |
| `document.referrer` | DOM manipulation |
| `window.name` | DOM manipulation |
| `postMessage()` | Message handler |
| `event.data` | DOM / application sink |
| Cookies | Client-side application state |
| Attacker-controlled DOM | DOM clobbering |

---

# 27. Final Mental Model

```text
WHAT IS THE SOURCE?
        ↓
CAN I CONTROL IT?
        ↓
WHERE DOES THE DATA GO?
        ↓
WHAT IS THE SINK?
        ↓
IS THE SINK DANGEROUS?
        ↓
CAN I TRIGGER THE BEHAVIOR?
        ↓
WHAT IS THE SECURITY IMPACT?
```

---

# Final Checklist

```text
☐ Source identified
☐ Source controllability confirmed
☐ Sink identified
☐ Source-to-sink flow traced
☐ Input validation reviewed
☐ Sanitization reviewed
☐ Web message handling reviewed
☐ Origin validation reviewed
☐ Location/navigation behavior reviewed
☐ Cookie manipulation reviewed
☐ DOM sinks reviewed
☐ DOM clobbering reviewed
☐ Exploitability confirmed
☐ Impact confirmed
☐ Evidence collected
☐ Remediation documented
```