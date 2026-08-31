# DevTools & DOM Invader — Quick Revision

## 1. DevTools

Main panels:

- **Elements** — live DOM
- **Sources** — JavaScript and breakpoints
- **Console** — runtime inspection
- **Network** — requests and responses
- **Application** — cookies and storage

## 2. Useful Console Checks

```javascript
location.href
location.search
location.hash
location.pathname
document.URL
document.referrer
document.cookie
```

## 3. JavaScript Search

Search for common sources:

```text
location.
document.URL
document.referrer
window.name
event.data
document.cookie
```

Search for common sinks:

```text
innerHTML
outerHTML
document.write
eval
location.href
location.assign
location.replace
setAttribute
```

## 4. Breakpoints

When a sink is found:

1. Set a breakpoint.
2. Trigger the functionality.
3. Inspect the sink argument.
4. Trace the value backwards.
5. Identify the source.
6. Observe the final browser behavior.

## 5. DOM Invader

DOM Invader can help identify:

- DOM sources
- DOM sinks
- Taint/data flow
- Web Message behavior

Use automation to speed up discovery, then manually verify the result.

## 6. Verification

```text
Automated Finding
       ↓
Source Verification
       ↓
Sink Verification
       ↓
Data-Flow Verification
       ↓
Runtime Test
       ↓
Impact Confirmation
```

## 7. Remember

`Tools accelerate discovery; manual source-to-sink analysis confirms the vulnerability.`
