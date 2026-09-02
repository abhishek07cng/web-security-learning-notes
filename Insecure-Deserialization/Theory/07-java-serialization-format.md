# Java Serialization Format

Java commonly uses a binary serialization format.

Although it is harder to read directly, serialized Java objects have recognizable characteristics.

## Identification

Serialized Java objects begin with bytes represented in hexadecimal as:

```text
ac ed
```

When Base64-encoded, they commonly begin with:

```text
rO0
```

## Serializable classes

A class that implements:

```java
java.io.Serializable
```

can be serialized and deserialized.

## Source-code indicators

If source code is available, look for:

```java
readObject()
```

This method is used to read and deserialize data from an `InputStream`.

## Testing approach

When a Java serialized object is identified:

1. Decode or inspect the serialized data.
2. Determine the object/class involved.
3. Identify whether its fields are controllable.
4. Investigate deserialization methods and available classes.
5. Look for dangerous methods or gadget chains.
