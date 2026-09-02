# Gadget Chains

A **gadget** is an existing piece of application code that can help an attacker reach a desired result.

A single gadget may not be directly dangerous.

## Gadget chain

A gadget chain links multiple existing methods:

```text
Deserialization
      ↓
Kick-off gadget
      ↓
Intermediate gadget
      ↓
Sink gadget
      ↓
Security impact
```

The attacker controls the data passed into the chain. The methods themselves already exist in the application.

## Kick-off gadget

A magic method automatically invoked during deserialization can act as the starting point.

## Sink gadget

A sink gadget is a method where attacker-controlled data reaches a dangerous operation.

## Important distinction

A gadget chain is **not** a payload consisting of newly created chained methods.

The chain already exists in application/library code. The attacker's control is primarily over the data flowing through it.

## Why chains matter

Many real-world deserialization vulnerabilities require a gadget chain rather than a simple attribute modification.
