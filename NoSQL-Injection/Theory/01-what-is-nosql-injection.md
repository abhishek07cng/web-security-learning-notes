# What is NoSQL Injection?

## Overview

NoSQL injection is a vulnerability that allows an attacker to interfere with the queries that an application makes to a NoSQL database.

Successful exploitation may enable an attacker to:

- Bypass authentication or protection mechanisms.
- Extract data.
- Modify data.
- Cause a denial of service.
- Execute code on the server.

---

# What Are NoSQL Databases?

Unlike traditional SQL databases, NoSQL databases:

- Store and retrieve data using formats other than relational tables.
- Use different query languages instead of a universal SQL standard.
- Have fewer relational constraints.

Because different NoSQL databases use different query languages and data structures, exploitation techniques vary depending on the technology in use.

---

# Impact

Successful NoSQL injection may allow attackers to:

- Bypass authentication.
- Read sensitive information.
- Modify application data.
- Execute server-side code.
- Disrupt application availability.

---

# Why It Happens

The vulnerability occurs when user-controlled input is incorporated into NoSQL queries without proper validation or sanitization.

An attacker can manipulate the query logic to change how the database processes requests.

---

# Key Takeaways

- NoSQL injection targets NoSQL database queries.
- It can affect authentication, data confidentiality, integrity, and availability.
- Different NoSQL databases require different exploitation techniques.