# DOM XSS Sinks CheatSheet

## Overview

A sink is a location where attacker-controlled data becomes dangerous.

---

# High-Risk HTML Sinks

## document.write()

```javascript
document.write(userInput);
```

---

## document.writeln()

```javascript
document.writeln(userInput);
```

---

## innerHTML

```javascript
element.innerHTML =
userInput;
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
element.insertAdjacentHTML(
'beforeend',
userInput
);
```

---

# JavaScript Execution Sinks

## eval()

```javascript
eval(userInput);
```

---

## Function()

```javascript
new Function(userInput);
```

---

## setTimeout()

```javascript
setTimeout(userInput);
```

---

## setInterval()

```javascript
setInterval(userInput);
```

---

# Event Handler Sinks

```javascript
element.onclick =
userInput;
```

---

# jQuery Sinks

```javascript
.html()
.attr()
$()
append()
prepend()
before()
after()
replaceWith()
```

---

# Common Testing Mindset

```text
Find Source
        ↓
Find Sink
        ↓
Trace Flow
        ↓
Craft Payload
        ↓
Verify Execution
```

---

# Related Labs

- Lab03
- Lab04
- Lab05
- Lab06
- Lab07
- Lab08
- Lab09
- Lab10

---

# Key Takeaways

- Most DOM XSS vulnerabilities revolve around dangerous sinks.
- innerHTML and document.write() are extremely common.
- eval() should always be investigated.
- jQuery introduces many additional sinks.