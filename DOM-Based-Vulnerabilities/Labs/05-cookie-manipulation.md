# Lab 05 — DOM-Based Cookie Manipulation

## 1. Lab Overview

DOM-based cookie manipulation occurs when client-side JavaScript takes attacker-controlled data and uses it to create or modify a browser cookie.

The basic model is:

```text
Attacker-Controlled Input
        ↓
DOM Source
        ↓
JavaScript Processing
        ↓
document.cookie
        ↓
Cookie Created / Modified
        ↓
Application Consumes Cookie
        ↓
Security Impact
```

The important mental model is:

```text
SOURCE → PROPAGATION → COOKIE SINK → CONSUMER → IMPACT
```

---

# 2. What Is Cookie Manipulation?

JavaScript can interact with cookies through:

```javascript
document.cookie
```

For example:

```javascript
document.cookie = "theme=dark";
```

A vulnerability can occur when attacker-controlled data is incorporated into a cookie value without appropriate validation.

Conceptually:

```text
Untrusted Input
      ↓
JavaScript
      ↓
document.cookie
```

The security impact depends on how the application subsequently uses the modified cookie.

---

# 3. Why `document.cookie` Matters

Search client-side JavaScript for:

```text
document.cookie
```

Pay particular attention to assignments:

```javascript
document.cookie = ...
```

The important question is:

```text
Can attacker-controlled data influence the value being written?
```

---

# 4. Vulnerable Pattern

A simplified vulnerable pattern is:

```javascript
document.cookie = "name=" + value;
```

If:

```text
value
```

is attacker-controlled:

```text
Attacker Input
      ↓
value
      ↓
" name=" + value
      ↓
document.cookie
```

the attacker may influence the resulting cookie.

---

# 5. Source Identification

Potential sources include:

```text
location.search
location.hash
location.pathname
document.URL
document.referrer
window.name
event.data
localStorage
sessionStorage
```

The source must be verified in the actual application.

---

# 6. Cookie Sink

The main sink is:

```javascript
document.cookie =
```

For testing, search JavaScript for:

```text
document.cookie =
```

rather than only searching for the word:

```text
cookie
```

---

# 7. Source → Sink Model

Example:

```javascript
const value = location.hash.slice(1);

document.cookie = "user=" + value;
```

The complete flow is:

```text
location.hash
      ↓
slice(1)
      ↓
value
      ↓
document.cookie
      ↓
user cookie
```

---

# 8. Step 1 — Identify the Functionality

Look for functionality that changes browser state.

Examples:

```text
Preferences
Language
Theme
Tracking
User Settings
Session State
Shopping State
```

Then inspect the JavaScript associated with the functionality.

---

# 9. Step 2 — Search JavaScript

Search for:

```text
document.cookie
```

Also search for:

```text
cookie =
cookie+
Set-Cookie
document.cookie =
```

The main objective is to identify where the browser cookie is created or modified.

---

# 10. Step 3 — Identify the Input

Determine where the cookie value originates.

For example:

```javascript
let value = location.search;
```

or:

```javascript
let value = location.hash;
```

Then trace the value forward.

---

# 11. Step 4 — Insert a Unique Marker

Use a harmless marker:

```text
cookietest123
```

For example:

```text
#cookietest123
```

Then inspect:

```text
DevTools → Application → Cookies
```

Determine whether the marker appears in a cookie.

---

# 12. Step 5 — Inspect the Cookie

Open:

```text
DevTools
    ↓
Application
    ↓
Storage
    ↓
Cookies
```

Check:

```text
Name
Value
Domain
Path
Expires
HttpOnly
Secure
SameSite
```

The important question is:

```text
Did attacker-controlled data reach the cookie value?
```

---

# 13. Step 6 — Trace Transformations

The value may be transformed before reaching `document.cookie`.

Look for:

```text
slice()
substring()
replace()
decodeURI()
decodeURIComponent()
encodeURI()
encodeURIComponent()
```

Record the transformation chain.

Example:

```text
location.hash
      ↓
slice(1)
      ↓
decodeURIComponent()
      ↓
document.cookie
```

---

# 14. Cookie Syntax

A basic cookie assignment looks like:

```javascript
document.cookie = "name=value";
```

Additional attributes may include:

```text
Path
Domain
Expires
Max-Age
Secure
SameSite
```

For example:

```javascript
document.cookie = "name=value; Path=/";
```

The exact behavior depends on the browser and cookie attributes.

---

# 15. Cookie Attribute Injection

When testing a vulnerable cookie assignment, determine whether attacker-controlled input can influence cookie attributes.

Conceptually:

```text
Attacker Input
      ↓
Cookie String
      ↓
Cookie Name / Value
      ↓
Cookie Attributes
```

The exact impact must be verified experimentally.

---

# 16. Cookie Scope

Important cookie properties include:

```text
Domain
Path
Secure
HttpOnly
SameSite
```

These affect where and how the browser sends the cookie.

Do not assume that modifying a cookie automatically means the cookie is sent everywhere.

---

# 17. Cookie Name vs Cookie Value

Determine whether attacker control affects:

```text
Cookie Name
```

or:

```text
Cookie Value
```

For example:

```javascript
document.cookie = "theme=" + value;
```

controls the value.

Another pattern may construct a larger cookie string from attacker-controlled input.

Always identify the exact controlled component.

---

# 18. Cookie Consumer

Creating a controllable cookie is not necessarily the final security impact.

Trace where the application uses the cookie.

Possible consumers include:

```text
Client-side JavaScript
Server-side application logic
Authentication state
Authorization decisions
HTML generation
Redirect logic
User preferences
Feature flags
```

The complete model is:

```text
Source
  ↓
document.cookie
  ↓
Cookie
  ↓
Consumer
  ↓
Impact
```

---

# 19. Why the Consumer Matters

Consider:

```text
Attacker
   ↓
Modify harmless preference cookie
   ↓
Application reads cookie
   ↓
Only changes theme
```

This may have little or no security impact.

Compare:

```text
Attacker
   ↓
Modify cookie
   ↓
Application trusts cookie for security decision
   ↓
Authorization / authentication behavior changes
```

This is potentially much more serious.

---

# 20. Testing Methodology

```text
START
  ↓
Identify Cookie Functionality
  ↓
Find document.cookie
  ↓
Identify Source
  ↓
Insert Unique Marker
  ↓
Confirm Cookie Modification
  ↓
Trace Transformations
  ↓
Identify Controlled Cookie Component
  ↓
Find Cookie Consumer
  ↓
Assess Security Impact
  ↓
Document Source → Sink → Consumer
```

---

# 21. DevTools Workflow

```text
DevTools
   ↓
Sources
   ↓
Search:
   document.cookie
   ↓
Identify Assignment
   ↓
Trace Input
   ↓
Set Breakpoint
   ↓
Trigger Functionality
   ↓
Inspect Runtime Value
   ↓
Application
   ↓
Cookies
   ↓
Confirm Result
```

---

# 22. Console Testing

You can inspect cookies using:

```javascript
document.cookie
```

This shows cookies accessible to JavaScript in the current context.

Important:

```text
HttpOnly cookies
```

are not accessible through:

```javascript
document.cookie
```

Therefore, the absence of a cookie from `document.cookie` does not necessarily mean the browser has no such cookie.

---

# 23. Burp Suite Workflow

```text
Burp Suite
      ↓
Open Burp Browser
      ↓
Load Target
      ↓
HTTP History
      ↓
Inspect JavaScript
      ↓
Search document.cookie
      ↓
Identify Source
      ↓
Trigger Functionality
      ↓
Inspect Browser Cookies
      ↓
Trace Cookie Consumer
      ↓
Confirm Impact
```

---

# 24. DOM Invader

DOM Invader can assist with identifying:

```text
Sources
Sinks
Taint Flow
```

For DOM-based cookie manipulation, manually verify:

```text
Source
  ↓
document.cookie
  ↓
Cookie
  ↓
Consumer
```

Automation is useful for discovery, but the security impact still needs to be confirmed.

---

# 25. Cookie Manipulation and DOM XSS

Cookie manipulation can sometimes become part of a larger DOM-XSS chain.

Conceptually:

```text
Attacker Input
      ↓
document.cookie
      ↓
Cookie Value
      ↓
Application Reads Cookie
      ↓
DOM Sink
      ↓
JavaScript Execution
```

For example:

```text
Cookie
  ↓
document.cookie
  ↓
innerHTML
  ↓
XSS
```

The exact chain must be demonstrated in the application.

---

# 26. Cookie Manipulation and Open Redirect

Another possible chain is:

```text
Attacker Input
      ↓
Cookie
      ↓
Application Reads Cookie
      ↓
Navigation Logic
      ↓
location.href
      ↓
Redirect
```

Again, the impact depends on the application's actual behavior.

---

# 27. Cookie Manipulation and Application State

Cookies are frequently used to store:

```text
Preferences
Feature Flags
State
Identifiers
Configuration
```

If a security-sensitive decision relies on a client-controlled cookie, test whether the value can influence that decision.

---

# 28. Testing Cookie Attributes

Inspect:

```text
Domain
Path
Secure
HttpOnly
SameSite
Expires
Max-Age
```

Questions:

```text
Can the attacker influence the Path?
Can the attacker influence the Domain?
Is Secure set?
Is HttpOnly set?
What SameSite policy is used?
```

Do not infer exploitability solely from the presence or absence of one attribute.

---

# 29. Cookie Shadowing

Multiple cookies with the same name can behave differently depending on:

```text
Domain
Path
```

This can create confusing application behavior.

When investigating a cookie vulnerability, record:

```text
Cookie Name
Cookie Value
Domain
Path
```

and determine which cookie the application actually consumes.

---

# 30. Cookie Scope Testing

Check:

```text
Current Domain
Parent Domain
Subdomains
Path
```

A cookie available to one path may not be available to another.

Likewise, a host-only cookie behaves differently from a domain cookie.

---

# 31. Common Mistakes

## Mistake 1 — Treating `document.cookie` as Automatically Vulnerable

The presence of:

```javascript
document.cookie
```

does not prove a vulnerability.

You need attacker control.

---

## Mistake 2 — Stopping After Cookie Modification

Creating a cookie is not necessarily the final impact.

Find:

```text
Cookie Consumer
```

---

## Mistake 3 — Ignoring Cookie Attributes

Always inspect:

```text
Domain
Path
Secure
HttpOnly
SameSite
```

---

## Mistake 4 — Assuming All Cookies Are JavaScript Accessible

Cookies marked:

```text
HttpOnly
```

cannot be read through:

```javascript
document.cookie
```

---

## Mistake 5 — Ignoring Server-Side Consumption

A cookie may be created client-side but consumed by the server on a subsequent request.

Inspect:

```text
HTTP Request
Cookie Header
Server Response
Application Behavior
```

---

# 32. HTTP Request Verification

After modifying a cookie, use:

```text
Burp Proxy
```

or:

```text
DevTools → Network
```

to determine whether the browser sends the cookie.

Inspect:

```text
Cookie:
```

in the HTTP request.

The flow becomes:

```text
JavaScript
   ↓
document.cookie
   ↓
Browser Cookie Store
   ↓
HTTP Request
   ↓
Cookie Header
   ↓
Server
```

---

# 33. Evidence Collection

Record:

```text
☐ Vulnerable functionality
☐ Source
☐ JavaScript assignment
☐ Input marker
☐ Cookie name
☐ Cookie value
☐ Domain
☐ Path
☐ Secure
☐ HttpOnly
☐ SameSite
☐ Cookie consumer
☐ HTTP request
☐ Application behavior
☐ Final security impact
```

---

# 34. Lab Write-Up Template

```markdown
# Lab 05 — DOM-Based Cookie Manipulation

## Objective

Identify attacker-controlled data that reaches document.cookie and determine the resulting security impact.

## Source

```text
[Source]
```

## Sink

```javascript
document.cookie =
```

## Vulnerable Code

```javascript
[Relevant code]
```

## Cookie

```text
Name:
Value:
Domain:
Path:
```

## Taint Flow

```text
Attacker Input
      ↓
Source
      ↓
JavaScript Processing
      ↓
document.cookie
      ↓
Cookie
      ↓
Application Consumer
      ↓
Security Impact
```

## Testing Steps

1. Identify cookie assignment.
2. Identify source.
3. Insert unique marker.
4. Trigger functionality.
5. Inspect browser cookie storage.
6. Trace cookie consumer.
7. Confirm security impact.

## Result

[Describe confirmed behavior.]

## Key Lesson

A controllable cookie becomes security-relevant when the application trusts and uses the manipulated value in a security-sensitive context.
```

---

# 35. Quick Revision

## Main Sink

```javascript
document.cookie =
```

## Main Source Categories

```text
location.search
location.hash
location.pathname
document.URL
document.referrer
window.name
event.data
```

## Important Cookie Properties

```text
Name
Value
Domain
Path
Secure
HttpOnly
SameSite
```

---

# 36. One-Line Taint Flow

```text
Attacker Input → DOM Source → document.cookie → Cookie → Application Consumer → Impact
```

---

# 37. Master Checklist

```text
☐ Cookie functionality identified
☐ document.cookie searched
☐ Cookie assignment identified
☐ Source identified
☐ Attacker control confirmed
☐ Unique marker used
☐ Cookie modification confirmed
☐ Cookie name identified
☐ Cookie value identified
☐ Domain checked
☐ Path checked
☐ Secure checked
☐ HttpOnly checked
☐ SameSite checked
☐ HTTP Cookie header checked
☐ Cookie consumer identified
☐ Security-sensitive use identified
☐ Impact confirmed
☐ Evidence captured
☐ Finding documented
```

---

# 38. Final Mental Model

```text
                 ATTACKER
                    ↓
             CONTROLLED INPUT
                    ↓
                DOM SOURCE
                    ↓
              JAVASCRIPT
                    ↓
             document.cookie
                    ↓
              COOKIE STORE
                    ↓
            COOKIE CONSUMER
                    ↓
          SECURITY-SENSITIVE
               OPERATION
                    ↓
                IMPACT
```

---

# Final Rule

```text
ATTACKER-CONTROLLED SOURCE
        +
document.cookie
        +
CONTROLLED COOKIE VALUE / ATTRIBUTE
        +
SECURITY-SENSITIVE CONSUMER
        +
REPRODUCIBLE IMPACT
        =
CONFIRMED DOM-BASED COOKIE MANIPULATION
```