# Types of NoSQL Injection

## Overview

The PortSwigger material describes two primary types of NoSQL injection.

Both allow attackers to manipulate database queries, but they work in different ways.

---

# 1. Syntax Injection

Syntax injection occurs when user input breaks the original NoSQL query syntax and allows the attacker to inject additional query logic.

This approach is similar to SQL injection, although NoSQL databases use different query languages and data structures.

---

## Characteristics

- Breaks query syntax.
- Injects additional expressions.
- Uses database-specific syntax.
- Often identified through syntax errors.

---

# 2. Operator Injection

Operator injection occurs when an attacker injects NoSQL query operators into user-controlled input.

Instead of breaking the query syntax, the attacker changes how the database evaluates conditions.

Examples mentioned in the PortSwigger material include:

- `$where`
- `$ne`
- `$in`
- `$regex`

---

# Comparison

| Syntax Injection | Operator Injection |
|------------------|--------------------|
| Breaks query syntax | Injects query operators |
| Similar to SQL injection | Manipulates query logic |
| Often causes syntax errors | Uses built-in database operators |

---

# MongoDB Focus

The supplied material focuses on exploiting vulnerabilities in **MongoDB**, which is described as the most popular NoSQL database.

---

# Key Takeaways

- NoSQL injection consists of syntax injection and operator injection.
- Both techniques manipulate server-side database queries.
- MongoDB provides several operators that may be abused during exploitation.