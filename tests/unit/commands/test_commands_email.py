import unittest
import io
from unittest.mock import patch, Mock
from goit_assistant_bot.address_book.classes import AddressBook
from goit_assistant_bot.commands.commands_email import (
    add_email,
    show_email,
    remove_email,
)


class TestCommandsOfEmail(unittest.TestCase):
    """Tests commands/commands_email"""

    book: AddressBook

    def setUp(self):
        self.book = Mock(spec=AddressBook)

    # For add_email
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_email_no_name(self, mock_stdout):
        """Tests add_email. Should ask arguments if there is no name."""
        add_email([], self.book)
        self.assertIn("Please give me <name> <email>", mock_stdout.getvalue())
        self.book.add_email.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_email_no_email(self, mock_stdout):
        """Tests add_email. Should ask arguments if there is no email."""
        add_email(["Maxima"], self.book)
        self.assertIn("Please give me <name> <email>", mock_stdout.getvalue())
        self.book.add_email.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_email(self, mock_stdout):
        """Tests add_email. Should call book.add_email."""
        add_email(["Maxima", "dummy@email.com"], self.book)
        self.assertNotIn("Please give me <name> <email>", mock_stdout.getvalue())
        self.book.add_email.assert_called_once_with("Maxima", "dummy@email.com")

    # For show_email
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_email_no_args(self, mock_stdout):
        """Tests show_email. Should ask arguments."""
        show_email([], self.book)
        self.assertIn("Please give me <name>", mock_stdout.getvalue())
        self.book.show_email.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_email(self, mock_stdout):
        """Tests show_email. Should call book.show_email."""
        show_email(["Maxima"], self.book)
        self.assertNotIn("Please give me <name>", mock_stdout.getvalue())
        self.book.show_email.assert_called_once_with("Maxima")

    # For remove_email
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_email_no_args(self, mock_stdout):
        """Tests remove_email. Should ask arguments."""
        remove_email([], self.book)
        self.assertIn("Please give me <name>", mock_stdout.getvalue())
        self.book.remove_email.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_email(self, mock_stdout):
        """Tests remove_email. Should call book.remove_email."""
        remove_email(["Maxima"], self.book)
        self.assertNotIn("Please give me <name>", mock_stdout.getvalue())
        self.book.remove_email.assert_called_once_with("Maxima")


if __name__ == "__main__":
    unittest.main()
