# NoSQL Injection Interview Notes

## What is NoSQL Injection?

NoSQL injection is a vulnerability that allows attackers to interfere with the queries an application makes to a NoSQL database.

---

## Possible Impact

Successful exploitation may allow attackers to:

- Bypass authentication
- Extract data
- Modify data
- Cause denial of service
- Execute server-side code

---

## Types of NoSQL Injection

### Syntax Injection

Breaks the original query syntax and injects additional query logic.

---

### Operator Injection

Injects MongoDB operators such as:

- `$where`
- `$ne`
- `$in`
- `$regex`

to manipulate query behavior.

---

## Common Detection Techniques

- Fuzz strings
- Special characters
- Boolean conditions
- Response comparison
- Timing-based payloads

---

## Common MongoDB Operators

```text
$where
```

Executes JavaScript expressions.

---

```text
$ne
```

Matches values that are not equal.

---

```text
$in
```

Matches values contained within an array.

---

```text
$regex
```

Matches values using regular expressions.

---

## Common Exploitation Techniques

- Authentication bypass
- Field enumeration
- Password extraction
- Password reset token extraction
- Timing-based injection

---

## Prevention

The PortSwigger material recommends:

- Validate and sanitize user input.
- Use parameterized queries.
- Apply allowlists for accepted keys.
- Prevent unexpected MongoDB operators.

---

# Interview Questions

### Q. What is NoSQL injection?

A vulnerability that allows attackers to manipulate NoSQL database queries through user-controlled input.

---

### Q. What are the two main types?

- Syntax Injection
- Operator Injection

---

### Q. Name four MongoDB operators commonly tested.

- `$where`
- `$ne`
- `$in`
- `$regex`

---

### Q. How can blind NoSQL injection be detected?

By using boolean conditions or timing-based payloads and comparing application responses.

---

### Q. What is the recommended defence?

Validate and sanitize input, use parameterized queries, and apply allowlists for accepted operators and keys.

---

# One-Minute Summary

NoSQL injection occurs when user-controlled input alters NoSQL database queries. In MongoDB, attackers commonly exploit syntax injection, query operators, and JavaScript evaluation to bypass authentication, enumerate fields, and extract sensitive information. Effective prevention relies on input validation, parameterized queries, and restricting accepted operators.