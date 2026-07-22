# SSRF Bypass Cheatsheet

## Localhost

```text
http://localhost

http://127.0.0.1

http://127.1

http://2130706433

http://017700000001
```

---

## Private IP Ranges

```text
10.0.0.0/8

172.16.0.0/12

192.168.0.0/16
```

---

## Blacklist Bypass

- Alternative IP formats
- URL Encoding
- Double URL Encoding
- DNS Resolution
- Redirect Chains

---

## Whitelist Bypass

```text
https://trusted-site:pass@evil.com

https://evil.com#trusted-site

https://trusted-site.evil.com
```

---

## Open Redirect

```
Allowed URL

↓

302 Redirect

↓

Internal Resource
```

---

## Blind SSRF

Test with:

- Burp Collaborator
- Referer Header
- Callback URLs
- Analytics Features

---

## Common SSRF Targets

- localhost
- Admin Panels
- Internal APIs
- Metadata Services
- Kubernetes
- Jenkins
- Elasticsearch
- Redis

---

## Bug Bounty Checklist

✓ Test localhost

✓ Test private IP ranges

✓ Try alternate IP formats

✓ Test redirect behavior

✓ Use Burp Collaborator

✓ Look for hidden URL fetchers

✓ Check Referer-based analytics

---

# Quick Revision

Remember these common SSRF techniques:

- Localhost SSRF
- Internal Network SSRF
- Blacklist Bypass
- Whitelist Bypass
- Open Redirect
- Blind SSRF
- OAST Detection