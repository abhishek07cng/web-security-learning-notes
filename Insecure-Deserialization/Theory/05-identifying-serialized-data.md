# Identifying Serialized Data

Identification is relatively simple in both black-box and white-box testing if the serialization formats are recognizable.

## Black-box approach

Inspect data being sent to the application and look for serialized objects in:

- Cookies.
- Request parameters.
- Other application-controlled data passed back to the server.

Once serialized data is found, determine whether you can control it.

## Burp Suite

Burp Suite Professional's Scanner can automatically flag HTTP messages that appear to contain serialized objects.

## White-box approach

Search application source code for deserialization operations.

Examples:

- PHP: `unserialize()`
- Java: `readObject()`

Then investigate what data reaches those operations.

## Main idea

Detection is only the first step. After identifying serialized data, test whether its object state or object type can be manipulated.
