# Data-Type Manipulation

## String to integer

Example from the Academy:

```text
s:12:"access_token";i:0;
```

The original value is changed from a string to integer `0`.

## PHP comparison example

```php
if ($login['password'] == $password) {
    // authentication logic
}
```

The exact exploitability depends on PHP version and the comparison behavior.

## PHP version note

PHP 7.x and earlier:

```text
0 == "Example string"
```

can evaluate to true.

PHP 8+:

```text
0 == "Example string"
```

evaluates to false.

However:

```text
5 == "5 of something"
```

continues to behave as a numeric comparison.

## Serialization warning

When changing a type, update its serialized type label and syntax.
