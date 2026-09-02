# Chaining Web Cache Poisoning Vulnerabilities

Sometimes no single weakness is sufficient.

The supplied material demonstrates chains such as:

```text
Cache-key weakness
      +
resource import
      +
DOM vulnerability
      +
language/redirect behavior
      ↓
complete exploit chain
```

## Why chaining matters

A first vulnerability may expose an input but not provide a useful impact.

A second vulnerability may provide the missing capability.

For example:

```text
X-Forwarded-Host
      ↓
malicious resource import
      ↓
DOM-XSS
```

or:

```text
cache parsing discrepancy
      ↓
parameter cloaking
      ↓
callback override
      ↓
JavaScript execution
```

The correct testing mindset is therefore to ask:

> What other application behavior can this cache weakness be combined with?
