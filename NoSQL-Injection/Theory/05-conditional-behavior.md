# Confirming Conditional Behavior

## Overview

After identifying a possible NoSQL injection vulnerability, the next step is to determine whether injected conditions can influence server-side query logic.

The PortSwigger methodology recommends comparing false and true conditions.

---

# False Condition

Example payload:

```text
' && 0 && 'x
```

---

# True Condition

Example payload:

```text
' && 1 && 'x
```

---

# Example Requests

False condition:

```text
category=fizzy' && 0 && 'x
```

True condition:

```text
category=fizzy' && 1 && 'x
```

---

# Expected Behavior

If the application behaves differently for the two requests:

- The false condition affects the query.
- The true condition preserves normal behavior.

This indicates that injected syntax is influencing the database query.

---

# Why It Works

The injected boolean expression becomes part of the server-side query.

By observing differences in the application's response, an attacker can determine whether query logic is under their control.

---

# Key Takeaways

- Compare true and false conditions.
- Response differences confirm server-side query manipulation.
- Boolean testing is an important step before attempting exploitation.