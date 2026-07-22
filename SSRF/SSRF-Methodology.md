# SSRF Methodology

## Phase 1 – Identify Potential SSRF Endpoints

Look for features that fetch remote resources, such as:

- Stock Checkers
- URL Preview
- Import by URL
- Webhooks
- Image Fetchers
- PDF Generators
- Feed Readers
- Analytics Systems
- Callback URLs

---

## Phase 2 – Confirm SSRF

Replace the supplied URL with a controlled destination.

Examples:

```text
http://example.com

http://localhost

http://127.0.0.1
```

Observe whether the server makes the request.

---

## Phase 3 – Test Localhost

Try:

```text
http://localhost

http://localhost/admin

http://127.0.0.1

http://127.1
```

Look for:

- Admin Panels
- Internal APIs
- Debug Pages
- Configuration Interfaces

---

## Phase 4 – Test Internal Network

Probe common private ranges:

```text
192.168.x.x

10.x.x.x

172.16.x.x
```

Use Burp Intruder to identify live hosts and exposed services.

---

## Phase 5 – Test SSRF Defenses

### Blacklist Bypass

- Alternative IP formats
- URL Encoding
- Double URL Encoding
- Redirect Chains

### Whitelist Bypass

- Embedded Credentials (`@`)
- URL Fragments (`#`)
- Double URL Encoding
- Nested Hostnames

---

## Phase 6 – Test Redirect Handling

Search for Open Redirect vulnerabilities.

Verify whether the backend follows redirects without validating the final destination.

---

## Phase 7 – Test Blind SSRF

Use Burp Collaborator.

Check:

- Referer
- Callback URLs
- Webhooks
- Analytics
- URL Preview

Poll Collaborator for:

- DNS interactions
- HTTP interactions

---

## Phase 8 – Assess Impact

Determine whether SSRF allows access to:

- Localhost
- Internal APIs
- Admin Panels
- Private Networks
- Sensitive Data
- Cloud Metadata
- Other Vulnerable Internal Services

---

## Phase 9 – Report

Include:

- Vulnerable endpoint
- Parameter
- Payload
- Proof of Concept
- Business Impact
- Screenshots
- Mitigation Recommendations