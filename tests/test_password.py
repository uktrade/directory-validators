import pytest
from django.core.exceptions import ValidationError

from directory_validators import password


@pytest.mark.parametrize(
    'value',
    ('', '12ab', '123', '%£$K')
)
def test_alphabetic_password_validator(value):
    validator = password.AlphabeticPasswordValidator()
    assert validator.validate(password=value) is None
    assert validator.get_help_text() == password.ALPHABETIC_HELP_TEXT


@pytest.mark.parametrize(
    'value',
    ('abc', 'AbC', 'ABC')
)
def test_alphabetic_password_validator_exception_raised(value):
    validator = password.AlphabeticPasswordValidator()
    with pytest.raises(ValidationError) as e:
        validator.validate(password=value)
    assert password.ALPHABETIC_VALIDATION_MESSAGE in str(e.value)


@pytest.mark.parametrize(
    'value',
    ('foobar', '12ab', '123', '%£$K')
)
def test_common_word_password_validator(value):
    validator = password.PasswordWordPasswordValidator()
    assert validator.validate(password=value) is None
    assert validator.get_help_text() == password.PASSWORD_WORD_HELP_TEXT


@pytest.mark.parametrize(
    'value',
    (
        'password',
        'PASSWORD',
        'PaSsWord',
        'FooPasswordBar',
        'foobarpassWord',
        'barPASSWORD',
        'passwordpassword'
    )
)
def test_common_word_validator_exception_raised(value):
    validator = password.PasswordWordPasswordValidator()
    with pytest.raises(ValidationError) as e:
        validator.validate(password=value)
    assert password.PASSWORD_WORD_VALIDATION_MESSAGE in str(e.value)


@pytest.mark.parametrize(
    'value',
    ('12ac456', 'jnfefedef', 'efwefweef', '4')
)
def test_whitespace_password_validator(value):
    validator = password.WhitespacePasswordValidator()
    assert validator.validate(password=value) is None
    assert validator.get_help_text() == password.WHITESPACE_WORD_HELP_TEXT


@pytest.mark.parametrize(
    'value',
    ('1 2 a c 4 5 6 ', ' jnfefedef', 'efwefweef ', '  4   ')
)
def test_whitespace_password_validator_exception_raised(value):
    validator = password.WhitespacePasswordValidator()
    with pytest.raises(ValidationError) as e:
        validator.validate(password=value)
    assert password.WHITESPACE_VALIDATION_MESSAGE in str(e.value)
