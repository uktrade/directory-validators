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


def test_case_study_social_link_facebook_accepts_schemes():
    expected_legal_urls = [
        'https://facebook.com/thing',
        'http://facebook.com/thing',
    ]
    for url in expected_legal_urls:
        assert company.case_study_social_link_facebook(url) is None


def test_case_study_social_link_facebook_accepts_subdomains():
    expected_legal_urls = [
        'http://thing.facebook.com/thing',
        'http://www.facebook.com/thing',
    ]
    for url in expected_legal_urls:
        assert company.case_study_social_link_facebook(url) is None


def test_case_study_social_link_facebook_rejects_wrong_service():
    url = 'http://google.com'
    message = company.MESSAGE_NOT_FACEBOOK
    with pytest.raises(forms.ValidationError, message=message):
        company.case_study_social_link_facebook(url)


def test_case_study_social_link_twitter_accepts_schemes():
    expected_legal_urls = [
        'https://twitter.com/thing',
        'http://twitter.com/thing',
    ]
    for url in expected_legal_urls:
        assert company.case_study_social_link_twitter(url) is None


def test_case_study_social_link_twitter_accepts_subdomains():
    expected_legal_urls = [
        'http://thing.twitter.com/thing',
        'http://www.twitter.com/thing',
    ]
    for url in expected_legal_urls:
        assert company.case_study_social_link_twitter(url) is None


def test_case_study_social_link_twitter_rejects_wrong_service():
    url = 'http://google.com'
    message = company.MESSAGE_NOT_TWITTER
    with pytest.raises(forms.ValidationError, message=message):
        company.case_study_social_link_twitter(url)


def test_case_study_social_link_linkedin_accepts_schemes():
    expected_legal_urls = [
        'https://linkedin.com/thing',
        'http://linkedin.com/thing',
    ]
    for url in expected_legal_urls:
        assert company.case_study_social_link_linkedin(url) is None


def test_case_study_social_link_linkedin_accepts_subdomains():
    expected_legal_urls = [
        'http://thing.linkedin.com/thing',
        'http://www.linkedin.com/thing',
    ]
    for url in expected_legal_urls:
        assert company.case_study_social_link_linkedin(url) is None


def test_case_study_social_link_linkedin_rejects_wrong_service():
    url = 'http://google.com'
    message = company.MESSAGE_NOT_LINKEDIN
    with pytest.raises(forms.ValidationError, message=message):
        company.case_study_social_link_linkedin(url)
