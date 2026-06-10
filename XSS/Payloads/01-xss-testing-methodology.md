# XSS Testing Methodology

## Goal

Determine whether:

```text
Attacker Input
        ↓
Becomes Executable JavaScript
```

---

# Step 1

Find input locations:

```text
Search
Comments
Profiles
Headers
POST Data
Cookies
```

---

# Step 2

Submit probe value:

```text
XSSTEST123
```

---

# Step 3

Search response.

Questions:

```text
Reflected?
Stored?
Not Returned?
```

---

# Step 4

Identify context.

Possible locations:

```text
HTML
Attribute
JavaScript
URL
CSS
```

---

# Step 5

Select payload.

---

HTML Context:

```html
<script>alert(1)</script>
```

---

Attribute Context:

```html
" onmouseover="alert(1)
```

---

JavaScript Context:

```javascript
";alert(1);//
```

---

# Step 6

Test in Burp Repeater.

Observe:

```text
Encoding
Filtering
Transformation
```

---

# Step 7

Verify in browser.

Use:

```javascript
alert(document.domain)
```

or

```javascript
print()
```

---

# Workflow

```text
Entry Point
        ↓
Probe
        ↓
Reflection
        ↓
Context
        ↓
Payload
        ↓
Execution
```

---

# Related Labs

- Lab01
- Lab02