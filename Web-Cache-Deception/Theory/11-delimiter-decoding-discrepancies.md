# Delimiter Decoding Discrepancies

## Overview

Delimiter decoding discrepancies occur when the cache and origin server decode URL characters differently before interpreting them.

An encoded delimiter may therefore be treated as:

```text
Data by one component
```

and:

```text
Delimiter by another component
```

---

# Basic Concept

```text
Encoded Character
       ↓
Cache Processing
       ↓
Origin Processing
       ↓
Different Interpretation
```

---

# Example

Consider:

```text
/profile%23wcd.css
```

Here:

```text
%23
```

represents:

```text
#
```

The origin may decode `%23` to `#`.

If `#` is treated as a delimiter, the origin interprets the path as:

```text
/profile
```

The cache may not decode `%23`.

It therefore interprets:

```text
/profile%23wcd.css
```

and may apply a `.css` cache rule.

---

# Another Example

Consider:

```text
/myaccount%3fwcd.css
```

Here:

```text
%3f
```

represents:

```text
?
```

The cache may apply cache rules to:

```text
/myaccount%3fwcd.css
```

and decide to cache it because of:

```text
.css
```

The cache can then decode `%3f` and forward:

```text
/myaccount?wcd.css
```

The origin interprets `?` as a delimiter and therefore processes:

```text
/myaccount
```

---

# Attack Flow

```text
Encoded Delimiter
       ↓
Cache sees static extension
       ↓
Cache decides to store response
       ↓
URL is decoded
       ↓
Origin sees delimiter
       ↓
Origin returns sensitive content
```

---

# Testing Methodology

Use the same methodology as normal delimiter testing, but test encoded characters.

Examples:

```text
%23
%3f
```

Also investigate encoded non-printable characters mentioned in the source material:

```text
%00
%0A
%09
```

These may cause URL truncation if decoded by the relevant parser.

---

# Burp Workflow

```text
Identify Sensitive Endpoint
        ↓
Identify Origin Delimiter
        ↓
Encode Delimiter
        ↓
Append Static Extension
        ↓
Send Request
        ↓
Inspect Cache Behavior
        ↓
Repeat
        ↓
Confirm Discrepancy
```

---

# Important

The exact behavior depends on:

```text
Cache implementation
Origin parser
URL decoding order
Browser processing
```

---

# Key Takeaways

- Encoded delimiters can create cache/origin discrepancies.
- The cache may apply rules before decoding.
- The origin may decode before interpreting the path.
- `%23` represents `#`.
- `%3f` represents `?`.
- `%00`, `%0A`, and `%09` may also be worth testing where appropriate.