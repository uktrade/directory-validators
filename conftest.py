def pytest_configure():
    from django.conf import settings
    settings.configure(
        DEBUG_PROPAGATE_EXCEPTIONS=True,
        VALIDATOR_MAX_LOGO_SIZE_BYTES=10 * 1024 * 1024,
        VALIDATOR_MAX_CASE_STUDY_IMAGE_SIZE_BYTES=2 * 1024 * 1024,
        VALIDATOR_MAX_CASE_STUDY_VIDEO_SIZE_BYTES=50 * 1024 * 1024,
    )
