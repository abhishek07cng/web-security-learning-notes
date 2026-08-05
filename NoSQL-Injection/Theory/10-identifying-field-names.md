# Identifying Field Names

## Overview

MongoDB stores semi-structured data and does not require a fixed schema.

Before extracting sensitive information, it may be necessary to identify the names of fields stored within a collection.

The PortSwigger methodology demonstrates using JavaScript injection to determine whether specific fields exist.

---

# Testing for Existing Fields

Suppose the application performs a lookup using:

```text
username=admin
```

To test whether a field named `password` exists, submit:

```text
admin' && this.password!='
```

---

# Comparing Responses

To confirm the result, compare three requests.

Known field:

```text
admin' && this.username!='
```

Suspected field:

```text
admin' && this.password!='
```

Unknown field:

```text
admin' && this.foo!='
```

---

# Expected Behavior

If the response for:

```text
this.password
```

matches the response for:

```text
this.username
```

but differs from:

```text
this.foo
```

this suggests that the `password` field exists.

---

# Dictionary Attacks

If field names are unknown, the supplied material recommends testing multiple possible field names using a dictionary attack.

Different candidate field names can be submitted until one produces a matching response.

---

# Alternative Technique

The PortSwigger material notes that operator injection can also be used to enumerate field names character by character.

This approach removes the need to guess field names manually.

---

# Key Takeaways

- MongoDB collections may contain unknown fields.
- Comparing responses helps identify valid field names.
- Dictionary attacks and operator injection can assist with field enumeration.