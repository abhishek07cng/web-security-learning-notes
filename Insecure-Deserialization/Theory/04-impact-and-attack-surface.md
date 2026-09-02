# Impact and Attack Surface

Insecure deserialization can expose a very large attack surface because an attacker may reuse existing application code in unintended ways.

## Possible impact

- Remote code execution (RCE).
- Privilege escalation.
- Arbitrary file access.
- Denial of service.

## Why impact can be severe

Deserialization can instantiate objects and invoke methods from classes already present in the application.

This allows an attacker to influence application behavior without necessarily needing a new vulnerability in every method involved.

A deserialization vulnerability can therefore become the entry point to other vulnerabilities.

## Testing perspective

When serialized input is identified, do not stop after confirming that an attribute can be changed. Investigate:

1. What classes can be instantiated?
2. What methods run during deserialization?
3. What attacker-controlled attributes reach application functionality?
4. Can a chain of method calls reach a dangerous sink?
