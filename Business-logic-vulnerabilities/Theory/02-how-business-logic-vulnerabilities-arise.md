# How Business Logic Vulnerabilities Arise

## Overview

Business logic vulnerabilities usually arise because developers make assumptions that attackers do not follow.

---

# Common Assumptions

Developers assume:

```text
Users Follow The UI
Users Behave Normally
Inputs Are Reasonable
Workflows Are Sequential
Client-Side Controls Are Sufficient
```

---

# Reality

Attackers use:

```text
Burp Proxy
Repeater
Intruder
Forced Browsing
Parameter Manipulation
```

to violate these assumptions.

---

# Complex Systems Increase Risk

Logic flaws become common when:

```text
Code Base Is Large
Components Depend On Each Other
Assumptions Are Undocumented
Developers Lack Full Context
```

---

# Root Cause Formula

```text
Assumption
        ↓
Unexpected Input
        ↓
Unexpected State
        ↓
Unintended Behavior
```

---

# Common Examples

```text
Negative Values
Skipping Workflow Steps
Parameter Removal
Trusting Hidden Fields
Reusing Coupons
```

---

# Key Takeaways

Most logic flaws are caused by bad assumptions.