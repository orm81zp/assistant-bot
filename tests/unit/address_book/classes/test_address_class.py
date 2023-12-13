import unittest
from goit_assistant_bot.address_book.classes import Address
from goit_assistant_bot.address_book.exceptions import ValidationValueException


class TestAddressClass(unittest.TestCase):
    """Tests Address class"""

    def test_init(self):
        """initial state. Address instance must value attribute."""
        address = Address("USA, West street D 98112")
        self.assertTrue(hasattr(address, "value"))
        self.assertEqual(address.value, "USA, West street D 98112")

    def test_value_getter(self):
        """value attribute getter. Should return value."""
        address = Address("USA, West street D 98112")
        self.assertEqual(address.value, "USA, West street D 98112")

    def test_value_setter(self):
        """value attribute setter. Must raise Exseptions."""
        with self.assertRaises(ValidationValueException) as less_exception:
            # less 10 characters
            Address("AaaAAaaAA")
        self.assertIn("Address failed validation", str(less_exception.exception))

        with self.assertRaises(ValidationValueException) as more_exception:
            # more 100 characters
            address = "".join([str("A") for _ in range(101)])
            Address(address)
        self.assertIn("Address failed validation", str(more_exception.exception))

    def test___str__(self):
        address = Address("USA, West street D 98112")
        self.assertEqual(str(address), "USA, West street D 98112")

    def test___repr__(self):
        address = Address("USA, West street D 98112")
        self.assertEqual(str(address), "USA, West street D 98112")
        self.assertEqual(repr(address), "Address: USA, West street D 98112")


if __name__ == "__main__":
    unittest.main()
