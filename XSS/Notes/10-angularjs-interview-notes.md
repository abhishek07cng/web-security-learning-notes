# AngularJS Interview Notes

## What Is CSTI?

Client-Side Template Injection occurs when user input becomes part of a template evaluated by a client-side framework.

---

## Detection Payload

```html
{{7*7}}
```

---

Expected Output

```text
49
```

---

## What Is AngularJS Sandbox?

A security mechanism intended to prevent dangerous object access.

---

## Was The Sandbox Secure?

```text
No
```

Multiple bypasses were discovered.

---

## Why Was Sandbox Removed?

Because:

```text
Repeated Escapes
```

made it unreliable.

---

## What Is A Sandbox Escape?

Bypassing AngularJS restrictions to execute arbitrary JavaScript.

---

## Common Sink

```javascript
orderBy
```

---

## What Is CSP Bypass?

Executing code despite:

```text
Content Security Policy
```

restrictions.

---

## Useful AngularJS Variable

```javascript
$event
```

---

## Useful AngularJS Event

```html
ng-focus
```

---

## Detection Workflow

```text
{{7*7}}
        ↓
49?
        ↓
AngularJS Present
        ↓
Sandbox Escape
```

---

# Interview Takeaways

- CSTI differs from traditional XSS.
- AngularJS sandbox is not a security boundary.
- orderBy is a common execution sink.
- CSP does not guarantee safety.