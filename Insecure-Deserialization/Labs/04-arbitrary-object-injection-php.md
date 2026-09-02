# Lab 04 — Arbitrary Object Injection in PHP

## Objective

Create and inject a malicious serialized object to delete:

```text
/home/carlos/morale.txt
```

This lab requires source-code access.

Credentials:

```text
wiener:peter
```

## Hint

The Academy notes that appending `~` to a filename can sometimes retrieve an editor-generated backup file.

## Steps

1. Log in.
2. Inspect the serialized session cookie.
3. From the site map, identify:

```text
/libs/CustomTemplate.php
```

4. Send the file request to Repeater.
5. Append:

```text
~
```

to retrieve the source backup.
6. Inspect the `CustomTemplate` class.
7. Identify the `__destruct()` magic method.
8. Observe that it invokes `unlink()` on the `lock_file_path` attribute.
9. Create a serialized `CustomTemplate` object with:

```text
lock_file_path = /home/carlos/morale.txt
```

Serialized object:

```text
O:14:"CustomTemplate":1:{s:14:"lock_file_path";s:23:"/home/carlos/morale.txt";}
```

10. Base64- and URL-encode the object.
11. Replace the session cookie in Repeater.
12. Send the request.

## Learning point

Arbitrary object injection can let an attacker instantiate a class whose magic method performs a dangerous operation automatically.
