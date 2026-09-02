# Prevention and Defensive Principles

The supplied material primarily focuses on exploitation behavior rather than a long prescriptive prevention section. Based on the source's identified root causes, the defensive focus should be:

## Cache-key consistency

Ensure that the cache and back-end interpret request components consistently.

## Avoid unsafe unkeyed inputs

Do not allow unkeyed headers, cookies, or parameters to influence cacheable responses in dangerous ways.

## Validate trusted headers

Do not blindly trust headers such as forwarding headers to construct security-sensitive or executable URLs.

## Safe resource generation

Generated JavaScript, JSON, CSS, and redirect responses should not reflect attacker-controlled data into executable contexts.

## Cache sensitive/dynamic responses carefully

Responses containing user-specific or security-sensitive content should not be broadly shared.

## Consistent normalization

The cache and application should normalize inputs consistently.

## Layer consistency

External and internal caches should have compatible cache-key and invalidation policies.

## Testing defense

Security testing should explicitly evaluate cache behavior instead of assuming that a keyed URL makes poisoning impossible.
