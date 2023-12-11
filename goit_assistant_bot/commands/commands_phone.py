from ..address_book import AddressBook
from .decorators import input_error
from .utils import get_validation_message
from .commands import CMD_CHANGE_PHONE, CMD_SHOW_PHONE, CMD_ADD_PHONE, CMD_REMOVE_PHONE


@input_error(get_validation_message(CMD_CHANGE_PHONE))
def change_phone(args, book: AddressBook):
    """
    Chenges a phone number for a specific contact found by name.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    name, phone, new_phone = args
    book.change_phone(name, phone, new_phone)


@input_error(get_validation_message(CMD_SHOW_PHONE))
def show_phone(args, book: AddressBook):
    """
    Shows phone numbers for a specific contact found by name.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    name = args[0]
    book.show_phone(name)


@input_error(get_validation_message(CMD_ADD_PHONE))
def add_phone(args, book: AddressBook):
    """
    Add a phone number for a specific contact found by name or create a new one.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    name, phone = args
    book.add_phone(name, phone)


@input_error(get_validation_message(CMD_REMOVE_PHONE))
def remove_phone(args, book: AddressBook):
    """
    Removes a phone number for a specific contact found by name.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    name, phone = args
    book.remove_phone(name, phone)


__all__ = [
    "add_phone",
    "remove_phone",
    "change_phone",
    "show_phone",
]
