from unittest import mock

import pytest

from django import forms
from django.conf import settings

from directory_validators import company


def create_mock_file_of_size(size):
    return mock.Mock(size=size)


def test_case_study_image_filesize_rejects_too_big():
    size = settings.VALIDATOR_MAX_CASE_STUDY_IMAGE_SIZE_BYTES + 1
    mock_file = create_mock_file_of_size(size)
    expected_message = company.MESSAGE_FILE_TOO_BIG
    with pytest.raises(forms.ValidationError, message=expected_message):
        company.case_study_image_filesize(mock_file)


def test_case_study_image_filesize_accepts_not_too_big():
    size = settings.VALIDATOR_MAX_CASE_STUDY_IMAGE_SIZE_BYTES
    mock_file = create_mock_file_of_size(size)
    assert company.case_study_image_filesize(mock_file) is None


def test_case_study_video_filesize_rejects_too_big():
    size = settings.VALIDATOR_MAX_CASE_STUDY_VIDEO_SIZE_BYTES + 1
    mock_file = create_mock_file_of_size(size)
    expected_message = company.MESSAGE_FILE_TOO_BIG
    with pytest.raises(forms.ValidationError, message=expected_message):
        company.case_study_video_filesize(mock_file)


def test_case_study_video_filesize_accepts_not_too_big():
    size = settings.VALIDATOR_MAX_CASE_STUDY_VIDEO_SIZE_BYTES
    mock_file = create_mock_file_of_size(size)
    assert company.case_study_video_filesize(mock_file) is None
