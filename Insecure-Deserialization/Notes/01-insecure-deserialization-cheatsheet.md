# Insecure Deserialization Cheatsheet

## Definition

User-controlled serialized data is deserialized by the application.

## Common locations

- Session cookies.
- Request parameters.
- API/application data.

## Identify

### PHP
```text
O:4:"User":...
```

### Java
Hex:
```text
ac ed
```

Base64:
```text
rO0
```

## PHP functions

```php
serialize()
unserialize()
```

## Java

```java
Serializable
readObject()
```

## Attack progression

```text
Identify serialized data
        ↓
Modify attributes
        ↓
Modify data types
        ↓
Abuse application functionality
        ↓
Inject arbitrary objects
        ↓
Find magic methods
        ↓
Build/use gadget chains
        ↓
Reach dangerous sink
```

## Impact

- RCE
- Privilege escalation
- Arbitrary file access
- DoS
