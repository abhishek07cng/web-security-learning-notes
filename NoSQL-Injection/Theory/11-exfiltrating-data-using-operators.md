# Exfiltrating Data Using Operators

## Overview

Even if the original MongoDB query does not use operators that execute JavaScript, an attacker may be able to inject one.

If the injected operator is evaluated, it can be used to extract information from the database.

---

# Testing JavaScript Execution

The PortSwigger material demonstrates adding the `$where` operator to an existing request.

False condition:

```json
{
  "username":"wiener",
  "password":"peter",
  "$where":"0"
}
```

---

True condition:

```json
{
  "username":"wiener",
  "password":"peter",
  "$where":"1"
}
```

---

# Expected Behavior

If the application's response differs between the two requests, this suggests that the JavaScript expression inside the `$where` operator is being evaluated.

---

# Extracting Field Names

The supplied material demonstrates using the JavaScript `Object.keys()` method.

Example:

```text
"$where":"Object.keys(this)[0].match('^.{0}a.*')"
```

This inspects the first field in the current document and compares its name against the supplied pattern.

By changing the character position and tested letter, field names can be extracted one character at a time.

---

# Why It Works

The injected JavaScript is evaluated by MongoDB.

Boolean responses allow attackers to infer information without directly viewing the underlying data.

---

# Key Takeaways

- Injected operators may introduce JavaScript execution.
- `Object.keys()` can be used to enumerate field names.
- Character-by-character extraction relies on observing true and false responses.