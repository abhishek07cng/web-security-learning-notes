# DOM XSS Testing Methodology

## Goal

Identify:

```text
Source
        ↓
Data Flow
        ↓
Dangerous Sink
        ↓
JavaScript Execution
```

---

# Step 1 - Identify Sources

Common sources:

```javascript
location.search
location.hash
location.pathname
document.referrer
document.cookie
window.name
postMessage
```

---

# Step 2 - Inject Canary

Use:

```text
DOMXSS123
```

---

Example:

```text
?search=DOMXSS123
```

or

```text
#DOMXSS123
```

---

# Step 3 - Search Live DOM

Open:

```text
F12
    ↓
Elements
```

Search:

```text
DOMXSS123
```

---

# Step 4 - Find Sink

Look for:

```javascript
document.write()
innerHTML
outerHTML
eval()
setTimeout()
setInterval()
Function()
$()
.html()
.attr()
```

---

# Step 5 - Trace Data Flow

```text
Source
        ↓
Variable
        ↓
Function
        ↓
Sink
```

---

# Step 6 - Determine Context

Possible contexts:

```text
HTML
Attribute
JavaScript
URL
```

---

# Step 7 - Select Payload

Based on context.

---

# Step 8 - Verify Execution

Use:

```javascript
alert(1)
```

or

```javascript
print()
```

---

# DOM XSS Workflow

```text
Source
        ↓
Canary
        ↓
DOM Search
        ↓
Sink Discovery
        ↓
Context Analysis
        ↓
Payload
        ↓
Execution
```

---

# Tools

```text
Burp Suite
DOM Invader
Chrome DevTools
```

---

# Related Labs

- Lab03
- Lab04
- Lab05
- Lab06
- Lab07
- Lab08
- Lab09
- Lab10