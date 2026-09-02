# Arbitrary Object Injection

Object-oriented applications associate behavior with classes.

If an attacker can control which serialized class is instantiated, they may influence which methods are available and executed.

## Why this works

Deserialization mechanisms may not verify that the serialized object is the class the application originally expected.

If another serializable class exists in the application, an attacker may be able to create an instance of it.

An exception later in the application does not necessarily undo the fact that the malicious object was already instantiated.

## Source-code approach

When source code is available:

1. Identify serializable classes.
2. Find classes containing deserialization magic methods.
3. Examine what those methods do.
4. Identify dangerous operations using controllable attributes.
5. Construct a serialized object for a useful class.

This is the foundation of many advanced deserialization exploits.
