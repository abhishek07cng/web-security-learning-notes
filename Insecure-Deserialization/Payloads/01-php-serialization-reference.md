# PHP Serialization Reference

## Object format

```text
O:4:"User":2:{s:4:"name";s:6:"carlos";s:10:"isLoggedIn";b:1;}
```

## Common labels used in the Academy examples

| Label | Meaning |
|---|---|
| `O` | Object |
| `s` | String |
| `b` | Boolean |
| `i` | Integer |

## Boolean example

```text
b:0
b:1
```

## String example

```text
s:6:"carlos"
```

The numeric value represents the string length.

## Integer example

```text
i:0
```

## Example modified object

```text
O:4:"User":2:{s:8:"username";s:13:"administrator";s:12:"access_token";i:0;}
```

Always preserve valid serialization structure and update length indicators after modifications.
