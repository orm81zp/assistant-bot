import unittest
import io
from unittest.mock import patch
from goit_assistant_bot.address_book.classes import AddressBook, Record


class TestNoteCommands(unittest.TestCase):
    """Tests AddressBook class commands related to notes"""

    book: AddressBook

    def setUp(self):
        self.book = AddressBook()

    def test_init(self):
        """initial state."""

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_note(self, mock_stdout):
        """add_note method. Should add a new note"""
        self.book.add_note("Lorem Ipsum is simply dummy text.")
        self.assertIn("Note added", mock_stdout.getvalue())
        self.assertEqual(len(self.book.data["notes"]), 1)
        note = self.book.get_note(1)
        self.assertEqual(note.get_content(), "Lorem Ipsum is simply dummy text.")


if __name__ == "__main__":
    unittest.main()
