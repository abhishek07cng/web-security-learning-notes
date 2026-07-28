# Inline Command Execution

## Overview

In addition to command separators, Unix-based systems support **inline command execution**.

Instead of executing commands sequentially, the shell first executes the injected command and then substitutes its output into the original command.

The PortSwigger material identifies two mechanisms for inline execution.

---

# Backticks

Syntax:

```text
`command`
```

Everything enclosed within backticks is executed by the shell.

The resulting output is substituted into the original command.

---

# Dollar Syntax

Syntax:

```text
$(command)
```

This provides another method for inline command execution.

Like backticks, the enclosed command executes first.

---

# Purpose

Inline execution enables attackers to:

- Execute additional commands.
- Insert command output into the original command.
- Perform more complex command injection attacks.

---

# Behaviour

Execution flow:

```
Original Command

↓

Inline Command Executes

↓

Command Output Generated

↓

Output Inserted

↓

Original Command Continues
```

---

# Important Considerations

The PortSwigger material notes that:

- Inline execution is supported on Unix-based systems.
- Different shell metacharacters may behave differently depending on the execution context.

Testing both supported syntaxes can help determine whether inline execution is possible.

---

# Key Takeaways

- Unix-based shells support inline command execution.
- Two supported syntaxes are:
  - Backticks ( `command` )
  - Dollar syntax ( `$(command)` )
- Inline execution runs the injected command before the original command continues.