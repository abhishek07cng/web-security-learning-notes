# Clickjacking With DOM XSS

## Overview

Clickjacking can sometimes be combined with a DOM-based XSS vulnerability.

In this scenario, the clickjacking technique is used to trick the victim into interacting with a vulnerable element inside a framed page.

The two vulnerabilities can therefore be chained:

```text
Clickjacking
      +
DOM XSS
      ↓
Combined Attack
```

---

# Core Concept

```text
Attacker-Controlled Page
        ↓
Target Page Loaded in iframe
        ↓
DOM XSS Vulnerability
        ↓
Victim Clicks Decoy
        ↓
Vulnerable Functionality Triggered
        ↓
JavaScript Executes
```

---

# DOM XSS

DOM-based XSS occurs when client-side JavaScript processes attacker-controlled data and writes it into a dangerous context.

The vulnerability exists in the browser-side processing of the data.

---

# Common Sources

Potential DOM XSS sources include:

```text
URL parameters
document.URL
document.location
document.referrer
window.name
```

The exact source depends on the application's JavaScript.

---

# Common Dangerous Sinks

Examples include:

```text
innerHTML
outerHTML
document.write()
eval()
```

Other JavaScript APIs can also become dangerous depending on how attacker-controlled data reaches them.

---

# Clickjacking + DOM XSS

The attack chain can look like:

```text
Attacker
   ↓
Creates Framed Page
   ↓
Target Page Loads
   ↓
Attacker-Controlled Input Reaches DOM
   ↓
DOM XSS Becomes Triggerable
   ↓
Clickjacking Hides Target Interface
   ↓
Victim Clicks Decoy
   ↓
Vulnerable Functionality Executes
```

---

# Why Combine the Techniques?

Clickjacking can provide a way to make the victim perform an interaction that triggers the vulnerable DOM functionality.

Instead of relying on the victim to recognize or interact with a suspicious URL or interface, the attacker can create a visually convincing decoy.

---

# Testing Workflow

## Step 1 — Identify a Frameable Page

Determine whether the target page can be embedded.

Check:

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

## Step 2 — Identify DOM XSS

Inspect the application's JavaScript.

Look for:

```text
Sources
   ↓
User-Controlled Data
   ↓
Dangerous Sink
```

Example conceptual flow:

```text
URL Parameter
      ↓
JavaScript
      ↓
innerHTML
```

---

## Step 3 — Confirm the Vulnerability

Use a harmless test in an authorized environment.

For example:

```html
<img src=x onerror=alert(1)>
```

The exact payload depends on the vulnerable context.

---

# Step 4 — Determine the Trigger

Some DOM XSS vulnerabilities execute immediately when the page loads.

Others require an interaction such as:

```text
Click
Hover
Form submission
Button activation
```

Clickjacking is particularly useful when the vulnerability requires a user interaction.

---

# Step 5 — Create the iframe

Example:

```html
<iframe
    src="https://victim-website.com/vulnerable-page">
</iframe>
```

---

# Step 6 — Create the Decoy

Example:

```html
<div>Click me</div>
```

Position the decoy above the target interaction.

---

# Basic Overlay

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

<iframe src="https://victim-website.com/vulnerable-page"></iframe>
```

Use partial opacity while aligning the elements.

---

# Step 7 — Hide the Target

After alignment:

```css
opacity: 0.0001;
```

can be used for the final demonstration.

---

# Attack Flow

```text
Victim Opens Attacker Page
          ↓
Target Page Loaded in iframe
          ↓
DOM XSS Context Present
          ↓
Visible Decoy Positioned
          ↓
Victim Clicks
          ↓
Target Interaction Triggered
          ↓
DOM XSS Executes
```

---

# CSP Considerations

A Content Security Policy may prevent certain XSS payloads from executing.

Inspect:

```http
Content-Security-Policy
```

Look for directives such as:

```text
script-src
script-src-elem
```

The supplied material includes a lab demonstrating a CSP weakness where a controllable `token` parameter could affect the CSP policy.

---

# CSP Investigation

Check:

```text
Proxy → HTTP history
```

Then inspect the response headers.

Example:

```http
Content-Security-Policy: default-src 'self'; script-src 'self'
```

Determine whether the policy contains weaknesses that affect the vulnerable functionality.

---

# Important

Do not assume that:

```text
DOM XSS exists
```

means:

```text
Clickjacking + DOM XSS is exploitable
```

The complete chain must be tested.

---

# Combined Testing Checklist

```text
☐ Identify frameable target
☐ Identify DOM XSS source
☐ Identify dangerous sink
☐ Confirm attacker-controlled data reaches sink
☐ Determine whether user interaction is required
☐ Inspect CSP
☐ Create iframe
☐ Create decoy
☐ Align target interaction
☐ Test with partial opacity
☐ Reduce opacity
☐ Verify interaction triggers vulnerable behavior
```

---

# Security Impact

The final impact depends on what the DOM XSS allows.

Possible consequences may include:

```text
JavaScript execution
Account actions
Session-related actions
DOM manipulation
Further application compromise
```

Only report impact that is actually demonstrated.

---

# Defensive Measures

For clickjacking:

```http
X-Frame-Options: DENY
```

or:

```http
Content-Security-Policy: frame-ancestors 'none';
```

For XSS:

```text
Encode output
Validate input
Use safe DOM APIs
Avoid dangerous sinks
Apply an appropriate CSP
```

---

# Key Takeaways

- Clickjacking and DOM XSS can sometimes be chained.
- The framed page must expose a useful DOM XSS execution path.
- User interaction can be used as the trigger for the vulnerable functionality.
- Inspect both client-side JavaScript and response security headers.
- CSP can affect whether an XSS payload executes.
- The presence of both vulnerabilities does not automatically mean the combined attack works.
- Confirm the complete attack chain in an authorized environment.