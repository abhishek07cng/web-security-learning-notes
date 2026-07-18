# OAuth Testing Methodology

## Phase 1 - Reconnaissance

- Identify OAuth providers.
- Capture authorization requests.
- Record parameters.
- Determine OAuth flow.

---

## Phase 2 - Parameter Analysis

Review:

- client_id
- redirect_uri
- response_type
- scope
- state
- nonce
- code_challenge

---

## Phase 3 - Callback Analysis

Inspect:

- Callback path
- Authorization code
- Access token
- ID Token

---

## Phase 4 - Validation Testing

Test:

- redirect_uri
- state
- scope
- PKCE
- ID Token validation

---

## Phase 5 - Callback Security

Search for:

- Open redirects
- XSS
- HTML injection
- postMessage()
- Directory traversal

---

## Phase 6 - Token Usage

Inspect:

- /token
- /userinfo
- /me

Confirm:

- Token ownership
- Scope enforcement
- Expiration
- Replay protection

---

## Phase 7 - Reporting

Document:

- Root cause
- Impact
- Exploitation steps
- Evidence
- Mitigation