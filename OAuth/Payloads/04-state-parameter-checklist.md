# state Parameter Checklist

Purpose

```
OAuth CSRF Protection
```

---

## Verify

- Present?
- Random?
- Long?
- Session-bound?
- Single-use?
- Validated?

---

## Tests

- Remove state
- Modify state
- Replay state
- Use another user's state
- Leave state blank

---

## Indicators

If login or account linking still succeeds, investigate for CSRF vulnerabilities.