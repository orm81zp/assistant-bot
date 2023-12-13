import unittest
import io
from unittest.mock import patch
from goit_assistant_bot.address_book.classes import AddressBook, Record


class TestPhoneCommands(unittest.TestCase):
    """Tests AddressBook class commands related to phone"""

    book: AddressBook

    def setUp(self):
        self.book = AddressBook()

    def test_init(self):
        """initial state."""

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_phone_with_contact(self, mock_stdout):
        """add_phone method. Should add phone and contact"""
        self.book.add_phone("Maxima", "+380631112233")
        self.assertIn("Phone added", mock_stdout.getvalue())
        contact = self.book.find("Maxima")
        self.assertTrue(contact.phone_exists("+380631112233"))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_phone(self, mock_stdout):
        """add_phone method. Should add phone, existing contact"""
        self.book.add_contact("Eva")
        self.book.add_phone("Eva", "+380631112200")
        self.assertIn("Phone added", mock_stdout.getvalue())
        contact = self.book.find("Eva")
        self.assertTrue(contact.phone_exists("+380631112200"))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_phone_exists(self, mock_stdout):
        """add_phone method. Should not add already existing phone"""
        self.book.add_phone("Eva", "+380631112299")
        self.book.add_phone("Eva", "+380631112299")
        self.assertIn("Phone already exists", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["y"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_phone(self, mock_stdout, mock_prompt_decorator):
        """remove_phone method. Should remove phone, contact and phone number already exist"""
        self.book.add_phone("Maxima", "+380631112211")
        self.book.remove_phone("Maxima", "+380631112211")
        mock_prompt_decorator.assert_called_once()
        self.assertIn("Phone deleted", mock_stdout.getvalue())
        contact = self.book.find("Maxima")
        self.assertFalse(contact.phone_exists("+380631112211"))
        self.assertEqual(len(contact.phones), 0)

    @patch("builtins.input", side_effect=["y"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_not_found_phone(self, mock_stdout, mock_prompt_decorator):
        """remove_phone method. Should not remove, not existing phone"""
        self.book.add_phone("Maxima", "+380631112211")
        self.book.remove_phone("Maxima", "+380777770077")
        mock_prompt_decorator.assert_called_once()
        self.assertIn("Phone not found", mock_stdout.getvalue())
        contact = self.book.find("Maxima")
        self.assertEqual(len(contact.phones), 1)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_phone_not_found_contact(self, mock_stdout):
        """remove_phone method. Should not remove phone, not existing contact"""
        self.book.remove_phone("Maxima", "+380631112211")
        self.assertIn("Contact not found", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
