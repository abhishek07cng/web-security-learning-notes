# Burp Tools for Information Disclosure

## Overview

The PortSwigger material highlights several Burp Suite tools that help identify Information Disclosure vulnerabilities.

These tools automate repetitive tasks and make it easier to identify leaked information.

---

# Burp Scanner

Burp Scanner can automatically identify:

- Sensitive information
- Backup files
- Directory listings
- Email addresses
- Private keys
- Credit card numbers

It performs both crawling and auditing of the application.

---

# Burp Intruder

Burp Intruder is useful for:

- Fuzzing parameters
- Testing invalid input
- Comparing responses
- Identifying unusual behavior

---

# Search

The Search engagement tool can locate:

- Keywords
- Regex patterns
- Specific text
- Missing values

Useful examples include:

```
error

SQL

password

admin
```

---

# Find Comments

This tool extracts HTML developer comments.

Developer comments may reveal:

- Hidden directories
- Application logic
- Debug notes
- TODO items

---

# Discover Content

Discover Content searches for hidden files and directories that are not linked from the application.

Examples include:

- Backup folders
- Administrative directories
- Hidden resources

---

# Logger++

The uploaded material also mentions Logger++.

Benefits include:

- Logging requests
- Logging responses
- Highlighting interesting entries
- Applying advanced filters

---

# Key Takeaways

Burp provides multiple tools that work together:

- Scanner
- Intruder
- Search
- Find Comments
- Discover Content
- Logger++

Using these together greatly improves Information Disclosure testing.