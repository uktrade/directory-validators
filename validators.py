import constants, helpers
from fixtures.disposable_email_domains import disposable_domains
from fixtures.free_email_domains import free_domains


MESSAGE_FILE_TOO_BIG = 'File is too big.'
MESSAGE_USE_CORPORATE_EMAIL = 'Plase use your corporate email address.'


def logo_filesize(value):
    """
    Confirms that the log is not too large in terms of filesize.
    @param {File} value
    @returns {None}
    @raises AssertionError

    """

    is_valid = value.size <= constants.MAX_LOGO_SIZE_BYTES
    assert is_valid, MESSAGE_FILE_TOO_BIG


def email_domain_free(value):
    """
    Confirms that the email address is not using a free service.
    @param {str} value
    @returns {None}
    @raises AssertionError

    """

    domain = helpers.get_domain_from_email_address(value)
    is_valid = domain.lower() not in free_domains
    assert is_valid, MESSAGE_USE_CORPORATE_EMAIL


def email_domain_disposable(value):
    """
    Confirms that the email address is not using a disposable service.
    @param {str} value
    @returns {None}
    @raises AssertionError

    """

    domain = helpers.get_domain_from_email_address(value)
    is_valid = domain.lower() not in disposable_domains
    assert is_valid, MESSAGE_USE_CORPORATE_EMAIL
