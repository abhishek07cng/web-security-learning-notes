# Lab 03 — Using Application Functionality

## Objective

Exploit a dangerous application operation using a modified serialized object to delete:

```text
/home/carlos/morale.txt
```

Credentials:

```text
wiener:peter
```

Backup account:

```text
gregg:rosebud
```

## Steps

1. Log in.
2. On **My account**, identify the account deletion feature.
3. It sends:

```http
POST /my-account/delete
```

4. Send a request containing the session cookie to Burp Repeater.
5. Inspect the serialized object.
6. Identify the `avatar_link` attribute.
7. Notice that it contains the avatar file path.
8. Modify it to:

```text
/home/carlos/morale.txt
```

9. Update the serialized length indicator.

The modified attribute is:

```text
s:11:"avatar_link";s:23:"/home/carlos/morale.txt"
```

10. Apply the changes.
11. Change the request to:

```http
POST /my-account/delete
```

12. Send the request.

## Learning point

Existing application functionality can become dangerous when insecure deserialization lets an attacker control the data supplied to that functionality.
