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
