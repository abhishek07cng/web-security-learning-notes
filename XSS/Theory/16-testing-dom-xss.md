# Testing For DOM-Based XSS

## Overview

Testing DOM XSS is different from testing traditional XSS.

The vulnerable behavior often exists only in client-side JavaScript.

---

# Step 1 - Find Sources

Look for:

```javascript
location.search
location.hash
document.cookie
document.referrer
window.name
postMessage
```

---

# Step 2 - Insert Canary

Example:

```text
domxss123
```

---

# Step 3 - Search Live DOM

Use:

```text
F12
Elements
Ctrl+F
```

Search:

```text
domxss123
```

---

Important:

```text
Do NOT Use View Source
```

because DOM updates occur after page load.

---

# Step 4 - Determine Context

Possible contexts:

```text
HTML
Attribute
JavaScript
URL
```

---

# Step 5 - Find Sink

Search page JavaScript for:

```javascript
innerHTML
document.write
eval
$()
```

---

# Step 6 - Trace Taint Flow

```text
Source
        ↓
Variable
        ↓
Variable
        ↓
Sink
```

---

# Step 7 - Verify Execution

Use:

```javascript
alert(1)
```

or

```javascript
print()
```

---

# DOM Invader

Burp Browser includes:

```text
DOM Invader
```

which automatically tracks:

```text
Source
        ↓
Sink
```

relationships.

---

# Related Theory

- 15-sources-and-sinks.md

---

# Key Takeaways

- View Source is often useless.
- DevTools Elements is critical.
- Follow the taint flow.
- DOM Invader saves significant time.