class MandatoryFieldMissing(Exception):
    def __init__(self, field_name=None):
        self.msg = f'The mandatory field {field_name} cannot be empty.'

    def __str__(self):
        return self.msg


class InvalidFieldValue(Exception):
    def __init__(self, field_name, value, allowed_values):
        self.msg = f'The field {field_name} was given an invalid value ({value}).\n' \
                   f'Allowed value(s): {list(v for v in allowed_values)}'

    def __str__(self):
        return self.msg
