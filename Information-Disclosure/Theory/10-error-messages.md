# Error Messages

## Overview

Verbose error messages are one of the most common sources of Information Disclosure.

They often reveal far more information than is necessary for users.

---

# Why Error Messages Matter

Error messages may disclose:

- Expected input
- Framework names
- Framework versions
- Database names
- Database tables
- Server software

---

# Example

Submitting an invalid parameter value may produce:

- Stack trace
- Exception details
- Framework version

This information can help identify known vulnerabilities.

---

# Framework Disclosure

The uploaded lab demonstrates that an invalid product ID reveals:

```
Apache Struts 2 2.3.31
```

Knowing the framework version allows attackers to search for public exploits.

---

# Technology Identification

Verbose errors can identify:

- Template engines
- Databases
- Programming languages
- Web servers

---

# Comparing Errors

Different error messages may indicate:

- Valid usernames
- Existing resources
- Different execution paths

This technique is commonly used during:

- SQL Injection
- Username Enumeration
- Information Disclosure testing

---

# Best Practices During Testing

Whenever an error occurs:

- Read the entire response.
- Compare it with previous responses.
- Record any disclosed information.
- Identify software versions and technologies.

---

# Key Takeaways

- Error messages frequently expose technical information.
- Framework versions can lead to known exploits.
- Always compare different error responses during testing.