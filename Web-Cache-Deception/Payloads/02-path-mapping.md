# Path Mapping Payloads

## Baseline

```text
/my-account
```

---

## Arbitrary Path Segment

```text
/my-account/abc
```

```text
/my-account/test
```

```text
/my-account/wcd
```

---

## Arbitrary Segment + Extension

```text
/my-account/abc.js
```

```text
/my-account/abc.css
```

```text
/my-account/abc.ico
```

---

## Generic Pattern

```text
/<dynamic-endpoint>/<arbitrary-string>
```

```text
/<dynamic-endpoint>/<arbitrary-string>.js
```

---

## Example

```text
/user/123/profile/wcd.css
```

Potential interpretation:

```text
Origin:
/user/123/profile
```

```text
Cache:
/user/123/profile/wcd.css
```

---

## Testing Sequence

```text
/dynamic-endpoint
/dynamic-endpoint/abc
/dynamic-endpoint/abc.js
```

Compare:

```text
Status
Response Body
X-Cache
```