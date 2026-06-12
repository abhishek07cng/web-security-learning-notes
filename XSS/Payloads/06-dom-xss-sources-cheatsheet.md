# DOM XSS Sources CheatSheet

## Overview

Sources are locations where attacker-controlled data enters client-side JavaScript.

---

# location.search

Example:

```text
?q=test
```

---

JavaScript:

```javascript
location.search
```

---

Labs

```text
Lab03
Lab04
Lab05
Lab06
Lab09
```

---

# location.hash

Example:

```text
#test
```

---

JavaScript:

```javascript
location.hash
```

---

Labs

```text
Lab07
```

---

# location.pathname

Example:

```text
/products/test
```

---

JavaScript:

```javascript
location.pathname
```

---

# document.referrer

Example:

```javascript
document.referrer
```

---

Source:

```text
Previous Page
```

---

# document.cookie

Example:

```javascript
document.cookie
```

---

Source:

```text
Cookies
```

---

# window.name

Example:

```javascript
window.name
```

---

Source:

```text
Window Storage
```

---

# postMessage

Example:

```javascript
window.addEventListener(
'message'
)
```

---

Source:

```text
Cross Window Messaging
```

---

# Bug Bounty Reminder

Whenever you see:

```javascript
location.*
document.*
window.*
```

ask:

```text
Can I Control This Value?
```