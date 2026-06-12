# DOM XSS Sinks CheatSheet

## Overview

Sinks are locations where attacker-controlled input becomes dangerous.

---

# HTML Sinks

## document.write()

```javascript
document.write(
userInput
);
```

Labs:

```text
Lab03
Lab04
```

---

## innerHTML

```javascript
element.innerHTML =
userInput;
```

Labs:

```text
Lab05
Lab10
```

---

## outerHTML

```javascript
element.outerHTML =
userInput;
```

---

## insertAdjacentHTML()

```javascript
element.insertAdjacentHTML()
```

---

# JavaScript Execution Sinks

## eval()

```javascript
eval(userInput);
```

Labs:

```text
Lab09
```

---

## Function()

```javascript
new Function(
userInput
)
```

---

## setTimeout()

```javascript
setTimeout(
userInput
)
```

---

## setInterval()

```javascript
setInterval(
userInput
)
```

---

# jQuery Sinks

## $()

```javascript
$(userInput)
```

Labs:

```text
Lab07
```

---

## .attr()

```javascript
.attr(
"href",
userInput
)
```

Labs:

```text
Lab06
```

---

## .html()

```javascript
.html(
userInput
)
```

---

# Bug Bounty Reminder

Whenever you find:

```javascript
innerHTML
eval
document.write
$()
```

investigate immediately.