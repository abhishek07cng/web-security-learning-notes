# Cookie-Based Cache Poisoning

Cookies can influence dynamically generated responses. If the cookie is not included in the cache key, one user's cookie-controlled response may be served to other users.

## Example

```http
Cookie: language=pl;
```

If the cache key contains the request line and Host but excludes Cookie, a cached Polish response could be served to later users regardless of their selected language.

## Security significance

Cookie-based poisoning is less common than header-based poisoning according to the supplied material. It can also be noticed quickly when legitimate users accidentally poison the cache.

## Testing idea

1. Observe a response that sets a cookie.
2. Reload and inspect whether the cookie value appears in the response.
3. Change the cookie.
4. Determine whether the response changes.
5. Determine whether the cache still reports a hit.
6. Assess whether attacker-controlled content can be reflected into an executable context.
