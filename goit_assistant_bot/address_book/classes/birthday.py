import re
import datetime
from ..exceptions import ValidationValueException
from ..constants import TEXT
from .field import Field


class Birthday(Field):
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        # check format DD.MM.YYYY
        if not new_value or not re.search(r"^\d{2}\.\d{2}\.\d{4}$", new_value):
            raise ValidationValueException(TEXT["BIRTHDAY_VALIDATION"])

        # check validation on correct day, month, year arguments
        try:
            day, month, year = new_value.split(".")
            birthday_date = datetime.date(
                year=int(year), month=int(month), day=int(day)
            )
        except Exception:
            raise ValidationValueException(TEXT["BIRTHDAY_VALIDATION"])

        # check that the birthday is not in the future
        if birthday_date > datetime.date.today():
            raise ValidationValueException(TEXT["BIRTHDAY_IN_THE_FUTURE"])

        self._value = new_value

    def __str__(self):
        return f"{self._value}"

    def __repr__(self):
        return f"Birthday: {self._value}"


__all__ = ["Birthday"]
