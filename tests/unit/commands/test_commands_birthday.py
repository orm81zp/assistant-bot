import unittest
import io
from unittest.mock import patch, Mock
from goit_assistant_bot.address_book.classes import AddressBook
from goit_assistant_bot.commands.commands_birthday import (
    add_birthday,
    show_birthday,
    remove_birthday,
)


class TestCommandsOfBirthday(unittest.TestCase):
    """Tests commands/commands_birthday"""

    book: AddressBook

    def setUp(self):
        self.book = Mock(spec=AddressBook)

    # For add_birthday
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_birthday_no_name(self, mock_stdout):
        """Tests add_birthday. Should ask arguments if there is no name."""
        add_birthday([], self.book)
        self.assertIn("Please give me <name> <birthday>", mock_stdout.getvalue())
        self.book.add_birthday.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_birthday_no_birthday(self, mock_stdout):
        """Tests add_birthday. Should ask arguments if there is no birthday."""
        add_birthday(["Maxima"], self.book)
        self.assertIn("Please give me <name> <birthday>", mock_stdout.getvalue())
        self.book.add_birthday.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_birthday(self, mock_stdout):
        """Tests add_birthday. Should call book.add_birthday."""
        add_birthday(["Maxima", "12.12.1981"], self.book)
        self.assertNotIn("Please give me <name> <birthday>", mock_stdout.getvalue())
        self.book.add_birthday.assert_called_once_with("Maxima", "12.12.1981")

    # For show_email
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_birthday_no_args(self, mock_stdout):
        """Tests show_birthday. Should ask arguments."""
        show_birthday([], self.book)
        self.assertIn("Please give me <name>", mock_stdout.getvalue())
        self.book.show_birthday.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_birthday(self, mock_stdout):
        """Tests show_birthday. Should call book.show_birthday."""
        show_birthday(["Maxima"], self.book)
        self.assertNotIn("Please give me <name>", mock_stdout.getvalue())
        self.book.show_birthday.assert_called_once_with("Maxima")

    # For remove_email
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_birthday_no_args(self, mock_stdout):
        """Tests remove_birthday. Should ask arguments."""
        remove_birthday([], self.book)
        self.assertIn("Please give me <name>", mock_stdout.getvalue())
        self.book.remove_birthday.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_birthday(self, mock_stdout):
        """Tests remove_birthday. Should call book.remove_birthday."""
        remove_birthday(["Maxima"], self.book)
        self.assertNotIn("Please give me <name>", mock_stdout.getvalue())
        self.book.remove_birthday.assert_called_once_with("Maxima")


if __name__ == "__main__":
    unittest.main()
