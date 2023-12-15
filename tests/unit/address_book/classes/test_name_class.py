import unittest
from goit_assistant_bot.address_book.classes.name import Name
from goit_assistant_bot.address_book.exceptions import ValidationValueException


class TestAddressClass(unittest.TestCase):
    """Tests Address class"""

    def test_value(self):
        """value attribute getter. Should return value."""
        name = Name("Dock")
        self.assertEqual(name.value, "Dock")

    def test_setter_exceptions(self):
        """value attribute. Must raise ValidationValueException."""
        names = ["", None, "".join([str("A") for _ in range(31)])]
        for name in names:
            with self.assertRaises(ValidationValueException):
                Name(name)

    def test___str__(self):
        """Tests magical __str__ method"""
        name = Name("Maxima")
        self.assertEqual(str(name), "Maxima")

    def test___repr__(self):
        """Tests magical __repr__ method"""
        name = Name("Maxima")
        self.assertEqual(repr(name), "Name: Maxima")


if __name__ == "__main__":
    unittest.main()
