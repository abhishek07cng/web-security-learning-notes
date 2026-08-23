# Multistep Clickjacking

## Overview

Multistep clickjacking involves tricking a victim into performing multiple unintended actions on a framed target website.

Instead of triggering a single button click, the attacker creates a sequence of decoy interactions that correspond to multiple controls inside the target iframe.

---

# Basic Concept

```text
Attacker Page
      ↓
Target Page in iframe
      ↓
Transparent Target Controls
      ↓
Multiple Visible Decoys
      ↓
Victim Interaction 1
      ↓
Target Action 1
      ↓
Victim Interaction 2
      ↓
Target Action 2
```

---

# Single-Step vs Multistep

## Single-Step

```text
Decoy
  ↓
One Target Button
  ↓
One Action
```

Example:

```text
Click me
   ↓
Delete account
```

---

## Multistep

```text
Decoy 1
   ↓
Target Action 1
   ↓
Decoy 2
   ↓
Target Action 2
   ↓
Final Result
```

The attacker must correctly position multiple decoy elements.

---

# Why Multistep Clickjacking Matters

Some sensitive operations require more than one interaction.

For example:

```text
Step 1
Open settings

Step 2
Select an option

Step 3
Confirm change
```

A single overlay may not be sufficient.

Multistep clickjacking attempts to align each required target interaction with a corresponding attacker-controlled decoy.

---

# Attack Structure

```text
Visible Page

+-----------------------------+
|                             |
|        Decoy 1              |
|                             |
|        Decoy 2              |
|                             |
|        Decoy 3              |
|                             |
+-----------------------------+

             ↓

Transparent iframe

+-----------------------------+
|                             |
|   Target Control 1          |
|                             |
|   Target Control 2          |
|                             |
|   Target Control 3          |
|                             |
+-----------------------------+
```

---

# Basic iframe

```html
<iframe
    src="https://victim-website.com/target">
</iframe>
```

The iframe contains the legitimate target interface.

---

# Overlay Structure

A basic layout can use:

```css
iframe {
    position: relative;
    width: 700px;
    height: 500px;
    opacity: 0.1;
    z-index: 2;
}

.decoy {
    position: absolute;
    z-index: 1;
}
```

Multiple decoys can then be positioned independently.

---

# Example

Suppose the target page contains:

```text
Button 1 → Open Settings
Button 2 → Confirm Change
```

The attacker page could display:

```text
Decoy 1 → Continue
Decoy 2 → Confirm
```

The alignment becomes:

```text
Continue
   ↓
Open Settings

Confirm
   ↓
Confirm Change
```

---

# Positioning

Each decoy needs to be aligned with the corresponding target control.

Example:

```css
.decoy-one {
    position: absolute;
    top: 200px;
    left: 100px;
}

.decoy-two {
    position: absolute;
    top: 300px;
    left: 100px;
}
```

The exact coordinates depend on the target interface.

---

# Testing With Opacity

During development, use:

```css
opacity: 0.1;
```

This allows the tester to see the target page through the iframe.

Align the first target:

```text
Decoy 1
   ↓
Target Control 1
```

Then align the second:

```text
Decoy 2
   ↓
Target Control 2
```

---

# Final Opacity

Once all interactions are correctly aligned:

```css
opacity: 0.0001;
```

can be used to make the iframe effectively invisible.

---

# Interaction Sequence

The sequence must be correct.

Example:

```text
Victim clicks Decoy 1
        ↓
Target Action 1
        ↓
Target page changes
        ↓
Victim clicks Decoy 2
        ↓
Target Action 2
```

This means that the target page's state changes between clicks.

---

# State Changes

Multistep clickjacking becomes more difficult when the target page changes after the first action.

For example:

```text
Before Click 1
    ↓
Button A visible

After Click 1
    ↓
Button B appears
```

The attacker must account for the new target position.

---

# Testing Workflow

```text
Identify Sensitive Workflow
        ↓
Record Required Steps
        ↓
Identify Each Target Control
        ↓
Create iframe
        ↓
Create Decoy 1
        ↓
Align With Target 1
        ↓
Create Decoy 2
        ↓
Align With Target 2
        ↓
Test Interaction Sequence
        ↓
Reduce Opacity
        ↓
Deliver in Authorized Environment
```

---

# Burp Suite Workflow

Use:

```text
Proxy → HTTP history
```

to understand the application's requests.

Identify:

```text
Initial page
First action
Second action
Final action
```

This helps determine the sequence that the target application expects.

---

# Testing Checklist

```text
☐ Identify sensitive multi-step workflow
☐ Identify first target control
☐ Identify second target control
☐ Identify additional required controls
☐ Confirm target page is frameable
☐ Check X-Frame-Options
☐ Check CSP frame-ancestors
☐ Create iframe
☐ Create decoy elements
☐ Align each decoy
☐ Test with opacity 0.1
☐ Verify interaction order
☐ Test page state changes
☐ Reduce iframe opacity
☐ Deliver exploit in authorized environment
```

---

# Common Challenges

## Page Movement

The target page may change after each interaction.

```text
Click 1
   ↓
Page changes
   ↓
Control moves
```

This can break the alignment.

---

## Dynamic Elements

Buttons may be dynamically generated or positioned.

This can make static overlay coordinates unreliable.

---

## Confirmation Dialogs

A workflow may contain:

```text
Action
   ↓
Confirmation
   ↓
Final Action
```

The attacker must account for every required interaction.

---

# Defensive Perspective

Multistep clickjacking is prevented by preventing the target page from being framed.

Recommended protections include:

```http
X-Frame-Options: DENY
```

or:

```http
Content-Security-Policy: frame-ancestors 'none';
```

For controlled framing:

```http
Content-Security-Policy: frame-ancestors 'self';
```

or an explicitly allowed set of trusted origins.

---

# Key Takeaways

- Multistep clickjacking extends the basic overlay technique to multiple interactions.
- Each decoy must correspond to a target control.
- The order of interactions matters.
- Target page state can change between clicks.
- Dynamic elements can make alignment difficult.
- Testing should begin with partial iframe opacity.
- Reduce opacity only after the complete interaction sequence works.
- Strong framing protections prevent the underlying attack by preventing the target page from being embedded.