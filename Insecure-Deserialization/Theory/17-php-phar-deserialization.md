# PHAR Deserialization

PHP can sometimes deserialize attacker-controlled data without an obvious `unserialize()` call.

## phar://

PHP provides URL-style wrappers, including:

```text
phar://
```

The wrapper provides a stream interface for PHP Archive (`.phar`) files.

## Why PHAR can deserialize data

PHAR manifest files contain serialized metadata.

When filesystem operations are performed on a `phar://` stream, this metadata can be implicitly deserialized.

Therefore, a filesystem operation can potentially become a deserialization vector.

## Less obvious filesystem methods

Obviously dangerous functions such as `include()` or `fopen()` may have countermeasures.

Methods such as:

```php
file_exists()
```

may be less obviously dangerous while still triggering the relevant behavior.

## Upload requirement

The attacker generally needs to get the PHAR onto the server.

An image upload can sometimes be used with a PHAR/JPG polyglot.

The extension does not necessarily prevent PHP from processing a `phar://` stream.

## Magic methods

If the required class is supported, methods such as:

- `__wakeup()`
- `__destruct()`

can be invoked and may start a gadget chain.
