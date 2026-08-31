# DOM-Based Vulnerabilities — Bug Bounty Checklist

## 1. Scope & Authorization

```text
☐ Confirm target is authorized
☐ Confirm application is within scope
☐ Identify allowed functionality
☐ Use authorized test accounts
☐ Avoid testing outside the defined scope
```

---

# 2. Client-Side Reconnaissance

Start by identifying JavaScript-driven functionality.

```text
☐ Inspect page source
☐ Inspect loaded JavaScript
☐ Identify DOM manipulation
☐ Identify event handlers
☐ Identify URL processing
☐ Identify Web Message handlers
☐ Identify cookie-related JavaScript
```

---

# 3. Identify Sources

Look for attacker-controllable data entering client-side code.

### Common Sources

```text
☐ URL parameters
☐ URL fragment
☐ document.URL
☐ document.location
☐ document.referrer
☐ window.name
☐ Web Messages
☐ Cookies
☐ Other browser-controlled data
```

Record:

```text
Source:
____________________________

Location in Code:
____________________________

Attacker Controlled:
YES / NO
```

---

# 4. Identify Sinks

Search the JavaScript for dangerous or security-sensitive operations.

### DOM / HTML Sinks

```text
☐ innerHTML
☐ document.write()
☐ Other DOM HTML manipulation
```

### Navigation Sinks

```text
☐ location
☐ Client-side redirects
☐ Other navigation-related functionality
```

### Web Message Handling

```text
☐ message event listener
☐ window.onmessage
☐ event.data
```

### Cookie Handling

```text
☐ document.cookie
☐ Cookie creation
☐ Cookie modification
☐ Cookie deletion
```

### Other DOM Behavior

```text
☐ DOM clobbering-related functionality
☐ Other DOM sinks
```

---

# 5. Source → Sink Analysis

The most important step:

```text
SOURCE
  ↓
Data
  ↓
JavaScript Processing
  ↓
SINK
```

Checklist:

```text
☐ Source identified
☐ Sink identified
☐ Data flow traced
☐ Attacker input reaches sink
☐ No effective protection blocks the flow
```

---

# 6. Input Control

Determine whether the attacker can actually influence the source.

```text
Can attacker control input?
          │
      ┌───┴───┐
      │       │
     NO      YES
      │       │
      ▼       ▼
Continue    Continue
analysis    source-to-sink
            testing
```

Record:

```text
Input:
____________________________

Source:
____________________________

Control Method:
____________________________
```

---

# 7. DOM XSS Checklist

For potential DOM XSS:

```text
☐ Attacker-controlled source identified
☐ HTML/DOM sink identified
☐ Data reaches sink
☐ Input is interpreted as HTML/markup
☐ Security impact demonstrated
```

Conceptual flow:

```text
Attacker Input
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

---

# 8. HTML Sink Review

Check code such as:

```javascript
element.innerHTML = value;
```

or:

```javascript
document.write(value);
```

Determine:

```text
☐ Is value attacker controlled?
☐ Is value sanitized?
☐ Is value encoded?
☐ Can attacker-controlled markup reach the sink?
☐ What browser behavior results?
```

---

# 9. DOM Open Redirection

Check client-side navigation behavior.

```text
☐ Location-related sink identified
☐ Destination influenced by attacker input
☐ URL validation reviewed
☐ Redirect behavior confirmed
```

Concept:

```text
Attacker Input
      ↓
Client-Side JavaScript
      ↓
Location Sink
      ↓
Attacker-Controlled Destination
```

---

# 10. Web Message Testing

Search for:

```javascript
window.addEventListener("message", ...)
```

or:

```javascript
window.onmessage = ...
```

Checklist:

```text
☐ Message handler identified
☐ event.data identified
☐ event.origin checked
☐ Message source validated
☐ Message content validated
☐ Message data traced to sink
```

---

# 11. Web Message Origin Validation

Check whether the application validates:

```javascript
event.origin
```

Conceptually:

```text
Incoming Message
      ↓
Origin Validation
      ↓
Message Processing
```

Record:

```text
Origin Validation:
YES / NO

Validation Method:
____________________________
```

---

# 12. Web Message Data Flow

Trace:

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

Determine:

```text
☐ Attacker can send message
☐ Message handler receives it
☐ Origin is insufficiently validated
☐ Data is insufficiently validated
☐ Data reaches a security-sensitive sink
```

---

# 13. Cookie Manipulation

Inspect:

```javascript
document.cookie
```

Determine:

```text
☐ Cookie is read by JavaScript
☐ Cookie is written by JavaScript
☐ Attacker-controlled data can influence cookie value
☐ Cookie affects application behavior
☐ Security-sensitive state depends on cookie
```

Record:

```text
Cookie:
____________________________

JavaScript Function:
____________________________

Security Impact:
____________________________
```

---

# 14. Other DOM Sinks

If a sink does not fit the primary categories:

```text
☐ Identify the sink
☐ Determine what browser behavior it triggers
☐ Determine whether attacker data reaches it
☐ Determine whether the behavior is security-sensitive
☐ Verify exploitability
```

Do not assume that every DOM sink is automatically vulnerable.

---

# 15. DOM Clobbering

Check whether attacker-controlled HTML can interfere with how the application resolves DOM-related properties.

```text
☐ Application relies on DOM properties
☐ HTML elements can influence those properties
☐ Application logic uses the affected property
☐ Unexpected value reaches security-sensitive logic
☐ Complete behavior is reproducible
```

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
Security Impact
```

---

# 16. Validation & Sanitization

For every potential vulnerability:

```text
☐ Input validation checked
☐ Encoding checked
☐ Sanitization checked
☐ Allowlist checked
☐ Origin validation checked where relevant
☐ Security controls tested against actual behavior
```

---

# 17. Exploitability

Do not stop at source and sink identification.

Confirm:

```text
☐ Attacker controls source
☐ Data reaches sink
☐ Sink produces relevant behavior
☐ Required conditions can be satisfied
☐ Vulnerability is reproducible
```

---

# 18. Impact Validation

Determine what the vulnerability actually allows.

Possible categories covered by the material include:

```text
DOM XSS
DOM Open Redirection
Web Message Vulnerability
Cookie Manipulation
DOM Clobbering
Other DOM-Based Behavior
```

Record:

```text
Impact:
____________________________
```

---

# 19. Evidence Collection

Capture:

```text
☐ Vulnerable JavaScript
☐ Source
☐ Sink
☐ Relevant request / URL
☐ Input used
☐ Browser behavior
☐ Successful reproduction
☐ Security impact
```

For source-to-sink findings, document the complete chain:

```text
Source
  ↓
Attacker Input
  ↓
JavaScript Processing
  ↓
Sink
  ↓
Result
```

---

# 20. Reproduction Steps

Use a clear sequence:

```text
1. Open the affected functionality.
2. Identify the attacker-controlled source.
3. Supply the controlled input.
4. Trigger the client-side functionality.
5. Observe the sink behavior.
6. Confirm the resulting security impact.
```

Modify the steps according to the specific vulnerability class.

---

# 21. Bug Bounty Report Structure

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

# 22. Finding Classification

Use the observed behavior to classify the finding:

```text
Source → HTML Sink
        ↓
Potential DOM XSS
```

```text
Source → Location Sink
        ↓
Potential DOM Open Redirection
```

```text
postMessage → Message Handler
        ↓
Potential Web Message Vulnerability
```

```text
Attacker Input → Cookie Manipulation
        ↓
Potential Cookie-Based DOM Issue
```

```text
Attacker-Controlled DOM
        ↓
Unexpected Property Resolution
        ↓
Potential DOM Clobbering
```

---

# 23. Final Decision

```text
Source Identified?
      │
  ┌───┴───┐
  NO      YES
  │        │
  ▼        ▼
Continue  Attacker Controls It?
             │
         ┌───┴───┐
         NO      YES
          │       │
          ▼       ▼
       Continue  Sink Identified?
                    │
                ┌───┴───┐
                NO      YES
                 │       │
                 ▼       ▼
              Continue  Data Reaches Sink?
                            │
                        ┌───┴───┐
                        NO      YES
                         │       │
                         ▼       ▼
                       Stop    Dangerous
                               Behavior?
                                  │
                              ┌───┴───┐
                              NO      YES
                               │       │
                               ▼       ▼
                            Document  Validate
                                      Impact
                                        │
                                        ▼
                                      Report
```

---

# 24. Final Bug Bounty Checklist

```text
☐ Scope confirmed
☐ Client-side JavaScript inspected
☐ Sources identified
☐ Attacker control confirmed
☐ Sinks identified
☐ Source-to-sink flow traced
☐ Validation reviewed
☐ Sanitization reviewed
☐ DOM XSS tested where relevant
☐ DOM open redirection tested where relevant
☐ Web message handlers reviewed
☐ event.origin validation reviewed
☐ event.data flow reviewed
☐ Cookie manipulation reviewed
☐ Other DOM sinks reviewed
☐ DOM clobbering reviewed
☐ Exploitability confirmed
☐ Impact confirmed
☐ Evidence collected
☐ Reproduction documented
☐ Remediation documented
☐ Bug bounty report prepared
```

---

# Core Bug Bounty Principle

```text
Source Found
    ≠
Vulnerability Confirmed
```

The important chain is:

```text
Attacker-Controlled Source
          ↓
      Data Flow
          ↓
      Dangerous Sink
          ↓
    Browser Behavior
          ↓
     Security Impact
```

Only after the complete chain is demonstrated should the issue be treated as a confirmed vulnerability.