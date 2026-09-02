# Gadget Chain Cheatsheet

## Key terms

**Gadget:** existing useful code.

**Kick-off gadget:** starts the chain, often a deserialization magic method.

**Intermediate gadget:** passes attacker-controlled data onward.

**Sink gadget:** performs the dangerous operation.

## Source-code workflow

1. Find deserialization.
2. Find magic methods.
3. Trace calls.
4. Track attacker-controlled values.
5. Identify a sink.
6. Build a valid serialized object.
7. Test safely.

## Tools named by the Academy

- `ysoserial` — Java.
- PHPGGC — PHP.
- Hackvertor — helps manipulate encoded/binary serialized data.
- Burp Collaborator — OAST detection/exfiltration in relevant labs.

## Important

The vulnerability is insecure deserialization, not simply the presence of a gadget chain.
