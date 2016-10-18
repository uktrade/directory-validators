def pytest_configure():
    from django.conf import settings
    settings.configure(
        DEBUG_PROPAGATE_EXCEPTIONS=True,
        VALIDATOR_MAX_LOGO_SIZE_BYTES=10 * 1024 * 1024,
    )
