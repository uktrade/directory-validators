import pytest

from django import forms

from directory_validators import company


def test_sectors_allows_one_or_less():
    for i in range(1):
        choices = ['choice'] * i
        assert company.sector_choice_limit(choices) is None


def test_sectors_rejects_more_than_one():
    choices = ['thing', 'thing']
    with pytest.raises(forms.ValidationError, message=company.SECTOR_LIMIT):
        company.sector_choice_limit(choices)


def test_keywords_word_limit_allows_ten_or_less():
    for i in range(11):
        choices = 'choice, ' * i
        assert company.keywords_word_limit(choices) is None


def test_keywords_word_limit_rejects_more_than_ten():
    choices = 'thing, ' * 11
    with pytest.raises(forms.ValidationError, message=company.KEYWORD_LIMIT):
        company.keywords_word_limit(choices)
