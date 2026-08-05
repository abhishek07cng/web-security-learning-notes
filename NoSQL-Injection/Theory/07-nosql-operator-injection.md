# NoSQL Operator Injection

## Overview

NoSQL databases often use query operators to define conditions that documents must satisfy before being returned.

If user input is not properly validated, an attacker may inject these operators to manipulate the query logic.

Unlike syntax injection, operator injection does not break the query syntax. Instead, it changes how the database evaluates the query.

---

# Common MongoDB Operators

The PortSwigger material highlights the following MongoDB operators:

```text
$where
```

Matches documents that satisfy a JavaScript expression.

---

```text
$ne
```

Matches all values that are **not equal** to a specified value.

---

```text
$in
```

Matches values contained within a specified array.

---

```text
$regex
```

Matches values using a regular expression.

---

# Why Operator Injection Works

If an application accepts these operators as user input, the attacker can alter the query conditions without breaking the original syntax.

This may lead to:

- Authentication bypass
- Data disclosure
- Enumeration of users
- Data extraction

---

# Key Takeaways

- Operator injection manipulates query logic rather than query syntax.
- MongoDB provides multiple operators that may be abused.
- Improper validation of user input enables this attack.