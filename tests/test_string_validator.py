import string_validator

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

def test_domain_ending_with_numbers():
    assert not validate_string.is_domain("example.com@")

def test_domain_without_protocol():
    assert not validate_string.is_domain("http://example.com")

def test_domain_with_non_char():
    assert not validate_string.is_domain("http://@example.com")
