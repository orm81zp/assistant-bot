import unittest
from goit_assistant_bot.address_book.classes.email import Email
from goit_assistant_bot.address_book.exceptions import ValidationValueException


class TestEmailClass(unittest.TestCase):
    """Tests Email class"""

    def test_value(self):
        """value attribute getter. Should return value."""
        email = Email("max21@gmail.com")
        self.assertEqual(email.value, "max21@gmail.com")

    def test_setter_exceptions(self):
        """value attribute. Must raise ValidationValueException."""
        emails = ["max21@gmail", "max 21@gmail.com", "", None]
        for email in emails:
            with self.assertRaises(ValidationValueException):
                Email(email)

    def test___str__(self):
        """Tests magical __str__ method"""
        email = Email("max21@gmail.com")
        self.assertEqual(str(email), "max21@gmail.com")

    def test___repr__(self):
        """Tests magical __repr__ method"""
        email = Email("max21@gmail.com")
        self.assertEqual(repr(email), "Email: max21@gmail.com")


if __name__ == "__main__":
    unittest.main()
