from .field import Field
from ..exceptions import ValidationValueExseption
from ..constants import TEXT


class Address(Field):
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if len(new_value) > 10 and len(new_value) <= 50:
            self._value = new_value
        else:
            raise ValidationValueExseption(TEXT["ADDRESS_VALIDATION"])

    def __str__(self):
        return f"{self._value}"

    def __repr__(self):
        return f"Address: {self._value}"


__all__ = ["Address"]
