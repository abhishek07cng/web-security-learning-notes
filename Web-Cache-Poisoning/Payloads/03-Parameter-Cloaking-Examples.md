# Parameter Cloaking Examples

## Secondary delimiter discrepancy

```text
/?example=123?excluded_param=bad-stuff-here
```

## Duplicate keyed parameter

```text
/?keyed_param=abc&excluded_param=123;keyed_param=bad-stuff-here
```

The security issue is inconsistent parsing between cache and back-end.

## Lab callback pattern

```text
/js/geolocate.js?callback=setCountryCookie&utm_content=foo;callback=alert(1)
```

This is lab material from the supplied source.
