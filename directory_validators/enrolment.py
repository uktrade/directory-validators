from django.core.validators import EmailValidator, RegexValidator


validate_email = EmailValidator(
    message="Not a valid email",
    code='invalid_email',
    whitelist=None
)

validate_company_number = RegexValidator(
    message="Company number must be 8 digits",
    regex='^\d{8}$',
    code='invalid_company_number',
)
