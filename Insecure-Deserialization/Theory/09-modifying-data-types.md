# Modifying Data Types

In addition to changing attribute values, an attacker may be able to supply an unexpected data type.

## PHP loose comparison

PHP's loose comparison operator `==` can produce dangerous logic when attacker-controlled deserialized data is compared with another value.

Example:

```php
$login = unserialize($_COOKIE);

if ($login['password'] == $password) {
    // log in successfully
}
```

If an attacker changes a password attribute to integer `0`, older PHP behavior can cause an authentication bypass when the stored password does not start with a number.

## Version detail

In PHP 7.x and earlier:

```text
0 == "Example string"
```

evaluates to true because the string is treated as integer `0`.

In PHP 8 and later, that comparison evaluates to false.

However, an alphanumeric string beginning with a number retains the relevant behavior described by the Academy. For example:

```text
5 == "5 of something"
```

is treated as:

```text
5 == 5
```

## Serialization requirement

If changing a serialized value's type, update the type label and remove/add syntax as required.

Example:

```text
s:12:"access_token";i:0;
```

The value is now an integer instead of a string.

Incorrect type labels or lengths can corrupt the serialized object.
