import pytest

from django import forms

from directory_validators import string


def test_tokenize_words_trailing_spaces():
    actual = string.tokenize_words('really good, nice, great and good')
    assert actual == ['really good', 'nice', 'great and good']


def test_tokenize_words_leading_spaces():
    actual = string.tokenize_words(' really good ,nice ,great and good ')
    assert actual == ['really good', 'nice', 'great and good']


def test_tokenize_words_no_spaces():
    actual = string.tokenize_words('really good,nice,great and good')
    assert actual == ['really good', 'nice', 'great and good']


def test_tokenize_words_trailing_comma():
    actual = string.tokenize_words('really good,nice,great and good,')
    assert actual == ['really good', 'nice', 'great and good']


def test_tokenize_words_trailing_comma_space():
    actual = string.tokenize_words('really good,nice,great and good, ')
    assert actual == ['really good', 'nice', 'great and good']


def test_word_limit_allows_ten_or_less():
    for i in range(11):
        choices = 'choice, ' * i
        assert string.word_limit(10)(choices) is None


def test_word_limit_rejects_more_than_ten():
    choices = 'thing, ' * 11
    with pytest.raises(forms.ValidationError) as excinfo:
        string.word_limit(10)(choices)
    assert string.MESSAGE_KEYWORD_LIMIT in str(excinfo.value)


def test_keywords_special_characters():
    choices = 'hello I am, not; allowed,'
    with pytest.raises(forms.ValidationError) as excinfo:
        string.no_special_characters(choices)
    assert string.MESSAGE_KEYWORD_SPECIAL_CHARS in str(excinfo.value)


def test_keywords_not_printable_special_characters():
    choices = 'hello I am, not\n allowed,'
    with pytest.raises(forms.ValidationError) as excinfo:
        string.no_special_characters(choices)
    assert string.MESSAGE_KEYWORD_SPECIAL_CHARS in str(excinfo.value)


@pytest.mark.parametrize('value', [
    'thing <a href="#">',
    '<a onmouseover=javascript:func()>stuff</a>'
])
def test_no_html_invalid(value):
    expected_message = string.MESSAGE_REMOVE_HTML
    with pytest.raises(forms.ValidationError) as excinfo:
        string.no_html(value)
    assert expected_message in str(excinfo.value)


@pytest.mark.parametrize('value', [
    'thing',
    'thing 1 < 2',
    'thing 1 <2',
    'thing 1<2',
    'thing 1<2>3',
    'thing 1<2 >3',
    'thing 1<2 > 3',
])
def test_no_html_valid(value):
    assert string.no_html(value) is None
