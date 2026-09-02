# Insecure Deserialization — Quick Revision

## Core definition

User-controllable serialized data is deserialized.

## Why dangerous?

It may allow:

- Object injection.
- Privilege escalation.
- Arbitrary file access.
- DoS.
- RCE.

## Formats

### PHP
```text
O:4:"User":...
```

Functions:

```php
serialize()
unserialize()
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

Method:

```java
readObject()
```

### Ruby

Serialization is commonly called **marshalling**.

## Attack path

```text
Serialized input
→ Modify attributes
→ Modify types
→ Abuse functionality
→ Inject objects
→ Magic method
→ Gadget chain
→ Sink
```

## Gadget chain

Existing code is chained together. The attacker controls the data flowing through it.

## Detection

For blind Java deserialization:

- URLDNS → DNS interaction.
- JRMPClient → TCP connection.

## PHAR

`phar://` can trigger implicit metadata deserialization during filesystem operations.

## Prevention

- Avoid deserializing user input.
- Verify signatures before deserialization.
- Prefer class-specific serialization.
- Do not rely on removing gadget chains.
