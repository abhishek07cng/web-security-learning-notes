# Impact and Attack Surface

## Impact depends on two major factors

### 1. What can be cached

The more powerful the injected payload, the greater the potential impact.

### 2. Traffic to the affected resource

A poisoned home page can affect many users, while a rarely visited page may have little practical impact.

## Why cache poisoning can amplify vulnerabilities

A reflected client-side issue normally requires a victim to visit a specially crafted URL. Cache poisoning can transform the delivery model:

```text
Reflected vulnerability
        ↓
attacker must induce victim to request payload URL
```

into:

```text
Cache poisoning + reflected vulnerability
        ↓
ordinary URL serves poisoned response
        ↓
many users can be affected
```

The supplied source specifically describes this as a way to turn some client-side issues into a stored/distributed form of attack.
