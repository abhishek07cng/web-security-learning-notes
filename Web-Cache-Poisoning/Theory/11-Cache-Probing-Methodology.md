# Cache Implementation Probing Methodology

For implementation-specific cache flaws, the source recommends:

```text
1. Identify a suitable cache oracle
2. Probe key handling
3. Identify an exploitable gadget
```

## Cache oracle

A cache oracle is a page/endpoint that provides feedback about cache behavior.

Useful signals include:

- explicit cache-hit header
- observable dynamic content
- response timing

An ideal oracle reflects the complete URL and at least one query parameter.

## Probe key handling

Test transformations such as:

- query-string exclusion
- parameter filtering
- Host-port handling
- path normalization
- delimiter handling
- other cache-specific normalization

If a direct cache-key display is available, compare keys directly. Otherwise, compare pairs of responses.

## Identify a gadget

A gadget is the application behavior that turns the cache-key flaw into impact.

Common examples from the source include:

- reflected XSS
- open redirects
- dynamic resource content
- malformed-request-only behaviors

## Core principle

A cache-key flaw by itself may not be enough. Severity depends heavily on what application behavior can be chained with it.
