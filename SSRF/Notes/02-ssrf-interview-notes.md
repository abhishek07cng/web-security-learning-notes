# SSRF Interview Notes

## What is SSRF?

Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to manipulate a server into making unintended requests to internal or external resources.

Instead of communicating with the intended destination, the server sends requests chosen by the attacker.

---

## Why is SSRF Dangerous?

Because the request originates from the server itself, it may access:

- Localhost
- Internal APIs
- Private Networks
- Administrative Interfaces

These resources are usually inaccessible from the Internet.

---

## Common SSRF Targets

- localhost
- 127.0.0.1
- Internal IP ranges
- Admin panels
- Cloud metadata services
- Internal APIs

---

## Types of SSRF

### Normal SSRF

The attacker receives the server's response.

---

### Blind SSRF

The server performs the request, but the response is not returned.

Detection requires Out-of-Band techniques such as Burp Collaborator.

---

## Common Bypass Techniques

### Blacklist Bypass

- Alternative IP formats
- URL Encoding
- Double URL Encoding

---

### Whitelist Bypass

- Embedded credentials (`@`)
- URL fragments (`#`)
- Nested hostnames
- Double URL encoding

---

### Open Redirect

If the backend follows redirects automatically, an Open Redirect can bypass SSRF restrictions.

---

## Detecting Blind SSRF

Use Burp Collaborator.

Look for:

- DNS interactions
- HTTP interactions

These interactions confirm that the server attempted an outbound request.

---

## Prevention

- Use strict allowlists.
- Validate the final destination after parsing.
- Restrict outbound network access.
- Protect internal services with authentication.
- Disable unnecessary automatic redirects.

---

## Interview Tips

### Difference Between SSRF and XXE

- **SSRF** abuses server-side request functionality to reach unintended resources.
- **XXE** exploits XML parsers and may lead to SSRF when external entities trigger server-side requests.

---

### Difference Between SSRF and CSRF

- **SSRF** tricks the **server** into making requests.
- **CSRF** tricks the **user's browser** into sending unwanted authenticated requests.

---

### Difference Between SSRF and Open Redirect

- **SSRF** causes the server to fetch unintended resources.
- **Open Redirect** changes where a client or server is redirected.
- An Open Redirect can sometimes be chained with SSRF to bypass URL validation.

---

## One-Minute Interview Answer

> SSRF is a vulnerability where an attacker manipulates a server into making unintended requests to resources such as localhost, internal APIs, or private networks. Depending on the reachable systems, SSRF can lead to information disclosure, authentication bypass, internal network access, or even remote code execution. Common testing includes localhost, private IP ranges, filter bypass techniques, and Blind SSRF detection using Burp Collaborator. Effective defenses include strict allowlists, secure URL parsing, outbound network restrictions, and authentication for internal services.