# Web Cache Poisoning Bug Bounty Checklist

## Cache discovery

- [ ] Cache oracle identified
- [ ] Hit/miss indicator found
- [ ] Cache lifetime observed
- [ ] Cache-Control reviewed
- [ ] Age/Via reviewed
- [ ] Vary reviewed

## Cache key

- [ ] Request line tested
- [ ] Host tested
- [ ] Port behavior tested
- [ ] Query string tested
- [ ] Query parameters tested
- [ ] Header behavior tested
- [ ] Cookie behavior tested
- [ ] Multiple cache layers considered

## Unkeyed inputs

- [ ] X-Forwarded-Host
- [ ] X-Forwarded-Scheme
- [ ] X-Host
- [ ] X-Original-URL
- [ ] Origin
- [ ] other application-specific inputs

## Cache-key flaws

- [ ] query-string exclusion
- [ ] parameter exclusion
- [ ] parameter cloaking
- [ ] normalization
- [ ] cache-key delimiter injection
- [ ] fat GET
- [ ] internal cache mismatch

## Gadgets

- [ ] reflected XSS
- [ ] DOM-XSS
- [ ] open redirect
- [ ] JavaScript resource import
- [ ] JSON resource
- [ ] dynamic CSS
- [ ] other client-side sink

## Safety

- [ ] cache buster used during discovery
- [ ] testing performed only with authorization
- [ ] destructive impact avoided
- [ ] cache re-poisoning controlled

## Evidence

- [ ] malicious request
- [ ] cache key
- [ ] cache hit
- [ ] poisoned response
- [ ] victim impact
- [ ] remediation
