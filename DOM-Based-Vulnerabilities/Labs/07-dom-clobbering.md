# Lab 07 — DOM Clobbering

## 1. Lab Overview

DOM Clobbering is a client-side technique where HTML elements can interfere with JavaScript's expected properties or variables through browser DOM property resolution.

The core model is:

```text
Attacker-Controlled HTML
        ↓
DOM Element / Attribute
        ↓
Named DOM Property
        ↓
JavaScript Variable / Property
        ↓
Application Logic
        ↓
Security Impact
```

The key idea is:

```text
HTML Naming
      ↓
DOM Property Resolution
      ↓
JavaScript Behavior
```

---

# 2. What Is DOM Clobbering?

DOM Clobbering occurs when an attacker-controlled HTML element creates or overrides a property that JavaScript subsequently accesses.

A simplified example is:

```html
<a id="config" href="https://example.com"></a>
```

JavaScript may unexpectedly resolve:

```javascript
config
```

through the DOM.

The important point is that the JavaScript developer may expect:

```javascript
config
```

to refer to a normal variable or object, while the browser's DOM can expose an element with the same name.

---

# 3. Why DOM Clobbering Matters

Consider application code such as:

```javascript
let config = window.config || {};
```

If attacker-controlled HTML can create a DOM property named:

```text
config
```

the application may operate on an unexpected object.

Conceptually:

```text
Attacker HTML
      ↓
DOM Property
      ↓
Expected JavaScript Property
      ↓
Application Logic
```

---

# 4. Important DOM Clobbering Sources

DOM Clobbering generally requires attacker-controlled HTML to reach the page.

Potential sources include:

```text
Stored HTML
Reflected HTML
Sanitized HTML
User-generated content
HTML injection
Unsafe DOM manipulation
```

The first question is:

```text
Can the attacker place HTML into the relevant document?
```

---

# 5. Named DOM Properties

Browsers expose certain HTML elements through named properties.

Common attributes involved include:

```text
id
name
```

For example:

```html
<a id="test"></a>
```

may result in:

```javascript
window.test
```

being associated with the element.

The exact browser behavior depends on the element and property involved.

---

# 6. Basic Example

HTML:

```html
<a id="test"></a>
```

JavaScript:

```javascript
console.log(window.test);
```

The browser may resolve:

```text
window.test
```

to the DOM element.

This is the primitive that DOM Clobbering attacks build upon.

---

# 7. `id` Attribute

An element with an attacker-controlled `id` may create a named property.

Example:

```html
<a id="redirect"></a>
```

Potential access:

```javascript
window.redirect
```

Testing question:

```text
Does application JavaScript use the same property name?
```

---

# 8. `name` Attribute

Some elements expose named properties using:

```html
name=
```

For example:

```html
<form name="config"></form>
```

may influence:

```javascript
window.config
```

depending on browser and DOM context.

Therefore, during testing search for both:

```text
id=
name=
```

---

# 9. DOM Clobbering and Global Variables

A dangerous pattern is:

```javascript
if (window.config) {
    useConfig(window.config);
}
```

If an attacker can create:

```html
<a id="config"></a>
```

the application may unexpectedly enter the:

```javascript
window.config
```

branch.

The security impact depends on what happens next.

---

# 10. Object Property Clobbering

DOM Clobbering can also target properties accessed through objects.

Example:

```javascript
window.someObject.config
```

or:

```javascript
window.config.url
```

The important task is to understand:

```text
Which property does JavaScript expect?
Which property does the DOM provide?
```

---

# 11. Multi-Level Clobbering

More complex DOM Clobbering can involve multiple elements.

Conceptually:

```text
Element 1
   ↓
Object Property
   ↓
Element 2
   ↓
Nested Property
   ↓
Application Logic
```

For example, applications may expect:

```javascript
config.url
```

while attacker-controlled DOM elements cause:

```text
config
```

and:

```text
config.url
```

to resolve unexpectedly.

---

# 12. Why Multiple Elements Matter

One HTML element may provide one named property.

Multiple elements can sometimes create a structure that resembles an object.

Conceptually:

```text
HTML
 ↓
Named DOM Collection / Property
 ↓
Nested Property Resolution
 ↓
JavaScript
```

This is why DOM Clobbering testing should not stop after finding one global variable collision.

---

# 13. DOM Clobbering and `window`

When reviewing code, search for:

```javascript
window.variable
```

and:

```javascript
window["variable"]
```

Also look for implicit global access:

```javascript
variable
```

The question is:

```text
Could an attacker-controlled element cause this property to resolve unexpectedly?
```

---

# 14. Common Vulnerable Pattern

Example:

```javascript
let redirectURL = window.redirectURL || "/home";
```

If attacker-controlled HTML can create:

```html
<a id="redirectURL" href="..."></a>
```

then:

```javascript
window.redirectURL
```

may no longer be the value the developer expected.

---

# 15. DOM Clobbering with URLs

A common security-sensitive pattern is:

```javascript
let url = window.redirectURL || "/home";

location = url;
```

The flow becomes:

```text
Attacker-Controlled HTML
        ↓
DOM Property
        ↓
window.redirectURL
        ↓
url
        ↓
location
        ↓
Navigation
```

The security impact depends on the exact browser behavior and how the value is interpreted.

---

# 16. DOM Clobbering with Script Configuration

Another pattern is:

```javascript
let scriptURL = window.scriptURL || "/default.js";
```

followed by:

```javascript
script.src = scriptURL;
```

The flow becomes:

```text
Attacker HTML
      ↓
DOM Property
      ↓
window.scriptURL
      ↓
scriptURL
      ↓
script.src
      ↓
Resource Loading
```

Investigate whether the attacker can meaningfully control the resulting resource.

---

# 17. DOM Clobbering with `href`

Consider:

```javascript
let url = window.url;

link.href = url;
```

Potential flow:

```text
Attacker HTML
      ↓
Named Property
      ↓
window.url
      ↓
link.href
      ↓
Navigation
```

The exact impact depends on the URL context and browser behavior.

---

# 18. DOM Clobbering with `src`

Similarly:

```javascript
let source = window.source;

image.src = source;
```

Potential flow:

```text
DOM
 ↓
window.source
 ↓
source
 ↓
image.src
 ↓
Resource Request
```

Trace the final URL rather than assuming exploitation.

---

# 19. DOM Clobbering and Fallback Logic

One especially important pattern is:

```javascript
let value = window.someValue || defaultValue;
```

The application assumes:

```text
someValue absent
      ↓
defaultValue used
```

But DOM Clobbering can potentially cause:

```text
someValue
      ↓
unexpected DOM property
      ↓
truthy value
      ↓
default bypassed
```

This can alter application behavior.

---

# 20. DOM Clobbering and Security Checks

Look for code such as:

```javascript
if (window.config) {
    ...
}
```

or:

```javascript
if (window.isAdmin) {
    ...
}
```

or:

```javascript
if (window.trusted) {
    ...
}
```

The important question is:

```text
Does the application use the property as a security decision?
```

Never assume that a clobbered property automatically results in privilege escalation.

---

# 21. Step 1 — Find HTML Injection

First determine whether attacker-controlled HTML can reach the page.

Possible locations:

```text
Comments
Profiles
Search Results
User Content
Rich Text
Markdown
Stored Content
```

---

# 22. Step 2 — Determine HTML Filtering

Check whether the application:

```text
Allows HTML
Sanitizes HTML
Encodes HTML
Removes attributes
Removes tags
Uses a sanitizer library
```

DOM Clobbering often depends on whether specific elements and attributes survive filtering.

---

# 23. Step 3 — Search JavaScript

Search for:

```text
window.
document.
id
name
config
url
src
href
```

Also search for:

```text
|| default
?? default
```

because fallback logic is often important.

---

# 24. Step 4 — Identify the Expected Property

Example:

```javascript
const config = window.config || {};
```

Record:

```text
Property:
window.config

Fallback:
{}

Consumer:
config
```

---

# 25. Step 5 — Create a Harmless Collision

In an authorized lab, test with a benign identifier.

For example:

```html
<a id="test"></a>
```

Then inspect:

```javascript
window.test
```

in DevTools.

The purpose is to establish whether the browser exposes the element as the expected named property.

---

# 26. Step 6 — Match the Application Property

If the application accesses:

```javascript
window.config
```

test whether controlled HTML can create:

```html
<a id="config"></a>
```

Then inspect:

```javascript
window.config
```

---

# 27. Step 7 — Inspect the Resulting Object

Do not stop at:

```text
window.config exists
```

Determine:

```text
What is its type?
What properties does it have?
What methods are available?
What values does the application read?
```

Use DevTools:

```javascript
typeof window.config
```

and inspect the object interactively.

---

# 28. Step 8 — Trace the Consumer

Find every place where the clobbered property is used.

For example:

```javascript
window.config.url
```

then:

```javascript
location = window.config.url;
```

The complete chain becomes:

```text
Attacker HTML
      ↓
window.config
      ↓
window.config.url
      ↓
location
      ↓
Navigation
```

---

# 29. Step 9 — Confirm Security Impact

The final question is:

```text
What security-sensitive behavior occurs?
```

Possible impacts include:

```text
Unexpected navigation
Resource loading
Security-control bypass
Application state manipulation
Cross-origin interaction
JavaScript execution
```

The actual impact must be demonstrated.

---

# 30. DevTools Workflow

```text
DevTools
   ↓
Elements
   ↓
Inspect Injected HTML
   ↓
Console
   ↓
Check Named Property
   ↓
Sources
   ↓
Search window.<property>
   ↓
Set Breakpoint
   ↓
Trigger Functionality
   ↓
Inspect Value
   ↓
Trace Consumer
   ↓
Confirm Impact
```

---

# 31. Console Testing

Test whether an element creates a named property:

```javascript
window.test
```

Then inspect:

```javascript
typeof window.test
```

You can also compare:

```javascript
window.test === document.getElementById("test")
```

This can help establish the relationship between:

```text
DOM Element
```

and:

```text
Named Property
```

---

# 32. Inspecting the Live DOM

Use:

```text
DevTools → Elements
```

rather than:

```text
View Source
```

when verifying dynamically inserted HTML.

The live DOM represents the browser's current document state.

---

# 33. Search Patterns

Useful JavaScript searches include:

```text
window.
document.
|| 
??
getElementById
querySelector
id
name
href
src
config
url
```

Security-sensitive patterns:

```text
window.config
window.url
window.redirect
window.script
window.trusted
```

---

# 34. Common DOM Clobbering Targets

Potentially interesting property names include:

```text
config
url
redirect
redirectURL
script
src
href
callback
data
options
settings
```

These are examples only.

The actual target must come from application code.

---

# 35. DOM Clobbering + Open Redirect

Potential chain:

```text
Attacker HTML
      ↓
Clobbered Property
      ↓
URL Value
      ↓
location.href
      ↓
Open Redirect
```

The key is proving that the attacker controls the effective navigation target.

---

# 36. DOM Clobbering + Script Loading

Potential chain:

```text
Attacker HTML
      ↓
Clobbered Property
      ↓
Script URL
      ↓
script.src
      ↓
Script Loading
```

Investigate:

```text
URL validation
CSP
Trusted Types
Origin restrictions
```

before determining impact.

---

# 37. DOM Clobbering + Web Messages

DOM Clobbering may also appear in applications that process:

```javascript
event.data
```

and then access configuration through DOM-resolved properties.

Potential chain:

```text
Web Message
      ↓
Application Logic
      ↓
Clobbered Property
      ↓
Unexpected Behavior
```

Analyze the complete flow rather than treating DOM Clobbering as an isolated primitive.

---

# 38. DOM Clobbering + Sanitization

A sanitizer may remove:

```text
<script>
onerror
onclick
```

while allowing:

```text
<a>
<form>
id
name
href
```

If those surviving elements can create dangerous named properties, DOM Clobbering may still be possible.

Therefore:

```text
"HTML is sanitized"
      ≠
"DOM Clobbering is impossible"
```

---

# 39. Common Mistakes

## Mistake 1 — Assuming an `id` Is Automatically Dangerous

```html
<a id="test"></a>
```

is not a vulnerability by itself.

There must be a security-relevant consumer.

---

## Mistake 2 — Ignoring `name`

Some DOM properties can be influenced through:

```html
name=
```

as well as:

```html
id=
```

---

## Mistake 3 — Stopping at Property Creation

Finding:

```javascript
window.config
```

is only the beginning.

Trace:

```text
Property
  ↓
Consumer
  ↓
Sink
```

---

## Mistake 4 — Ignoring Fallbacks

Look carefully at:

```javascript
window.config || defaultConfig
```

and:

```javascript
window.url ?? defaultURL
```

---

## Mistake 5 — Assuming DOM Clobbering Means XSS

DOM Clobbering can lead to many different impacts.

Do not automatically label it:

```text
XSS
```

without demonstrating JavaScript execution.

---

# 40. Evidence Collection

Record:

```text
☐ Attacker-controlled HTML source
☐ HTML filtering behavior
☐ Element used
☐ id/name attribute
☐ Named property created
☐ JavaScript property accessed
☐ Expected value
☐ Actual value
☐ Consumer
☐ Sink
☐ Browser behavior
☐ Security impact
```

---

# 41. Lab Write-Up Template

```markdown
# Lab 07 — DOM Clobbering

## Objective

Demonstrate how attacker-controlled HTML can interfere with JavaScript property resolution and produce security-sensitive behavior.

## Injection Point

```text
[HTML injection point]
```

## Controlled HTML

```html
[Benign lab HTML]
```

## Clobbered Property

```javascript
window.[property]
```

## Vulnerable Code

```javascript
[Relevant JavaScript]
```

## Expected Behavior

```text
[What the developer intended]
```

## Actual Behavior

```text
[What the browser resolves]
```

## Taint Flow

```text
Attacker-Controlled HTML
        ↓
DOM Element
        ↓
Named Property
        ↓
JavaScript Property
        ↓
Application Logic
        ↓
Sink
        ↓
Security Impact
```

## Result

[Describe confirmed behavior.]

## Key Lesson

DOM Clobbering becomes security-relevant when attacker-controlled HTML changes a JavaScript property or object that the application subsequently trusts.
```

---

# 42. Quick Revision

## Primitive

```text
Attacker HTML
      ↓
id / name
      ↓
Named DOM Property
```

## Application Interaction

```text
Named Property
      ↓
JavaScript
      ↓
Application Logic
```

## Vulnerability

```text
Clobbered Property
      ↓
Security-Sensitive Consumer
      ↓
Impact
```

---

# 43. Key Patterns

### Global property

```javascript
window.config
```

### Fallback

```javascript
window.config || defaultConfig
```

### URL consumer

```javascript
location = window.url;
```

### Resource consumer

```javascript
script.src = window.scriptURL;
```

### DOM consumer

```javascript
element.setAttribute("href", window.url);
```

---

# 44. Master Checklist

```text
☐ HTML injection identified
☐ HTML filtering understood
☐ Allowed elements identified
☐ Allowed attributes identified
☐ id tested
☐ name tested
☐ Named property identified
☐ window property identified
☐ Expected application property identified
☐ Fallback logic checked
☐ Property consumer identified
☐ Sink identified
☐ Runtime behavior observed
☐ Security impact confirmed
☐ Evidence captured
☐ Finding documented
```

---

# 45. Final Detection Model

```text
ATTACKER-CONTROLLED HTML
          ↓
      id / name
          ↓
    DOM PROPERTY
          ↓
   JAVASCRIPT ACCESS
          ↓
   APPLICATION LOGIC
          ↓
        SINK
          ↓
   BROWSER BEHAVIOR
          ↓
   SECURITY IMPACT
```

---

# Final Rule

```text
ATTACKER-CONTROLLED HTML
        +
DOM NAMED PROPERTY
        +
APPLICATION TRUSTS PROPERTY
        +
SECURITY-SENSITIVE CONSUMER
        +
CONFIRMED IMPACT
        =
DOM CLOBBERING VULNERABILITY
```

The key mental model is:

```text
HTML
 ↓
DOM PROPERTY RESOLUTION
 ↓
JAVASCRIPT
 ↓
APPLICATION LOGIC
 ↓
SINK
 ↓
IMPACT
```

Do not stop at the clobbered property. **Always trace it to the final security-sensitive behavior.**