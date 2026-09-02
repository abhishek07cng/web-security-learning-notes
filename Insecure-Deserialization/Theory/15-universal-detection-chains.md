# Universal Detection Gadget Chains

Some gadget chains can help detect deserialization without immediately attempting a destructive action.

## URLDNS

The `URLDNS` chain causes a DNS lookup for a supplied URL.

According to the Academy:

- It does not depend on a specific vulnerable library.
- It works across known Java versions.
- It can be used with Burp Collaborator to detect DNS interaction.
- A resulting interaction can confirm that deserialization occurred.

## JRMPClient

`JRMPClient` can cause the server to attempt a TCP connection to a supplied IP address.

The source notes:

- A raw IP address should be supplied.
- It can be useful when outbound DNS is blocked.
- Comparing response timing using a local and firewalled external IP can provide evidence of server-side processing.

## Testing principle

For blind deserialization, an out-of-band interaction can provide evidence when the application does not visibly respond.
