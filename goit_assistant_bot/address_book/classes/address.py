from ..exceptions import ValidationValueException
from ..constants import TEXT
from .field import Field


class Address(Field):
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value and (10 <= len(new_value) <= 100):
            self._value = new_value
        else:
            raise ValidationValueException(TEXT["ADDRESS_VALIDATION"])

    def __str__(self):
        return f"{self._value}"

    def __repr__(self):
        return f"Address: {self._value}"


__all__ = ["Address"]
