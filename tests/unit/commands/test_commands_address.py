import unittest
import io
from unittest.mock import patch, Mock
from goit_assistant_bot.address_book.classes import AddressBook
from goit_assistant_bot.commands.commands_address import (
    add_address,
    show_address,
    remove_address,
)


class TestCommandsOfAddress(unittest.TestCase):
    """Tests commands/commands_address"""

    book: AddressBook

    def setUp(self):
        self.book = Mock(spec=AddressBook)

    # For add_address
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_address_no_args(self, mock_stdout):
        """Tests add_address. Should ask arguments."""
        add_address([], self.book)
        self.assertIn("Please give me <name> <address>", mock_stdout.getvalue())
        self.book.add_address.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_address_no_address(self, mock_stdout):
        """Tests add_address. Should ask arguments if address is empty."""
        add_address(["Maxima"], self.book)
        self.assertIn("Please give me <name> <address>", mock_stdout.getvalue())
        self.book.add_address.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_address(self, mock_stdout):
        """Tests add_address. Should call book.add_address."""
        add_address(["Maxima", "USA,", "Down", "street", "128"], self.book)
        self.assertNotIn("Please give me <name> <address>", mock_stdout.getvalue())
        self.book.add_address.assert_called_once_with("Maxima", "USA, Down street 128")

    # For show_address
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_address_no_args(self, mock_stdout):
        """Tests show_address. Should ask arguments."""
        show_address([], self.book)
        self.assertIn("Please give me <name>", mock_stdout.getvalue())
        self.book.show_address.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_address(self, mock_stdout):
        """Tests show_address. Should call book.show_address."""
        show_address(["Maxima"], self.book)
        self.assertNotIn("Please give me <name>", mock_stdout.getvalue())
        self.book.show_address.assert_called_once_with("Maxima")

    # For remove_address
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_address_no_args(self, mock_stdout):
        """Tests remove_address. Should ask arguments."""
        remove_address([], self.book)
        self.assertIn("Please give me <name>", mock_stdout.getvalue())
        self.book.remove_address.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_address(self, mock_stdout):
        """Tests remove_address. Should call book.remove_address."""
        remove_address(["Maxima"], self.book)
        self.assertNotIn("Please give me <name>", mock_stdout.getvalue())
        self.book.remove_address.assert_called_once_with("Maxima")


if __name__ == "__main__":
    unittest.main()
