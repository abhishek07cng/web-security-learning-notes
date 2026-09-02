# Unkeyed Query Parameters

Some caches exclude only selected query parameters from the cache key.

Analytics and advertising parameters such as UTM parameters are common candidates.

## Why this matters

An excluded parameter might seem harmless if it does not directly control useful application functionality.

However, if the full URL is reflected or passed to a dangerous gadget, an excluded parameter can become an injection point.

## Testing

1. Determine whether the query string is generally keyed.
2. Identify supported parameters.
3. Test likely excluded parameters.
4. Confirm cache-hit behavior.
5. Check whether the parameter is reflected or affects generated content.
6. Test the relevant context in an authorized environment.
