from django.core.validators import ValidationError


SECTOR_LIMIT = 'Please choose no more than 10 sectors.'


def sector_choice_limit(choices):
    """
    Confirms that the number of sectors selected is less than the allowed max.
    @param {str[]} choices
    @returns {None}
    @raises AssertionError

    """

    if len(choices) > 10:
        raise ValidationError(SECTOR_LIMIT)
