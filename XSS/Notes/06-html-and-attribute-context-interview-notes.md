# HTML & Attribute Context Interview Notes

## What Is HTML Context XSS?

User input appears between HTML tags.

Example:

```html
<p>USER_INPUT</p>
```

---

## What Is Attribute Context XSS?

User input appears inside an attribute.

Example:

```html
<input value="USER_INPUT">
```

---

## Which Is Easier To Exploit?

Usually:

```text
HTML Context
```

because no breakout is required.

---

## What Is Attribute Injection?

Breaking out of an existing attribute and injecting a new one.

Example:

```html
" onmouseover="alert(1)
```

---

## What Is AccessKey Abuse?

Using:

```html
accesskey
```

plus:

```html
onclick
```

to trigger execution.

---

## Why Is SVG Important?

Many filters block:

```html
<script>
```

but allow:

```html
svg
animate
```

---

## Why Are Custom Tags Important?

Many filters forget:

```html
<xss>
<custom>
```

elements.

---

## Common Interview Question

### If Angle Brackets Are Encoded, Is XSS Impossible?

Answer:

```text
No
```

Attribute Injection may still be possible.

---

## Key Interview Takeaways

- Context determines payload.
- HTML Context is generally easiest.
- Attribute Context requires breakout.
- SVG is a common filter bypass.
- Custom elements are often overlooked.