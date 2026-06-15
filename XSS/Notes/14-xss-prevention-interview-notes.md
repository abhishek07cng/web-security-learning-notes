# XSS Prevention Interview Notes

## What Is The Best XSS Defense?

```text
Context-Aware Output Encoding
```

---

## Is Input Validation Enough?

```text
No
```

---

## Is CSP Enough?

```text
No
```

---

## Why Use CSP?

Provides:

```text
Defense In Depth
```

---

## What Is HttpOnly?

Prevents:

```javascript
document.cookie
```

access.

---

## Why Is Output Encoding Important?

Because:

```text
Context
Determines
Encoding
```

---

## What Is DOMPurify?

A trusted HTML sanitization library.

---

## What Is The Most Common Mistake?

Using:

```text
Blacklists
```

instead of:

```text
Context-Aware Encoding
```

---

# Interview Takeaways

- Output encoding is the primary defense.
- CSP is a secondary defense.
- Input validation alone is insufficient.
- HttpOnly reduces XSS impact.