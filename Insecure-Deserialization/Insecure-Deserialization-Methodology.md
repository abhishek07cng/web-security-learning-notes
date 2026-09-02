# Insecure Deserialization Methodology

## 1. Detect

Find data that appears to contain a serialized object.

## 2. Identify the format

Determine whether the data is:

- PHP serialization.
- Java serialization.
- Ruby Marshal.
- Another serialized representation.

## 3. Decode

Remove Base64, URL encoding, or other transport encoding.

## 4. Understand the object

Identify:

- Class.
- Fields.
- Types.
- Length indicators.
- Session/security relevance.

## 5. Manipulate

Start with simple attribute changes.

Then investigate data-type changes and arbitrary object injection.

## 6. Follow the data

Determine how each controlled value is used after deserialization.

## 7. Find automatic execution

Inspect magic methods such as:

- `__wakeup()`
- `__destruct()`
- Java `readObject()`

## 8. Build the chain

Follow method calls until controlled data reaches a dangerous sink.

## 9. Use suitable detection/exploitation techniques

Depending on the environment:

- Pre-built gadget chains.
- Documented chains.
- Custom chains.
- OAST detection.
- PHAR deserialization.

## 10. Confirm impact

Demonstrate the security consequence in an authorized environment and document the exact data flow.
