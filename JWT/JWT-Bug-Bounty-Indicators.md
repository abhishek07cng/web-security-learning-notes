# JWT Bug Bounty Indicators

## Indicator 1

JWT Used For Authentication

Examples:

```text
Authorization: Bearer

session=<JWT>
```

---

## Indicator 2

Interesting Claims

```text
sub

role

isAdmin

permissions
```

---

## Indicator 3

Interesting Headers

```text
alg

kid

jwk

jku
```

---

## Indicator 4

Symmetric Algorithms

```text
HS256

HS384

HS512
```

---

## Indicator 5

Asymmetric Algorithms

```text
RS256

ES256
```

---

## Indicator 6

JWT Libraries

Look for:

```text
Old Frameworks

Custom JWT Logic

Homegrown Authentication
```

---

## Indicator 7

Key Management

Questions:

```text
Where Does The Verification Key Come From?

Can I Influence It?
```

---

# Personal Reminder

Ask:

```text
Does The Server Trust
The Token

Or

The Signature?
```