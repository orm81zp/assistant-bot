import unittest
import io
from unittest.mock import patch
from goit_assistant_bot.address_book.classes import AddressBook, Record


class TestEmailCommands(unittest.TestCase):
    """Tests AddressBook class commands related to email"""

    book: AddressBook

    def setUp(self):
        self.book = AddressBook()

    def test_init(self):
        """initial state."""

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_and_email_with_contact(self, mock_stdout):
        """add_email method. Should add contact and email"""
        self.book.add_email("Eva", "eva19@gmail.com")
        self.assertIn("Email added", mock_stdout.getvalue())
        contact = self.book.find("Eva")
        self.assertEqual("eva19@gmail.com", str(contact.email))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_email(self, mock_stdout):
        """add_email method. Should add email, existing contact"""
        self.book.add_contact("Erica")
        self.book.add_email("Erica", "erica-new@gmail.com")
        self.assertIn("Email added", mock_stdout.getvalue())
        contact = self.book.find("Erica")
        self.assertEqual("erica-new@gmail.com", str(contact.email))

    @patch(
        "goit_assistant_bot.address_book.classes.address_book.is_yes_prompt",
        return_value=True,
    )
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_update_email(self, mock_stdout, mock_is_yes_prompt):
        """add_email method. Should update email"""
        self.book.add_email("Maxima", "maxxi21@gmail.com")
        self.book.add_email("Maxima", "new-maxxi21@gmail.com")
        mock_is_yes_prompt.assert_called_once()
        self.assertIn("Email updated", mock_stdout.getvalue())
        contact = self.book.find("Maxima")
        self.assertEqual("new-maxxi21@gmail.com", str(contact.email))

    @patch("builtins.input", side_effect=["y"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_email(self, mock_stdout, mock_prompt_decorator):
        """remove_email method. Should remove email, existing contact"""
        self.book.add_email("Maxima", "maxima21@gmail.com")
        self.book.remove_email("Maxima")
        mock_prompt_decorator.assert_called_once()
        self.assertIn("Email deleted", mock_stdout.getvalue())
        contact = self.book.find("Maxima")
        self.assertIsNone(contact.email)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_email_no_contact(self, mock_stdout):
        """remove_email method. Should not remove email, not existing contact"""
        self.book.remove_email("Maxima")
        self.assertIn("Contact not found", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
