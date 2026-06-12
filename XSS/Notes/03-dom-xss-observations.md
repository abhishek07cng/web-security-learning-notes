# DOM XSS Observations

## Observation 1

DOM XSS often does not appear in:

```text
View Source
```

Use:

```text
Elements Tab
```

instead.

---

## Observation 2

Most DOM XSS vulnerabilities follow:

```text
Source
        ↓
Sink
```

pattern.

---

## Observation 3

Finding:

```javascript
innerHTML
```

should immediately trigger investigation.

---

## Observation 4

Finding:

```javascript
eval()
```

should be treated as high-risk.

---

## Observation 5

jQuery introduces additional sinks:

```javascript
$()
.attr()
.html()
```

---

## Observation 6

AngularJS introduces:

```html
{{ }}
```

expression execution.

---

## Observation 7

Most beginners search for:

```html
<script>
```

but real DOM XSS often involves:

```html
Event Handlers
JavaScript URLs
Angular Expressions
```

---

## Observation 8

DOM Invader significantly speeds up testing.

---

## Personal Revision Formula

```text
Source
        ↓
Canary
        ↓
Sink
        ↓
Context
        ↓
Payload
        ↓
Execution
```