# How OS Command Injection Works

## Overview

OS Command Injection occurs when an application constructs operating system commands using user-controlled input without properly validating or restricting that input.

Instead of treating the supplied value as data, the operating system interprets it as additional commands.

---

# Normal Flow

A user requests stock information:

```http
GET /stockStatus?productID=381&storeID=29
```

The application executes:

```bash
stockreport.pl 381 29
```

The command runs normally and returns the stock status.

---

# Vulnerable Flow

If the application does not validate input, an attacker can submit:

```text
& echo aiwefwlguh &
```

The resulting command becomes:

```bash
stockreport.pl & echo aiwefwlguh & 29
```

The shell interprets the metacharacters and executes multiple commands.

---

# Why This Happens

The operating system shell recognises command separators such as:

```
&
```

Instead of treating the supplied input as a normal parameter, it executes it as a new command.

---

# Execution Flow

```
User Input

↓

Application

↓

Builds Shell Command

↓

Operating System Shell

↓

Parses Metacharacters

↓

Executes Injected Command

↓

Returns Output
```

---

# Evidence of Successful Injection

The PortSwigger example demonstrates successful execution because:

- The original command produces an error.
- The injected `echo` command executes.
- The remaining value is interpreted as a command.

This sequence confirms that arbitrary commands are being processed.

---

# Why Attackers Exploit It

Executing operating system commands enables attackers to:

- Inspect the environment.
- Gather system information.
- Execute additional commands.
- Expand access within the environment.

---

# Key Takeaways

- The vulnerability exists because user input is inserted directly into shell commands.
- Shell metacharacters change how the command is interpreted.
- Successful execution proves that the attacker controls part of the operating system command.