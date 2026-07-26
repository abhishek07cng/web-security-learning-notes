# Fuzzing for Information Disclosure

## Overview

Fuzzing is one of the most effective techniques for identifying Information Disclosure vulnerabilities.

Instead of sending normal input, the tester submits unexpected values and observes how the application responds.

The objective is to trigger unexpected behavior that reveals sensitive information.

---

# Why Fuzzing Works

Applications often handle invalid input differently from valid input.

Unexpected input may trigger:

- Error messages
- Stack traces
- Debug output
- Database errors
- Framework information

Even subtle differences in responses can provide valuable clues.

---

# What to Fuzz

Interesting targets include:

- URL parameters
- Form fields
- Cookies
- HTTP headers
- JSON values

---

# What to Look For

During fuzzing, compare:

- HTTP status codes
- Response length
- Response time
- Error messages
- Keywords
- Stack traces

---

# Burp Intruder

The PortSwigger material recommends Burp Intruder for automating fuzzing.

Benefits include:

- Testing many payloads quickly
- Comparing responses
- Detecting unusual behavior
- Identifying hidden information

---

# Useful Features

Burp Intruder allows you to:

- Add payload positions
- Use predefined fuzz wordlists
- Compare response lengths
- Compare status codes
- Compare response times

---

# Grep Match

Useful for locating keywords such as:

```
error

invalid

SELECT

SQL
```

---

# Grep Extract

Can automatically extract interesting values from responses for comparison.

---

# Key Takeaways

- Fuzzing intentionally sends unexpected input.
- Compare every response carefully.
- Small differences may indicate Information Disclosure.
- Burp Intruder significantly improves testing efficiency.