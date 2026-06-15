# Preventing Client-Side Template Injection

## Overview

CSTI vulnerabilities occur when user-controlled data becomes executable template code.

The safest approach is:

```text
Never Treat User Input As Templates
```

---

# Secure Design

Avoid:

```html
{{ USER_INPUT }}
```

inside templates.

---

Prefer:

```text
Plain Text Rendering
```

instead.

---

# Filter Template Syntax

Block:

```html
{{
}}
```

---

Block:

```javascript
${}
```

when relevant.

---

# Do Not Rely On HTML Encoding

Example:

```html
&lt;
&gt;
```

---

Reason:

```text
Framework
        ↓
HTML Decodes
        ↓
Template Evaluates
```

---

# Keep Frameworks Updated

Older:

```text
AngularJS < 1.6
```

contain numerous sandbox escapes.

---

# CSP Helps But Is Not Enough

CSP reduces risk.

However:

```text
AngularJS CSP Bypasses Exist
```

---

# Secure Checklist

```text
Never Generate Templates From User Input
Sanitize Expressions
Use Updated Frameworks
Deploy CSP
Validate Input
```

---

# Related Labs

- Lab24
- Lab25

---

# Key Takeaways

- Avoid embedding untrusted input into templates.
- HTML encoding alone is insufficient.
- Upgrade legacy AngularJS applications.
- Defense should be layered.