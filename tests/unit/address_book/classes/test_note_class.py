import unittest
from unittest.mock import patch
import io
from goit_assistant_bot.address_book.classes.note import Note
from goit_assistant_bot.address_book.exceptions import ValidationValueException


class TestAddressClass(unittest.TestCase):
    """Tests Address class"""

    def test_ini(self):
        """__init__ methom. Should have all attributes value."""
        note = Note("more than 10 characters", "uuid")
        self.assertEqual(note.content, "more than 10 characters")
        self.assertEqual(note.uuid, "uuid")
        self.assertEqual(len(note.tags), 0)

    def test_exceptions(self):
        """value attribute. Must raise ValidationValueException."""
        contents = ["", None, "less 10", "".join([str("A") for _ in range(501)])]
        for content in contents:
            with self.assertRaises(ValidationValueException):
                Note(content, "uuid")

        note = Note("more than 10 characters", "uuid")
        with self.assertRaises(ValidationValueException):
            note.content = "less 10"

    def test___str__(self):
        """Tests magical __str__ method"""
        note = Note("a valid note", "uuid")
        self.assertEqual(str(note), "no tags; uuid; a valid note")

    def test___repr__(self):
        """Tests magical __repr__ method"""
        note = Note("a valid note", "uuid")
        self.assertEqual(repr(note), "Note: no tags; uuid; a valid note")

    def test_get_content(self):
        """Tests get_content method. Should return correct content"""
        note = Note("a valid note", "uuid")
        self.assertEqual(note.content, "a valid note")

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_tag(self, mock_stdout):
        """Tests add_tag method. Should add a tag"""
        note = Note("a valid note", "uuid")
        note.add_tag("test")
        self.assertIn("Tag added", mock_stdout.getvalue())
        self.assertTrue(note.tag_exists("test"))
        self.assertEqual(len(note.tags), 1)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_tag_exceptions(self, _):
        """add_tag method. Must raise ValidationValueException."""
        tags = ["", None, "with space", "more15characters"]
        note = Note("some valid text to add", "uuid")
        for tag in tags:
            with self.assertRaises(ValidationValueException):
                note.add_tag(tag)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_tag_exists(self, mock_stdout):
        """Tests add_tag method. Should not add an existing tag"""
        note = Note("a valid note", "uuid")
        note.add_tag("test")
        self.assertIn("Tag added", mock_stdout.getvalue())
        note.add_tag("test")
        self.assertIn("The same tag already exists", mock_stdout.getvalue())
        self.assertTrue(note.tag_exists("test"))
        self.assertEqual(len(note.tags), 1)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_tag_exists(self, _):
        """Tests tag_exists method. Should return True"""
        note = Note("a valid note", "uuid")
        note.add_tag("test")
        self.assertTrue(note.tag_exists("test"))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_tag_exists_not_found(self, _):
        """Tests tag_exists method. Should return False"""
        note = Note("a valid note", "uuid")
        note.add_tag("newtag")
        self.assertFalse(note.tag_exists("tag"))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_tags(self, _):
        """Tests get_tags method. Should return tags as string"""
        note = Note("a valid note", "uuid")
        note.add_tag("tag1")
        note.add_tag("tag2")
        self.assertEqual(note.get_tags(), "tag1 tag2")

    def test_get_tags_not_found(self):
        """Tests get_tags method. Should return a message if there are no tags"""
        note = Note("a valid note", "uuid")
        self.assertEqual(note.get_tags(), "no tags")
        self.assertEqual(note.get_tags(" - "), " - ")

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_tag(self, mock_stdout):
        """Tests remove_tag method. Should remove tag"""
        note = Note("a valid note", "uuid")
        note.add_tag("tag1")
        note.add_tag("tag2")
        note.remove_tag("tag1")
        self.assertIn("Tag deleted", mock_stdout.getvalue())
        # check if removed tag is not available any more
        self.assertFalse(note.tag_exists("tag1"))
        self.assertTrue(note.tag_exists("tag2"))
        self.assertEqual(len(note.tags), 1)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_tag_not_found(self, mock_stdout):
        """Tests remove_tag method. Should not remove not existing tag"""
        note = Note("a valid note", "uuid")
        note.add_tag("tag1")
        note.add_tag("tag2")
        note.remove_tag("unknown")
        self.assertIn("Tag not found", mock_stdout.getvalue())
        self.assertTrue(note.tag_exists("tag1"))
        self.assertTrue(note.tag_exists("tag2"))
        self.assertEqual(len(note.tags), 2)


if __name__ == "__main__":
    unittest.main()
