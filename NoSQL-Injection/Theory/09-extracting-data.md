# Exploiting NoSQL Injection to Extract Data

## Overview

Some MongoDB operators and functions allow limited JavaScript execution.

If an application uses these features, injected JavaScript expressions may be evaluated as part of the database query.

This enables attackers to extract sensitive information from the database.

---

# Example Query

The application performs a user lookup using:

```json
{
  "$where":"this.username == 'admin'"
}
```

Because the query uses the `$where` operator, attacker-controlled JavaScript may also be executed.

---

# Extracting Password Characters

Example payload:

```text
admin' && this.password[0] == 'a' || 'a'=='b
```

This checks whether the first character of the administrator password is:

```text
a
```

By changing the character position and tested letter, the password can be extracted one character at a time.

---

# Using match()

The supplied material also demonstrates using the JavaScript `match()` function.

Example:

```text
admin' && this.password.match(/\d/) || 'a'=='b
```

This checks whether the password contains numeric characters.

---

# Why It Works

The injected JavaScript becomes part of the `$where` expression.

By observing true and false responses, attackers can infer sensitive data without directly viewing it.

---

# Key Takeaways

- `$where` allows JavaScript expressions to be evaluated.
- Boolean conditions enable character-by-character data extraction.
- JavaScript functions such as `match()` may also assist during enumeration.