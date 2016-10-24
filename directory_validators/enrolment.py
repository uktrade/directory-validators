from django.conf import settings
from django.core.validators import RegexValidator, ValidationError

from directory_validators.constants import (
    choices,
    NO_EXPORT_INTENTION_ERROR_LABEL,
)
from directory_validators.constants.disposable_email_domains import (
    disposable_domains
)
from directory_validators.constants.free_email_domains import free_domains
from directory_validators import helpers


MESSAGE_FILE_TOO_BIG = 'File is too big.'
MESSAGE_USE_COMPANY_EMAIL = 'Plase use your company email address.'

company_number = RegexValidator(
    message="Company number must be 8 characters",
    regex='^[A-Za-z0-9]{8}$',  # allow alphanumeric of length 8.
    code='invalid_company_number',
)


def logo_filesize(value):
    """
    Confirms that the logo is not too large in terms of filesize.
    @param {File} value
    @returns {None}
    @raises AssertionError

    """

    if value.size > settings.VALIDATOR_MAX_LOGO_SIZE_BYTES:
        raise ValidationError(MESSAGE_FILE_TOO_BIG)


def email_domain_free(value):
    """
    Confirms that the email address is not using a free service.
    @param {str} value
    @returns {None}
    @raises AssertionError

    """

    domain = helpers.get_domain_from_email_address(value)
    if domain.lower() in free_domains:
        raise ValidationError(MESSAGE_USE_COMPANY_EMAIL)


def email_domain_disposable(value):
    """
    Confirms that the email address is not using a disposable service.
    @param {str} value
    @returns {None}
    @raises AssertionError

    """

    domain = helpers.get_domain_from_email_address(value)
    if domain.lower() in disposable_domains:
        raise ValidationError(MESSAGE_USE_COMPANY_EMAIL)


def export_status_intention(value):
    if value == choices.NO_EXPORT_INTENTION:
        raise ValidationError(NO_EXPORT_INTENTION_ERROR_LABEL)
