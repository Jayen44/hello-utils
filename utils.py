def reverse_string(s):
    """Return the reverse of a string."""
    return s[::-1]


def capitalize_words(s):
    """Capitalize the first letter of each word."""
    return s.title()


def is_palindrome(s):
    """Return True if the string reads the same forwards and backwards."""
    cleaned = s.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
