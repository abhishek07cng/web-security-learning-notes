# Lab 01 — Modifying Serialized Objects

## Objective

Exploit a serialization-based session mechanism to gain administrative privileges, then delete the user `carlos`.

Credentials:

```text
wiener:peter
```

## Analysis / Steps

1. Log in using your own credentials.
2. Observe the post-login `GET /my-account` request.
3. Notice that the session cookie appears URL- and Base64-encoded.
4. Use Burp Inspector to decode and inspect the cookie.
5. Identify the serialized PHP object.
6. Notice the `admin` attribute contains:

```text
b:0
```

This represents boolean `false`.

7. Send the request to Burp Repeater.
8. In Inspector, change the attribute to:

```text
b:1
```

9. Click **Apply changes**. Burp re-encodes the object.
10. Send the request.
11. Observe the `/admin` link in the response.
12. Request:

```text
/admin
```

13. Find the delete-user functionality.
14. Request:

```text
/admin/delete?username=carlos
```

## Learning point

The exploit is based on trusting a serialized session object without verifying its authenticity.
