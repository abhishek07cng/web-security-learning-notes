# NoSQL Injection Observations

## Overview

NoSQL injection allows attackers to manipulate NoSQL database queries by supplying crafted input that changes how the database interprets the request.

The PortSwigger material demonstrates that exploitation generally progresses from identifying syntax injection to operator injection and finally to data extraction.

---

# Observation 1 — Different NoSQL Databases Behave Differently

Unlike SQL databases, NoSQL databases do not share a universal query language.

Testing methodology therefore depends on the underlying database technology.

The supplied material focuses on MongoDB.

---

# Observation 2 — Always Start with Syntax Testing

The first step should always be determining whether user input breaks the database query.

Examples include:

```text
'
```

or the MongoDB fuzz string.

Changes in application behavior may indicate insufficient sanitization.

---

# Observation 3 — Boolean Conditions Confirm Injection

Comparing:

```text
' && 0 && 'x
```

and

```text
' && 1 && 'x
```

helps determine whether injected expressions influence server-side query logic.

Different responses confirm successful injection.

---

# Observation 4 — Operator Injection Is Extremely Powerful

MongoDB operators such as:

- $where
- $ne
- $regex
- $in

can manipulate authentication queries and expose sensitive data when accepted as user input.

---

# Observation 5 — JavaScript Execution Enables Data Extraction

The `$where` operator can evaluate JavaScript expressions.

Boolean conditions allow sensitive values, such as passwords, to be extracted one character at a time without displaying them directly.

---

# Observation 6 — Timing Can Confirm Blind Injection

If syntax errors or response differences are unavailable, timing payloads provide another detection technique.

A measurable delay indicates that injected JavaScript has been executed.

---

# Personal Testing Workflow

1. Identify user-controlled input.
2. Test syntax injection.
3. Confirm boolean behavior.
4. Test MongoDB operators.
5. Attempt authentication bypass.
6. Enumerate fields.
7. Extract sensitive values.
8. Use timing-based payloads if necessary.

---

# Biggest Lesson

NoSQL injection is more than authentication bypass.

Successful testing often involves moving step by step from detection to enumeration and finally to controlled extraction of sensitive information.