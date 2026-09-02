# Cache Key Injection

## Concept

Caches often concatenate components to form a cache key.

If delimiters are not properly escaped, an attacker may inject delimiter sequences and manipulate the apparent cache key.

Example from the source:

```http
Origin: '-alert(1)-'__
```

producing a key resembling:

```text
/path?param=123__Origin='-alert(1)-'__
```

The attacker can then construct another request whose normal-looking input produces the same effective cache key.

## Security lesson

A cache key is security-sensitive data. Delimiters and component boundaries must be encoded safely before constructing composite keys.
