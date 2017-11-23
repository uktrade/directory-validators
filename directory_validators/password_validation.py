from django.core.exceptions import ValidationError

ALPHABETIC_VALIDATION_MESSAGE = 'This password contains letters only.'
ALPHABETIC_HELP_TEXT = 'Your password cannot contain letters only.'


class AlphabeticPasswordValidator:

    def validate(self, password, user=None):
        if password.isalpha():
            raise ValidationError(
                ALPHABETIC_VALIDATION_MESSAGE,
                code='password_entirely_alphabetic'
            )

    def get_help_text(self):
        return ALPHABETIC_HELP_TEXT
