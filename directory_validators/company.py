from django.core.validators import ValidationError


SECTOR_LIMIT = 'Please choose no more than 10 sectors.'
KEYWORD_LIMIT = 'Please choose no more than 10 keywords.'


def sector_choice_limit(choices):
    """
    Confirms that the number of sectors selected is less than the allowed max.
    @param {str[]} choices
    @returns {None}
    @raises AssertionError

    """

    if len(choices) > 10:
        raise ValidationError(SECTOR_LIMIT)


def keywords_word_limit(keywords):
    """
    Confirms that the number of keywords selected is less than the allowed max.
    @param {str} keywords
    @returns {None}
    @raises AssertionError

    """

    if len(keywords.split()) > 10:
        raise ValidationError(KEYWORD_LIMIT)
