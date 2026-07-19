# Origin Testing Payloads

Use these Origin values while testing CORS.

---

## Basic

```http
Origin: https://evil.com
```

---

## Null Origin

```http
Origin: null
```

---

## Prefix Bypass

```http
Origin: https://trusted.com.evil.com
```

---

## Username Injection

```http
Origin: https://trusted.com@evil.com
```

---

## Similar Domain

```http
Origin: https://eviltrusted.com
```

---

## Different Protocol

```http
Origin: http://trusted.com
```

---

## Localhost

```http
Origin: http://localhost:3000
```

---

## IP Address

```http
Origin: http://127.0.0.1
```

---

## Observe

Check whether the server responds with:

```http
Access-Control-Allow-Origin
```

matching the supplied Origin.

If yes, continue testing for credentialed access and sensitive data exposure.# Origin Testing Payloads

Use these Origin values while testing CORS.

---

## Basic

```http
Origin: https://evil.com
```

---

## Null Origin

```http
Origin: null
```

---

## Prefix Bypass

```http
Origin: https://trusted.com.evil.com
```

---

## Username Injection

```http
Origin: https://trusted.com@evil.com
```

---

## Similar Domain

```http
Origin: https://eviltrusted.com
```

---

## Different Protocol

```http
Origin: http://trusted.com
```

---

## Localhost

```http
Origin: http://localhost:3000
```

---

## IP Address

```http
Origin: http://127.0.0.1
```

---

## Observe

Check whether the server responds with:

```http
Access-Control-Allow-Origin
```

matching the supplied Origin.

If yes, continue testing for credentialed access and sensitive data exposure.