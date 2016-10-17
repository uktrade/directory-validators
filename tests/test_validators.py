from unittest import mock

import pytest

import constants, validators


def create_mock_file_of_size(size):
    return mock.Mock(size=size)


def test_logo_filesize_rejects_too_big():
    mock_file = create_mock_file_of_size(constants.MAX_LOGO_SIZE_BYTES + 1)
    with pytest.raises(AssertionError):
        assert validators.logo_filesize(mock_file)


def test_logo_filesize_accepts_not_too_big():
    mock_file = create_mock_file_of_size(constants.MAX_LOGO_SIZE_BYTES)
    assert validators.logo_filesize(mock_file) is None


def test_email_domain_free_rejects_free_email():
    with pytest.raises(AssertionError):
        assert validators.email_domain_free('contact@example.com')


def test_email_domain_free_accepts_corporate_email():
    assert validators.email_domain_free('contact@google.com') is None


def test_email_domain_disposable_rejects_disposable_email():
    with pytest.raises(AssertionError):
        assert validators.email_domain_disposable('contact@guerillamail.com')


def test_email_domain_disposable_accepts_corporate_email():
    assert validators.email_domain_disposable('contact@google.com') is None
