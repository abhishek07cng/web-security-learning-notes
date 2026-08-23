# Delimiter Decoding Payloads

## Encoded Delimiters

```text
%23
```

represents:

```text
#
```

---

```text
%3f
```

represents:

```text
?
```

---

## Basic Testing

```text
/my-account%23abc
```

```text
/my-account%3fabc
```

---

## With Static Extension

```text
/my-account%23abc.js
```

```text
/my-account%3fabc.js
```

---

## Generic Pattern

```text
/<dynamic-endpoint><encoded-delimiter><arbitrary-string>.js
```

---

## Other Encoded Characters

Where relevant, investigate:

```text
%00
%0A
%09
```

These may produce different parsing behavior depending on the cache and origin server.

---

## Testing Objective

Determine whether:

```text
Cache
   ↓
Treats encoded character as ordinary data
```

while:

```text
Origin
   ↓
Decodes it as a delimiter
```