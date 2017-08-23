import pytest

from django import forms

from directory_validators import company


def test_keywords_word_limit_allows_ten_or_less():
    for i in range(11):
        choices = 'choice, ' * i
        assert company.keywords_word_limit(choices) is None


def test_keywords_word_limit_rejects_more_than_ten():
    choices = 'thing, ' * 11
    with pytest.raises(forms.ValidationError, message=company.KEYWORD_LIMIT):
        company.keywords_word_limit(choices)


def test_keywords_special_characters():
    choices = 'hello I am, not; allowed,'
    with pytest.raises(forms.ValidationError,
                       message=company.KEYWORD_SPECIAL_CHARS):
        company.keywords_special_characters(choices)


def test_keywords_not_printable_special_characters():
    choices = 'hello I am, not\n allowed,'
    with pytest.raises(forms.ValidationError,
                       message=company.KEYWORD_SPECIAL_CHARS):
        company.keywords_special_characters(choices)


def test_no_email_allowed():
    value = 'foo@bar.com'
    with pytest.raises(forms.ValidationError, message=company.NO_EMAIL):
        company.no_email(value)


def test_no_website_allowed_no_scheme():
    value = 'www.foo.bar'
    with pytest.raises(forms.ValidationError, message=company.NO_WEBSITE):
        company.no_website(value)


def test_no_website_allowed_scheme():
    value = 'http://www.foo.bar'
    with pytest.raises(forms.ValidationError, message=company.NO_WEBSITE):
        company.no_website(value)


def test_no_email_allowed_happy_path():
    value = 'foo'
    company.no_email(value)


def test_no_website_allowed_happy_path():
    value = 'foo.'
    company.no_website(value)
