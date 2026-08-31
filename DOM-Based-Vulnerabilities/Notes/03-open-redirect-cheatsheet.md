# DOM-Based Open Redirect — Quick Revision

## 1. What Is DOM Open Redirect?

A DOM-based open redirect occurs when client-side JavaScript takes attacker-controlled data and uses it to navigate the browser to a destination controlled by the attacker.

Core flow:

`Source → JavaScript Processing → Navigation Sink → Attacker-Controlled Destination`

## 2. Common Sources

```javascript
location.search
location.hash
location.pathname
document.URL
document.referrer
```

Common example:

```javascript
const url = new URLSearchParams(location.search).get("url");
```

## 3. Common Navigation Sinks

```javascript
location = value
location.href = value
location.assign(value)
location.replace(value)
window.open(value)
```

Also inspect URL-related DOM properties:

```javascript
element.href = value
element.setAttribute("href", value)
```

## 4. Basic Data Flow

Example:

```javascript
const url = new URLSearchParams(location.search).get("url");
location.href = url;
```

Flow:

`location.search → url → location.href → Browser Navigation`

If the attacker can control `url`, investigate whether an external destination is accepted.

## 5. Testing Method

Start with a harmless marker:

```text
redirecttest123
```

Then test a controlled external destination in an authorized environment:

```text
https://example.com
```

Example:

```text
https://target.example/page?url=https://example.com
```

Observe whether the browser navigates to the supplied destination.

## 6. URL Fragment Testing

If the source is:

```javascript
location.hash
```

test:

```text
#https://example.com
```

Then trace how the application processes the fragment.

## 7. Validation Checks

Look for:

```javascript
startsWith()
endsWith()
includes()
indexOf()
match()
test()
```

Determine whether the application:

- Allows only trusted hosts.
- Allows only relative URLs.
- Validates the URL scheme.
- Normalizes the destination before validation.
- Validates the final value actually used by the sink.

## 8. Important Scheme Check

Pay attention to whether the application accepts dangerous URL schemes such as:

```text
javascript:
```

For example:

```text
javascript:print()
```

Only test executable schemes in an authorized lab.

## 9. Common Weak Pattern

```javascript
const url = location.hash.substring(1);

if (url) {
    location = url;
}
```

The important issue is not merely the presence of `location`.

Confirm:

`Attacker Control → External Destination → Navigation`

## 10. Impact

A successful DOM open redirect can be useful for:

- Phishing
- Social engineering
- Trust abuse
- Redirect-based exploit chains

The report should demonstrate that the destination can actually be controlled.

## 11. Verification Checklist

```text
[ ] Source identified
[ ] Attacker control confirmed
[ ] Navigation sink identified
[ ] Data flow traced
[ ] URL parsing understood
[ ] Scheme validation checked
[ ] Host validation checked
[ ] Relative/absolute URL handling checked
[ ] External navigation reproduced
[ ] Security impact confirmed
```

## 12. Common Mistakes

- Assuming every `location` assignment is vulnerable.
- Testing only server-side redirects.
- Ignoring URL parsing and normalization.
- Ignoring scheme validation.
- Assuming a reflected URL is automatically an open redirect.
- Reporting without reproducing the browser navigation.

## 13. Quick Mapping

| Source | Sink | Potential Issue |
|---|---|---|
| `location.search` | `location.href` | DOM Open Redirect |
| `location.hash` | `location` | DOM Open Redirect |
| `document.URL` | `window.open()` | DOM Open Redirect |
| `location.search` | `element.href` | URL manipulation |
| `event.data` | `iframe.src` | Client-side navigation issue |

## 14. Remember

`Attacker-Controlled Source + Unvalidated Destination + Navigation Sink = Potential DOM Open Redirect`

Always trace the complete source-to-sink flow and verify the actual browser behavior.
