# Magic Methods

Magic methods are methods that are automatically invoked when a particular event or condition occurs.

They are common in object-oriented programming.

## PHP example

```php
__construct()
```

is automatically invoked when an object is instantiated.

During deserialization, PHP's:

```php
__wakeup()
```

can be invoked automatically.

## Java example

Java deserialization uses:

```java
ObjectInputStream.readObject()
```

and a Serializable class may declare its own `readObject()` method.

## Why magic methods matter

Magic methods are not vulnerabilities by themselves.

They become dangerous when they process attacker-controlled data from a deserialized object.

This allows an attacker to cause application methods to execute automatically during or around deserialization.

## Testing

When source code is available, prioritize classes containing:

- PHP `__wakeup()`
- PHP `__destruct()`
- Other relevant magic methods
- Java `readObject()`

Then trace the data they process.
