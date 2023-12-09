from ..address_book import Record, AddressBook
from ..decorators import input_error
from ..constants import TEXT
from .utils import get_validation_message
from .commands import CMD_CHANGE_PHONE, CMD_SHOW_PHONE, CMD_ADD_PHONE, CMD_REMOVE_PHONE

@input_error(get_validation_message(CMD_CHANGE_PHONE))
def change_phone(args, book: AddressBook):
    name, old_phone, new_phone = args
    contact = book.find(name)

    if contact:
        contact.edit_phone(old_phone, new_phone)
    else:
        print(TEXT["NOT_FOUND"])

@input_error(get_validation_message(CMD_SHOW_PHONE))
def show_phone(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)

    if contact:
        contact.find_phones()
    else:
        print(TEXT["NOT_FOUND"])

@input_error(get_validation_message(CMD_ADD_PHONE))
def add_phone(args, book: AddressBook):
    name, phone = args
    contact = book.find(name)

    if contact:
        contact.add_phone(phone)
    else:
        contact = Record(name)
        if contact.add_phone(phone):
            book.add_record(contact)

@input_error(get_validation_message(CMD_REMOVE_PHONE))
def remove_phone(args, book: AddressBook):
    name, phone = args
    contact = book.find(name)

    if contact:
        contact.remove_phone(phone)
    else:
        print(TEXT["NOT_FOUND"])


__all__ = [
    "add_phone",
    "remove_phone",
    "change_phone",
    "show_phone",
]
