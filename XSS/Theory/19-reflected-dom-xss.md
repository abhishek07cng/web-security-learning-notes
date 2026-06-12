# Reflected DOM XSS

## Overview

Reflected DOM XSS combines:

```text
Server Reflection
        +
Client-Side Processing
```

The server reflects attacker-controlled data into the page, and JavaScript later processes that data in an unsafe way.

---

# Difference From Traditional Reflected XSS

Traditional Reflected XSS:

```text
Server
        ↓
Returns Executable Payload
```

---

Reflected DOM XSS:

```text
Server Reflects Data
        ↓
JavaScript Processes Data
        ↓
Dangerous Sink
        ↓
Execution
```

---

# Common Pattern

```javascript
eval(
'var data = "' +
userInput +
'"'
);
```

---

# Attack Flow

```text
User Input
        ↓
Server Reflection
        ↓
JSON Response
        ↓
JavaScript Processing
        ↓
eval()
        ↓
Execution
```

---

# Dangerous Sink

Most common:

```javascript
eval()
```

---

# Why eval() Is Dangerous

Example:

```javascript
eval(userInput);
```

---

Result:

```text
User Input
=
JavaScript Code
```

---

# Testing Methodology

## Step 1

Find reflected parameter.

---

## Step 2

Locate JavaScript processing.

---

## Step 3

Identify dangerous sink.

Example:

```javascript
eval()
```

---

## Step 4

Test escaping behavior.

Try:

```text
"
'
\
```

---

## Step 5

Break out of context.

---

# Related Lab

- lab09-reflected-dom-xss.md

---

# Key Takeaways

- Reflection alone is not enough.
- JavaScript processing creates exploitation.
- eval() should immediately attract attention.
- Improper escaping often leads to execution.