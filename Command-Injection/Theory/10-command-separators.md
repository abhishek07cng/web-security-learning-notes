# Command Separators

## Overview

OS Command Injection relies on **shell metacharacters** to separate or chain commands.

The PortSwigger material identifies several command separators that attackers use to execute additional operating system commands.

The behaviour of each separator varies depending on the operating system and shell implementation.

---

# Cross-Platform Command Separators

The following command separators work on both **Windows** and **Unix-based** systems:

```text
&
&&
|
||
```

These characters allow multiple commands to be executed within a single shell command.

---

# Unix-Specific Command Separators

The following separators work only on Unix-based systems:

```text
;
```

```text
Newline (\n / 0x0a)
```

These can also be used to terminate one command and begin another.

---

# Example

Suppose the application normally executes:

```bash
stockreport.pl 381 29
```

An attacker supplies:

```text
& echo test &
```

The resulting command becomes:

```bash
stockreport.pl & echo test & 29
```

The shell interprets the `&` characters as command separators and executes:

1. `stockreport.pl`
2. `echo test`
3. `29`

---

# Why Separators Matter

Command separators allow attackers to:

- Inject additional commands.
- Break the intended execution flow.
- Execute arbitrary operating system commands.

Without these metacharacters, user input is more likely to be treated as a normal argument.

---

# Choosing a Separator

The PortSwigger material notes that different metacharacters have subtly different behaviour.

Depending on:

- Operating system
- Shell implementation
- Application context

one separator may work while another does not.

Testing multiple separators can therefore help identify exploitable command injection points.

---

# Key Takeaways

- Command separators are fundamental to OS Command Injection.
- `&`, `&&`, `|`, and `||` work on both Windows and Unix-based systems.
- `;` and newline characters are Unix-specific separators.
- Different environments may interpret separators differently.