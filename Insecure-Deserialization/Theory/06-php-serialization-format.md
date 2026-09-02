# PHP Serialization Format

PHP uses a mostly human-readable serialization format.

Letters identify data types and numbers commonly identify lengths or counts.

## Example

```text
O:4:"User":2:{s:4:"name":s:6:"carlos";s:10:"isLoggedIn";b:1;}
```

This represents a `User` object.

### Breakdown

```text
O:4:"User"
```

An object with the four-character class name `User`.

```text
2
```

The object has two attributes.

```text
s:4:"name"
```

A string key of length 4: `name`.

```text
s:6:"carlos"
```

A string value of length 6: `carlos`.

```text
s:10:"isLoggedIn"
```

A string key of length 10.

```text
b:1
```

A boolean value of `true`.

## PHP functions

Native PHP serialization functions include:

```php
serialize()
unserialize()
```

If source code is available, `unserialize()` is an important function to investigate.

## Testing warning

When modifying serialized PHP objects, update the relevant type labels, lengths, and structure so the object remains valid.
