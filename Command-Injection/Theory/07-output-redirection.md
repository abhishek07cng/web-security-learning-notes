# Exploiting Blind OS Command Injection Using Output Redirection

## Overview

When an application is vulnerable to **Blind OS Command Injection**, the output of injected commands is not returned in the HTTP response.

One technique to overcome this limitation is **output redirection**.

Instead of displaying the output directly, the attacker redirects it to a file that can later be accessed through the web server.

---

# How Output Redirection Works

The PortSwigger material demonstrates redirecting the output of an injected command into a writable directory inside the web root.

Example payload:

```bash
& whoami > /var/www/static/whoami.txt &
```

The `>` operator redirects the output of the `whoami` command into the file:

```text
/var/www/static/whoami.txt
```

The attacker can then retrieve the file using the browser.

---

# Lab Scenario

The vulnerable application contains a writable directory:

```text
/var/www/images/
```

The application serves files from this directory.

---

# Lab Payload

The email parameter is modified to:

```text
email=||whoami>/var/www/images/output.txt||
```

This executes the `whoami` command and stores its output inside:

```text
output.txt
```

---

# Retrieving the Output

Instead of requesting an image, modify the request to load:

```text
filename=output.txt
```

The application returns the contents of the generated file, revealing the command output.

---

# Attack Workflow

```
Inject Command

↓

Redirect Output

↓

Write File

↓

Request File

↓

View Command Output
```

---

# Why It Works

Although the application suppresses command output, it still allows the injected command to create files.

If the output is written to a web-accessible location, the attacker can retrieve it through a normal HTTP request.

---

# Key Takeaways

- Output redirection is useful for exploiting Blind Command Injection.
- The `>` operator redirects command output into a file.
- Writable directories inside the web root can expose command results.