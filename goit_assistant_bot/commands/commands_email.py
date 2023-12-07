from colorama import Fore, Style

from ..address_book import Record, AddressBook
from ..decorators import input_error
from ..constants import TEXT
from ..utils import is_yes_prompt

from goit_assistant_bot.utils import print_diff


@input_error("Please give me name and email.")
def add_email(args, book: AddressBook):
    name, email = args
    contact = book.find(name)

    if contact:
        if contact.email:
            if is_yes_prompt("Email already added, update?"):
                old_value = contact.email.value
                if contact.add_email(email):
                    print_diff(old_value, email)
        else:
            contact.add_email(email)
    else:
        contact = Record(name)
        if contact.add_email(email):
            book.add_record(contact)

@input_error("Please give me name.")
def show_email(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)
    if contact:
        contact.show_email()
    else:
        print(Fore.LIGHTBLACK_EX + TEXT["CONTACT_NOT_FOUND"] + Style.RESET_ALL)

@input_error("Please give me name.")
def remove_email(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)
    if contact:
        if is_yes_prompt("Please confirm the removal of the email"):
            contact.remove_email()
    else:
        print(Fore.LIGHTBLACK_EX + TEXT["CONTACT_NOT_FOUND"] + Style.RESET_ALL)

__all__ = [
    "add_email",
    "show_email",
    "remove_email",
]
