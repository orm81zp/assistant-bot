from ..address_book import Record, AddressBook
from ..decorators import input_error
from ..constants import TEXT
from ..utils import is_yes_prompt
from .utils import get_validation_message
from .commands import (
    CMD_ADD_BIRTHDAY,
    CMD_SHOW_BIRTHDAY,
    CMD_REMOVE_BIRTHDAY,
    CMD_BIRTHDAYS,
)


@input_error(get_validation_message(CMD_ADD_BIRTHDAY))
def add_birthday(args, book: AddressBook):
    """
    Adds a birthday for a specific user found by name or create a new one.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    name, birthday = args
    birthday = birthday.strip()

    contact = book.find(name)
    if contact:
        if contact.birthday:
            if is_yes_prompt("Existing birthday will be updated, continue?"):
                contact.add_birthday(birthday)
        else:
            contact.add_birthday(birthday)
    else:
        contact = Record(name)
        if contact.add_birthday(birthday):
            book.add_record(contact)


@input_error(get_validation_message(CMD_SHOW_BIRTHDAY))
def show_birthday(args, book: AddressBook):
    """
    Shows a birthday for a specific user found by name.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    name = args[0]
    contact = book.find(name)

    if contact:
        contact.show_birthday()
    else:
        print(TEXT["NOT_FOUND"])


@input_error(get_validation_message(CMD_REMOVE_BIRTHDAY))
def remove_birthday(args, book: AddressBook):
    """
    Removes a birthday for a specific user found by name.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    name = args[0]

    contact = book.find(name)
    if contact:
        contact.remove_birthday()
    else:
        print(TEXT["NOT_FOUND"])


@input_error(get_validation_message(CMD_BIRTHDAYS))
def birthdays(args, book: AddressBook):
    """
    Shows birthdays for a specific [days range] if passed (7 days by default).

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    days_range = int(args[0]) if len(args) > 0 else None
    book.birthdays(days_range)


__all__ = [
    "add_birthday",
    "show_birthday",
    "birthdays",
    "remove_birthday",
]
