from ..address_book.classes import AddressBook
from .decorators import input_error
from .utils import get_validation_message
from .commands import (
    CMD_REMOVE_CONTACT,
    CMD_CHANGE_CONTACT_NAME,
    CMD_ADD_CONTACT,
    CMD_SEARCH_CONTACT,
    CMD_SHOW_CONTACT,
)


def show_all(_, book: AddressBook):
    """
    Shows all contacts.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """
    book.show_all()


@input_error(get_validation_message(CMD_REMOVE_CONTACT))
def remove_contact(args, book: AddressBook):
    """
    Removes a specific contact found by name.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """
    name = args[0]
    book.remove_contact(name)


@input_error(get_validation_message(CMD_CHANGE_CONTACT_NAME))
def change_contact_name(args, book: AddressBook):
    """
    Changes a specific contact found by name.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """
    name, new_name = args
    book.change_name(name, new_name)


@input_error(get_validation_message(CMD_ADD_CONTACT))
def add_contact(args, book: AddressBook):
    """
    Adds a new contact.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """
    name = args[0]
    book.add_contact(name)


@input_error(get_validation_message(CMD_SEARCH_CONTACT))
def search_contact(args, book: AddressBook):
    """
    Search in all contacts.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """
    _ = args[0]
    book.search_contact(" ".join(args))


@input_error(get_validation_message(CMD_SHOW_CONTACT))
def show_contact(args, book: AddressBook):
    """
    Shows a specific contact found by name.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """
    name = args[0]
    book.show_contact(name)


__all__ = [
    "show_all",
    "remove_contact",
    "add_contact",
    "search_contact",
    "change_contact_name",
    "show_contact",
]
