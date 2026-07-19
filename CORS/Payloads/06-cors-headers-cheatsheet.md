# CORS Headers Cheatsheet

| Header | Purpose |
|---------|----------|
| Origin | Identifies requesting origin |
| Access-Control-Allow-Origin | Trusted origin |
| Access-Control-Allow-Credentials | Allows cookies/authentication |
| Access-Control-Allow-Methods | Allowed HTTP methods |
| Access-Control-Allow-Headers | Allowed request headers |
| Access-Control-Expose-Headers | Readable response headers |
| Access-Control-Max-Age | Cache preflight response |

---

## Dangerous Combination

```http
Access-Control-Allow-Origin:
https://evil.com

Access-Control-Allow-Credentials:
true
```

---

## Safe Configuration

```http
Access-Control-Allow-Origin:
https://app.example.com
```

Exact allowlists are preferred.