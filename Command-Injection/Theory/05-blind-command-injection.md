# Blind OS Command Injection

## Overview

Many OS Command Injection vulnerabilities are **blind**.

In a blind vulnerability, the application executes the injected command, but **does not return the command output in the HTTP response**.

Because no output is visible, attackers must use alternative techniques to determine whether their payload executed successfully.

---

# Example Scenario

A feedback form accepts:

- Email address
- Feedback message

The application sends the submitted information using a system mail command.

Example:

```bash
mail -s "This site is great" -aFrom:peter@normal-user.net feedback@vulnerable-website.com
```

The command executes on the server, but its output is not displayed to the user.

---

# Why Echo Doesn't Work

In a normal Command Injection vulnerability, an attacker may use:

```bash
echo test
```

to verify execution.

In a blind vulnerability, the application's response never includes the command output, so this technique cannot confirm whether the command executed.

---

# Alternative Techniques

The PortSwigger material introduces several approaches for exploiting blind Command Injection:

- Time delays
- Output redirection
- Out-of-band (OAST) interactions

Each technique provides evidence that the injected command executed successfully.

---

# Blind Injection Workflow

```
Inject Command

↓

Application Executes Command

↓

No Output Returned

↓

Use Alternative Detection Technique

↓

Confirm Execution
```

---

# Challenges

Blind Command Injection is more difficult to detect because:

- No command output is displayed.
- Successful execution is not immediately visible.
- Additional techniques are required to verify exploitation.

---

# Key Takeaways

- Blind Command Injection executes commands without returning their output.
- Standard output-based payloads such as `echo` are ineffective.
- Time delays, output redirection, and OAST techniques are useful alternatives.