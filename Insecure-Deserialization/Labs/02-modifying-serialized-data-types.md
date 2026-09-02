# Lab 02 — Modifying Serialized Data Types

## Objective

Exploit PHP serialized data-type manipulation to access the administrator account and delete `carlos`.

Credentials:

```text
wiener:peter
```

## Steps

1. Log in.
2. Inspect the session cookie using Burp Inspector.
3. Identify the serialized PHP object.
4. Send the request to Burp Repeater.
5. Modify the username length to `13`.
6. Change the username to:

```text
administrator
```

7. Change `access_token` from a string to integer `0`.
8. Remove the quotation marks around the integer.
9. Change the type label from `s` to `i`.

The resulting object is:

```text
O:4:"User":2:{s:8:"username";s:13:"administrator";s:12:"access_token";i:0;}
```

10. Apply the changes.
11. Send the request.
12. Access `/admin`.
13. Delete:

```text
/admin/delete?username=carlos
```

## Learning point

Serialization preserves data types. This can interact with language-specific comparison behavior.
