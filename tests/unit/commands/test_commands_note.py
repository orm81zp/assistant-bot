import unittest
import io
from unittest.mock import patch, Mock
from goit_assistant_bot.address_book.classes import AddressBook
from goit_assistant_bot.commands.commands_note import (
    remove_tag,
    add_tag,
    show_all_tags,
    show_tag,
    add_note,
    change_note,
    show_all_notes,
    search_note_by_tag,
    show_note,
    remove_note,
    search_note,
)


class TestCommandsOfNote(unittest.TestCase):
    """Tests commands/commands_note"""

    book: AddressBook

    def setUp(self):
        self.book = Mock(spec=AddressBook)

    # For remove_tag
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_tag_no_note_index(self, mock_stdout):
        """Tests remove_tag. Should ask arguments if there is no note index."""
        remove_tag([], self.book)
        self.assertIn("Please give me <note index> <tag>", mock_stdout.getvalue())
        self.book.remove_tag.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_tag_no_tag(self, mock_stdout):
        """Tests remove_tag. Should ask arguments if there is no tag."""
        remove_tag(["1"], self.book)
        self.assertIn("Please give me <note index> <tag>", mock_stdout.getvalue())
        self.book.remove_tag.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_tag(self, mock_stdout):
        """Tests remove_tag. Should call book.remove_tag."""
        remove_tag(["1", "tag1"], self.book)
        self.assertNotIn("Please give me <note index> <tag>", mock_stdout.getvalue())
        self.book.remove_tag.assert_called_once_with(1, "tag1")

    # For add_tag
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_tag_no_note_index(self, mock_stdout):
        """Tests add_tag. Should ask arguments if there is no note index."""
        add_tag([], self.book)
        self.assertIn("Please give me <note index> <tag>", mock_stdout.getvalue())
        self.book.add_tag.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_tag_no_tag(self, mock_stdout):
        """Tests add_tag. Should ask arguments if there is no tag."""
        add_tag(["1"], self.book)
        self.assertIn("Please give me <note index> <tag>", mock_stdout.getvalue())
        self.book.add_tag.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_tag(self, mock_stdout):
        """Tests add_tag. Should call book.add_tag."""
        add_tag(["1", "tag1"], self.book)
        self.assertNotIn("Please give me <note index> <tag>", mock_stdout.getvalue())
        self.book.add_tag.assert_called_once_with(1, "tag1")

    # For show_all_tags
    def test_show_all_tags(self):
        """Tests show_all_tags. Should call book.show_all_tags."""
        show_all_tags([], self.book)
        self.book.show_all_tags.assert_called_once()

    # For show_tag
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_tag_no_note_index(self, mock_stdout):
        """Tests show_tag. Should ask arguments if there is no note index."""
        show_tag([], self.book)
        self.assertIn("Please give me <note index>", mock_stdout.getvalue())
        self.book.show_tag.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_tag(self, mock_stdout):
        """Tests show_tag. Should call book.show_tag."""
        show_tag(["1"], self.book)
        self.assertNotIn("Please give me <note index>", mock_stdout.getvalue())
        self.book.show_tag.assert_called_once_with(1)

    # For add_note
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_note_empty(self, mock_stdout):
        """Tests add_note. Should ask arguments if there is no text."""
        add_note([], self.book)
        self.assertIn("Please give me <text>", mock_stdout.getvalue())
        self.book.add_note.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_note(self, mock_stdout):
        """Tests add_note. Should call book.add_note."""
        add_note(["some", "text", "to", "add"], self.book)
        self.assertNotIn("Please give me <text>", mock_stdout.getvalue())
        self.book.add_note.assert_called_once_with("some text to add")

    # For change_note
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_change_note_no_note_index(self, mock_stdout):
        """Tests change_note. Should ask arguments if there is no note index."""
        change_note([], self.book)
        self.assertIn("Please give me <note index> <text>", mock_stdout.getvalue())
        self.book.change_note.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_change_note_no_text(self, mock_stdout):
        """Tests change_note. Should ask arguments if there is no text."""
        change_note(["1"], self.book)
        self.assertIn("Please give me <note index> <text>", mock_stdout.getvalue())
        self.book.change_note.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_change_note(self, mock_stdout):
        """Tests change_note. Should call book.change_note."""
        change_note(["1", "some", "text", "to", "change"], self.book)
        self.assertNotIn("Please give me <note index> <text>", mock_stdout.getvalue())
        self.book.change_note.assert_called_once_with(1, "some text to change")

    # For show_all_notes
    def test_show_all_notes(self):
        """Tests show_all_notes. Should call book.show_all_notes."""
        show_all_notes([], self.book)
        self.book.show_all_notes.assert_called_once()

    # For search_note_by_tag
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_search_note_by_tag_no_tag(self, mock_stdout):
        """Tests search_note_by_tag. Should ask arguments if there is no tag."""
        search_note_by_tag([], self.book)
        self.assertIn("Please give me <tag>", mock_stdout.getvalue())
        self.book.show_notes_by_tag.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_notes_by_tag(self, mock_stdout):
        """Tests show_notes_by_tag. Should call book.show_notes_by_tag."""
        search_note_by_tag(["tag1"], self.book)
        self.assertNotIn("Please give me <tag>", mock_stdout.getvalue())
        self.book.show_notes_by_tag.assert_called_once_with("tag1")

    # For show_note
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_note_no_note_index(self, mock_stdout):
        """Tests show_note. Should ask arguments if there is no note index."""
        show_note([], self.book)
        self.assertIn("Please give me <note index>", mock_stdout.getvalue())
        self.book.show_note.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_note(self, mock_stdout):
        """Tests show_note. Should call book.show_note."""
        show_note(["2"], self.book)
        self.assertNotIn("Please give me <note index>", mock_stdout.getvalue())
        self.book.show_note.assert_called_once_with(2)

    # For remove_note
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_note_no_note_index(self, mock_stdout):
        """Tests remove_note. Should ask arguments if there is no note index."""
        remove_note([], self.book)
        self.assertIn("Please give me <note index>", mock_stdout.getvalue())
        self.book.remove_note.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_note(self, mock_stdout):
        """Tests remove_note. Should call book.remove_note."""
        remove_note(["10"], self.book)
        self.assertNotIn("Please give me <note index>", mock_stdout.getvalue())
        self.book.remove_note.assert_called_once_with(10)

    # For search_note
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_search_note_empty_search_value(self, mock_stdout):
        """Tests search_note. Should ask arguments if there is no searching value."""
        search_note([], self.book)
        self.assertIn("Please give me <search value>", mock_stdout.getvalue())
        self.book.search_note.assert_not_called()

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_search_note(self, mock_stdout):
        """Tests search_note. Should call book.search_note."""
        search_note(["some", "text", "to", "search"], self.book)
        self.assertNotIn("Please give me <search value>", mock_stdout.getvalue())
        self.book.search_note.assert_called_once_with("some text to search")


if __name__ == "__main__":
    unittest.main()
