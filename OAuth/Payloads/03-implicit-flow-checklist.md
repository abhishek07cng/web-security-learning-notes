# Implicit Flow Checklist

Expected

```
response_type=token
```

---

## Token Location

Check whether the token appears in:

```
URL Fragment

#access_token=
```

---

## Client-side Risks

Look for:

- JavaScript
- postMessage()
- location.hash
- window.location
- document.location
- localStorage
- sessionStorage

---

## Questions

- Can token leak through redirects?
- Can token leak via Referer?
- Can XSS access it?
- Can postMessage expose it?

---

## Recommendation

Prefer Authorization Code Flow + PKCE.