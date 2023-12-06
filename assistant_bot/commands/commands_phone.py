from colorama import Fore, Style

from ..address_book import Record, AddressBook
from ..decorators import input_error
from ..constants import TEXT

@input_error("Please give me name, old phone and new phone.")
def change_phone(args, book: AddressBook):
    name, old_phone, new_phone = args
    contact = book.find(name)

    if contact is not None:
        contact.edit_phone(old_phone, new_phone)
    else:
        print(Fore.LIGHTBLACK_EX + TEXT["CONTACT_NOT_FOUND"] + Style.RESET_ALL)

@input_error("Please give me name.")
def show_phone(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)

    if contact:
        contact.find_phones()
    else:
        print(Fore.LIGHTBLACK_EX + TEXT["CONTACT_NOT_FOUND"] + Style.RESET_ALL)

@input_error("Please give me name and phone.")
def add_phone(args, book: AddressBook):
    name, phone = args
    contact = book.find(name)

    if contact:
        contact.add_phone(phone)
    else:
        contact = Record(name)
        added = contact.add_phone(phone)
        if added:
            book.add_record(contact)

@input_error("Please give me name and phone.")
def remove_phone(args, book: AddressBook):
    name, phone = args
    contact = book.find(name)

    if contact:
        contact.remove_phone(phone)
    else:
        print(Fore.LIGHTBLACK_EX + TEXT["CONTACT_NOT_FOUND"] + Style.RESET_ALL)


__all__ = [
    "add_phone",
    "remove_phone",
    "change_phone",
    "show_phone",
]
