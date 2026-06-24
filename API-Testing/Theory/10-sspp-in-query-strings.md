# SSPP In Query Strings

## Overview

Query strings may be interpreted differently by internal APIs.

---

# Example

```text
?username=wiener
```

Attacker injects:

```text
&admin=true
```

or

```text
#
```

to truncate parameters.

---

# Attack Flow

```text
User Input
        ↓
Internal API
        ↓
Parameter Injection
        ↓
Unexpected Behavior
```

---

# Common Characters

```text
&
#
=
?
```

---

# Related Lab

```text
Lab04
```

---

# Key Takeaways

Query-string parsing differences create vulnerabilities.