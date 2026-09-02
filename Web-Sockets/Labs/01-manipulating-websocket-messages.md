# Lab 01 — Manipulating WebSocket Messages

## Goal
Trigger `alert()` in the support agent's browser.

## Steps
1. Open Live chat and send a message.
2. Find it in Burp WebSockets history.
3. Send a character and observe client-side HTML encoding.
4. Enable WebSocket interception.
5. Intercept another message.
6. Replace the content with:

```html
<img src=1 onerror='alert(1)'>
```

7. Forward the message and observe the alert.
