# Clickjacking

## Overview

Clickjacking is an interface-based attack where an attacker places a target website inside a transparent or otherwise disguised iframe and tricks a victim into clicking on an element that performs an unintended action.

The victim believes they are interacting with the attacker's page, while their click is actually being delivered to the framed target website.

---

# Basic Concept

```text
Attacker-Controlled Page
        │
        ▼
Transparent Iframe
        │
        ▼
Target Website
        │
        ▼
Victim Click
        │
        ▼
Unintended Target Action
```

---

# Why Clickjacking Works

Clickjacking is possible when the target website can be loaded inside a frame.

The attacker can:

1. Load the target page inside an iframe.
2. Make the iframe transparent.
3. Position the target action underneath a visible decoy.
4. Encourage the victim to click the decoy.
5. The click is actually delivered to the target website.

---

# Basic Iframe

A simple target iframe can look like:

```html
<iframe src="https://victim-website.com/my-account"></iframe>
```

The attacker can then use CSS to position the iframe and decoy content.

---

# Transparent Iframe

A transparent iframe can be created using CSS:

```css
iframe {
    opacity: 0.0001;
}
```

During development, a higher opacity such as:

```css
opacity: 0.1;
```

can be useful for aligning the elements.

Once the alignment is correct, the opacity can be reduced.

---

# Basic Overlay Structure

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

<iframe src="https://victim-website.com/my-account"></iframe>
```

The exact dimensions and positioning depend on the target page.

---

# Alignment

The attacker needs to align the visible decoy with the target action inside the iframe.

For example:

```text
Visible Decoy
     ↓
"Click me"
     │
     │
     ▼
Transparent Target Button
```

The victim believes they are clicking:

```text
Click me
```

but the browser actually sends the click to the target iframe.

---

# Testing With Opacity

During testing:

```css
opacity: 0.1;
```

can make the target iframe partially visible.

This makes it easier to determine whether the target button and decoy are aligned.

After alignment:

```css
opacity: 0.0001;
```

can be used for the final demonstration.

---

# Basic Attack Flow

```text
Identify Frameable Target
        ↓
Identify Sensitive Action
        ↓
Load Target in iframe
        ↓
Make iframe Transparent
        ↓
Create Decoy Element
        ↓
Align Decoy With Target Action
        ↓
Victim Clicks Decoy
        ↓
Target Action Executes
```

---

# Common Targets

Clickjacking may be relevant to actions such as:

```text
Change email
Delete account
Change account settings
Submit forms
Like or follow content
Perform administrative actions
```

The actual impact depends on what the target application allows the victim to perform.

---

# Authentication

A particularly important condition is that the victim is authenticated to the target application.

For example:

```text
Victim
   ↓
Logged into target website
   ↓
Visits attacker-controlled page
   ↓
Target website loads inside iframe
   ↓
Victim clicks decoy
   ↓
Authenticated action executes
```

---

# CSRF Token Protection

Clickjacking can sometimes remain possible even when a target action has CSRF protection.

If the target page itself can be framed and the victim is authenticated, the attacker may not need to know the CSRF token.

The victim's browser submits the form containing the valid token when the victim interacts with the framed page.

The source material demonstrates this with a lab involving a CSRF-token-protected account action.

---

# Prefilled Form Input

Some applications allow form values to be supplied through GET parameters.

For example:

```text
/my-account?email=hacker@attacker-website.com
```

If the page uses this parameter to prepopulate an email field, the attacker can frame the page with the desired value already entered.

The victim only needs to click the target button.

---

# Clickjacking With Prefilled Input

```text
Attacker Page
      ↓
iframe:
 /my-account?email=attacker@example.com
      ↓
Email field already populated
      ↓
Transparent Update button
      ↓
Victim clicks decoy
      ↓
Email changed
```

---

# Frame Busting

Some websites attempt to prevent clickjacking using JavaScript frame-busting scripts.

Typical frame-busting behavior can:

```text
Check whether the page is the top-level window
Make frames visible
Prevent interaction with invisible frames
Detect potential framing
```

The source material notes that frame-busting techniques can often be circumvented because they depend on browser-side JavaScript behavior.

---

# iframe Sandbox

An HTML5 iframe can use the `sandbox` attribute.

For example:

```html
<iframe
    src="https://victim-website.com"
    sandbox="allow-forms">
</iframe>
```

The source material explains that omitting `allow-top-navigation` can prevent a frame-busting script from navigating the top-level window while still allowing form functionality.

---

# Clickjacking + DOM XSS

Clickjacking can also act as a carrier for another vulnerability.

If a target page contains a DOM XSS vulnerability that is triggered by a click, an attacker can combine:

```text
Clickjacking
        +
DOM XSS
```

The victim is tricked into clicking a visible decoy, while the click actually activates the vulnerable functionality inside the framed page.

---

# Clickbandit

Burp Suite provides a tool called:

```text
Clickbandit
```

Clickbandit can help generate clickjacking proof-of-concept overlays.

Instead of manually creating all HTML and CSS, the tester can interact with the frameable page and Clickbandit can generate an HTML file containing the overlay.

---

# Clickbandit Workflow

```text
Open Frameable Page
        ↓
Start Clickbandit
        ↓
Perform Desired Action
        ↓
Clickbandit Records Interaction
        ↓
Generate Overlay
        ↓
Review PoC
```

---

# Multistep Clickjacking

Clickjacking does not necessarily have to involve a single click.

An attacker can construct an interface that requires multiple clicks.

Example:

```text
Click 1
   ↓
First Target Action

Click 2
   ↓
Second Target Action
```

The attacker positions multiple decoy elements over corresponding target controls.

---

# Defenses

The source material describes two important server-side protections:

```text
X-Frame-Options
Content Security Policy
```

---

# X-Frame-Options

Examples include:

```http
X-Frame-Options: deny
```

This prevents framing.

Another option is:

```http
X-Frame-Options: sameorigin
```

which restricts framing to the same origin.

The material also discusses:

```http
X-Frame-Options: allow-from https://normal-website.com
```

although browser support for `allow-from` is inconsistent.

---

# Content Security Policy

The recommended CSP directive for controlling framing is:

```http
Content-Security-Policy: frame-ancestors 'none';
```

This prevents framing.

To allow framing only from the same origin:

```http
Content-Security-Policy: frame-ancestors 'self';
```

Specific origins can also be allowed:

```http
Content-Security-Policy: frame-ancestors normal-website.com;
```

---

# X-Frame-Options vs CSP

```text
X-Frame-Options
       ↓
Simple framing restrictions
```

```text
CSP frame-ancestors
       ↓
More flexible framing policy
```

The source material recommends CSP `frame-ancestors` and notes that combining CSP with X-Frame-Options can provide layered protection.

---

# Testing Checklist

```text
☐ Identify sensitive action
☐ Determine whether target can be framed
☐ Check X-Frame-Options
☐ Check Content-Security-Policy
☐ Check frame-ancestors
☐ Identify whether authentication is required
☐ Test basic iframe embedding
☐ Test transparent overlay
☐ Align decoy with target action
☐ Test CSRF-protected actions
☐ Test GET-prefilled form parameters
☐ Check for frame-busting scripts
☐ Test authorized lab bypass techniques
☐ Check for DOM XSS combinations
☐ Consider multistep actions
```

---

# Key Takeaways

- Clickjacking tricks a victim into interacting with a framed target website.
- A transparent iframe can hide the actual target action.
- CSS positioning is used to align the target action with a visible decoy.
- Authentication can make clickjacking particularly impactful.
- CSRF tokens do not necessarily prevent clickjacking.
- GET parameters can sometimes be used to prepopulate target forms.
- Frame-busting scripts are client-side defenses and may have limitations.
- Clickjacking can be combined with DOM XSS.
- Burp Clickbandit can automate creation of clickjacking overlays.
- Multistep clickjacking can involve several target actions.
- `X-Frame-Options` and CSP `frame-ancestors` are important server-side protections.