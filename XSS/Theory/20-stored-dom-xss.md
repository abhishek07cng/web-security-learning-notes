# Stored DOM XSS

## Overview

Stored DOM XSS occurs when:

```text
User Input
        ↓
Stored By Server
        ↓
Returned Later
        ↓
Processed By JavaScript
        ↓
Dangerous Sink
```

Unlike traditional Stored XSS, the final execution happens because of client-side JavaScript.

---

# Attack Flow

```text
Attacker Input
        ↓
Database Storage
        ↓
Future Response
        ↓
JavaScript Processing
        ↓
innerHTML
        ↓
Execution
```

---

# Example

Stored comment:

```html
<><img src=1 onerror=alert(1)>
```

---

JavaScript:

```javascript
element.innerHTML =
comment.author;
```

---

Result:

```text
Stored Data
        ↓
innerHTML
        ↓
HTML Parsing
        ↓
alert(1)
```

---

# Common Sinks

```javascript
innerHTML
outerHTML
document.write()
```

---

# Why Stored DOM XSS Is Dangerous

Combines:

```text
Persistence
        +
Client-Side Execution
```

---

# Typical Targets

```text
Comments
Forums
Support Tickets
User Profiles
```

---

# Detection Methodology

## Step 1

Store probe value.

---

## Step 2

Locate output.

---

## Step 3

Identify JavaScript processing.

---

## Step 4

Determine sink.

---

## Step 5

Craft payload.

---

# Related Lab

- lab10-stored-dom-xss.md

---

# Key Takeaways

- Stored DOM XSS is a hybrid vulnerability.
- Data is stored server-side.
- Execution occurs client-side.
- innerHTML is a common sink.