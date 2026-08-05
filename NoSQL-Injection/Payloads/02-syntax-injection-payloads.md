# Syntax Injection Payloads

## Single Quote

```text
'
```

---

## Escaped Quote

```text
\''
```

---

## Confirm Injection

```text
Gifts'+'
```

---

## Null Character

```text
fizzy'%00
```

---

# Purpose

These payloads help determine whether user input breaks MongoDB query syntax.

---

# Expected Result

- Syntax error
- Different application response
- Successful query execution after escaping

---

# Key Takeaways

- Start with simple payloads.
- Confirm syntax injection before moving to exploitation.