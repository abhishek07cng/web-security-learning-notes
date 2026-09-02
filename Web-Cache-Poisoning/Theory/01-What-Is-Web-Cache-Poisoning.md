# Web Cache Poisoning

## Overview

Web cache poisoning is an advanced technique in which an attacker manipulates the interaction between a web server and its cache so that a harmful response is cached and later served to other users.

## Core Concept

The attack has two phases:

```text
1. Make the back-end generate a dangerous response
2. Make the cache store that response
```

Once cached, the poisoned response can be distributed to users who request the matching cache key.

## Why It Is Dangerous

Web cache poisoning is primarily a **delivery mechanism**. The final impact depends on the payload that can be cached. The supplied material describes possible combinations with:

- XSS
- JavaScript injection
- open redirection
- DOM-based vulnerabilities
- denial of service
- malicious resource imports

The number of affected users also depends on traffic to the poisoned resource.

## Fundamental attack model

```text
Attacker-controlled input
        ↓
Back-end processes input unsafely
        ↓
Harmful response generated
        ↓
Response becomes cached
        ↓
Other users request same cache key
        ↓
Poisoned response delivered
```

The source emphasizes that a cache entry can potentially be repeatedly re-poisoned, so short cache lifetimes do not automatically eliminate impact.
