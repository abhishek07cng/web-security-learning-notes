# What is OS Command Injection?

## Overview

OS Command Injection, also known as **Shell Injection**, is a vulnerability that allows an attacker to execute operating system (OS) commands on the server running a vulnerable application.

If successfully exploited, attackers can often fully compromise the application and its data. In many cases, attackers can also use the compromised server as a pivot point to attack other systems within the organization's infrastructure.

---

# Why It Is Dangerous

An OS Command Injection vulnerability may allow an attacker to:

- Execute arbitrary operating system commands.
- Read sensitive files.
- Gather information about the host system.
- Compromise the application.
- Pivot to other trusted systems within the infrastructure.

---

# Example Scenario

A shopping application allows users to check stock levels using the following request:

```http
GET /stockStatus?productID=381&storeID=29
```

Internally, the application executes:

```bash
stockreport.pl 381 29
```

The application directly inserts user-supplied input into a shell command without proper validation.

---

# Vulnerable Input

Suppose an attacker supplies the following value for `productID`:

```text
& echo aiwefwlguh &
```

The command becomes:

```bash
stockreport.pl & echo aiwefwlguh & 29
```

Because `&` is a shell command separator, three commands are executed:

1. `stockreport.pl`
2. `echo aiwefwlguh`
3. `29`

---

# Response

The application returns:

```text
Error - productID was not provided
aiwefwlguh
29: command not found
```

This confirms that the injected command was executed.

---

# Why `echo` Is Used

The PortSwigger material uses the `echo` command because it returns user-controlled output.

Seeing the echoed string in the application's response confirms that command injection is possible.

---

# Key Characteristics

- User input is inserted into an OS command.
- No input validation prevents command execution.
- Shell metacharacters separate commands.
- The injected command executes with the application's privileges.

---

# Key Takeaways

- OS Command Injection is also called Shell Injection.
- It allows arbitrary OS command execution.
- Successful exploitation can lead to complete server compromise.
- Simple commands such as `echo` can be used to confirm the vulnerability.