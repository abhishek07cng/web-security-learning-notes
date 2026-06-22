# Excessive Trust In Client-Side Controls

## Overview

Applications should never trust data supplied by the client.

Attackers can modify:

```text
Parameters
Hidden Fields
Cookies
Headers
JavaScript Variables
```

using:

```text
Burp Suite
Repeater
DevTools
```

---

# Example

Application sends:

```text
Price = $100
```

inside the request.

Attacker changes:

```text
Price = $1
```

Server accepts modified value.

---

# Attack Flow

```text
Client Controls Value
        ↓
Attacker Modifies Value
        ↓
Server Trusts Value
        ↓
Logic Flaw
```

---

# Common Targets

```text
Prices
Roles
Discounts
Quantity
Shipping Costs
```

---

# Related Lab

```text
Lab01
```

---

# Key Takeaways

Never trust client-controlled data.