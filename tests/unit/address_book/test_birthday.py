import unittest
import io
from unittest.mock import patch
from goit_assistant_bot.address_book.classes import AddressBook, Record


class TestBirthdayCommands(unittest.TestCase):
    """Tests AddressBook class commands related to birthday"""

    book: AddressBook

    def setUp(self):
        self.book = AddressBook()

    def test_init(self):
        """initial state."""

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_and_birthday_with_contact(self, mock_stdout):
        """add_birthday method. Should add contact and birthday"""
        self.book.add_birthday("Eva", "12.12.2001")
        self.assertIn("Birthday added", mock_stdout.getvalue())
        contact = self.book.find("Eva")
        self.assertEqual("12.12.2001", str(contact.birthday))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_birthday(self, mock_stdout):
        """add_birthday method. Should add birthday, existing contact"""
        self.book.add_contact("Erica")
        self.book.add_birthday("Erica", "28.10.1984")
        self.assertIn("Birthday added", mock_stdout.getvalue())
        contact = self.book.find("Erica")
        self.assertEqual("28.10.1984", str(contact.birthday))

    @patch(
        "goit_assistant_bot.address_book.classes.address_book.is_yes_prompt",
        return_value=True,
    )
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_update_birthday(self, mock_stdout, mock_is_yes_prompt):
        """add_birthday method. Should update birthday"""
        self.book.add_birthday("Maxima", "12.12.2001")
        new_birthday = "12.10.1982"
        self.book.add_birthday("Maxima", new_birthday)
        mock_is_yes_prompt.assert_called_once()
        self.assertIn("Birthday updated", mock_stdout.getvalue())
        contact = self.book.find("Maxima")
        self.assertEqual(new_birthday, str(contact.birthday))

    @patch("builtins.input", side_effect=["y"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_birthday(self, mock_stdout, mock_prompt_decorator):
        """remove_birthday method. Should remove birthday, existing contact"""
        self.book.add_birthday("Maxima", "12.12.2001")
        self.book.remove_birthday("Maxima")
        mock_prompt_decorator.assert_called_once()
        self.assertIn("Birthday deleted", mock_stdout.getvalue())
        contact = self.book.find("Maxima")
        self.assertIsNone(contact.birthday)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_birthday_no_contact(self, mock_stdout):
        """remove_birthday method. Should not remove birthday, not existing contact"""
        self.book.remove_birthday("Maxima")
        self.assertIn("Contact not found", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
