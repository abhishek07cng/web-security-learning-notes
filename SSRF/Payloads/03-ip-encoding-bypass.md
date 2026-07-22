# IP Encoding Bypass

## Decimal Representation

```text
127.0.0.1

↓

2130706433
```

---

## Octal Representation

```text
127.0.0.1

↓

017700000001
```

---

## Shortened Loopback

```text
127.1
```

---

## Mixed Representations

Test different encodings accepted by the backend HTTP client.

---

## Why It Works

Some filters compare strings rather than resolving the final IP address, allowing alternative representations to bypass blacklist checks.

---

## Notes

Always compare the application's validation logic with the backend request behavior.