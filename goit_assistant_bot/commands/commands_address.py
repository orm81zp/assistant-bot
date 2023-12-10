from ..address_book import Record, AddressBook
from ..decorators import input_error
from ..constants import TEXT
from ..utils import is_yes_prompt
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
    address = " ".join(address).strip()

    contact = book.find(name)
    if contact:
        if contact.address:
            if is_yes_prompt("Existing address will be updated, continue?"):
                contact.add_address(address)
        else:
            contact.add_address(address)
    else:
        contact = Record(name)
        if contact.add_address(address):
            book.add_record(contact)

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

    contact = book.find(name)
    if contact:
        contact.show_address()
    else:
        print(TEXT["NOT_FOUND"])

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
    contact = book.find(name)
    if contact:
        contact.remove_address()
    else:
        print(TEXT["NOT_FOUND"])

__all__ = [
    "add_address",
    "show_address",
    "remove_address",
]
