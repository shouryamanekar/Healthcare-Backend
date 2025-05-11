import re
from rest_framework.exceptions import ValidationError

def validate_phone_number(value):
    if not re.match(r'^\+?[1-9]\d{1,14}$', value):
        raise ValidationError(f"{value} is not a valid phone number.")
    return value
