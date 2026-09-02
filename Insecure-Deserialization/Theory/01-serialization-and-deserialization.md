# Serialization and Deserialization

## Serialization

Serialization converts complex data structures, such as objects and their fields, into a flatter format that can be transmitted as a sequential stream of bytes.

It makes it easier to:

- Write complex data to inter-process memory, files, or databases.
- Send complex data over a network between application components or through an API.
- Preserve the state of an object, including its attributes and assigned values.

## Deserialization

Deserialization restores the byte stream into a functional replica of the original object, preserving its state.

After deserialization, application logic can interact with the resulting object like any other object.

## Language terminology

Serialization is also called:

- **Marshalling** in Ruby.
- **Pickling** in Python.

These terms describe the same general concept in this context.

## Important security detail

Native serialization can preserve all original object attributes, including private fields. A field must normally be explicitly marked as `transient` if it should not be serialized.

The exact serialized representation depends on the programming language. Some formats are binary while others are human-readable strings.

Source basis: PortSwigger Web Security Academy — Insecure deserialization.
