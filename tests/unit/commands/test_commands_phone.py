import unittest
import io
from unittest.mock import patch, Mock
from goit_assistant_bot.address_book.classes import AddressBook
from goit_assistant_bot.commands.commands_phone import (
    change_phone,
    show_phone,
    add_phone,
    remove_phone,
)


class TestCommandsOfPhone(unittest.TestCase):
    """Tests commands/commands_phone"""

    book: AddressBook

    def setUp(self):
        self.book = Mock(spec=AddressBook)

    # For change_phone
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_change_phone_no_args(self, mock_stdout):
        """Tests change_phone. Should ask arguments if there are no args."""
        change_phone([], self.book)
        self.assertIn(
            "Please give me <name> <old phone> <new phone>", mock_stdout.getvalue()
        )
        self.book.change_phone.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_change_phone_no_phone(self, mock_stdout):
        """Tests change_phone. Should ask arguments if there is no phone."""
        change_phone(["Maxima"], self.book)
        self.assertIn(
            "Please give me <name> <old phone> <new phone>", mock_stdout.getvalue()
        )
        self.book.change_phone.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_change_phone_no_new_phone(self, mock_stdout):
        """Tests change_phone. Should ask arguments if there is no new phone."""
        change_phone(["Maxima", "+380631111111"], self.book)
        self.assertIn(
            "Please give me <name> <old phone> <new phone>", mock_stdout.getvalue()
        )
        self.book.change_phone.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_change_phone(self, mock_stdout):
        """Tests change_phone. Should call book.change_phone."""
        change_phone(["Maxima", "+380631111111", "+380731111111"], self.book)
        self.assertNotIn(
            "Please give me <name> <old phone> <new phone>", mock_stdout.getvalue()
        )
        self.book.change_phone.assert_called_once_with(
            "Maxima", "+380631111111", "+380731111111"
        )

    # For show_phone
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_phone_no_name(self, mock_stdout):
        """Tests show_phone. Should ask arguments if there is no name."""
        show_phone([], self.book)
        self.assertIn("Please give me <name>", mock_stdout.getvalue())
        self.book.show_phone.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_phone(self, mock_stdout):
        """Tests show_phone. Should call book.show_phone."""
        show_phone(["Maxima"], self.book)
        self.assertNotIn("Please give me <name>", mock_stdout.getvalue())
        self.book.show_phone.assert_called_once_with("Maxima")

    # For add_phone
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_phone_no_name(self, mock_stdout):
        """Tests add_phone. Should ask arguments if there is no name."""
        add_phone([], self.book)
        self.assertIn("Please give me <name> <phone>", mock_stdout.getvalue())
        self.book.add_phone.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_phone_no_phone(self, mock_stdout):
        """Tests add_phone. Should ask arguments if there is no phone."""
        add_phone(["Maxima"], self.book)
        self.assertIn("Please give me <name> <phone>", mock_stdout.getvalue())
        self.book.add_phone.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_phone(self, mock_stdout):
        """Tests add_phone. Should call book.add_phone."""
        add_phone(["Maxima", "+380631111111"], self.book)
        self.assertNotIn("Please give me <name> <phone>", mock_stdout.getvalue())
        self.book.add_phone.assert_called_once_with("Maxima", "+380631111111")

    # For remove_phone
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_phone_no_name(self, mock_stdout):
        """Tests remove_phone. Should ask arguments if there is no name."""
        remove_phone([], self.book)
        self.assertIn("Please give me <name> <phone>", mock_stdout.getvalue())
        self.book.remove_phone.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_phone_no_phone(self, mock_stdout):
        """Tests remove_phone. Should ask arguments if there is no phone."""
        remove_phone(["Maxima"], self.book)
        self.assertIn("Please give me <name> <phone>", mock_stdout.getvalue())
        self.book.remove_phone.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_phone(self, mock_stdout):
        """Tests remove_phone. Should call book.remove_phone."""
        remove_phone(["Maxima", "+380631111111"], self.book)
        self.assertNotIn("Please give me <name> <phone>", mock_stdout.getvalue())
        self.book.remove_phone.assert_called_once_with("Maxima", "+380631111111")


if __name__ == "__main__":
    unittest.main()
