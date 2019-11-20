from unittest import mock

from io import BytesIO
from PIL import Image, ImageDraw, PngImagePlugin, JpegImagePlugin, GifImagePlugin
import pytest

from django import forms
from django.conf import settings

from directory_validators import file


def create_mock_file_of_size(size):
    return mock.Mock(size=size)


def test_logo_filesize_rejects_too_big():
    size = settings.VALIDATOR_MAX_LOGO_SIZE_BYTES + 1
    mock_file = create_mock_file_of_size(size)
    with pytest.raises(forms.ValidationError):
        file.logo_filesize(mock_file)


def test_logo_filesize_accepts_not_too_big():
    size = settings.VALIDATOR_MAX_LOGO_SIZE_BYTES
    mock_file = create_mock_file_of_size(size)
    assert file.logo_filesize(mock_file) is None


def create_test_image(extension):
    image = Image.new("RGB", (300, 50))
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), "This text is drawn on image")
    byte_io = BytesIO()
    image.save(byte_io, extension)
    byte_io.seek(0)
    return byte_io


@pytest.fixture(scope='session')
def gif_image():
    return GifImagePlugin.GifImageFile(create_test_image('gif'))


@pytest.fixture(scope='session')
def png_image():
    return PngImagePlugin.PngImageFile(create_test_image('png'))


@pytest.fixture(scope='session')
def jpeg_image():
    return JpegImagePlugin.JpegImageFile(create_test_image('jpeg'))


def test_image_format_invalid_format(gif_image):
    with pytest.raises(forms.ValidationError):
        file.image_format(mock.Mock(image=gif_image))


def test_image_format_valid_format(png_image, jpeg_image):
    for image in (jpeg_image, png_image):
        assert file.image_format(mock.Mock(image=image)) is None


def test_case_study_image_filesize_rejects_too_big():
    size = settings.VALIDATOR_MAX_CASE_STUDY_IMAGE_SIZE_BYTES + 1
    mock_file = create_mock_file_of_size(size)
    expected_message = file.MESSAGE_FILE_TOO_BIG
    with pytest.raises(forms.ValidationError) as excinfo:
        file.case_study_image_filesize(mock_file)
    assert expected_message in str(excinfo.value)


def test_case_study_image_filesize_accepts_not_too_big():
    size = settings.VALIDATOR_MAX_CASE_STUDY_IMAGE_SIZE_BYTES
    mock_file = create_mock_file_of_size(size)
    assert file.case_study_image_filesize(mock_file) is None
