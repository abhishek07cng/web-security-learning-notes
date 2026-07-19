# Origin Validation Bypass Payloads

Use these values to test weak origin validation.

```http
Origin: https://evil.com
```

```http
Origin: null
```

```http
Origin: https://trusted.com.evil.com
```

```http
Origin: https://trusted.com@evil.com
```

```http
Origin: https://eviltrusted.com
```

```http
Origin: http://trusted.com
```

```http
Origin: http://localhost
```

```http
Origin: http://127.0.0.1
```

---

## Observe

Does the application return:

```http
Access-Control-Allow-Origin
```

with the supplied value?

If yes, investigate further for sensitive data exposure.