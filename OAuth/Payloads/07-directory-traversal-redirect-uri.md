# Directory Traversal in redirect_uri

Goal

Reach unintended callback pages.

---

Common Payloads

```
../
..%2f
%2e%2e/
%252e%252e/
```

---

Examples

```
/oauth-callback/../post
```

```
/oauth/../comment-form
```

---

Questions

- Is normalization applied?
- Can callback path escape restrictions?
- Can an internal page become the callback?

---

Impact

- Open redirect chaining
- Token leakage
- Proxy page abuse