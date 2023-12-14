import re
from ..exceptions import ValidationValueException
from ..constants import TEXT
from .field import Field


class Email(Field):
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value and re.search(
            r"^[a-zA-Z]{1}[a-zA-Z0-9_\.-]{1,}@[a-zA-Z]+\.[a-zA-Z]{2,}$", new_value
        ):
            self._value = new_value
        else:
            raise ValidationValueException(TEXT["EMAIL_VALIDATION"])

    def __str__(self):
        return f"{self._value}"

    def __repr__(self):
        return f"Email: {self._value}"


__all__ = ["Email"]
