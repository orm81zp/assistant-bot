import re
from .field import Field
from ..exceptions import ValidationValueExseption
from ..constants import TEXT

class Email(Field):
    def __init__(self, value = ""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if re.search(r"^[a-zA-Z][\w.]+@[a-zA-Z]+\.[a-zA-Z]{2,}$", new_value):
            self._value = new_value
        else:
            raise ValidationValueExseption(TEXT["EMAIL_VALIDATION"])

    def __str__(self):
        return f'{self._value}'

    def __repr__(self):
        return f'Email: {self._value}'

__all__ = ["Email"]
