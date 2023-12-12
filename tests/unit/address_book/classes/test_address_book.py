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
        self.assertIsNone(first_note_uuid)

        self.book.add_note(content)
        second_note_uuid = self.book.get_last_note_uuid()
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
        self.assertEqual(0, number_of_contacts)

        self.book.add_record(Record(name))
        self.assertEqual(number_of_contacts + 1, len(self.book.data["contacts"]))
        # find contact, check name
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
        self.assertEqual(0, number_of_contacts)

        self.book.add_contact(name)

        self.assertIn("Contact added", mocked_stdout.getvalue())
        self.assertEqual(number_of_contacts + 1, len(self.book.data["contacts"]))
        # find contact, check name
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
        self.assertEqual(0, number_of_notes)

        self.book.add_note(content)

        self.assertIn("Note added", mocked_stdout.getvalue())
        self.assertEqual(number_of_notes + 1, len(self.book.data["notes"]))
        # find note, check content
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
        self.assertIn("Birthday added", mocked_stdout.getvalue())
        # find contact, check birthday
        contact = self.book.find(name)
        self.assertEqual(birthday, str(contact.birthday))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_birthday(self, mocked_stdout):
        """
        Tests add_birthday method

        Should add birthday for existing contact
        """
        name = "Erica"
        birthday = "28.10.1984"
        self.book.add_contact(name)

        self.book.add_birthday(name, birthday)
        self.assertIn("Birthday added", mocked_stdout.getvalue())
        # find contact, check birthday
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
        # create contact, add birthday
        self.book.add_birthday(name, birthday)

        # update birthday
        new_birthday = "12.10.1982"
        self.book.add_birthday(name, new_birthday)

        # check if prompt "yes/no" called
        mocked_yes_prompt.assert_called_once()
        self.assertIn("Birthday updated", mock_stdout.getvalue())
        # find contact, check updated birthday
        contact = self.book.find(name)
        self.assertEqual(new_birthday, str(contact.birthday))

    @patch("builtins.input", side_effect=["y"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_birthday(self, mock_stdout, mocked_prompt_decorator):
        """
        Tests remove_birthday method

        Should remove birthday of existing contact
        """
        name = "Maxima"
        birthday = "12.12.2001"
        # create contact, add birthday
        self.book.add_birthday(name, birthday)

        # remove birthday
        self.book.remove_birthday(name)

        # check if prompt "yes/no" called
        mocked_prompt_decorator.assert_called_once()
        self.assertIn("Birthday deleted", mock_stdout.getvalue())
        # find contact, check if birthday is None
        contact = self.book.find(name)
        self.assertIsNone(contact.birthday)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_birthday_not_found_contact(self, mock_stdout):
        """
        Tests remove_birthday method

        Should remove birthday of existing contact
        """
        name = "Maxima"
        # remove birthday, not existing contact
        self.book.remove_birthday(name)
        # check message
        self.assertIn("Contact not found", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_contact_and_email(self, mocked_stdout):
        """
        Tests add_email method

        Should add contact and email
        """
        name = "Eva"
        email = "eva19@gmail.com"
        self.book.add_email(name, email)
        self.assertIn("Email added", mocked_stdout.getvalue())
        # find contact, check email
        contact = self.book.find(name)
        self.assertEqual(email, str(contact.email))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_email(self, mocked_stdout):
        """
        Tests add_email method

        Should add email for existing contact
        """
        name = "Erica"
        email = "erica-new@gmail.com"
        self.book.add_contact(name)

        self.book.add_email(name, email)
        self.assertIn("Email added", mocked_stdout.getvalue())
        # find contact, check email
        contact = self.book.find(name)
        self.assertEqual(email, str(contact.email))

    @patch(
        "goit_assistant_bot.address_book.classes.address_book.is_yes_prompt",
        return_value=True,
    )
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_update_email(self, mock_stdout, mocked_yes_prompt):
        """
        Tests add_email method

        Should update email
        """
        name = "Maxima"
        email = "maxxi21@gmail.com"
        # create contact, add email
        self.book.add_email(name, email)

        # update email
        new_email = "max21xi@gmail.com"
        self.book.add_email(name, new_email)

        # check if prompt "yes/no" called
        mocked_yes_prompt.assert_called_once()
        self.assertIn("Email updated", mock_stdout.getvalue())
        # find contact, check updated email
        contact = self.book.find(name)
        self.assertEqual(new_email, str(contact.email))

    @patch("builtins.input", side_effect=["y"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_email(self, mock_stdout, mocked_prompt_decorator):
        """
        Tests remove_email method

        Should remove email, existing contact
        """
        name = "Maxima"
        email = "maxima21@gmail.com"
        # create contact, add email
        self.book.add_email(name, email)

        # remove email
        self.book.remove_email(name)

        # check if prompt "yes/no" called
        mocked_prompt_decorator.assert_called_once()
        self.assertIn("Email deleted", mock_stdout.getvalue())
        # find contact, check if email is None
        contact = self.book.find(name)
        self.assertIsNone(contact.email)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_email_not_found_contact(self, mock_stdout):
        """
        Tests remove_email method

        Should remove email, existing contact
        """
        name = "Maxima"
        # remove email, not existing contact
        self.book.remove_email(name)
        # check message
        self.assertIn("Contact not found", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_contact_and_address(self, mocked_stdout):
        """
        Tests add_address method

        Should add contact and address
        """
        name = "Eva"
        address = "USA, D18 street 69118"
        self.book.add_address(name, address)
        self.assertIn("Address added", mocked_stdout.getvalue())
        # find contact, check address
        contact = self.book.find(name)
        self.assertEqual(address, str(contact.address))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_address(self, mocked_stdout):
        """
        Tests add_address method

        Should add address for existing contact
        """
        name = "Erica"
        address = "USA, C18 street Ride"
        self.book.add_contact(name)

        self.book.add_address(name, address)
        self.assertIn("Address added", mocked_stdout.getvalue())
        # find contact, check address
        contact = self.book.find(name)
        self.assertEqual(address, str(contact.address))

    @patch(
        "goit_assistant_bot.address_book.classes.address_book.is_yes_prompt",
        return_value=True,
    )
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_update_address(self, mock_stdout, mocked_yes_prompt):
        """
        Tests add_address method

        Should update address
        """
        name = "Maxima"
        address = "Dalas, W18 street Wide"
        # create contact, add address
        self.book.add_address(name, address)

        # update address
        new_address = "Dalas 12, S18 street Harry"
        self.book.add_address(name, new_address)

        # check if prompt "yes/no" called
        mocked_yes_prompt.assert_called_once()
        self.assertIn("Address updated", mock_stdout.getvalue())
        # find contact, check updated address
        contact = self.book.find(name)
        self.assertEqual(new_address, str(contact.address))

    @patch("builtins.input", side_effect=["y"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_address(self, mock_stdout, mocked_prompt_decorator):
        """
        Tests remove_address method

        Should remove address, existing contact
        """
        name = "Maxima"
        address = "USA D19, street Red Stone"
        # create contact, add address
        self.book.add_address(name, address)

        # remove address
        self.book.remove_address(name)

        # check if prompt "yes/no" called
        mocked_prompt_decorator.assert_called_once()
        self.assertIn("Address deleted", mock_stdout.getvalue())
        # find contact, check if address is None
        contact = self.book.find(name)
        self.assertIsNone(contact.address)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_address_not_found_contact(self, mock_stdout):
        """
        Tests remove_address method

        Should remove address, not existing contact
        """
        name = "Maxima"
        # remove address, not existing contact
        self.book.remove_address(name)
        # check message
        self.assertIn("Contact not found", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_phone_and_contact(self, mock_stdout):
        """
        Tests add_phone method

        Should add phone and create contact
        """
        name = "Maxima"
        phone = "+380631112233"
        # create contact, add phone
        self.book.add_phone(name, phone)

        self.assertIn("Phone added", mock_stdout.getvalue())
        # find contact, check phone
        contact = self.book.find(name)
        self.assertEqual(phone, str(contact.get_phone(phone)))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_phone(self, mock_stdout):
        """
        Tests add_phone method

        Should add phone for existing contact
        """
        name = "Eva"
        # create contact
        self.book.add_contact(name)

        # add phone
        phone = "+380631112200"
        self.book.add_phone(name, phone)

        self.assertIn("Phone added", mock_stdout.getvalue())
        # find contact, check phone
        contact = self.book.find(name)
        self.assertEqual(phone, str(contact.get_phone(phone)))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_phone_exists(self, mock_stdout):
        """
        Tests add_phone method

        Should check if phone already exists
        """
        name = "Eva"
        phone = "+380631112299"
        self.book.add_phone(name, phone)

        # add the same phone
        self.book.add_phone(name, phone)
        self.assertIn("Phone already exists", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["y"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_phone(self, mock_stdout, mocked_prompt_decorator):
        """
        Tests remove_phone method

        Should remove phone of existing contact and phone
        """
        name = "Maxima"
        phone = "+380631112211"
        # create contact, add phone
        self.book.add_phone(name, phone)

        # remove phone
        self.book.remove_phone(name, phone)

        # check if prompt "yes/no" called
        mocked_prompt_decorator.assert_called_once()
        self.assertIn("Phone deleted", mock_stdout.getvalue())
        # find contact, check if phone is None
        contact = self.book.find(name)
        self.assertIsNone(contact.get_phone(phone))
        # check if contact has no phones
        self.assertEqual(0, len(contact.phones))

    @patch("builtins.input", side_effect=["y"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_not_found_phone(self, mock_stdout, mocked_prompt_decorator):
        """
        Tests remove_phone method

        Should remove not existing phone of existing contact
        """
        name = "Maxima"
        phone = "+380631112211"
        # create contact, add phone
        self.book.add_phone(name, phone)

        # remove phone
        wrong_phone = "+380991112211"
        self.book.remove_phone(name, wrong_phone)

        # check if prompt "yes/no" called
        mocked_prompt_decorator.assert_called_once()
        self.assertIn("hone not found", mock_stdout.getvalue())
        # find contact, check if phone was not deleted
        contact = self.book.find(name)
        self.assertEqual(phone, str(contact.get_phone(phone)))
        # check if contact still has a phone
        self.assertEqual(1, len(contact.phones))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_phone_not_found_contact(self, mock_stdout):
        """
        Tests remove_phone method

        Should remove phone of not existing contact
        """
        name = "Maxima"
        phone = "+380631112211"
        # remove birthday, not existing contact
        self.book.remove_phone(name, phone)
        # check message
        self.assertIn("Contact not found", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
