import re
from ..exceptions import ValidationValueException
from ..constants import TEXT
from .field import Field


class Phone(Field):
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value and re.search(r"^\+[0-9]{12}$", new_value):
            self._value = new_value
        else:
            raise ValidationValueException(TEXT["PHONE_VALIDATION"])

    def __str__(self):
        return f"{self._value}"

    def __repr__(self):
        return f"Phone: {self._value}"


__all__ = ["Phone"]
