# Command Injection Contexts

## Overview

The success of an OS Command Injection attack depends on **how user input is incorporated into the original shell command**.

Different application contexts may require different payloads.

The PortSwigger material highlights one important example involving quoted input.

---

# Unquoted Context

If user input is inserted directly into the shell command, command separators may execute immediately.

Example:

```bash
stockreport.pl USER_INPUT 29
```

In this situation, shell metacharacters can be interpreted directly.

---

# Quoted Context

Sometimes the application places user-controlled input inside quotation marks.

Example:

```bash
command "USER_INPUT"
```

In this context, injected metacharacters may simply be treated as part of the quoted string.

---

# Breaking Out of Quotes

The PortSwigger material explains that attackers may first terminate the quoted context before injecting additional commands.

This can be done using either:

```text
"
```

or

```text
'
```

depending on how the application constructs the original command.

After leaving the quoted context, suitable shell metacharacters can be used to inject a new command.

---

# Why Context Matters

Different applications build shell commands differently.

Before selecting a payload, it is important to understand:

- Whether input is quoted.
- Whether metacharacters are interpreted.
- Which shell syntax is accepted.

The same payload may succeed in one context and fail in another.

---

# Testing Strategy

During testing:

1. Observe how the application processes input.
2. Determine whether input appears inside quotation marks.
3. Adjust payloads according to the execution context.
4. Test appropriate shell metacharacters.

---

# Key Takeaways

- The execution context determines which payloads are effective.
- Quoted input may require breaking out of the quoted string before injecting commands.
- Understanding command construction improves the effectiveness of Command Injection testing.