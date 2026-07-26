# Engineering Informative Responses

## Overview

Sometimes applications do not reveal sensitive information during normal operation.

Instead, attackers intentionally trigger unexpected conditions to make the application produce more informative responses.

The PortSwigger material refers to this as **Engineering Informative Responses**.

---

# Goal

Cause the application to generate responses containing useful information.

---

# How It Works

Supply unexpected or invalid input.

Examples include:

- Invalid parameter values
- Incorrect data types
- Missing parameters
- Malformed requests

These inputs may trigger:

- Exceptions
- Stack traces
- Debug messages
- Detailed error responses

---

# Example

Instead of:

```
productId=1
```

Try:

```
productId="example"
```

The application may return:

- Framework version
- File paths
- Stack traces
- Database information

---

# Studying Error Messages

Do not focus only on the message itself.

Also compare:

- Response length
- Status code
- Error type
- Processing time

Even different error conditions can reveal useful information.

---

# Benefits

Engineering informative responses may reveal:

- Application logic
- Internal data
- Technology stack
- Runtime behavior

---

# Key Takeaways

- Unexpected input often produces informative errors.
- Error responses frequently reveal technical details.
- Compare multiple responses to identify useful differences.