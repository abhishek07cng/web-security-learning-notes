# DOM-Based Cookie Manipulation — Quick Revision

## 1. Core Concept

DOM-based cookie manipulation occurs when client-side JavaScript uses attacker-controlled data to modify a cookie.

Core flow:

`Source → JavaScript Processing → document.cookie → Modified Cookie → Application Behavior`

## 2. Common Sources

```javascript
location.search
location.hash
location.pathname
document.URL
event.data
```

## 3. Cookie Sink

```javascript
document.cookie = value;
```

Example:

```javascript
document.cookie = "test=" + location.hash.slice(1);
```

Flow:

`location.hash → slice() → document.cookie`

## 4. Testing

Start with:

```text
cookietest123
```

Example:

```text
#cookietest123
```

Then inspect:

```javascript
document.cookie
```

or:

`DevTools → Application → Cookies`

## 5. What to Check

- Which cookie is modified?
- Can the attacker control the value?
- Is the cookie later trusted?
- Is the cookie security-sensitive?
- Are attributes such as `Secure`, `SameSite`, and expiration relevant?

## 6. Checklist

```text
[ ] Source identified
[ ] Attacker control confirmed
[ ] document.cookie sink identified
[ ] Cookie name identified
[ ] Cookie value traced
[ ] Validation checked
[ ] Downstream usage identified
[ ] Security impact confirmed
```

## 7. Remember

`Attacker-Controlled Source → document.cookie → Security-Sensitive Application Behavior`
