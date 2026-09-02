# Memory Corruption and Prevention

## Memory corruption

Even without a useful gadget chain, publicly documented memory-corruption vulnerabilities may sometimes be exploitable through insecure deserialization.

These can potentially result in remote code execution.

Deserialization functions such as PHP's `unserialize()` expose substantial attack surface and are generally not intended for user-controlled input.

## Prevention

### 1. Avoid deserializing user input

This is the preferred approach whenever possible.

### 2. Verify integrity before deserialization

If untrusted serialized data must be accepted, use robust integrity protection such as a digital signature.

The check must happen **before deserialization**.

A signature check performed after deserialization is too late.

### 3. Avoid generic deserialization

Prefer class-specific serialization methods where possible.

This limits which fields are exposed instead of automatically serializing all object attributes, including private fields.

### 4. Do not rely on removing gadgets

The vulnerability is the deserialization of user-controllable data.

Trying to remove every gadget chain is impractical because applications contain large dependency graphs and new/publicly documented vulnerabilities may appear.

## Core defensive principle

Do not treat serialized user input as trustworthy.
