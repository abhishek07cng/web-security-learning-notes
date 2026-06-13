# XSS Context Observations

## Observation 1

The most important XSS question is:

```text
Where Is My Input Reflected?
```

not:

```text
What Payload Should I Use?
```

---

## Observation 2

The same payload can:

```text
Work In HTML Context
Fail In Attribute Context
Fail In JavaScript Context
```

---

## Observation 3

Reflection does not equal XSS.

Need:

```text
Execution
```

to confirm vulnerability.

---

## Observation 4

HTML Context is often the easiest context.

Examples:

```html
<img src=1 onerror=alert(1)>
<svg onload=alert(1)>
```

---

## Observation 5

When:

```html
<
>
```

are encoded:

look for:

```text
Attribute Injection
```

instead.

---

## Observation 6

Modern XSS testing is mostly:

```text
Context Identification
```

rather than:

```text
Payload Memorization
```

---

# Personal Revision Formula

```text
Reflection
        ↓
Context
        ↓
Payload
        ↓
Execution
```