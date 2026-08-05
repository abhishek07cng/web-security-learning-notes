# NoSQL Syntax Injection

## Overview

NoSQL syntax injection occurs when attacker-controlled input breaks the original database query syntax and injects additional query logic.

The testing methodology is similar to SQL injection, although payloads depend on the target NoSQL database.

---

# Detecting Syntax Injection

One method is to submit fuzz strings and special characters that may break the query syntax.

If user input is not properly sanitized, the application may:

- Return database errors.
- Produce different responses.
- Behave unexpectedly.

---

# MongoDB Example

The supplied material demonstrates a shopping application that filters products by category.

Original query:

```text
this.category == 'fizzy'
```

The attacker injects a MongoDB fuzz string into the category parameter to determine whether the query can be broken.

---

# Fuzz Testing

Testing should be systematic.

Different NoSQL databases use different query languages, so fuzz strings should be adapted to the target technology whenever possible.

---

# Why It Works

If special characters are interpreted as query syntax rather than user input, the attacker can alter the database query.

---

# Key Takeaways

- Syntax injection attempts to break NoSQL query syntax.
- Fuzz strings help identify insufficient input sanitization.
- MongoDB syntax differs from traditional SQL syntax.