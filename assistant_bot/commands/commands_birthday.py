from colorama import Fore, Style

from ..address_book import Record, AddressBook
from ..decorators import input_error
from ..constants import TEXT


@input_error("Please give me name and birthday.")
def add_birthday(args, book: AddressBook):
    name, birthday = args

    contact = book.find(name)
    if contact:
        contact.add_birthday(birthday)
    else:
        contact = Record(name)
        added = contact.add_birthday(birthday)

        if added:
            book.add_record(contact)

@input_error("Please give me name.")
def show_birthday(args, book: AddressBook):
    name = args[0]

    contact = book.find(name)
    if contact:
        print(contact.find_birthday())
    else:
        print(Fore.LIGHTBLACK_EX + TEXT["CONTACT_NOT_FOUND"] + Style.RESET_ALL)

def birthdays(_, book: AddressBook):
    all_birthdays = book.birthdays()
    if all_birthdays:
        print(all_birthdays)
    else:
        print(Fore.LIGHTBLACK_EX + TEXT["NO_DATA_TO_DISPLAY"] + Style.RESET_ALL)

__all__ = [
    "add_birthday",
    "show_birthday",
    "birthdays",
]
