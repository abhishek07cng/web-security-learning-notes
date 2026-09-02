# Modifying Serialized Objects

A basic deserialization exploit may require nothing more than modifying an attribute in an existing serialized object.

Because object state is persisted, serialized data can reveal interesting attributes.

## Two approaches

### Direct editing

Modify the serialized byte/string representation directly.

This is practical for human-readable formats such as PHP serialization.

### Programmatic serialization

Write a short script/program in the corresponding language to:

1. Create the desired object.
2. Set its attributes.
3. Serialize it.
4. Encode it as required by the application.

This is often easier for binary formats such as Java serialization.

## Critical requirement

The modified data must remain a valid serialized object.

When changing types or lengths, update:

- Type labels.
- String lengths.
- Attribute structure.
- Any encoding layers such as Base64 or URL encoding.

A corrupted serialized object will generally fail to deserialize.
