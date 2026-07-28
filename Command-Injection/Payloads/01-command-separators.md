# Command Separators

## Overview

Command separators allow attackers to execute additional operating system commands by terminating or chaining the original command.

The effectiveness of each separator depends on the operating system and shell implementation.

---

# Cross-Platform Separators

The following separators work on both Windows and Unix-based systems:

```text
&
&&
|
||
```

---

# Unix-Only Separators

```text
;
```

```text
Newline (\n)
```

---

# Example

```text
& echo test &
```

---

# Usage

Use different separators during testing because one may succeed where another fails depending on the application's execution context.

---

# Key Takeaways

- Command separators are fundamental to OS Command Injection.
- Test multiple separators when probing for vulnerabilities.