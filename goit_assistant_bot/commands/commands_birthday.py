from ..address_book import AddressBook
from .decorators import input_error
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
    book.add_birthday(name, birthday.strip())


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
    book.show_birthday(name)


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
    book.remove_birthday(name)


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
