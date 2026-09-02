# What Is Insecure Deserialization?

Insecure deserialization occurs when **user-controllable data is deserialized by a website**.

This can allow an attacker to manipulate serialized objects and pass harmful data into application code.

## Object injection

An attacker may be able to replace an expected serialized object with an object belonging to a completely different class.

If the class is available to the website, the object may still be instantiated even though the application expected another class.

For this reason, insecure deserialization is sometimes called **object injection**.

## Why the danger can occur early

An unexpected object may eventually cause an exception, but the harmful behavior can already have happened.

Many deserialization attacks are triggered during the deserialization process itself, before normal application logic finishes processing the object.

Therefore, strong typing does not automatically prevent these attacks.

## Core rule

The fundamental dangerous condition is:

> User-controlled serialized data is being deserialized.

The presence of a gadget chain alone is not the vulnerability. Gadget chains are mechanisms that can make an insecure deserialization flaw more powerful.

Source: PortSwigger Web Security Academy.
