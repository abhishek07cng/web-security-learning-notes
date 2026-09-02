# GraphQL CSRF

Cross-site request forgery occurs when an attacker can cause a victim's browser to perform an unintended authenticated action.

GraphQL can become a CSRF vector when the endpoint accepts requests that browsers can forge and does not have adequate CSRF protection.

## Source conditions

Risk arises when:

- the endpoint does not validate request content type;
- CSRF tokens are not implemented;
- GET is accepted; or
- `application/x-www-form-urlencoded` POST is accepted.

The source explains that JSON POST requests are protected against the described browser-forgery technique when the content type is correctly validated.

## Testing workflow

1. Observe an authenticated mutation.
2. Determine the accepted request content type.
3. Test whether the same mutation works as form-urlencoded.
4. Check whether a CSRF token is required.
5. If vulnerable, determine whether an attacker-controlled page can cause the browser to submit the mutation.
