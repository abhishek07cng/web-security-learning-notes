# Delimiter Discrepancies

## Overview

A delimiter discrepancy occurs when the origin server and cache server interpret a character in the URL path differently.

This can allow an attacker to append a static extension that is recognized by the cache but ignored by the origin.

---

# Basic Concept

```text
Same URL
    ↓
Different delimiter interpretation
    ↓
Different path interpretation
```

---

# Identifying Origin Delimiters

Start with a target endpoint:

```text
/settings/users/list
```

Add an arbitrary string:

```text
/settings/users/listaaa
```

Use this response as a reference.

---

# Test a Possible Delimiter

Insert a character between the original path and arbitrary string:

```text
/settings/users/list;aaa
```

If the response matches the original endpoint:

```text
/settings/users/list
```

the origin may use `;` as a delimiter.

If it matches:

```text
/settings/users/listaaa
```

the character may not be treated as a delimiter.

---

# Burp Intruder

Burp Intruder can be used to test many possible delimiter characters.

Example payload position:

```text
/settings/users/list§§aaa
```

Test a list of possible characters.

When using Intruder, disable automatic URL encoding for the delimiter characters so that the characters are sent as intended.

---

# Example

Suppose the origin uses:

```text
;
```

as a delimiter.

The origin interprets:

```text
/settings/users/list;aaa
```

as:

```text
/settings/users/list
```

---

# Test Cache Interpretation

Add a static extension:

```text
/settings/users/list;aaa.js
```

If the response is cached, this can indicate:

```text
Origin
   ↓
Uses ; as delimiter

Cache
   ↓
Does not use ; as delimiter

Cache
   ↓
Sees .js
```

---

# Example Attack

```text
/settings/users/list;aaa.js
```

Cache interprets:

```text
/settings/users/list;aaa.js
```

Origin interprets:

```text
/settings/users/list
```

The origin returns dynamic information.

The cache stores the response because it sees:

```text
.js
```

---

# Multiple Extensions

Test:

```text
.js
.css
.ico
.exe
```

---

# Browser Considerations

Some characters may be processed by the browser before reaching the cache.

For example, browsers can encode certain characters, while `#` can truncate the URL path.

Therefore, a delimiter that works in Repeater may not necessarily work directly in a victim's browser.

Encoded versions may sometimes be relevant.

---

# Key Takeaways

- Delimiter discrepancies depend on different interpretations by cache and origin.
- First identify delimiters used by the origin.
- Then determine whether the cache also recognizes them.
- Burp Intruder can automate delimiter discovery.
- A successful discrepancy can allow a static extension to be visible to the cache but not the origin.