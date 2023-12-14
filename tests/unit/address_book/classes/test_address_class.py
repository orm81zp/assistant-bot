import unittest
from goit_assistant_bot.address_book.classes.address import Address
from goit_assistant_bot.address_book.exceptions import ValidationValueException


class TestAddressClass(unittest.TestCase):
    """Tests Address class"""

    def test_value(self):
        """value attribute getter. Should return value."""
        address = Address("USA, West street D 98112")
        self.assertEqual(address.value, "USA, West street D 98112")

    def test_setter_exceptions(self):
        """value attribute. Must raise ValidationValueException."""
        addresses = ["AaaAAaaAA", None, "," "".join([str("A") for _ in range(101)])]
        for address in addresses:
            with self.assertRaises(ValidationValueException):
                Address(address)

    def test___str__(self):
        """Tests magical __str__ method"""
        address = Address("USA, West street D 98112")
        self.assertEqual(str(address), "USA, West street D 98112")

    def test___repr__(self):
        """Tests magical __repr__ method"""
        address = Address("USA, West street D 98112")
        self.assertEqual(repr(address), "Address: USA, West street D 98112")


if __name__ == "__main__":
    unittest.main()
