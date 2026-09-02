# Dynamic Content in Resource Imports

Imported resource files such as JavaScript or CSS are normally considered static.

However, some resource endpoints reflect query-string input.

## Example

```http
GET /style.css?excluded_param=123);@import…
```

could result in reflected content inside CSS:

```css
@import url(/site/home/index.part1.css?excluded_param=123);@import…
```

The source explains that cache poisoning can sometimes turn this into malicious CSS or other resource-level injection.

## Important idea

A resource file should not automatically be considered safe simply because it is not an HTML page. If its content is dynamically generated and cacheable, it belongs in the cache-poisoning attack surface.
