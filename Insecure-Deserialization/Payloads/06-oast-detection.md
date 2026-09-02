# OAST Detection

## URLDNS

The Academy identifies `URLDNS` as a broadly useful Java deserialization detection chain.

Concept:

```text
Serialized object
      ↓
Deserialization
      ↓
URLDNS gadget
      ↓
DNS lookup
      ↓
Collaborator interaction
```

A DNS interaction can confirm that the serialized object was deserialized.

## JRMPClient

`JRMPClient` causes an attempted TCP connection to a supplied IP address.

The Academy suggests comparing behavior for a local address and a firewalled external address when DNS is unavailable.

## Why OAST matters

Blind deserialization may produce no visible response, so an out-of-band interaction can provide evidence of server-side execution.
