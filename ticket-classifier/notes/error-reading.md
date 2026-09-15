# Python Error Reading

## Error

- Exception type: `KeyError`
- Message: `'email'`
- File: `scripts/error_demo.py`
- Exact line: `5`
- Failing code: `print(user["email"])`

## Cause

The dictionary contained the `name` key, but the code attempted to access the missing `email` key. Accessing a missing dictionary key with `user["email"]` raises a `KeyError`.

## Fix

Changed:

```python
print(user["email"])