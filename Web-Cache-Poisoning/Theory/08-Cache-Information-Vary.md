# Cache-Control and Vary Information

## Cache-Control information

Responses may reveal useful cache timing information:

```http
Via: 1.1 varnish-v4
Age: 174
Cache-Control: public, max-age=1800
```

This can reveal:

- whether a response is publicly cacheable;
- approximate cache age;
- maximum cache lifetime.

It does not itself create a poisoning vulnerability, but it can reduce the guesswork needed to time an attack.

## Vary

The `Vary` header specifies additional request headers that should participate in cache variation.

For example, if `User-Agent` is included, mobile and desktop responses can be cached separately.

## Security relevance

If the tester can determine that the victim belongs to a particular cache-key subset, a poison can potentially be targeted to that subset.

The supplied lab demonstrates identifying the victim's User-Agent through an allowed comment feature and then poisoning the corresponding cache variant.
