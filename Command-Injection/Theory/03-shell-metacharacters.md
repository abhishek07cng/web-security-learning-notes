# Shell Metacharacters

## Overview

Shell metacharacters are special characters interpreted by the operating system shell.

Instead of being treated as normal input, they modify how commands are executed.

Attackers use these characters to inject additional commands.

---

# Command Separators

The PortSwigger material identifies the following command separators that work on both Windows and Unix-based systems:

```text
&
&&
|
||
```

These characters allow multiple commands to be chained together.

---

# Unix-Specific Separators

The following separators work only on Unix-based systems:

```text
;

Newline (\n / 0x0a)
```

---

# Inline Command Execution

Unix-based systems also support inline execution using:

```text
`command`
```

and

```text
$(command)
```

These execute the enclosed command before continuing with the original command.

---

# Example

A payload such as:

```text
& echo test &
```

causes the shell to execute:

1. Original command
2. `echo test`
3. Remaining input

---

# Why They Matter

Metacharacters allow attackers to:

- Execute additional commands.
- Chain multiple commands together.
- Modify command flow.
- Inject commands into existing shell operations.

---

# Important Note

The behaviour of each metacharacter differs slightly depending on:

- Operating system
- Shell implementation
- Context in which user input is inserted

As a result, different separators may work in different situations.

---

# Key Takeaways

- Metacharacters control shell behaviour.
- Command separators are commonly used in OS Command Injection.
- Unix systems also support inline command execution using backticks and `$()`.