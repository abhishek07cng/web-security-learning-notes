# Web Cache Poisoning Testing Methodology

```text
DISCOVERY
  ↓
Find cache oracle
  ↓
Determine cache key
  ↓
Find unkeyed inputs
  ↓
Understand application reflection/behavior
  ↓
Find cacheability conditions
  ↓
Find exploitable gadget
  ↓
Construct poison
  ↓
Verify cache hit
  ↓
Verify victim impact
```

## Phase 1 — Cache oracle

Find a page where cache behavior is observable.

## Phase 2 — Key mapping

Change one input at a time and compare cache behavior.

## Phase 3 — Input discovery

Use manual testing and Param Miner.

## Phase 4 — Application behavior

Determine whether input is:

- reflected;
- used to build URLs;
- passed into JavaScript;
- used in redirects;
- used in resource imports.

## Phase 5 — Cacheability

Study status, headers, route, content type, cookies, and timing.

## Phase 6 — Cache implementation

Test:

- query-string exclusion
- parameter filtering
- delimiter inconsistencies
- normalization
- Host-port handling
- GET bodies
- multiple cache layers

## Phase 7 — Gadget

Look for XSS, redirects, dynamic resource imports, or other useful behavior.

## Phase 8 — Proof

Use the smallest safe proof in the authorized lab and document the exact cache-key and response behavior.
