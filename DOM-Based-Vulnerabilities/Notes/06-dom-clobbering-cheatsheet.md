# DOM Clobbering — Quick Revision

## 1. Core Concept

DOM Clobbering occurs when attacker-controlled HTML creates named DOM elements that interfere with JavaScript properties or application assumptions.

Core flow:

`Attacker HTML → id/name → Named DOM Property → JavaScript → Sensitive Logic`

## 2. Basic Test

```html
<a id="test"></a>
```

Then inspect:

```javascript
window.test
```

Another form:

```html
<form name="test"></form>
```

## 3. Common Pattern

Potentially interesting code:

```javascript
let config = window.config || defaultConfig;
```

Investigate whether attacker-controlled markup can cause:

```javascript
window.config
```

to become unexpectedly defined.

## 4. What to Trace

Look for:

```text
window.<name>
document.<name>
element.<name>
global fallback variables
```

Then determine whether the clobbered property reaches a security-sensitive operation.

## 5. Testing Workflow

`Find Global Property → Identify Fallback → Create Named Element → Inspect Property → Trace Usage → Confirm Impact`

## 6. Checklist

```text
[ ] Interesting global/property identified
[ ] id/name interaction confirmed
[ ] DOM property created or modified
[ ] Application consumes the property
[ ] Security-sensitive behavior identified
[ ] Exploitability confirmed
```

## 7. Remember

`DOM Element Naming + Unsafe Property Assumption + Security-Sensitive Use = Potential DOM Clobbering`
