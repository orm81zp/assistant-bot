from ..address_book import Record, AddressBook
from ..decorators import input_error
from ..constants import TEXT
from ..utils import is_yes_prompt
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
    email = email.strip()
    contact = book.find(name)

    if contact:
        if contact.email:
            if is_yes_prompt("Existing email will be updated, continue?"):
                contact.add_email(email)
        else:
            contact.add_email(email)
    else:
        contact = Record(name)
        if contact.add_email(email):
            book.add_record(contact)


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
    contact = book.find(name)
    if contact:
        contact.show_email()
    else:
        print(TEXT["NOT_FOUND"])


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
    contact = book.find(name)
    if contact:
        contact.remove_email()
    else:
        print(TEXT["NOT_FOUND"])


__all__ = [
    "add_email",
    "show_email",
    "remove_email",
]
