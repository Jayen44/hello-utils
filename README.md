# hello-utils

A small collection of Python string utility functions.

## Functions

- `reverse_string(s)` — returns the reversed string
- `capitalize_words(s)` — capitalizes the first letter of each word
- `is_palindrome(s)` — returns `True` if the string is a palindrome

## Usage

```python
from utils import reverse_string, capitalize_words, is_palindrome

reverse_string("hello")       # "olleh"
capitalize_words("hi there")  # "Hi There"
is_palindrome("racecar")      # True
```

## Running tests

```bash
pytest test_utils.py
```
