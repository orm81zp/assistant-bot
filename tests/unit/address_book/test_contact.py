import unittest
import io
from unittest.mock import patch
from goit_assistant_bot.address_book.classes import AddressBook, Record
from goit_assistant_bot.address_book.exceptions import ValidationValueException


class TestContactCommands(unittest.TestCase):
    """Tests AddressBook class commands related to contact"""

    book: AddressBook

    def setUp(self):
        self.book = AddressBook()

    def test_init(self):
        """initial state."""

    def test_add_record(self):
        """add_record method. Should add a new contact"""
        self.book.add_record(Record("John"))
        self.assertEqual(len(self.book.data["contacts"]), 1)
        contact = self.book.find("John")
        self.assertEqual("John", str(contact.name))

    def test_add_record_exception(self):
        """add_record method. Should raise ValidationValueException"""
        with self.assertRaises(ValidationValueException) as validation_exception:
            self.book.add_record(Record(""))

        self.assertIn(
            "Name failed validation",
            str(validation_exception.exception),
        )

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_contact(self, mock_stdout):
        """add_contact method. Should add a new contact"""
        self.book.add_contact("Eva")
        self.assertIn("Contact added", mock_stdout.getvalue())
        self.assertEqual(1, len(self.book.data["contacts"]))
        contact = self.book.find("Eva")
        self.assertEqual("Eva", str(contact.name))

    def test_add_contact_exception(self):
        """add_contact method. Should raise ValidationValueException"""
        with self.assertRaises(ValidationValueException) as validation_exception:
            self.book.add_contact("")

        self.assertIn(
            "Name failed validation",
            str(validation_exception.exception),
        )


if __name__ == "__main__":
    unittest.main()
