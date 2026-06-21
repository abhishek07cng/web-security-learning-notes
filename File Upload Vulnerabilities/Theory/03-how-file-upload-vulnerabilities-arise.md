# How File Upload Vulnerabilities Arise

## Developers Usually Add Validation

But validation is often:

```text
Incomplete
Incorrect
Inconsistent
```

---

# Common Mistakes

## Blacklists

Block:

```text
.php
```

But forget:

```text
.php5
.phtml
.pHp
```

---

## Trusting MIME Type

Server checks:

```http
Content-Type:image/jpeg
```

Attacker changes header.

---

## Trusting Filename

Example:

```text
shell.php.jpg
```

---

## Weak Content Validation

Checks only:

```text
Magic Bytes
```

Can be bypassed using polyglots.

---

## Different Server Behavior

Front-end:

```text
Rejects
```

Backend:

```text
Accepts
```

---

# Root Cause

```text
Untrusted User Input
```

being trusted by the server.

---

# Key Takeaways

- Blacklists fail.
- User-controlled metadata should never be trusted.