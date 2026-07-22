# SSRF Observations

## What I Learned

- SSRF (Server-Side Request Forgery) allows an attacker to force a vulnerable server to make requests to unintended locations.
- Unlike client-side attacks, the server itself becomes the attacker’s proxy.
- SSRF is especially dangerous because the server usually has access to resources that external users cannot reach.

---

## Important Attack Surfaces

While studying PortSwigger labs, I noticed that SSRF commonly appears in features such as:

- Stock Checkers
- Image Fetchers
- Import by URL
- Webhooks
- URL Preview Features
- Feed Readers
- Analytics Systems
- Callback URLs

Whenever I encounter these features during bug bounty hunting, I should immediately consider SSRF testing.

---

## Localhost Testing

The first thing I should test after identifying SSRF is localhost.

Examples:

```text
http://localhost

http://127.0.0.1

http://127.1
```

Then try common endpoints:

```text
/admin

/debug

/dashboard
```

Many applications trust requests originating from localhost.

---

## Internal Network Testing

If localhost works, the next step is testing private networks.

Common ranges:

```text
192.168.x.x

10.x.x.x

172.16.x.x
```

Burp Intruder is useful for discovering live internal hosts.

---

## SSRF Defenses

The labs demonstrated several weak protections.

### Blacklist Filters

Developers block:

- localhost
- 127.0.0.1
- /admin

These can often be bypassed using:

- Alternative IP formats
- URL encoding
- Double URL encoding

---

### Whitelist Filters

Whitelist validation is stronger but still vulnerable if URL parsing is flawed.

Useful techniques:

- Embedded credentials (`@`)
- URL fragments (`#`)
- Double URL encoding
- Nested hostnames

---

## Open Redirect

An Open Redirect can sometimes bypass SSRF filters.

If the backend automatically follows redirects, an allowed URL may ultimately reach an internal resource.

---

## Blind SSRF

Blind SSRF is harder to detect because the response is never returned.

The most reliable detection method is using Burp Collaborator (OAST).

Possible interactions:

- DNS
- HTTP

Even DNS-only interactions can confirm a vulnerability.

---

## Bug Bounty Takeaways

When testing SSRF:

✓ Test localhost

✓ Test private IP ranges

✓ Try filter bypasses

✓ Look for Open Redirects

✓ Use Burp Collaborator for Blind SSRF

✓ Assess access to admin panels, internal APIs, and sensitive resources

---

## Personal Notes

- Always understand how the application builds backend requests.
- Compare validation logic with the final request made by the server.
- Small parser inconsistencies can lead to major security issues.
- SSRF often becomes much more severe when chained with other vulnerabilities.