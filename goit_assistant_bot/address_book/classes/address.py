from ..exceptions import ValidationValueExseption
from ..constants import TEXT
from .field import Field


class Address(Field):
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if 10 <= len(value) <= 100:
            self._value = value
        else:
            raise ValidationValueExseption(TEXT["ADDRESS_VALIDATION"])

    def __str__(self):
        return f"{self._value}"

    def __repr__(self):
        return f"Address: {self._value}"


__all__ = ["Address"]
