# Access Token Leakage Checklist

Inspect:

- URL Fragment
- Browser History
- Referer Header
- JavaScript
- localStorage
- sessionStorage
- postMessage()
- Logs
- Analytics
- Third-party scripts

---

Questions

- Can another origin read the token?
- Can the token be replayed?
- Does it grant API access?

---

Mitigation

- Use Authorization Code Flow + PKCE
- Avoid storing tokens in URLs