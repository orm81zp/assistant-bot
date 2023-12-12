import unittest
import io
from unittest.mock import patch, Mock
from goit_assistant_bot.address_book.classes import AddressBook, Record


class TestAddressBook(unittest.TestCase):
    dump_file = "tests_assistant_data.bin"
    book: AddressBook

    def setUp(self):
        self.book = AddressBook(self.dump_file)

    def test_init(self):
        """
        Tests initial state.

        Check is_dirty, dump_file values.
        """
        self.assertEqual(False, self.book.is_dirty)
        self.assertEqual(self.dump_file, self.book.get_dump_file())

    def test_get_dump_file(self):
        """
        Tests get_dump_file method.

        Checks if dump_file exists and equals to the initial one
        """
        self.assertEqual(self.dump_file, self.book.get_dump_file())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_last_note_uuid(self, _):
        """
        Tests get_last_note_uuid method.

        Check if note_uuid is increasing.
        """
        content = "Lorem Ipsum is simply dummy text."
        first_note_uuid = self.book.get_last_note_uuid()
        self.book.add_note(content)
        second_note_uuid = self.book.get_last_note_uuid()

        # Asserts
        # check before adding note
        self.assertIsNone(first_note_uuid)
        # check after adding note
        self.assertEqual(1, second_note_uuid)

    @patch("goit_assistant_bot.address_book.classes.address_book.save_address_book")
    def test_save(self, mocked_save_address_book):
        """
        Tests save method.

        Checks if save_address_book func called
        """
        self.book.save()
        mocked_save_address_book.assert_called_once_with(self.book)

    @patch(
        "goit_assistant_bot.address_book.classes.address_book.save_address_book",
        Mock(side_effect=Exception),
    )
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_save_exception(self, mocked_stdout):
        """
        Tests save method for Exception

        Checks printed catched error message
        """
        # mocked_save_address_book.side_effect = Exception
        self.book.save()
        self.assertIn(
            "Oh! Something went wrong, the data was not saved!",
            mocked_stdout.getvalue(),
        )

    def test_add_record(self):
        """
        Tests add_record method

        Should add a new contact by Record
        """
        name = "John"
        number_of_contacts = len(self.book.data["contacts"])
        self.book.add_record(Record(name))

        # Asserts
        # check the number of contacts before adding
        self.assertEqual(0, number_of_contacts)
        # check the number of contacts after adding
        self.assertEqual(number_of_contacts + 1, len(self.book.data["contacts"]))
        # find contact and check name
        contact = self.book.find(name)
        self.assertEqual(name, str(contact.name))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_contact(self, mocked_stdout):
        """
        Tests add_contact method

        Should add a new contact by name, checks printed message
        """
        name = "Eva"
        number_of_contacts = len(self.book.data["contacts"])
        self.book.add_contact(name)

        # Asserts
        # check the number of contacts before adding
        self.assertEqual(0, number_of_contacts)
        self.assertIn("Contact added", mocked_stdout.getvalue())
        # check the number of contacts after adding
        self.assertEqual(number_of_contacts + 1, len(self.book.data["contacts"]))
        # find contact and check name
        contact = self.book.find(name)
        self.assertEqual(name, str(contact.name))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_note(self, mocked_stdout):
        """
        Tests add_note method

        Should add a new note, checks printed message
        """
        content = "Lorem Ipsum is simply dummy text."
        number_of_notes = len(self.book.data["notes"])
        self.book.add_note(content)

        # Asserts
        # check the number of notes before adding
        self.assertEqual(0, number_of_notes)
        # check printed message
        self.assertIn("Note added", mocked_stdout.getvalue())
        # check the number of notes after adding
        self.assertEqual(number_of_notes + 1, len(self.book.data["notes"]))
        # find note and check content
        note = self.book.get_note(self.book.get_last_note_uuid())
        self.assertEqual(content, note.get_content())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_contact_and_birthday(self, mocked_stdout):
        """
        Tests add_birthday method

        Should add contact and birthday
        """
        name = "Eva"
        birthday = "12.12.2001"
        self.book.add_birthday(name, birthday)

        # Asserts
        # check printed message
        self.assertIn("Birthday added", mocked_stdout.getvalue())
        # find contact and check birthday
        contact = self.book.find(name)
        self.assertEqual(birthday, str(contact.birthday))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_birthday(self, mocked_stdout):
        """
        Tests add_birthday method

        Should add birthday
        """
        name = "Erica"
        birthday = "28.10.1984"
        self.book.add_contact(name)
        self.book.add_birthday(name, birthday)

        # Asserts
        # check printed message
        self.assertIn("Birthday added", mocked_stdout.getvalue())
        # find contact and check birthday
        contact = self.book.find(name)
        self.assertEqual(birthday, str(contact.birthday))

    @patch(
        "goit_assistant_bot.address_book.classes.address_book.is_yes_prompt",
        return_value=True,
    )
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_update_birthday(self, mock_stdout, mocked_yes_prompt):
        """
        Tests add_birthday method

        Should update birthday
        """
        name = "Maxima"
        birthday = "12.12.2001"
        # create contact and add birthday
        self.book.add_birthday(name, birthday)

        # update birthday
        new_birthday = "12.10.1982"
        self.book.add_birthday(name, new_birthday)

        # Asserts
        # check if prompted "yes/no" called
        mocked_yes_prompt.assert_called_once()
        # check message
        self.assertIn("Birthday updated", mock_stdout.getvalue())
        # find contact and check updated birthday
        contact = self.book.find(name)
        self.assertEqual(new_birthday, str(contact.birthday))


if __name__ == "__main__":
    unittest.main()
