# Gadget Chain Reference

## Chain structure

```text
Serialized input
      ↓
Deserialization
      ↓
Magic method / kick-off gadget
      ↓
Intermediate gadgets
      ↓
Sink gadget
      ↓
Impact
```

## Important concepts

- **Gadget:** existing code useful to an attacker.
- **Kick-off gadget:** starts the chain, often through a magic method.
- **Sink gadget:** receives attacker-controlled data and performs a dangerous operation.
- **Gadget chain:** a sequence of existing methods.

The attacker controls the data, not the existence of the methods.
