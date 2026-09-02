# WebSockets Bug Bounty Checklist

## Discovery
- [ ] Find WebSocket functionality.
- [ ] Review endpoint and handshake.
- [ ] Identify message formats.

## Messages
- [ ] Intercept.
- [ ] Modify.
- [ ] Replay.
- [ ] Generate.
- [ ] Test attacker-controlled input.

## Handshake
- [ ] Review cookies/session handling.
- [ ] Review trusted headers.
- [ ] Review custom headers.
- [ ] Check CSRF protection.
- [ ] Check for CSWSH.

## Validation
- [ ] Confirm security impact.
- [ ] Test only systems you are authorized to assess.
