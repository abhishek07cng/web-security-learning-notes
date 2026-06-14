# JavaScript Context Observations

## Observation 1

JavaScript Context is very different from:

```text
HTML Context
```

---

## Observation 2

The first question should be:

```text
Where Am I Inside JavaScript?
```

Examples:

```text
String
Script Block
Event Handler
Template Literal
```

---

## Observation 3

Many applications escape:

```javascript
'
```

but forget:

```javascript
\
```

creating bypass opportunities.

---

## Observation 4

HTML parsing happens before:

```javascript
JavaScript Parsing
```

which allows:

```html
</script>
```

payloads.

---

## Observation 5

Template literals create:

```javascript
${}
```

execution opportunities.

---

## Observation 6

HTML entities may become dangerous after decoding.

Example:

```html
&apos;
```

---

## Observation 7

Most JavaScript Context XSS relies on:

```text
Breaking Existing Syntax
```

rather than injecting HTML.

---

# Personal Revision Formula

```text
Reflection
        ↓
Determine JS Context
        ↓
Break Syntax
        ↓
Execute JS
```