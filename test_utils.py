from utils import reverse_string, capitalize_words, is_palindrome


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"
    assert capitalize_words("python is fun") == "Python Is Fun"


def test_is_palindrome():
    assert is_palindrome("racecar") is True
    assert is_palindrome("race car") is True
    assert is_palindrome("hello") is False
    assert is_palindrome("") is True
