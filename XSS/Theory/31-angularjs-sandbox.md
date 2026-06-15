# AngularJS Sandbox

## Overview

AngularJS originally implemented a sandbox mechanism.

The goal was to prevent template expressions from accessing dangerous JavaScript functionality.

---

# Why The Sandbox Exists

AngularJS expressions can execute logic:

```html
{{7*7}}
```

---

Without restrictions attackers could execute arbitrary JavaScript.

The sandbox attempted to block:

```javascript
window
document
Function
constructor
__proto__
```

---

# Restricted Objects

Examples:

```javascript
window
document
location
```

---

# Restricted Properties

Examples:

```javascript
__proto__
__lookupGetter__
constructor
```

---

# Restricted Functions

Examples:

```javascript
call()
apply()
bind()
```

---

# Internal Security Functions

AngularJS uses:

```javascript
ensureSafeObject()
```

to detect dangerous objects.

---

It uses:

```javascript
ensureSafeMemberName()
```

to block dangerous properties.

---

It uses:

```javascript
ensureSafeFunction()
```

to block dangerous functions.

---

# Important Note

AngularJS developers never considered the sandbox a true security boundary.

However:

```text
Developers Trusted It
Researchers Broke It
```

multiple times.

---

# Removal

The sandbox was eventually removed in:

```text
AngularJS 1.6
```

because bypasses became widespread.

---

# Related Theory

- 32-angularjs-sandbox-escape.md

---

# Key Takeaways

- AngularJS sandbox attempted to restrict dangerous operations.
- It was repeatedly bypassed.
- Legacy applications remain vulnerable.