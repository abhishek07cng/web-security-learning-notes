# DOM-Based Vulnerabilities — DOM Clobbering

## 1. Overview

DOM clobbering is a technique in which attacker-controlled HTML can interfere with JavaScript references to DOM elements.

The browser automatically creates global variables or properties for elements with certain `id` and `name` attributes.

If application JavaScript assumes that a particular global variable or property refers to a trusted object, an attacker may be able to replace or influence that reference using HTML.

The core concept is:

```text
Attacker-Controlled HTML
        ↓
Element with id / name
        ↓
DOM Property / Global Variable
        ↓
Application JavaScript
        ↓
Unexpected Object / Value
        ↓
Security Impact
```

---

## 2. What Is DOM Clobbering?

DOM clobbering occurs when HTML elements overwrite, shadow, or interfere with JavaScript variables and properties that the application expects to contain specific values or objects.

For example:

```html
<a id="config"></a>
```

The browser may expose the element through:

```javascript
window.config
```

If application code expects:

```javascript
window.config
```

to contain an object or configuration value, the attacker-controlled element can change the application's behavior.

---

## 3. Why DOM Clobbering Matters

Modern web applications frequently use global variables and DOM APIs.

For example:

```javascript
let config = window.config || {};
```

If an attacker can influence the DOM before this code executes, the value of:

```javascript
window.config
```

may not be what the developer expects.

The security model becomes:

```text
Expected Object
      ↓
Application Trusts Reference
      ↓
DOM Clobbering
      ↓
Unexpected DOM Element
      ↓
Application Behavior Changes
```

---

## 4. HTML `id` and Global Variables

An HTML element with an `id` may become accessible through the global `window` object.

Example:

```html
<div id="test"></div>
```

JavaScript may be able to access it as:

```javascript
window.test
```

and potentially:

```javascript
test
```

depending on browser behavior and execution context.

This creates an important relationship:

```text
HTML id
   ↓
DOM
   ↓
window Property
   ↓
JavaScript Reference
```

---

## 5. Basic DOM Clobbering Example

Consider:

```html
<a id="config"></a>
```

JavaScript may resolve:

```javascript
window.config
```

to the HTML element.

If application code performs:

```javascript
if (window.config) {
    useConfig(window.config);
}
```

the attacker-controlled element may influence the application logic.

The important point is:

```text
HTML
  ↓
DOM
  ↓
JavaScript Reference
```

---

## 6. `id` Attribute

The `id` attribute can create a named property on the global object in relevant browser contexts.

Example:

```html
<form id="login"></form>
```

Potentially:

```javascript
window.login
```

The exact behavior depends on the element and browser environment.

For testing, verify the behavior directly in the browser.

---

## 7. `name` Attribute

The `name` attribute can also participate in named property behavior.

For example:

```html
<form name="config"></form>
```

may create a reference accessible through:

```javascript
window.config
```

DOM clobbering therefore commonly involves:

```text
id
name
```

attributes.

---

## 8. HTML Elements Commonly Used

Elements that may be relevant include:

```text
<a>
<form>
<iframe>
<img>
<object>
```

The exact behavior depends on the element and the properties being accessed.

Always verify the resulting DOM object.

---

## 9. DOM Clobbering as a Source

In a DOM-based vulnerability model, attacker-controlled HTML creates the source.

Conceptually:

```text
Attacker-Controlled HTML
        ↓
DOM Element
        ↓
Named Property
        ↓
Application JavaScript
```

The application may then use the clobbered property in a security-sensitive operation.

---

## 10. Property Clobbering

DOM clobbering can affect properties that application code expects to contain values.

For example:

```javascript
const redirect = window.redirect || "/home";
```

If an attacker can create:

```html
<a id="redirect"></a>
```

then:

```javascript
window.redirect
```

may resolve to the element instead of the expected value.

The application may then process the unexpected value.

---

## 11. Clobbering Variables

Consider:

```javascript
let url = window.url || "https://example.com";
```

If the DOM contains:

```html
<a id="url"></a>
```

the application may receive an unexpected object instead of the intended URL value.

The important security question is:

```text
Does the application perform security-sensitive operations
with the clobbered value?
```

---

## 12. DOM Clobbering and Fallback Logic

A particularly important pattern is:

```javascript
const config = window.config || defaultConfig;
```

The developer assumes:

```text
If config does not exist
      ↓
Use defaultConfig
```

However, attacker-controlled HTML may cause:

```text
window.config
      ↓
Unexpected DOM Element
```

Therefore:

```text
window.config exists
      ↓
Fallback is not used
      ↓
Unexpected object reaches application logic
```

---

## 13. Why `||` Can Be Relevant

Consider:

```javascript
const url = window.url || "/default";
```

The fallback only executes if:

```javascript
window.url
```

is falsy.

A DOM-clobbered element may be truthy.

Therefore:

```text
Clobbered Element
      ↓
Truthy
      ↓
Fallback Bypassed
```

This can produce unexpected application behavior.

---

## 14. DOM Clobbering and Property Access

An application may access properties on the clobbered element.

For example:

```javascript
const config = window.config;
const value = config.href;
```

If:

```html
<a id="config" href="..."></a>
```

is injected, the application may receive an object with an `href` property.

The flow becomes:

```text
Attacker HTML
      ↓
<a id="config" href="...">
      ↓
window.config
      ↓
config.href
      ↓
Application Logic
```

---

## 15. Clobbering Object Properties

DOM clobbering can be used to influence nested property access.

For example:

```javascript
const config = window.config || {};
const url = config.url || "/home";
```

The attacker may attempt to influence:

```text
window.config
      ↓
config.url
```

using suitable DOM elements.

The exact object structure depends on the browser's named-property behavior.

---

## 16. Multiple Elements

Some DOM clobbering techniques use multiple elements to create a more complex object structure.

For example:

```html
<form id="config">
    <input name="url" value="...">
</form>
```

This can potentially produce:

```text
window.config
      ↓
Form Element
      ↓
url
```

The resulting structure should be inspected directly in the browser.

---

## 17. Named Properties

The important browser behavior is often described as named properties.

Conceptually:

```text
HTML Element
      ↓
id / name
      ↓
Named DOM Property
      ↓
window / Document
      ↓
JavaScript
```

DOM clobbering exploits this relationship.

---

## 18. Testing DOM Clobbering

### Step 1 — Identify HTML Injection

First determine whether attacker-controlled HTML can be inserted into the page.

Possible locations include:

```text
Comments
Profile Fields
Rich Text
HTML Content
User-Generated Content
```

---

### Step 2 — Identify JavaScript Globals

Search client-side JavaScript for:

```text
window.
global variables
fallback expressions
```

Look for patterns such as:

```javascript
window.config
window.url
window.redirect
```

---

### Step 3 — Identify Fallback Logic

Search for:

```javascript
|| default
```

or:

```javascript
?? default
```

and similar patterns.

These may indicate that the application assumes a value is absent and falls back to a default.

---

### Step 4 — Determine Whether the DOM Can Control the Property

Test whether an attacker-controlled element can create the expected named property.

---

### Step 5 — Trace the Property

Follow:

```text
HTML Element
      ↓
window Property
      ↓
Application Variable
      ↓
Property Access
      ↓
Security-Sensitive Operation
```

---

## 19. Browser Console Testing

The browser console can be used to inspect named properties.

Example:

```javascript
window.test
```

After inserting:

```html
<a id="test"></a>
```

check:

```javascript
window.test
```

Determine whether it resolves to the injected element.

---

## 20. Inspecting the DOM

Use:

```text
DevTools
   ↓
Elements
```

Look for:

```text
id
name
```

attributes.

Then use:

```text
DevTools
   ↓
Console
```

to inspect the corresponding global property.

---

## 21. Finding Clobberable Variables

Search JavaScript for patterns such as:

```javascript
window.variable
```

and:

```javascript
window.variable || fallback
```

Also look for:

```javascript
document.variable
```

and variables that are implicitly resolved through global scope.

---

## 22. DOM Clobbering with URLs

A clobbered DOM element may provide URL-related properties.

For example:

```html
<a id="redirect" href="https://example.com"></a>
```

The application may access:

```javascript
window.redirect.href
```

The flow is:

```text
Attacker HTML
      ↓
<a id="redirect" href="...">
      ↓
window.redirect
      ↓
redirect.href
      ↓
Application Navigation Logic
```

This can become security-sensitive if the application assumes the URL is trusted.

---

## 23. DOM Clobbering + Open Redirect

A potential attack chain is:

```text
HTML Injection
      ↓
DOM Clobbering
      ↓
Clobbered URL Property
      ↓
Navigation Logic
      ↓
Unexpected Destination
```

The final impact depends on whether the attacker can control the destination.

---

## 24. DOM Clobbering + JavaScript Execution

DOM clobbering can also participate in an execution chain when a clobbered property eventually reaches a dangerous sink.

Conceptually:

```text
Attacker HTML
      ↓
DOM Clobbering
      ↓
Unexpected Property
      ↓
Application Logic
      ↓
Dangerous Sink
      ↓
JavaScript Execution
```

The complete source-to-sink chain must be demonstrated.

---

## 25. DOM Clobbering + Web Messages

A Web Message can potentially provide data that becomes HTML, which then creates a clobbered DOM property.

Conceptual flow:

```text
postMessage()
      ↓
event.data
      ↓
HTML Sink
      ↓
DOM Element
      ↓
Clobbered Property
      ↓
Application Logic
```

This demonstrates why DOM vulnerabilities can combine into multi-stage attack chains.

---

## 26. DOM Clobbering and HTML Sanitization

A sanitizer may restrict which elements and attributes can be injected.

Therefore, when testing:

```text
HTML Injection
      ↓
Sanitization
      ↓
DOM Clobbering
```

determine:

```text
Which elements are allowed?
Which attributes are allowed?
Are id attributes allowed?
Are name attributes allowed?
```

Do not assume that HTML injection automatically enables DOM clobbering.

---

## 27. Testing Methodology

The complete methodology is:

```text
START
  ↓
Identify HTML Injection
  ↓
Identify JavaScript Global / Property
  ↓
Identify Fallback Logic
  ↓
Determine Named Property Behavior
  ↓
Create Controlled DOM Element
  ↓
Verify window Property
  ↓
Trace Property Usage
  ↓
Identify Security-Sensitive Sink
  ↓
Confirm Browser Behavior
  ↓
Assess Impact
```

---

## 28. DevTools Workflow

```text
Open DevTools
      ↓
Elements
      ↓
Identify User-Controlled HTML
      ↓
Inspect id / name
      ↓
Console
      ↓
Inspect window.<property>
      ↓
Sources
      ↓
Find Property Usage
      ↓
Set Breakpoint
      ↓
Trace Data Flow
      ↓
Confirm Impact
```

---

## 29. Burp Suite Workflow

```text
Burp Proxy
      ↓
Identify HTML Injection Point
      ↓
Send Controlled Input
      ↓
Open Target in Browser
      ↓
Inspect Live DOM
      ↓
Identify id / name
      ↓
Inspect JavaScript
      ↓
Trace Clobbered Property
      ↓
Identify Security-Sensitive Operation
      ↓
Confirm Behavior
```

---

## 30. Testing Questions

Ask:

```text
1. Can attacker-controlled HTML reach the DOM?
2. Which HTML elements are allowed?
3. Are id attributes allowed?
4. Are name attributes allowed?
5. Which global variables does the application use?
6. Does window.<property> exist?
7. Is fallback logic used?
8. Can a DOM element replace the expected value?
9. Does the application access properties on the clobbered object?
10. Does the clobbered value reach a security-sensitive operation?
11. Can it influence navigation?
12. Can it influence script execution?
13. Can it influence application state?
14. What is the final security impact?
```

---

## 31. Common Mistakes

### Mistake 1 — Assuming Every `id` Is Dangerous

The presence of:

```html
id="test"
```

does not automatically create a vulnerability.

There must be a meaningful interaction with application JavaScript.

---

### Mistake 2 — Ignoring the JavaScript

DOM clobbering is about the interaction between:

```text
DOM
+
JavaScript
```

Finding a named element alone is not sufficient.

---

### Mistake 3 — Ignoring Fallback Logic

Pay special attention to:

```javascript
window.value || fallback
```

because clobbering can potentially prevent the fallback from being used.

---

### Mistake 4 — Assuming `JSON.parse()` Is the Sink

If a clobbered value comes from JSON-derived application state, continue tracing the value.

The dangerous operation may occur later.

---

### Mistake 5 — Stopping at the Clobbered Property

Finding:

```javascript
window.config
```

is only the beginning.

Continue:

```text
window.config
      ↓
Application Logic
      ↓
Sink
      ↓
Impact
```

---

## 32. Source → Sink Examples

### Example 1 — Basic Property

```text
Attacker HTML
      ↓
id="config"
      ↓
window.config
      ↓
Application Logic
```

### Example 2 — URL Property

```text
Attacker HTML
      ↓
<a id="redirect" href="...">
      ↓
window.redirect
      ↓
redirect.href
      ↓
Navigation
```

### Example 3 — Fallback Bypass

```text
Attacker HTML
      ↓
id="config"
      ↓
window.config
      ↓
window.config || defaultConfig
      ↓
Clobbered Object Used
```

### Example 4 — Security-Sensitive Sink

```text
Attacker HTML
      ↓
DOM Clobbering
      ↓
Application Variable
      ↓
Dangerous Sink
      ↓
Security Impact
```

---

## 33. Evidence Collection

Capture:

```text
☐ HTML injection point
☐ Injected element
☐ id / name attribute
☐ Resulting DOM
☐ window property
☐ Relevant JavaScript
☐ Fallback logic
☐ Property access
☐ Final sink
☐ Browser behavior
☐ Reproduction steps
☐ Security impact
```

---

## 34. Reporting Structure

A good report should show:

```text
HTML Injection
      ↓
DOM Element
      ↓
Named Property
      ↓
JavaScript Reference
      ↓
Application Logic
      ↓
Security-Sensitive Operation
      ↓
Impact
```

Include:

```text
Title
Affected Functionality
Injection Point
Injected HTML
Clobbered Property
Relevant JavaScript
Data Flow
Reproduction Steps
Observed Behavior
Impact
Remediation
```

---

## 35. Remediation Principles

General defensive principles include:

```text
☐ Avoid relying on implicit global variables created from DOM ids
☐ Use explicit variable declarations
☐ Avoid trusting DOM-created named properties
☐ Validate user-controlled HTML
☐ Sanitize HTML using an appropriate allowlist
☐ Restrict id and name attributes where appropriate
☐ Avoid dangerous sinks
☐ Validate security-sensitive values before use
☐ Use explicit object references instead of global DOM properties
```

---

## 36. Quick Reference

### Common HTML Attributes

```text
id
name
```

### Common Elements

```text
<a>
<form>
<iframe>
<img>
<object>
```

### Common Global Access

```javascript
window.property
```

### Common Vulnerable Pattern

```javascript
const value = window.value || fallback;
```

### Important Security Areas

```text
Navigation
URLs
JavaScript execution
Application state
Security-sensitive configuration
```

---

## 37. Complete Testing Workflow

```text
START
  ↓
Find HTML Injection
  ↓
Determine Allowed HTML
  ↓
Identify id / name Possibilities
  ↓
Identify JavaScript Globals
  ↓
Test Named Property Creation
  ↓
Inspect window Property
  ↓
Find Property Usage
  ↓
Trace Application Logic
  ↓
Identify Security-Sensitive Sink
  ↓
Confirm Behavior
  ↓
Assess Impact
  ↓
Document Finding
```

---

## 38. Final Checklist

```text
☐ HTML injection confirmed
☐ Allowed elements identified
☐ id attributes checked
☐ name attributes checked
☐ JavaScript globals identified
☐ Named property behavior tested
☐ window property inspected
☐ Fallback logic reviewed
☐ Property access traced
☐ URL properties reviewed
☐ Navigation logic reviewed
☐ Dangerous sinks reviewed
☐ Sanitization reviewed
☐ Browser behavior confirmed
☐ Exploitability confirmed
☐ Security impact confirmed
☐ Evidence captured
☐ Remediation documented
```

---

# Final Mental Model

```text
ATTACKER-CONTROLLED HTML
          ↓
id / name ATTRIBUTE
          ↓
DOM NAMED PROPERTY
          ↓
window / JAVASCRIPT REFERENCE
          ↓
APPLICATION LOGIC
          ↓
SECURITY-SENSITIVE OPERATION
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
APPLICATION TRUSTS CLOBBERED REFERENCE
        +
SECURITY-SENSITIVE USE
        +
REPRODUCIBLE BEHAVIOR
        +
SECURITY IMPACT
        =
CONFIRMED DOM CLOBBERING VULNERABILITY
```