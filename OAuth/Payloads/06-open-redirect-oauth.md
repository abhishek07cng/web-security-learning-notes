# OAuth Open Redirect Checklist

Look for parameters:

```
next
url
redirect
redirect_uri
continue
return
returnTo
dest
destination
target
path
```

---

## Tests

External URL

```
https://evil.com
```

---

Protocol-relative

```
////evil.com
```

---

Encoded

```
https:%2f%2fevil.com
```

---

Nested Redirect

```
trusted.com?next=https://evil.com
```

---

Directory Traversal

```
../
```

---

## Impact

- Authorization code theft
- Access token theft
- OAuth account takeover