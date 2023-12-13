import unittest
import io
from unittest.mock import patch
from goit_assistant_bot.address_book.classes import AddressBook, Record


class TestAddressBookAddress(unittest.TestCase):
    book: AddressBook

    def setUp(self):
        self.book = AddressBook()

    def test_init(self):
        """initial state."""

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_address_with_contact(self, mock_stdout):
        """add_address method. Should add contact and address"""
        self.book.add_address("Eva", "USA, D18 street 69118")
        self.assertIn("Address added", mock_stdout.getvalue())
        contact = self.book.find("Eva")
        self.assertEqual("USA, D18 street 69118", str(contact.address))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_address(self, mock_stdout):
        """add_address method. Should add address, existing contact"""
        self.book.add_contact("Erica")
        self.book.add_address("Erica", "USA, C18 street Ride")
        self.assertIn("Address added", mock_stdout.getvalue())
        contact = self.book.find("Erica")
        self.assertEqual("USA, C18 street Ride", str(contact.address))

    @patch(
        "goit_assistant_bot.address_book.classes.address_book.is_yes_prompt",
        return_value=True,
    )
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_update_address(self, mock_stdout, mock_is_yes_prompt):
        """add_address method. Should update address"""
        self.book.add_address("Maxima", "Dalas, W18 street Wide")
        self.book.add_address("Maxima", "New Address Dalas 12, S18 street Harry")
        mock_is_yes_prompt.assert_called_once()
        self.assertIn("Address updated", mock_stdout.getvalue())
        contact = self.book.find("Maxima")
        self.assertEqual("New Address Dalas 12, S18 street Harry", str(contact.address))

    @patch("builtins.input", side_effect=["y"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_address(self, mock_stdout, mock_prompt_decorator):
        """remove_address method. Should remove address, existing contact"""
        self.book.add_address("Maxima", "USA D19, street Red Stone")
        self.book.remove_address("Maxima")
        mock_prompt_decorator.assert_called_once()
        self.assertIn("Address deleted", mock_stdout.getvalue())
        contact = self.book.find("Maxima")
        self.assertIsNone(contact.address)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_address_no_contact(self, mock_stdout):
        """remove_address method. Should not remove address, not existing contact"""
        self.book.remove_address("Maxima")
        self.assertIn("Contact not found", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
