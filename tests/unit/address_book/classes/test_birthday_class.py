import unittest
import datetime
from goit_assistant_bot.address_book.classes.birthday import Birthday
from goit_assistant_bot.address_book.exceptions import ValidationValueException


class TestBirthdayClass(unittest.TestCase):
    """Tests Birthday class"""

    def test_value(self):
        """value attribute getter. Should return value."""
        birthday = Birthday("12.12.2001")
        self.assertEqual(birthday.value, "12.12.2001")

    def test_setter_exceptions(self):
        """value attribute. Must raise ValidationValueException."""
        year = datetime.date.today().year
        future_birthday = f"01.10.{year + 1}"
        birthdays = [
            "12-10-2001",
            "12-13-2001",
            "32-10-2001",
            "12/10/2001",
            "2001/10/10",
            None,
            "",
            future_birthday,
        ]

        for birthday in birthdays:
            with self.assertRaises(ValidationValueException):
                Birthday(birthday)

        # check future birthday message
        with self.assertRaises(ValidationValueException) as future_exception:
            Birthday(future_birthday)
        self.assertIn(
            "The future's date of birth is not accepted",
            str(future_exception.exception),
        )

    def test___str__(self):
        """Tests magical __str__ method"""
        birthday = Birthday("12.12.2001")
        self.assertEqual(str(birthday), "12.12.2001")

    def test___repr__(self):
        """Tests magical __repr__ method"""
        birthday = Birthday("12.12.2001")
        self.assertEqual(repr(birthday), "Birthday: 12.12.2001")


if __name__ == "__main__":
    unittest.main()
