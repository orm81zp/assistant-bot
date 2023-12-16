from ..address_book.classes import AddressBook
from .decorators import input_error
from .utils import get_validation_message
from .commands import CMD_ADD_ADDRESS, CMD_SHOW_ADDRESS, CMD_REMOVE_ADDRESS


@input_error(get_validation_message(CMD_ADD_ADDRESS))
def add_address(args, book: AddressBook):
    """
    Adds an address for a specific user found by name or create a new one.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    name, *address = args
    _ = address[0]
    book.add_address(name, " ".join(address).strip())


@input_error(get_validation_message(CMD_SHOW_ADDRESS))
def show_address(args, book: AddressBook):
    """
    Show an address for a specific user found by name.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    name = args[0]
    book.show_address(name)


@input_error(get_validation_message(CMD_REMOVE_ADDRESS))
def remove_address(args, book: AddressBook):
    """
    Removes an address for a specific user found by name.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    name = args[0]
    book.remove_address(name)


__all__ = [
    "add_address",
    "show_address",
    "remove_address",
]
