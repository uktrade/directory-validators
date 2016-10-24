from unittest import mock

import pytest

from django import forms
from django.conf import settings

from directory_validators import enrolment, constants


def create_mock_file_of_size(size):
    return mock.Mock(size=size)


def test_company_number_eight_chars_accepted():
    assert enrolment.company_number('88888888') is None
    assert enrolment.company_number('NI888888') is None


def test_company_number_seven_chars_rejected():
    with pytest.raises(forms.ValidationError):
        enrolment.company_number('8888888')


def test_company_number_nine_chars_rejected():
    with pytest.raises(forms.ValidationError):
        enrolment.company_number('888888888')


def test_logo_filesize_rejects_too_big():
    size = settings.VALIDATOR_MAX_LOGO_SIZE_BYTES + 1
    mock_file = create_mock_file_of_size(size)
    with pytest.raises(forms.ValidationError):
        enrolment.logo_filesize(mock_file)


def test_logo_filesize_accepts_not_too_big():
    size = settings.VALIDATOR_MAX_LOGO_SIZE_BYTES
    mock_file = create_mock_file_of_size(size)
    assert enrolment.logo_filesize(mock_file) is None


def test_email_domain_free_rejects_free_email():
    with pytest.raises(forms.ValidationError):
        enrolment.email_domain_free('contact@gmail.com')


def test_email_domain_free_accepts_corporate_email():
    assert enrolment.email_domain_free('contact@google.com') is None


def test_email_domain_disposable_rejects_disposable_email():
    with pytest.raises(forms.ValidationError):
        enrolment.email_domain_disposable('contact@guerillamail.com')


def test_email_domain_disposable_accepts_corporate_email():
    assert enrolment.email_domain_disposable('contact@google.com') is None


def test_export_status_rejects_no_intention():
    choice = constants.choices.NO_EXPORT_INTENTION
    with pytest.raises(forms.ValidationError) as error:
        enrolment.export_status_intention(choice)
        assert str(error) == constants.NO_EXPORT_INTENTION_ERROR_LABEL


def test_export_status_accepts_intention():
    choice = constants.choices.EXPORT_STATUSES[1][0]
    assert enrolment.export_status_intention(choice) is None
