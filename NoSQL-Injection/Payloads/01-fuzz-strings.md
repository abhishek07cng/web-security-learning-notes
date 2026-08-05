# MongoDB Fuzz Strings

## Overview

Fuzz strings help identify NoSQL syntax injection vulnerabilities by attempting to break the database query.

The PortSwigger material recommends submitting special characters and observing changes in the application's response.

---

# MongoDB Fuzz String

```text
'"`{
;$Foo}
$Foo \xYZ
```

---

# URL-Encoded Version

```text
'%22%60%7b%0d%0a%3b%24Foo%7d%0d%0a%24Foo%20%5cxYZ%00
```

---

# JSON Version

```text
'\"`{\r;$Foo}\n$Foo \\xYZ\u0000
```

---

# Purpose

Use these payloads to determine whether user input is:

- Filtered
- Sanitized
- Directly incorporated into MongoDB queries

---

# Expected Result

If the application's response changes or a syntax error occurs, the input may be vulnerable to NoSQL injection.

---

# Key Takeaways

- Begin testing with fuzz strings.
- Different injection contexts require different encodings.