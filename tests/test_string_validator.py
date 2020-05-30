import string_validator
import pytest

validate_string = string_validator

def test_valid_user():
    assert validate_string.is_username("user.name")

def test_wrong_user_without_dot():
    assert not validate_string.is_username("username")

def test_wrong_user_with_numbers():
    assert not validate_string.is_username("user2name")

def test_wrong_user_with_non_char():
    assert not validate_string.is_username("user@name")

def test_valid_domain():
    assert validate_string.is_domain("example.com")

def test_valid_subdomain():
    assert validate_string.is_domain("sub.example.com")

def test_valid_domain_with_dash():
    assert validate_string.is_domain("some-example.com")

def test_domain_starting_with_non_char():
    assert not validate_string.is_domain("-example.com")

def test_domain_ending_with_non_char():
    assert not validate_string.is_domain("example.com@")

def test_domain_without_protocol():
    assert not validate_string.is_domain("http://example.com")

def test_domain_is_email():
    assert not validate_string.is_domain("user@example.com")

def test_domain_length_is_less_or_equal_253():
    long_domain = "nqnwsjlgxuywzojugeagcfbphrvgacffmuqppnehpzenoixzplrwmhisoytxfgsbarqgrcgqqblyhrdxfqzeirzojyrgjtbfapnzkguqzhyuirazmymxakypbwulmuxcjcfxkhgcgbivohcbxvvkgczaqdoekepwzcxkciwjdpkrdaqdywezqauskkfhmgjubmxhddcbqjvimeqfgjnwhxeufqamrlfxddmlkeonbwmwiypnknmqbclsgm.tlo"
    assert not validate_string.is_domain(long_domain)
