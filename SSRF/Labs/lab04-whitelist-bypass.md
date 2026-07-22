# Lab 04: SSRF with Whitelist-Based Input Filter

## Lab Description

This lab contains a stock checking feature that is vulnerable to SSRF.

Unlike previous labs, the application validates the supplied URL against a whitelist of trusted hosts.

Your objective is to bypass the whitelist validation, access the administrator interface running on the local server, and delete the user **carlos**.

---

# Objective

- Bypass the whitelist validation.
- Access the administrator interface.
- Delete the user `carlos`.

---

# Vulnerability

The application validates the hostname using flawed URL parsing.

It supports embedded credentials within URLs, allowing an attacker to manipulate how the hostname is interpreted.

---

# Initial Testing

Replace the `stockApi` parameter with:

```text
http://127.0.0.1/
```

The request is rejected because the hostname is not on the whitelist.

---

## Embedded Credentials

Try:

```text
http://username@stock.weliketoshop.net/
```

The request is accepted.

This indicates that the application supports URLs containing credentials.

---

## URL Fragment Test

Append a fragment:

```text
http://username#@stock.weliketoshop.net/
```

The request is rejected.

This suggests the filter parses the URL before decoding.

---

## Double URL Encoding

Encode the `#` character twice.

```
#

↓

%23

↓

%2523
```

---

## Final Payload

```text
http://localhost:80%2523@stock.weliketoshop.net/admin/delete?username=carlos
```

---

# Why This Works

The whitelist validates:

```
stock.weliketoshop.net
```

However, after decoding, the backend interprets the URL differently and connects to:

```
localhost
```

The attacker bypasses the hostname validation using inconsistent URL parsing.

---

# Burp Workflow

```
Intercept

↓

Repeater

↓

127.0.0.1

↓

Blocked

↓

Embedded Credentials

↓

Double URL Encoding

↓

localhost/admin

↓

Delete Carlos
```

---

# Impact

Improper URL parsing allows attackers to bypass hostname allowlists and access internal resources.

---

# Mitigation

- Use a standards-compliant URL parser.
- Decode input before validation.
- Validate the final resolved destination.
- Disable unnecessary redirects.

---

# Bug Bounty Methodology

Whenever you encounter hostname allowlists, test:

- `@`
- `#`
- `%23`
- `%2523`
- URL encoding
- Double URL encoding
- Nested hostnames

---

# Key Learnings

- Whitelists can fail due to inconsistent URL parsing.
- Embedded credentials are a common SSRF bypass technique.
- Double URL encoding can defeat naive validation.