# Why Insecure Deserialization Arises

## 1. Misunderstanding the risk

Developers may not realize how dangerous it is to deserialize user-controllable data.

Ideally, user input should not be deserialized.

## 2. Post-deserialization validation

A developer may attempt to validate or sanitize the object after deserialization.

This is fundamentally problematic because the dangerous behavior may already have occurred during deserialization.

It is also extremely difficult to validate every possible malicious object state.

## 3. Trusting serialized data

Binary formats can appear difficult for users to understand or manipulate. This can create a false sense of security.

Attackers can still manipulate binary serialized objects.

## 4. Large dependency graphs

Modern applications may contain many libraries and dependencies. These introduce many classes and methods that may be instantiated during deserialization.

An attacker may be able to chain unexpected method calls and eventually pass controlled data into a dangerous sink.

## Fundamental conclusion

The Academy states that it can be argued that securely deserializing untrusted input is not possible.

The safer approach is to avoid deserializing untrusted input whenever possible.
