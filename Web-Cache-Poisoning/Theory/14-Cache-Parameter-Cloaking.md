# Cache Parameter Cloaking

## Concept

Parameter cloaking exploits a disagreement between how the cache parses a URL and how the back-end parses it.

Example:

```text
/?example=123?excluded_param=bad-stuff-here
```

A flawed cache may treat the second `?` as starting a new parameter and remove it from the cache key.

The application may instead treat everything after the first `?` as part of the `example` value.

## Duplicate-parameter variant

The source also describes differences involving `&` and `;`.

Example:

```text
/?keyed_param=abc&excluded_param=123;keyed_param=bad-stuff-here
```

The cache may see:

```text
keyed_param=abc
excluded_param=123;keyed_param=bad-stuff-here
```

while a framework such as Ruby on Rails may split on `;` and obtain:

```text
keyed_param=abc
excluded_param=123
keyed_param=bad-stuff-here
```

If the back-end uses the final duplicate value, the cache can retain the innocent keyed value while the application processes the attacker-controlled value.

## Security lesson

Parameter parsing must be consistent across every layer.
