from django.core.validators import RegexValidator, ValidationError

from directory_validators.fixtures.disposable_email_domains import (
    disposable_domains
)
from directory_validators.fixtures.free_email_domains import free_domains
from directory_validators import constants, helpers


MESSAGE_FILE_TOO_BIG = 'File is too big.'
MESSAGE_USE_CORPORATE_EMAIL = 'Plase use your corporate email address.'

company_number = RegexValidator(
    message="Company number must be 8 digits",
    regex='^[A-Za-z0-9]{8}$',
    code='invalid_company_number',
)


def logo_filesize(value):
    """
    Confirms that the log is not too large in terms of filesize.
    @param {File} value
    @returns {None}
    @raises AssertionError

    """

    if value.size > constants.MAX_LOGO_SIZE_BYTES:
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
        raise ValidationError(MESSAGE_USE_CORPORATE_EMAIL)


def email_domain_disposable(value):
    """
    Confirms that the email address is not using a disposable service.
    @param {str} value
    @returns {None}
    @raises AssertionError

    """

    domain = helpers.get_domain_from_email_address(value)
    if domain.lower() in disposable_domains:
        raise ValidationError(MESSAGE_USE_CORPORATE_EMAIL)
