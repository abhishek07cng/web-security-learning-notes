# Command Injection Observations

## Overview

OS Command Injection is one of the most severe web application vulnerabilities because it allows user-controlled input to be interpreted as operating system commands.

The PortSwigger Academy demonstrates both direct and blind exploitation techniques, showing that even when command output is hidden, successful execution can still be confirmed using alternative methods.

---

# Key Observations

## 1. Visible Output Is the Simplest Confirmation

If the application returns the output of an injected command, confirming the vulnerability is straightforward.

Example:

```text
& echo aiwefwlguh &
```

If the string appears in the HTTP response, the application is executing injected operating system commands.

---

## 2. Hidden Output Does Not Mean Safe

Many applications suppress command output.

This does **not** prevent OS Command Injection.

Instead, alternative techniques can be used, including:

- Time delays
- Output redirection
- Out-of-Band (OAST) interactions

---

## 3. Command Separators Are Critical

The vulnerability relies on shell metacharacters to modify command execution.

The PortSwigger material demonstrates separators including:

```text
&
&&
|
||
;
```

Different separators may behave differently depending on the operating system and shell.

---

## 4. Reconnaissance Is Important

After confirming command execution, gathering basic system information helps understand the execution environment.

Useful commands include:

Linux:

```bash
whoami
uname -a
ifconfig
```

Windows:

```cmd
whoami
ver
ipconfig /all
```

---

## 5. Burp Collaborator Is Valuable

When:

- output is hidden,
- response timing is unreliable, or
- files cannot be written,

Burp Collaborator provides a reliable way to confirm command execution through DNS interactions.

---

## Personal Notes

- Start with harmless payloads before attempting more advanced techniques.
- Observe how the application handles user input.
- If visible output fails, move to blind detection methods in a structured order.
- Test multiple command separators because application context may affect behaviour.
- Record successful payloads for future testing.

---

# Key Learnings

- OS Command Injection may be visible or blind.
- Blind vulnerabilities still allow reliable confirmation through indirect techniques.
- Understanding shell behaviour is essential when testing for this vulnerability.