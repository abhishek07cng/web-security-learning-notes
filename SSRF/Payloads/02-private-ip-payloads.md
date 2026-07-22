# Private IP Payloads

## RFC1918 Address Ranges

```text
10.0.0.0/8

172.16.0.0/12

192.168.0.0/16
```

---

## Common Targets

```text
http://192.168.0.1

http://192.168.0.10

http://192.168.0.100

http://192.168.0.254

http://10.0.0.1

http://10.0.1.1

http://172.16.0.1
```

---

## Common Admin Paths

```text
/admin

/admin/login

/dashboard

/manage

/api

/debug
```

---

## Burp Intruder Scan

Payload Type:

```
Numbers
```

Range:

```
1 → 255
```

Example:

```
http://192.168.0.§1§:8080/admin
```

---

## Notes

Internal services are often protected only by network isolation and may have weaker authentication.