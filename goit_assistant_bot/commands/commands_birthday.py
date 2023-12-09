from colorama import Fore, Style

from ..address_book import Record, AddressBook
from ..decorators import input_error
from ..constants import TEXT
from ..utils import is_yes_prompt

from goit_assistant_bot.utils import print_diff


@input_error("Please give me <name> <birthday>")
def add_birthday(args, book: AddressBook):
    name, birthday = args
    birthday = birthday.strip()

    contact = book.find(name)
    if contact:
        if contact.birthday:
            if is_yes_prompt("Birthday already exists, update?"):
                old_value = contact.birthday.value
                if contact.add_birthday(birthday):
                    print_diff(old_value, birthday)
        else:
            contact.add_birthday(birthday)
    else:
        contact = Record(name)
        if contact.add_birthday(birthday):
            book.add_record(contact)

@input_error("Please give me <name>")
def show_birthday(args, book: AddressBook):
    name = args[0]

    contact = book.find(name)
    if contact:
        contact.show_birthday()
    else:
        print(Fore.LIGHTBLACK_EX + TEXT["CONTACT_NOT_FOUND"] + Style.RESET_ALL)

@input_error("Please give me <name>")
def remove_birthday(args, book: AddressBook):
    name = args[0]

    contact = book.find(name)
    if contact:
            contact.remove_birthday()
    else:
        print(Fore.LIGHTBLACK_EX + TEXT["CONTACT_NOT_FOUND"] + Style.RESET_ALL)

@input_error("[days range] must be a number, 7 days by default")
def birthdays(args, book: AddressBook):
    days_range = int(args[0]) if len(args) > 0 else None
    book.birthdays(days_range)

__all__ = [
    "add_birthday",
    "show_birthday",
    "birthdays",
    "remove_birthday",
]
