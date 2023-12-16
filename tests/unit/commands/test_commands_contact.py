import unittest
import io
from unittest.mock import patch, Mock
from goit_assistant_bot.address_book.classes import AddressBook
from goit_assistant_bot.commands.commands_contact import (
    show_all,
    remove_contact,
    change_contact_name,
    add_contact,
    search_contact,
    show_contact,
)


class TestCommandsOfContact(unittest.TestCase):
    """Tests commands/commands_contact"""

    book: AddressBook

    def setUp(self):
        self.book = Mock(spec=AddressBook)

    # For show_all
    def test_show_all(self):
        """Tests show_all. Should call book.show_all."""
        show_all([], self.book)
        self.book.show_all.assert_called_once()

    # For remove_contact
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_contact_no_args(self, mock_stdout):
        """Tests remove_contact. Should ask arguments if there is no name."""
        remove_contact([], self.book)
        self.assertIn("Please give me <name>", mock_stdout.getvalue())
        self.book.remove_contact.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_contact(self, mock_stdout):
        """Tests remove_contact. Should call book.remove_contact."""
        remove_contact(["Maxima"], self.book)
        self.assertNotIn("Please give me <name>", mock_stdout.getvalue())
        self.book.remove_contact.assert_called_once_with("Maxima")

    # For change_contact_name
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_change_contact_name_no_name(self, mock_stdout):
        """Tests change_contact_name. Should ask arguments if there is no name."""
        change_contact_name([], self.book)
        self.assertIn("Please give me <name> <new name>", mock_stdout.getvalue())
        self.book.change_name.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_change_contact_name_no_new_name(self, mock_stdout):
        """Tests change_contact_name. Should ask arguments if there is no new name."""
        change_contact_name(["Maxima"], self.book)
        self.assertIn("Please give me <name> <new name>", mock_stdout.getvalue())
        self.book.change_name.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_birthday(self, mock_stdout):
        """Tests change_contact_name. Should call book.change_name."""
        change_contact_name(["Maxima", "Maxima2"], self.book)
        self.assertNotIn("Please give me <name> <new name>", mock_stdout.getvalue())
        self.book.change_name.assert_called_once_with("Maxima", "Maxima2")

    # For add_contact
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_contact_no_args(self, mock_stdout):
        """Tests add_contact. Should ask arguments if there is no name."""
        add_contact([], self.book)
        self.assertIn("Please give me <name>", mock_stdout.getvalue())
        self.book.add_contact.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_contact(self, mock_stdout):
        """Tests add_contact. Should call book.add_contact."""
        add_contact(["Maxima"], self.book)
        self.assertNotIn("Please give me <name>", mock_stdout.getvalue())
        self.book.add_contact.assert_called_once_with("Maxima")

    # For show_contact
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_contact_no_args(self, mock_stdout):
        """Tests show_contact. Should ask arguments if there is no name."""
        show_contact([], self.book)
        self.assertIn("Please give me <name>", mock_stdout.getvalue())
        self.book.show_contact.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_contact(self, mock_stdout):
        """Tests show_contact. Should call book.show_contact."""
        show_contact(["Maxima"], self.book)
        self.assertNotIn("Please give me <name>", mock_stdout.getvalue())
        self.book.show_contact.assert_called_once_with("Maxima")

    # For search_contact
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_search_contact_empty(self, mock_stdout):
        """Tests search_contact. Should ask arguments if there is no searching value."""
        search_contact([], self.book)
        self.assertIn("Please give me <search value>", mock_stdout.getvalue())
        self.book.search_contact.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_search_contact(self, mock_stdout):
        """Tests search_contact. Should call book.search_contact."""
        search_contact(["eva"], self.book)
        self.assertNotIn("Please give me <search value>", mock_stdout.getvalue())
        self.book.search_contact.assert_called_once_with("eva")


if __name__ == "__main__":
    unittest.main()
