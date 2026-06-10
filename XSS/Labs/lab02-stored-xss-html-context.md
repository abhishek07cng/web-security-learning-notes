# Lab02 - Stored XSS Into HTML Context With Nothing Encoded

## Objective

Exploit a Stored XSS vulnerability in the comment functionality.

---

# Lab Information

| Field | Value |
|---------|---------|
| Category | XSS |
| Difficulty | Apprentice |
| Vulnerability | Stored XSS |
| Context | HTML Context |
| Platform | PortSwigger |

---

# Vulnerability Overview

The application stores comments and later displays them without encoding.

This allows malicious JavaScript to be saved and executed whenever the page is viewed.

---

# Analysis

## Step 1

Open blog post.

---

## Step 2

Submit normal comment.

Example:

```text
Hello World
```

---

## Step 3

Verify comment appears on page.

Observation:

```text
Comment Stored Successfully
```

---

## Step 4

Test XSS payload.

---

# Full Payload(s) Used

## Final Payload

```html
<script>alert(1)</script>
```

---

# Exploitation Steps

### Step 1

Open comment section.

---

### Step 2

Enter payload:

```html
<script>alert(1)</script>
```

---

### Step 3

Submit comment.

---

### Step 4

Reload blog page.

---

### Step 5

Browser executes:

```javascript
alert(1)
```

---

### Step 6

Lab solved.

---

# Why The Payload Works

Application performs:

```text
User Input
        ↓
Database Storage
        ↓
HTML Output
```

without:

```text
Encoding
Filtering
Sanitization
```

The stored payload becomes part of the page source.

---

# Personal Analysis & Testing Process

## Initial Goal

Verify comments are stored.

---

## First Test

Submitted normal comment.

Confirmed:

```text
Comment Appears Later
```

which indicates:

```text
Stored Input
```

---

## Payload Selection

Because comments appeared inside:

```text
HTML Context
```

simple payload chosen:

```html
<script>alert(1)</script>
```

---

## Result

Payload executed automatically when page loaded.

---

## Important Observation

Unlike Reflected XSS:

```text
No Malicious Link Needed
```

Payload already exists inside application.

---

# Related Theory

- 11-stored-xss.md
- 12-impact-of-stored-xss.md
- 13-testing-for-stored-xss.md

---

# Key Learnings

- Stored XSS persists inside the application.
- Every future visitor becomes a potential victim.
- Stored XSS is generally more dangerous than Reflected XSS.