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
