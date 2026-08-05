# Detecting NoSQL Syntax Injection

## Overview

A common way to detect NoSQL syntax injection is to attempt to break the database query by submitting fuzz strings and special characters.

If the application does not correctly sanitize or filter user input, the database may return an error or exhibit different behavior.

---

# MongoDB Example

The PortSwigger material demonstrates a shopping application that retrieves products by category.

Example request:

```text
https://insecure-website.com/product/lookup?category=fizzy
```

The application constructs the following MongoDB query:

```text
this.category == 'fizzy'
```

---

# Fuzz String

The supplied material provides the following MongoDB fuzz string:

```text
'"`{
;$Foo}
$Foo \xYZ
```

When injected into the category parameter (URL-encoded), changes in the application's response may indicate that user input is not being filtered or sanitized correctly.

---

# Injecting Individual Characters

Instead of using a complete fuzz string, individual characters can also be tested.

Example:

```text
'
```

This produces:

```text
this.category == '''
```

If this causes a syntax error, it may indicate that the quote character is breaking the query.

---

# Confirming the Result

To confirm the behavior, submit an escaped quote:

```text
\''
```

If the escaped version no longer causes a syntax error, this suggests that the application may be vulnerable to NoSQL syntax injection.

---

# Key Takeaways

- Fuzz strings help identify syntax injection vulnerabilities.
- Individual special characters can reveal parsing issues.
- Response differences may indicate insufficient input sanitization.