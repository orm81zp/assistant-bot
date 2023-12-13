import unittest
import io
from unittest.mock import patch
from goit_assistant_bot.address_book.classes import AddressBook, Record


class TestAddressBook(unittest.TestCase):
    book: AddressBook

    def setUp(self):
        self.book = AddressBook()

    def test_init(self):
        """initial state. Contacts and notes are empty."""
        self.assertEqual(len(self.book.data["contacts"]), 0)
        self.assertEqual(len(self.book.data["notes"]), 0)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_get_note_uuid(self, _):
        """Check if note_uuid is increasing."""
        self.assertEqual(self.book.get_note_uuid(), 1)
        self.book.add_note("Lorem Ipsum is simply dummy text.")
        self.assertEqual(self.book.get_note_uuid(), 2)

    def test_add_record(self):
        """add_record method. Should add a new contact"""
        self.book.add_record(Record("John"))
        self.assertEqual(len(self.book.data["contacts"]), 1)
        contact = self.book.find("John")
        self.assertEqual("John", str(contact.name))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_contact(self, mock_stdout):
        """add_contact method. Should add a new contact"""
        self.book.add_contact("Eva")
        self.assertIn("Contact added", mock_stdout.getvalue())
        self.assertEqual(1, len(self.book.data["contacts"]))
        contact = self.book.find("Eva")
        self.assertEqual("Eva", str(contact.name))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_note(self, mock_stdout):
        """add_note method. Should add a new note"""
        self.book.add_note("Lorem Ipsum is simply dummy text.")
        self.assertIn("Note added", mock_stdout.getvalue())
        self.assertEqual(len(self.book.data["notes"]), 1)
        note = self.book.get_note(1)
        self.assertEqual(note.get_content(), "Lorem Ipsum is simply dummy text.")

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_and_birthday_with_contact(self, mock_stdout):
        """add_birthday method. Should add contact and birthday"""
        self.book.add_birthday("Eva", "12.12.2001")
        self.assertIn("Birthday added", mock_stdout.getvalue())
        contact = self.book.find("Eva")
        self.assertEqual("12.12.2001", str(contact.birthday))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_birthday(self, mock_stdout):
        """add_birthday method. Should add birthday, existing contact"""
        self.book.add_contact("Erica")
        self.book.add_birthday("Erica", "28.10.1984")
        self.assertIn("Birthday added", mock_stdout.getvalue())
        contact = self.book.find("Erica")
        self.assertEqual("28.10.1984", str(contact.birthday))

    @patch(
        "goit_assistant_bot.address_book.classes.address_book.is_yes_prompt",
        return_value=True,
    )
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_update_birthday(self, mock_stdout, mock_is_yes_prompt):
        """add_birthday method. Should update birthday"""
        self.book.add_birthday("Maxima", "12.12.2001")
        new_birthday = "12.10.1982"
        self.book.add_birthday("Maxima", new_birthday)
        mock_is_yes_prompt.assert_called_once()
        self.assertIn("Birthday updated", mock_stdout.getvalue())
        contact = self.book.find("Maxima")
        self.assertEqual(new_birthday, str(contact.birthday))

    @patch("builtins.input", side_effect=["y"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_birthday(self, mock_stdout, mock_prompt_decorator):
        """remove_birthday method. Should remove birthday, existing contact"""
        self.book.add_birthday("Maxima", "12.12.2001")
        self.book.remove_birthday("Maxima")
        mock_prompt_decorator.assert_called_once()
        self.assertIn("Birthday deleted", mock_stdout.getvalue())
        contact = self.book.find("Maxima")
        self.assertIsNone(contact.birthday)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_birthday_no_contact(self, mock_stdout):
        """remove_birthday method. Should not remove birthday, not existing contact"""
        self.book.remove_birthday("Maxima")
        self.assertIn("Contact not found", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_and_email_with_contact(self, mock_stdout):
        """add_email method. Should add contact and email"""
        self.book.add_email("Eva", "eva19@gmail.com")
        self.assertIn("Email added", mock_stdout.getvalue())
        contact = self.book.find("Eva")
        self.assertEqual("eva19@gmail.com", str(contact.email))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_email(self, mock_stdout):
        """add_email method. Should add email, existing contact"""
        self.book.add_contact("Erica")
        self.book.add_email("Erica", "erica-new@gmail.com")
        self.assertIn("Email added", mock_stdout.getvalue())
        contact = self.book.find("Erica")
        self.assertEqual("erica-new@gmail.com", str(contact.email))

    @patch(
        "goit_assistant_bot.address_book.classes.address_book.is_yes_prompt",
        return_value=True,
    )
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_update_email(self, mock_stdout, mock_is_yes_prompt):
        """add_email method. Should update email"""
        self.book.add_email("Maxima", "maxxi21@gmail.com")
        self.book.add_email("Maxima", "new-maxxi21@gmail.com")
        mock_is_yes_prompt.assert_called_once()
        self.assertIn("Email updated", mock_stdout.getvalue())
        contact = self.book.find("Maxima")
        self.assertEqual("new-maxxi21@gmail.com", str(contact.email))

    @patch("builtins.input", side_effect=["y"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_email(self, mock_stdout, mock_prompt_decorator):
        """remove_email method. Should remove email, existing contact"""
        self.book.add_email("Maxima", "maxima21@gmail.com")
        self.book.remove_email("Maxima")
        mock_prompt_decorator.assert_called_once()
        self.assertIn("Email deleted", mock_stdout.getvalue())
        contact = self.book.find("Maxima")
        self.assertIsNone(contact.email)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_email_no_contact(self, mock_stdout):
        """remove_email method. Should not remove email, not existing contact"""
        self.book.remove_email("Maxima")
        self.assertIn("Contact not found", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_address_with_contact(self, mock_stdout):
        """add_address method. Should add contact and address"""
        self.book.add_address("Eva", "USA, D18 street 69118")
        self.assertIn("Address added", mock_stdout.getvalue())
        contact = self.book.find("Eva")
        self.assertEqual("USA, D18 street 69118", str(contact.address))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_address(self, mock_stdout):
        """add_address method. Should add address, existing contact"""
        self.book.add_contact("Erica")
        self.book.add_address("Erica", "USA, C18 street Ride")
        self.assertIn("Address added", mock_stdout.getvalue())
        contact = self.book.find("Erica")
        self.assertEqual("USA, C18 street Ride", str(contact.address))

    @patch(
        "goit_assistant_bot.address_book.classes.address_book.is_yes_prompt",
        return_value=True,
    )
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_update_address(self, mock_stdout, mock_is_yes_prompt):
        """add_address method. Should update address"""
        self.book.add_address("Maxima", "Dalas, W18 street Wide")
        self.book.add_address("Maxima", "New Address Dalas 12, S18 street Harry")
        mock_is_yes_prompt.assert_called_once()
        self.assertIn("Address updated", mock_stdout.getvalue())
        contact = self.book.find("Maxima")
        self.assertEqual("New Address Dalas 12, S18 street Harry", str(contact.address))

    @patch("builtins.input", side_effect=["y"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_address(self, mock_stdout, mock_prompt_decorator):
        """remove_address method. Should remove address, existing contact"""
        self.book.add_address("Maxima", "USA D19, street Red Stone")
        self.book.remove_address("Maxima")
        mock_prompt_decorator.assert_called_once()
        self.assertIn("Address deleted", mock_stdout.getvalue())
        contact = self.book.find("Maxima")
        self.assertIsNone(contact.address)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_address_no_contact(self, mock_stdout):
        """remove_address method. Should not remove address, not existing contact"""
        self.book.remove_address("Maxima")
        self.assertIn("Contact not found", mock_stdout.getvalue())

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_phone_with_contact(self, mock_stdout):
        """add_phone method. Should add phone and contact"""
        self.book.add_phone("Maxima", "+380631112233")
        self.assertIn("Phone added", mock_stdout.getvalue())
        contact = self.book.find("Maxima")
        self.assertTrue(contact.phone_exists("+380631112233"))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_phone(self, mock_stdout):
        """add_phone method. Should add phone, existing contact"""
        self.book.add_contact("Eva")
        self.book.add_phone("Eva", "+380631112200")
        self.assertIn("Phone added", mock_stdout.getvalue())
        contact = self.book.find("Eva")
        self.assertTrue(contact.phone_exists("+380631112200"))

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_add_phone_exists(self, mock_stdout):
        """add_phone method. Should not add existing phone"""
        self.book.add_phone("Eva", "+380631112299")
        self.book.add_phone("Eva", "+380631112299")
        self.assertIn("Phone already exists", mock_stdout.getvalue())

    @patch("builtins.input", side_effect=["y"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_phone(self, mock_stdout, mock_prompt_decorator):
        """remove_phone method. Should remove phone, contact and phone number already exist"""
        self.book.add_phone("Maxima", "+380631112211")
        self.book.remove_phone("Maxima", "+380631112211")
        mock_prompt_decorator.assert_called_once()
        self.assertIn("Phone deleted", mock_stdout.getvalue())
        contact = self.book.find("Maxima")
        self.assertFalse(contact.phone_exists("+380631112211"))
        self.assertEqual(len(contact.phones), 0)

    @patch("builtins.input", side_effect=["y"])
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_not_found_phone(self, mock_stdout, mock_prompt_decorator):
        """remove_phone method. Should not remove, not existing phone"""
        self.book.add_phone("Maxima", "+380631112211")
        self.book.remove_phone("Maxima", "+380777770077")
        mock_prompt_decorator.assert_called_once()
        self.assertIn("Phone not found", mock_stdout.getvalue())
        contact = self.book.find("Maxima")
        self.assertEqual(len(contact.phones), 1)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_remove_phone_not_found_contact(self, mock_stdout):
        """remove_phone method. Should not remove phone, not existing contact"""
        self.book.remove_phone("Maxima", "+380631112211")
        self.assertIn("Contact not found", mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
