# Client-Side Template Injection (CSTI)

## Overview

Client-Side Template Injection (CSTI) occurs when user-controlled input is embedded into a client-side template and later evaluated by a JavaScript framework.

Unlike traditional XSS:

```text
User Input
        ↓
HTML Page
        ↓
JavaScript Executes
```

CSTI follows:

```text
User Input
        ↓
Template Expression
        ↓
Framework Evaluation
        ↓
JavaScript Execution
```

---

# What Is A Template?

Modern frameworks use templates to dynamically generate content.

Example:

```html
{{ username }}
```

---

When rendered:

```html
John
```

appears.

---

# Vulnerable Scenario

Application:

```html
<div>

{{ USER_INPUT }}

</div>
```

---

Attacker Input:

```html
{{7*7}}
```

---

Result:

```text
49
```

---

# Why CSTI Is Dangerous

A successful CSTI can lead to:

```text
Cross-Site Scripting
Sandbox Escape
CSP Bypass
Remote Code Execution
```

depending on framework capabilities.

---

# Common Frameworks

```text
AngularJS
Vue.js
Handlebars
Mustache
React (rare)
```

---

# Detection Payload

```html
{{7*7}}
```

---

Expected Result:

```text
49
```

---

# Attack Flow

```text
User Input
        ↓
Template Engine
        ↓
Expression Evaluation
        ↓
JavaScript Execution
```

---

# Related Labs

- Lab24
- Lab25

---

# Key Takeaways

- CSTI occurs before traditional XSS.
- Frameworks evaluate template expressions.
- HTML encoding alone does not stop CSTI.