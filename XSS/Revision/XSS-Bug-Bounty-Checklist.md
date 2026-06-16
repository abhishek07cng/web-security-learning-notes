# XSS Bug Bounty Checklist

## Reflection

- [ ] Reflected
- [ ] Stored
- [ ] DOM

---

## Context

- [ ] HTML
- [ ] Attribute
- [ ] JavaScript
- [ ] URL
- [ ] Template Literal
- [ ] AngularJS

---

## Filters

- [ ] Tag Filtering
- [ ] Attribute Filtering
- [ ] Event Filtering
- [ ] Quote Filtering
- [ ] CSP Present

---

## Payload Testing

### HTML

- [ ] `<img src=1 onerror=alert(1)>`
- [ ] `<svg onload=alert(1)>`

---

### Attribute

- [ ] `" onmouseover="alert(1)`
- [ ] `" autofocus onfocus="alert(1)`

---

### JavaScript

- [ ] `';alert(1)//`
- [ ] `${alert(1)}`

---

### AngularJS

- [ ] `{{7*7}}`

---

## Impact

- [ ] Cookie Theft
- [ ] Credential Theft
- [ ] CSRF Bypass
- [ ] Email Change
- [ ] Password Change
- [ ] Account Takeover

---

## Reporting

- [ ] PoC Included
- [ ] Impact Demonstrated
- [ ] Remediation Added