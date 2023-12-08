from colorama import Fore, Style

from ..address_book import AddressBook, Record
from ..decorators import input_error
from ..utils import is_yes_prompt
from ..constants import TEXT

from goit_assistant_bot.utils import print_diff

def show_all(_, book: AddressBook):
    book.find_all()

@input_error("Please give me <name>")
def remove_contact(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)

    if is_yes_prompt("Please confirm the removal of the contact"):
        if contact:
            book.delete(name)
        else:
            print(Fore.LIGHTBLACK_EX + TEXT["CONTACT_NOT_FOUND"] + Style.RESET_ALL)

@input_error("Please give me <name> <new name>")
def change_contact_name(args, book: AddressBook):
    name, new_name = args
    contact = book.find(name)

    if contact:
        new_contact = book.find(new_name)
        if new_contact:
            print(Fore.LIGHTBLACK_EX + TEXT["CONTACT_EXISTS"] + Style.RESET_ALL)
        else:
            if is_yes_prompt("Please confirm updating"):
                if contact.change_name(name, new_name):
                    print_diff(name, new_name)

    else:
        print(Fore.LIGHTBLACK_EX + TEXT["CONTACT_NOT_FOUND"] + Style.RESET_ALL)

@input_error("Please give me <name>")
def add_contact(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)
    if contact:
        print(Fore.LIGHTBLACK_EX + TEXT["CONTACT_EXISTS"] + Style.RESET_ALL)
    else:
        book.add_contact(name)

@input_error("Please give me <name>")
def search_contact(args, book: AddressBook):
    search_value = " ".join(args)
    book.search_contact(search_value)

__all__ = [
    "show_all",
    "remove_contact",
    "add_contact",
    "search_contact",
    "change_contact_name",
]
