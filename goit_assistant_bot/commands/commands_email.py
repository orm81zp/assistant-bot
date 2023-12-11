from ..address_book import AddressBook
from .decorators import input_error
from .utils import get_validation_message
from .commands import CMD_ADD_EMAIL, CMD_REMOVE_EMAIL, CMD_SHOW_EMAIL


@input_error(get_validation_message(CMD_ADD_EMAIL))
def add_email(args, book: AddressBook):
    """
    Adds an email for a specific contact found by name or create a new one.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    name, email = args
    book.add_email(name, email.strip())


@input_error(get_validation_message(CMD_SHOW_EMAIL))
def show_email(args, book: AddressBook):
    """
    Shows an email for a specific contact found by name.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    name = args[0]
    book.show_email(name)


@input_error(get_validation_message(CMD_REMOVE_EMAIL))
def remove_email(args, book: AddressBook):
    """
    Removes an email for a specific contact found by name.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    name = args[0]
    book.remove_email(name)


__all__ = [
    "add_email",
    "show_email",
    "remove_email",
]
