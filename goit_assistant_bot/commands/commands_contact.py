from ..address_book import AddressBook
from ..decorators import input_error
from ..constants import TEXT
from .utils import get_validation_message
from .commands import CMD_REMOVE_CONTACT, CMD_CHANGE_CONTACT_NAME, CMD_ADD_CONTACT, CMD_SEARCH_CONTACT, CMD_SHOW_CONTACT

def show_all(_, book: AddressBook):
    book.find_all()

@input_error(get_validation_message(CMD_REMOVE_CONTACT))
def remove_contact(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)

    if contact:
        book.remove_contact(name)
    else:
        print(TEXT["NOT_FOUND"])

@input_error(get_validation_message(CMD_CHANGE_CONTACT_NAME))
def change_contact_name(args, book: AddressBook):
    name, new_name = args
    contact = book.find(name)

    if contact:
        new_contact = book.find(new_name)
        if new_contact:
            print(TEXT["EXISTS"])
        else:
            contact.change_name(name, new_name)
    else:
        print(TEXT["NOT_FOUND"])

@input_error(get_validation_message(CMD_ADD_CONTACT))
def add_contact(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)

    if contact:
        print(TEXT["EXISTS"])
    else:
        book.add_contact(name)

@input_error(get_validation_message(CMD_SEARCH_CONTACT))
def search_contact(args, book: AddressBook):
    search_value = " ".join(args)
    book.search_contact(search_value)

@input_error(get_validation_message(CMD_SHOW_CONTACT))
def show_contact(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)

    if contact:
        book.show_contact(name)
    else:
        print(TEXT["NOT_FOUND"])

__all__ = [
    "show_all",
    "remove_contact",
    "add_contact",
    "search_contact",
    "change_contact_name",
    "show_contact",
]
