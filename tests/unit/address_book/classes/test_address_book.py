import unittest
import io
from unittest.mock import patch
from goit_assistant_bot.address_book.classes import AddressBook, Record, Note


class TestAddressBook(unittest.TestCase):
    """Tests AddressBook methods, not related to commands"""

    book: AddressBook

    def setUp(self):
        self.book = AddressBook()

    def test_init(self):
        """initial state. Contacts and notes are empty."""
        self.assertEqual(len(self.book.data["contacts"]), 0)
        self.assertEqual(len(self.book.data["notes"]), 0)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_note_uuid(self, _):
        """Check if note_uuid returns increasing number."""
        self.assertEqual(self.book.get_note_uuid(), 1)
        self.book.add_note("Lorem Ipsum is simply dummy text.")
        self.assertEqual(self.book.get_note_uuid(), 2)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_find(self, _):
        """find method. Returns None or a Record instance."""
        contact = self.book.find("Maxima")
        self.assertIsNone(contact)
        self.book.add_contact("Maxima")
        contact = self.book.find("Maxima")
        self.assertTrue(isinstance(contact, Record))
        self.assertEqual(str(contact.name), "Maxima")

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_find_with_key(self, _):
        """find_with_key method. Returns (key, Record) or (None, None)."""
        self.book.add_contact("Maxima")
        key, contact = self.book.find_with_key("Maxima")
        self.assertTrue(isinstance(contact, Record))
        self.assertIsNotNone(key)
        # should return (None, None) for not existing contact
        key, contact = self.book.find_with_key("Unknown")
        self.assertIsNone(contact)
        self.assertIsNone(key)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_note(self, _):
        """get_note method. Returns None or Note instance found be index."""
        self.book.add_note("Lorem Ipsum is simply dummy text.")
        note = self.book.get_note(1)
        self.assertTrue(isinstance(note, Note))
        # should return None for not existing note
        note = self.book.get_note(10)
        self.assertIsNone(note)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_note_by_content(self, _):
        """get_note_by_content method. Returns None or Note instance found be index."""
        self.book.add_note("Lorem Ipsum is simply dummy text.")
        note = self.book.get_note_by_content("Lorem Ipsum is simply dummy text.")
        self.assertTrue(isinstance(note, Note))
        # should return None for not found content
        note = self.book.get_note_by_content("Dummy Lorem Ipsum is simply dummy text.")
        self.assertIsNone(note)

    @patch(
        "goit_assistant_bot.address_book.classes.address_book.generate_uuid",
        return_value="dummy:uuid",
    )
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_record(self, mock_stdout, mock_generate_uuid):
        """add_record method. Adds only Record instance to contacts."""
        # should not add a new contact if it's not an instacne of Record
        self.book.add_record("Eva")
        self.assertIn("Must be Record instance.", mock_stdout.getvalue())
        self.assertEqual(len(self.book.data["contacts"]), 0)
        # should add a new contact
        contact = Record("Erik")
        self.book.add_record(contact)
        self.assertEqual(len(self.book.data["contacts"]), 1)
        key, contact = self.book.find_with_key("Erik")
        # check contact key and name
        self.assertEqual(key, "dummy:uuid")
        self.assertEqual(str(contact.name), "Erik")
        mock_generate_uuid.assert_called()


if __name__ == "__main__":
    unittest.main()
