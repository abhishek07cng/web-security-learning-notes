# DOM-Based Vulnerabilities — DOM Open Redirection

## 1. Overview

DOM-based open redirection occurs when client-side JavaScript takes attacker-controlled data and uses it to control browser navigation.

The core model is:

```text
Attacker-Controlled Source
        ↓
Client-Side JavaScript
        ↓
Navigation Sink
        ↓
Browser Navigation
        ↓
Attacker-Controlled Destination
```

The vulnerability exists in the client-side processing of the navigation value.

---

# 2. What Is DOM Open Redirection?

A DOM-based open redirect occurs when JavaScript uses attacker-controlled data to determine where the browser should navigate.

Conceptually:

```text
Attacker Input
      ↓
JavaScript
      ↓
location / Navigation API
      ↓
Browser
      ↓
External Destination
```

The important elements are:

```text
1. Attacker-controlled source
2. Client-side processing
3. Navigation sink
4. Attacker-controlled destination
```

---

# 3. Common Sources

Potential sources include:

```text
location.search
location.hash
location.pathname
document.URL
document.location
document.referrer
window.name
Web Messages
Other browser-controlled data
```

The source must be controllable by the attacker.

---

# 4. Navigation Sinks

Important navigation-related sinks include:

```text
location
location.href
location.assign()
location.replace()
```

Other URL-related attributes may also be relevant depending on the application.

Examples:

```javascript
location = value;
```

```javascript
location.href = value;
```

```javascript
location.assign(value);
```

```javascript
location.replace(value);
```

---

# 5. Basic Source → Sink Flow

The fundamental flow is:

```text
Attacker-Controlled Source
        ↓
JavaScript Variable
        ↓
Application Processing
        ↓
Navigation Sink
        ↓
Browser Navigation
```

For example:

```text
location.search
      ↓
JavaScript Variable
      ↓
location.href
      ↓
Browser Navigation
```

---

# 6. URL Parameter as a Source

Consider:

```text
/page?returnPath=/home
```

JavaScript may retrieve:

```text
returnPath
```

and use it for navigation.

Conceptual flow:

```text
returnPath
    ↓
location.search
    ↓
JavaScript
    ↓
location
    ↓
Navigation
```

If the attacker can influence the destination, continue investigating.

---

# 7. URL Fragment as a Source

A URL fragment may also be used as navigation data.

Example:

```text
/page#https://example.com
```

Potential flow:

```text
location.hash
      ↓
JavaScript
      ↓
Navigation Sink
      ↓
Browser Navigation
```

Determine whether the fragment is actually used to construct a destination.

---

# 8. document.URL

JavaScript can access the current URL using:

```javascript
document.URL
```

Potential flow:

```text
Attacker-Controlled URL
      ↓
document.URL
      ↓
JavaScript
      ↓
Navigation Sink
```

Investigate which portion of the URL reaches the sink.

---

# 9. document.location

Another potential source is:

```javascript
document.location
```

Conceptual flow:

```text
Current Location
      ↓
document.location
      ↓
JavaScript
      ↓
Navigation
```

Determine whether attacker-controlled URL data can influence the resulting destination.

---

# 10. document.referrer

The referring URL can be accessed through:

```javascript
document.referrer
```

Potential flow:

```text
Referrer
    ↓
document.referrer
    ↓
JavaScript
    ↓
Navigation Sink
```

Determine whether the value can be influenced in the relevant application context.

---

# 11. window.name

Another browser-controlled source is:

```javascript
window.name
```

Potential flow:

```text
window.name
      ↓
JavaScript
      ↓
Navigation Logic
      ↓
Navigation Sink
```

If the application trusts this value, investigate how it reaches the navigation operation.

---

# 12. Web Messages

Web Messages can also provide attacker-controlled navigation data.

Conceptual flow:

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
Navigation Sink
```

For Web Message-based navigation, inspect:

```text
event.origin
event.data
```

---

# 13. event.origin Validation

When processing Web Messages, inspect whether the application validates:

```javascript
event.origin
```

Conceptual flow:

```text
Incoming Message
      ↓
event.origin
      ↓
Origin Validation
      ↓
event.data
      ↓
Navigation
```

Determine whether unexpected message origins are rejected.

---

# 14. event.data Validation

Also inspect:

```javascript
event.data
```

The message data may contain a destination.

Potential flow:

```text
event.data
     ↓
Application Logic
     ↓
Destination
     ↓
location
     ↓
Navigation
```

Determine whether the destination is validated.

---

# 15. Basic Vulnerable Pattern

A conceptual vulnerable pattern is:

```javascript
const url = new URLSearchParams(location.search)
    .get("returnPath");

location.href = url;
```

The flow is:

```text
URL Parameter
      ↓
location.search
      ↓
returnPath
      ↓
location.href
      ↓
Browser Navigation
```

If `returnPath` is attacker controlled and an external destination is accepted, investigate as a potential DOM open redirect.

---

# 16. Another Vulnerable Pattern

Another conceptual pattern is:

```javascript
const target = location.hash.slice(1);

location.assign(target);
```

Flow:

```text
URL Fragment
      ↓
location.hash
      ↓
target
      ↓
location.assign()
      ↓
Browser Navigation
```

---

# 17. Testing Methodology

## Step 1 — Identify Navigation Functionality

Look for functionality such as:

```text
Login redirects
Logout redirects
Return links
Back links
Continue links
Language redirects
Client-side routing
Navigation parameters
```

---

## Step 2 — Identify Input

Look for:

```text
returnPath
redirect
redirectUrl
returnUrl
next
url
target
destination
```

These names are only indicators.

Do not assume a parameter is vulnerable based on its name.

---

## Step 3 — Test with a Controlled Value

Start with a harmless marker:

```text
test123
```

Determine whether the value influences navigation logic.

---

## Step 4 — Trace the JavaScript

Search client-side JavaScript for:

```text
location
location.href
location.assign
location.replace
```

Also search for:

```text
location.search
location.hash
document.URL
document.location
```

---

# 18. DevTools Workflow

Use browser DevTools:

```text
Open DevTools
      ↓
Sources
      ↓
Search JavaScript
      ↓
Find Source
      ↓
Find Navigation Sink
      ↓
Set Breakpoint
      ↓
Trigger Input
      ↓
Inspect Destination
```

Useful search terms:

```text
location
location.href
location.assign
location.replace
location.search
location.hash
document.URL
document.location
```

---

# 19. Burp Suite Workflow

Burp Suite can help identify relevant parameters and requests.

```text
Burp Proxy
    ↓
HTTP History
    ↓
Identify Redirect / Navigation Parameters
    ↓
Open Relevant Page
    ↓
Inspect JavaScript
    ↓
Trace Source → Sink
    ↓
Test Controlled Destination
```

---

# 20. Source-to-Sink Analysis

For each candidate:

```text
SOURCE
  ↓
Can Attacker Control It?
  ↓
JavaScript Processing
  ↓
NAVIGATION SINK
  ↓
What Destination Is Generated?
  ↓
Can Attacker Control Destination?
```

The key question is:

```text
Can attacker-controlled data determine where
the browser navigates?
```

---

# 21. Validation Analysis

Inspect whether the application validates the destination.

Potential controls include:

```text
Allowlisting
Origin validation
Protocol validation
Host validation
Path validation
Relative URL enforcement
```

Determine whether the protection actually restricts the destination as intended.

---

# 22. Relative vs External Destinations

A security-sensitive distinction is whether navigation is restricted to an expected application destination.

Conceptually:

```text
Expected Internal Destination
        ↓
/account
```

versus:

```text
Attacker-Controlled External Destination
        ↓
https://attacker.example
```

The security impact depends on whether the application allows an attacker to redirect users to an unintended destination.

---

# 23. Protocol Considerations

When analyzing navigation values, inspect the protocol as well as the destination.

Potential values may include:

```text
https:
http:
```

Other browser URL schemes may behave differently and should be evaluated according to the application's context and security controls.

Do not assume that checking only whether a value "looks like a URL" is sufficient.

---

# 24. Validation Does Not Automatically Mean Safe

A common mistake is assuming:

```text
Validation Present
      ↓
Safe
```

Instead:

```text
Validation Present
      ↓
Analyze What It Actually Allows
      ↓
Analyze Whether Destination Can Still Be Controlled
```

The actual browser behavior is what matters.

---

# 25. Testing Flow

```text
Identify Navigation Functionality
          ↓
Identify Potential Source
          ↓
Confirm Attacker Control
          ↓
Find Navigation Sink
          ↓
Trace Data Flow
          ↓
Review Validation
          ↓
Determine Final Destination
          ↓
Confirm Browser Navigation
          ↓
Assess Security Impact
```

---

# 26. Example Source → Sink

```text
/page?returnPath=/home
          ↓
location.search
          ↓
URLSearchParams
          ↓
returnPath
          ↓
location.href
          ↓
Browser Navigation
```

Potential issue:

```text
Attacker-Controlled returnPath
          ↓
External Destination
          ↓
Browser Navigation
```

---

# 27. Web Message Source → Navigation Sink

Potential flow:

```text
postMessage()
      ↓
event.data
      ↓
Destination
      ↓
location.assign()
      ↓
Browser Navigation
```

Review:

```text
☐ Origin validation
☐ Data validation
☐ Destination validation
☐ Final navigation behavior
```

---

# 28. Evidence Collection

Capture:

```text
☐ Affected page
☐ Source
☐ Input
☐ Relevant JavaScript
☐ Navigation sink
☐ Final destination
☐ Browser behavior
☐ Reproduction steps
☐ Security impact
```

The strongest evidence demonstrates:

```text
Source
  ↓
Attacker-Controlled Value
  ↓
Navigation Sink
  ↓
Attacker-Controlled Destination
```

---

# 29. Reporting Structure

A report should contain:

```text
Title
Affected Functionality
Source
Sink
Data Flow
Reproduction Steps
Proof of Concept
Observed Navigation
Security Impact
Remediation
```

Example structure:

```text
Attacker-Controlled Parameter
        ↓
Client-Side JavaScript
        ↓
location.href
        ↓
External Destination
```

---

# 30. Remediation Principles

General defensive principles include:

```text
☐ Avoid using untrusted data directly for navigation
☐ Restrict destinations to trusted values
☐ Prefer allowlists
☐ Validate URL origins
☐ Validate URL protocols
☐ Validate hosts where appropriate
☐ Prefer safe relative paths when possible
☐ Validate Web Message origins
☐ Validate Web Message data
```

---

# 31. Quick Reference

## Common Sources

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

## Common Navigation Sinks

```text
location
location.href
location.assign()
location.replace()
```

## Common Parameter Names

```text
redirect
redirectUrl
returnUrl
returnPath
next
url
target
destination
```

Parameter names are only clues and do not prove vulnerability.

---

# 32. Testing Questions

Ask:

```text
1. What is the source?
2. Can I control the source?
3. How is the value processed?
4. What is the navigation sink?
5. What destination is generated?
6. Can I control the destination?
7. Is destination validation present?
8. Is origin validation present?
9. Is protocol validation present?
10. Does the browser actually navigate?
11. What is the security impact?
```

---

# 33. One-Minute Decision Tree

```text
Navigation Functionality?
        ↓
Potential Source?
        ↓
Can Attacker Control It?
        ↓
Navigation Sink?
        ↓
Does Data Reach Sink?
        ↓
Can Destination Be Controlled?
        ↓
Is Validation Effective?
        ↓
Browser Navigates?
        ↓
Security Impact?
        ↓
Document / Report
```

---

# 34. Core Mental Model

```text
SOURCE
  ↓
ATTACKER CONTROL
  ↓
DATA FLOW
  ↓
NAVIGATION SINK
  ↓
DESTINATION
  ↓
BROWSER NAVIGATION
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
NAVIGATION SINK
  +
ATTACKER-CONTROLLED DESTINATION
  +
REPRODUCIBLE NAVIGATION
  +
SECURITY IMPACT
  =
CONFIRMED DOM OPEN REDIRECTION
```