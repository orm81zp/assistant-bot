import unittest
from goit_assistant_bot.address_book.classes.phone import Phone
from goit_assistant_bot.address_book.exceptions import ValidationValueException


class TestPhoneClass(unittest.TestCase):
    """Tests Phone class"""

    def test_value(self):
        """value attribute getter. Should return value."""
        phone = Phone("+380733331111")
        self.assertEqual(phone.value, "+380733331111")

    def test_setter_exceptions(self):
        """value attribute. Must raise ValidationValueException."""
        phones = ["380733331111", "0733331111", None, ""]
        for phone in phones:
            with self.assertRaises(ValidationValueException):
                Phone(phone)

    def test___str__(self):
        """Tests magical __str__ method"""
        phone = Phone("+380733331111")
        self.assertEqual(str(phone), "+380733331111")

    def test___repr__(self):
        """Tests magical __repr__ method"""
        phone = Phone("+380733331111")
        self.assertEqual(repr(phone), "Phone: +380733331111")


if __name__ == "__main__":
    unittest.main()
