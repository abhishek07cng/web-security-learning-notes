# CSP Directives Reference

## script-src

Controls:

```text
JavaScript Sources
```

Example:

```http
script-src 'self'
```

---

## img-src

Controls:

```text
Image Sources
```

Example:

```http
img-src 'self'
```

---

## style-src

Controls:

```text
CSS Sources
```

---

## frame-src

Controls:

```text
Frames
```

---

## frame-ancestors

Controls:

```text
Who Can Embed The Site
```

---

## object-src

Controls:

```text
Flash
Java
Plugins
```

---

Recommended:

```http
object-src 'none'
```

---

## base-uri

Controls:

```html
<base>
```

element usage.

---

Recommended:

```http
base-uri 'none'
```

---

## form-action

Controls:

```html
<form action="">
```

targets.

---

Recommended:

```http
form-action 'self'
```

---

# Strong CSP Example

```http
default-src 'self';
script-src 'self';
object-src 'none';
frame-src 'none';
base-uri 'none';
form-action 'self';
frame-ancestors 'none';
```