import unittest
from goit_assistant_bot.address_book.classes import Address
from goit_assistant_bot.address_book.exceptions import ValidationValueExseption


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
        with self.assertRaises(ValidationValueExseption) as rule1:
            # less 10 characters
            Address("AaaAAaaAA")
        self.assertIn("Address failed validation", str(rule1.exception))

        with self.assertRaises(ValidationValueExseption) as rule2:
            # more 100 characters
            address = "".join([str("A") for _ in range(101)])
            Address(address)
        self.assertIn("Address failed validation", str(rule2.exception))

    def test___str__(self):
        address = Address("USA, West street D 98112")
        self.assertEqual(str(address), "USA, West street D 98112")

    def test___repr__(self):
        address = Address("USA, West street D 98112")
        self.assertEqual(str(address), "USA, West street D 98112")
        self.assertEqual(repr(address), "Address: USA, West street D 98112")


if __name__ == "__main__":
    unittest.main()
