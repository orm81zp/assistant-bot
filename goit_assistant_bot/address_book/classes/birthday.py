import re
from .field import Field
from ..exceptions import ValidationValueExseption
from ..constants import TEXT

class Birthday(Field):
    def __init__(self, value = ""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if re.search(r"^\d{2}\.\d{2}\.\d{4}$", new_value):
            self._value = new_value
        else:
            raise ValidationValueExseption(TEXT["BIRTHDAY_VALIDATION"])

    def __str__(self):
        return f'{self._value}'

    def __repr__(self):
        return f'Birthday: {self._value}'

__all__ = ["Birthday"]
