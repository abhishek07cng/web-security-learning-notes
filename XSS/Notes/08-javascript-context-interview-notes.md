# JavaScript Context Interview Notes

## What Is JavaScript Context XSS?

User input is reflected inside existing JavaScript code.

Example:

```javascript
var input = 'USER_INPUT';
```

---

## Why Is It Harder Than HTML Context?

Because:

```text
Payload Must Produce Valid JavaScript
```

---

## Common JavaScript Contexts

```javascript
String
Script Block
Event Handler
Template Literal
JavaScript URL
```

---

## What Is Script Termination?

Closing current script and creating a new one.

Example:

```html
</script><script>alert(1)</script>
```

---

## What Is String Breakout?

Breaking existing string and injecting code.

Example:

```javascript
';alert(1)//
```

---

## Why Use Comments?

To remove remaining code.

Example:

```javascript
//
```

---

## What Is Template Literal Injection?

Abusing:

```javascript
${expression}
```

inside backtick strings.

---

## Detection Payload

```javascript
${7*7}
```

Expected:

```text
49
```

---

## What Is HTML Entity Bypass?

Using:

```html
&apos;
```

instead of:

```javascript
'
```

---

## Key Interview Takeaways

- Context determines payload.
- JavaScript parsing behavior matters.
- Template literals are a modern attack surface.
- HTML entity decoding creates bypasses.