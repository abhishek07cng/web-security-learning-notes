# Using Application Functionality

A website may perform dangerous operations using attributes from a deserialized object.

The attacker can sometimes modify an object so that existing application functionality operates on an attacker-selected value.

## Example

Suppose a delete-user function removes a profile picture using:

```php
$user->image_location
```

If the object came from serialized user-controlled data, changing the path could cause the application to delete an arbitrary file when the delete function is invoked.

## Key concept

The application functionality itself may appear legitimate.

The vulnerability arises because insecure deserialization allows the attacker to control the data supplied to that functionality.

## Testing

Look for:

- File paths.
- Commands.
- URLs.
- Callback names.
- Database identifiers.
- Template values.
- Other attributes later passed into sensitive functions.
