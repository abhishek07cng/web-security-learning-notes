# Overriding Existing Conditions

## Overview

Once boolean conditions can be influenced, the next step is to override existing query conditions.

The PortSwigger material demonstrates injecting a condition that always evaluates to true.

---

# Example Payload

```text
'||'1'=='1
```

---

# Example Request

```text
category=fizzy'||'1'=='1
```

This produces the following MongoDB query:

```text
this.category == 'fizzy'||'1'=='1'
```

---

# Result

Because the injected condition always evaluates to true, the modified query returns all matching documents.

In the supplied example, this allows the application to display products from all categories, including hidden or unreleased products.

---

# Warning

The PortSwigger material warns that injecting conditions that always evaluate to true can have unintended consequences.

If the same user input is reused in update or delete operations, it may result in accidental data loss.

---

# Why It Works

The injected condition changes the query logic.

Instead of filtering only the intended records, the query evaluates to true for all matching documents.

---

# Key Takeaways

- Always-true conditions override existing query restrictions.
- This technique may expose hidden or restricted data.
- Care should be taken when testing production systems because modified queries may affect application behavior.