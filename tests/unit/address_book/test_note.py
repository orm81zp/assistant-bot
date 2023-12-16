import unittest
import io
from unittest.mock import patch
from goit_assistant_bot.address_book.classes import AddressBook
from goit_assistant_bot.address_book.exceptions import ValidationValueException


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
        self.assertEqual(note.content, "Lorem Ipsum is simply dummy text.")

    def test_add_note_exception(self):
        """add_note method. Should raise ValidationValueException"""
        with self.assertRaises(ValidationValueException) as validation_exception:
            self.book.add_note("less 10")

        self.assertIn(
            "Note failed validation",
            str(validation_exception.exception),
        )

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_note(self, mock_stdout):
        """show_note method. Should show a note"""
        self.book.add_note("Lorem Ipsum is simply dummy text.")
        self.book.show_note(1)
        self.assertIn("Lorem Ipsum is simply dummy text", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_note_not_found(self, mock_stdout):
        """show_note method. Should not show an existing note"""
        self.book.add_note("Lorem Ipsum is simply dummy text.")
        self.book.show_note(100)
        self.assertIn("Note not found", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_change_note(self, mock_stdout):
        """change_note method. Should change a note"""
        self.book.add_note("Lorem Ipsum is simply dummy text.")
        new_content = "NEW Lorem Ipsum is simply dummy text."
        self.book.change_note(1, new_content)
        self.assertIn("Note updated", mock_stdout.getvalue())
        self.assertEqual(self.book.get_note(1).content, new_content)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_change_note_not_found(self, mock_stdout):
        """change_note method. Should not change a not existing note"""
        self.book.add_note("Lorem Ipsum is simply dummy text.")
        self.book.change_note(100, "NEW Lorem Ipsum is simply dummy text.")
        self.assertIn("Note not found", mock_stdout.getvalue())
        self.assertEqual(
            self.book.get_note(1).content, "Lorem Ipsum is simply dummy text."
        )

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_change_note_exists(self, mock_stdout):
        """change_note method. Should not change a note if the content already exists"""
        self.book.add_note("1 Lorem Ipsum is simply dummy text.")
        self.book.add_note("2 Lorem Ipsum is simply dummy text.")
        new_content = "1 Lorem Ipsum is simply dummy text."
        self.book.change_note(2, new_content)
        self.assertIn(
            "A note with the same content already exists", mock_stdout.getvalue()
        )
        self.assertEqual(
            self.book.get_note(1).content, "1 Lorem Ipsum is simply dummy text."
        )
        self.assertEqual(
            self.book.get_note(2).content, "2 Lorem Ipsum is simply dummy text."
        )

    def test_change_note_exception(self):
        """change_note method. Should raise ValidationValueException"""
        with self.assertRaises(ValidationValueException) as validation_exception:
            self.book.add_note("Lorem Ipsum is simply dummy text.")
            self.book.change_note(1, "less 10")

        self.assertIn(
            "Note failed validation",
            str(validation_exception.exception),
        )

    @patch("builtins.input", side_effect=["y"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_note(self, mock_stdout, mock_prompt_decorator):
        """remove_note method. Should remove a note"""
        self.book.add_note("Lorem Ipsum is simply dummy text.")
        self.book.remove_note(1)
        mock_prompt_decorator.assert_called_once()
        self.assertIn("Note deleted", mock_stdout.getvalue())
        self.assertIsNone(self.book.get_note(1))

    @patch("builtins.input", side_effect=["n"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_note_not_confirmed(self, mock_stdout, mock_prompt_decorator):
        """remove_note method. Should not remove a note if it was not confirmed"""
        self.book.add_note("Lorem Ipsum is simply dummy text.")
        self.book.remove_note(1)
        mock_prompt_decorator.assert_called_once()
        self.assertNotIn("Note deleted", mock_stdout.getvalue())
        # check of a note is still available, not deleted
        self.assertIsNotNone(self.book.get_note(1))

    # For tags
    # For add_tag
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_tag(self, mock_stdout):
        """add_tag method. Should add a tag"""
        self.book.add_note("Lorem Ipsum is simply dummy text.")
        self.book.add_tag(1, "tag1")
        self.assertIn("Tag added", mock_stdout.getvalue())
        note = self.book.get_note(1)
        self.assertTrue(note.tag_exists("tag1"))
        self.assertEqual(len(note.tags), 1)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_tag_exists(self, mock_stdout):
        """add_tag method. Should not add a tag if one already exists"""
        self.book.add_note("Lorem Ipsum is simply dummy text.")
        self.book.add_tag(1, "tag1")
        self.book.add_tag(1, "tag1")
        self.assertIn("The same tag already exists", mock_stdout.getvalue())
        note = self.book.get_note(1)
        self.assertTrue(note.tag_exists("tag1"))
        self.assertEqual(len(note.tags), 1)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_tag_note_not_found(self, mock_stdout):
        """add_tag method. Should not add a tag if a note not found"""
        self.book.add_note("Lorem Ipsum is simply dummy text.")
        self.book.add_tag(100, "tag1")
        self.assertIn("Note not found", mock_stdout.getvalue())
        note = self.book.get_note(1)
        self.assertFalse(note.tag_exists("tag1"))
        self.assertEqual(len(note.tags), 0)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_tag_exception(self, _):
        """add_tag method. Should raise ValidationValueException"""
        with self.assertRaises(ValidationValueException) as validation_exception:
            self.book.add_note("Lorem Ipsum is simply dummy text.")
            self.book.add_tag(1, "more 15 characters with spaces")

        self.assertIn(
            "Tag failed validation",
            str(validation_exception.exception),
        )

    # For show_tag
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_show_tag(self, mock_stdout):
        """show_tag method. Should show tags in a note"""
        self.book.add_note("Lorem Ipsum is simply dummy text.")
        self.book.add_tag(1, "super1tag")
        self.book.add_tag(1, "super2tag")
        self.book.show_tag(1)
        self.assertIn("super1tag", mock_stdout.getvalue())
        self.assertIn("super2tag", mock_stdout.getvalue())

    # For remove_tag
    @patch("builtins.input", side_effect=["y"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_tag(self, mock_stdout, mock_prompt_decorator):
        """remove_tag method. Should remove a tag"""
        self.book.add_note("Lorem Ipsum is simply dummy text.")
        self.book.add_tag(1, "tag1")
        self.book.add_tag(1, "tag2")
        self.book.remove_tag(1, "tag2")
        mock_prompt_decorator.assert_called_once()
        self.assertIn("Tag deleted", mock_stdout.getvalue())
        note = self.book.get_note(1)
        self.assertFalse(note.tag_exists("tag2"))
        self.assertEqual(len(note.tags), 1)

    @patch("builtins.input", side_effect=["n"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_tag_not_confirmed(self, mock_stdout, mock_prompt_decorator):
        """remove_tag method. Should not remove a tag if it was not confirmed"""
        self.book.add_note("Lorem Ipsum is simply dummy text.")
        self.book.add_tag(1, "tag1")
        self.book.add_tag(1, "tag2")
        self.book.remove_tag(1, "tag2")
        mock_prompt_decorator.assert_called_once()
        self.assertNotIn("Tag deleted", mock_stdout.getvalue())
        note = self.book.get_note(1)
        self.assertTrue(note.tag_exists("tag2"))
        self.assertEqual(len(note.tags), 2)


if __name__ == "__main__":
    unittest.main()
