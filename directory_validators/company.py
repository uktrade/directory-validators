from django.conf import settings
from django.core.validators import ValidationError

from directory_validators import helpers


SECTOR_LIMIT = 'Please choose no more than 10 sectors.'
KEYWORD_LIMIT = 'Please choose no more than 10 keywords.'
MESSAGE_FILE_TOO_BIG = 'File is too big.'


def sector_choice_limit(choices):
    """
    Confirms that the number of sectors selected is less than the allowed max.

    Args:
        choices (str[])

    Raises:
        django.forms.ValidationError

    """

    if len(choices) > 10:
        raise ValidationError(SECTOR_LIMIT)


def keywords_word_limit(keywords):
    """
    Confirms that the number of keywords selected is less than the allowed max.

    Args:
        keywords (str)

    Raises:
        django.forms.ValidationError

    """

    if len(helpers.tokenize_keywords(keywords)) > 10:
        raise ValidationError(KEYWORD_LIMIT)


def case_study_image_filesize(value):
    """
    Confirms that the case study image is not too large in terms of file size.

    Args:
        value (File): The case study image.

    Raises:
        django.forms.ValidationError

    """

    if value.size > settings.VALIDATOR_MAX_CASE_STUDY_IMAGE_SIZE_BYTES:
        raise ValidationError(MESSAGE_FILE_TOO_BIG)


def case_study_video_filesize(value):
    """
    Confirms that the case study video is not too large in terms of file size.

    Args:
        value (File): The case study video.

    Raises:
        django.forms.ValidationError

    """

    if value.size > settings.VALIDATOR_MAX_CASE_STUDY_VIDEO_SIZE_BYTES:
        raise ValidationError(MESSAGE_FILE_TOO_BIG)
