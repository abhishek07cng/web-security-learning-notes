# Preventing NoSQL Injection

## Overview

The PortSwigger material recommends implementing multiple layers of defence to reduce the risk of NoSQL injection.

The exact prevention strategy depends on the NoSQL technology being used.

---

# 1. Sanitize and Validate Input

Validate all user-controlled input before processing it.

Prefer an allowlist of accepted characters.

Reject unexpected input before it reaches the database.

---

# 2. Use Parameterized Queries

Do not concatenate user input directly into database queries.

Instead, insert user input using parameterized queries.

This prevents user-controlled input from altering query structure.

---

# 3. Prevent Operator Injection

Apply an allowlist of accepted keys.

Reject unexpected MongoDB operators supplied by users.

---

# Recommended Practices

✔ Sanitize user input.

✔ Validate user input.

✔ Use parameterized queries.

✔ Apply allowlists for accepted keys.

---

# Why These Defences Work

Input validation reduces malicious input reaching the database.

Parameterized queries separate user data from query logic.

Allowlists prevent attackers from introducing unexpected operators.

---

# Key Takeaways

- Validate and sanitize all user input.
- Avoid concatenating user input into database queries.
- Restrict accepted operators through allowlists.