import re
from ..exceptions import ValidationValueException
from ..constants import TEXT
from .field import Field


class Name(Field):
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        new_value = new_value.strip()
        if re.search(r"^[a-zA-Z0-9_.-]{1,30}$", new_value):
            self._value = new_value
        else:
            raise ValidationValueException(TEXT["NAME_VALIDATION"])

    def __str__(self):
        return f"{self._value}"

    def __repr__(self):
        return f"Name: {self._value}"


__all__ = ["Name"]
