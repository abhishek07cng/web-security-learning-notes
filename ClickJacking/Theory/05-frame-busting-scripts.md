# Frame-Busting Scripts

## Overview

Some websites attempt to defend against clickjacking using client-side JavaScript known as frame-busting scripts.

The basic idea is to detect whether the page is being displayed inside a frame and then attempt to prevent the framing.

---

# Basic Concept

```text
Target Page
    ↓
JavaScript Executes
    ↓
Checks Whether Page Is Framed
    ↓
Frame Detected
    ↓
Frame-Busting Action
```

---

# Typical Frame Detection

A frame-busting script may compare:

```javascript
window.top
```

with:

```javascript
window.self
```

Conceptually:

```javascript
if (window.top !== window.self) {
    // page is framed
}
```

The application may then attempt to navigate the top-level window.

---

# Why Frame-Busting Is a Client-Side Defense

Frame-busting depends on JavaScript executing correctly inside the browser.

Therefore:

```text
JavaScript Behavior
        ↓
Browser Enforcement
```

rather than:

```text
Server
   ↓
HTTP Header
   ↓
Browser Enforcement
```

This distinction is important when assessing the strength of the defense.

---

# Basic Frame-Busting Logic

A simplified example is:

```javascript
if (window.top !== window.self) {
    window.top.location = window.self.location;
}
```

The intention is:

```text
Page detects iframe
        ↓
Attempts to escape iframe
```

---

# Testing Frame-Busting

When testing an authorized target:

```text
1. Determine whether the page can be framed.
2. Load the page in an iframe.
3. Observe whether the page attempts to escape.
4. Inspect the JavaScript responsible for frame-busting.
5. Determine whether browser restrictions affect the script.
```

---

# Browser Restrictions

Frame-busting scripts can depend on browser behavior involving:

```text
Cross-origin frames
Top-level navigation
Sandboxed iframes
JavaScript execution
```

The exact result depends on the browser and iframe configuration.

---

# iframe Sandbox

HTML5 provides the `sandbox` attribute.

Example:

```html
<iframe
    src="https://victim-website.com"
    sandbox="allow-forms">
</iframe>
```

The sandbox can restrict actions available to the framed document.

---

# Relevant Sandbox Behavior

The supplied material describes a technique where:

```text
allow-forms
```

is permitted while:

```text
allow-top-navigation
```

is omitted.

This can interfere with frame-busting behavior that attempts to navigate the top-level window.

Conceptually:

```text
Target Page
     ↓
Frame-Busting Script
     ↓
Attempts Top-Level Navigation
     ↓
Sandbox Restriction
     ↓
Navigation Prevented
```

---

# Why This Matters

A frame-busting script may exist but still fail to provide effective protection under certain browser and iframe conditions.

Therefore:

```text
Frame-Busting Script Present
        ≠
Clickjacking Fully Prevented
```

---

# Testing Workflow

```text
Identify Frameable Page
        ↓
Inspect Response Headers
        ↓
Search JavaScript for Frame-Busting Logic
        ↓
Load Page in iframe
        ↓
Observe Frame Behavior
        ↓
Test Browser Restrictions
        ↓
Determine Whether Framing Can Be Maintained
```

---

# Burp Suite

Use Burp Suite to inspect:

```text
Proxy → HTTP history
```

Review:

```text
HTML
JavaScript
Response Headers
```

Search for terms such as:

```text
window.top
window.self
top.location
parent.location
frame
iframe
```

---

# Important Defensive Distinction

Client-side frame-busting should not be considered equivalent to server-side framing controls.

Server-side mechanisms include:

```http
X-Frame-Options: DENY
```

and:

```http
Content-Security-Policy: frame-ancestors 'none';
```

These provide browser-enforced restrictions based on response headers.

---

# Testing Checklist

```text
☐ Determine whether page is frameable
☐ Inspect X-Frame-Options
☐ Inspect Content-Security-Policy
☐ Search JavaScript for frame-busting logic
☐ Identify window.top checks
☐ Identify top-level navigation
☐ Test iframe behavior
☐ Test sandbox behavior in authorized labs
☐ Observe whether frame-busting succeeds
☐ Document browser-specific behavior
```

---

# Key Takeaways

- Frame-busting scripts are client-side clickjacking defenses.
- They commonly detect whether the page is running inside a frame.
- JavaScript may attempt to navigate the page out of the iframe.
- Browser and iframe restrictions can affect frame-busting behavior.
- The supplied material demonstrates the relevance of the iframe `sandbox` attribute.
- `allow-forms` can permit form functionality while omitting `allow-top-navigation`.
- The presence of frame-busting JavaScript does not automatically prove that clickjacking is impossible.
- Server-side protections such as `X-Frame-Options` and CSP `frame-ancestors` provide stronger framing controls.