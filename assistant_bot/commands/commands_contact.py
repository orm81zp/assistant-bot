from colorama import Fore, Style

from ..address_book import AddressBook
from ..decorators import input_error
from ..utils import is_yes_prompt
from ..constants import TEXT


def show_all(_, book: AddressBook):
    all_contacts = book.find_all()
    if all_contacts:
        print(all_contacts)
    else:
        print(Fore.LIGHTBLACK_EX + TEXT["NO_DATA_TO_DISPLAY"] + Style.RESET_ALL)

@input_error("Please give me name.")
def remove_contact(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)

    if is_yes_prompt("Please confirm the deletion"):
        if contact:
            book.delete(name)
        else:
            print(Fore.LIGHTBLACK_EX + TEXT["CONTACT_NOT_FOUND"] + Style.RESET_ALL)

__all__ = [
    "show_all",
    "remove_contact",
]
