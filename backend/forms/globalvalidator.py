from wtforms.validators import ValidationError


def is_42(message=None):
    if  message is None:
        message = 'Must be 42'
    def _is_42(form, field):
        if field.data != 42:
            raise ValidationError(message)
    return _is_42