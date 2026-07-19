# Burp Suite Workflow for CORS Testing

## Step 1

Browse the application normally.

---

## Step 2

Intercept an authenticated API request.

---

## Step 3

Send the request to Repeater.

---

## Step 4

Modify the `Origin` header.

Examples:

```http
Origin: https://evil.com
```

```http
Origin: null
```

```http
Origin: https://trusted.com.evil.com
```

---

## Step 5

Inspect:

```http
Access-Control-Allow-Origin
```

and

```http
Access-Control-Allow-Credentials
```

---

## Step 6

If vulnerable:

- Confirm sensitive data
- Build proof of concept
- Assess business impact

---

## Useful Burp Tools

- Proxy
- Repeater
- Comparer
- Logger
- HTTP History