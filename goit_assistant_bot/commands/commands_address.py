from colorama import Fore, Style

from ..address_book import Record, AddressBook
from ..decorators import input_error
from ..constants import TEXT
from ..utils import is_yes_prompt

from goit_assistant_bot.utils import print_diff


@input_error("Please give me name and address.")
def add_address(args, book: AddressBook):
    name, *address_list = args
    address = " ".join(address_list)

    contact = book.find(name)
    if contact:
        if contact.address:
            if is_yes_prompt("Address already added, update?"):
                old_value = contact.address.value
                if contact.add_address(address):
                    print_diff(old_value, address)
        else:
            contact.add_address(address)
    else:
        contact = Record(name)
        if contact.add_address(address):
            book.add_record(contact)

@input_error("Please give me name.")
def show_address(args, book: AddressBook):
    name = args[0]

    contact = book.find(name)
    if contact:
        contact.show_address()
    else:
        print(Fore.LIGHTBLACK_EX + TEXT["CONTACT_NOT_FOUND"] + Style.RESET_ALL)

@input_error("Please give me name.")
def remove_address(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)
    if contact:
        if is_yes_prompt("Please confirm the removal of the address"):
            contact.remove_address()
    else:
        print(Fore.LIGHTBLACK_EX + TEXT["CONTACT_NOT_FOUND"] + Style.RESET_ALL)

__all__ = [
    "add_address",
    "show_address",
    "remove_address",
]
