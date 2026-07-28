# Preventing OS Command Injection

## Overview

The PortSwigger material states that the most effective way to prevent OS Command Injection is to avoid executing operating system commands from application-layer code.

Whenever possible, safer platform APIs should be used instead.

---

# Avoid Calling OS Commands

Instead of invoking shell commands, applications should implement the required functionality using native platform APIs.

This eliminates the possibility of shell command injection.

---

# Validate User Input

If operating system commands must be used, all user-supplied input should undergo strict validation.

Examples include:

- Whitelisting permitted values.
- Validating numeric input.
- Allowing only alphanumeric characters.
- Rejecting unexpected syntax and whitespace.

---

# Whitelisting

Accept only predefined values that are known to be safe.

Any value outside the approved list should be rejected.

---

# Numeric Validation

Where numeric values are expected, verify that the supplied input is a valid number before using it.

---

# Character Validation

Restrict input to:

- Letters
- Numbers

Reject:

- Shell metacharacters
- Special characters
- Whitespace where unnecessary

---

# Avoid Escaping Metacharacters

The PortSwigger material advises against relying on escaping shell metacharacters.

Attempting to sanitise input in this way is error-prone and may be bypassed by skilled attackers.

---

# Prevention Checklist

✔ Avoid shell commands whenever possible.

✔ Use safer platform APIs.

✔ Apply strict input validation.

✔ Validate expected data types.

✔ Use allowlists instead of blocklists.

✔ Reject unexpected characters.

---

# Key Takeaways

- The safest defence is to avoid executing OS commands.
- Strong input validation is essential when OS commands cannot be avoided.
- Escaping shell metacharacters alone is not a reliable defence.