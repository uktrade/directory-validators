import pytest

from django import forms

from directory_validators import company


def test_sectors_allows_ten_or_less():
    for i in range(11):
        choices = ['choice'] * i
        assert company.sector_choice_limit(choices) is None


def test_sectors_rejects_more_than_ten():
    choices = ['thing'] * 11
    with pytest.raises(forms.ValidationError, message=company.SECTOR_LIMIT):
        company.sector_choice_limit(choices)
