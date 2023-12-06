from ..address_book import Record, AddressBook
from ..decorators import input_error
from ..constants import TEXT

@input_error("Please give me name, old phone and new phone.")
def change_phone(args, book: AddressBook):
    name, old_phone, new_phone = args
    contact = book.find(name)

    if contact is not None:
        return contact.edit_phone(old_phone, new_phone)
    else:
        return TEXT["CONTACT_NOT_FOUND"]

@input_error("Please give me name.")
def show_phone(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)

    if contact:
        return contact.find_phones()
    else:
        return TEXT["CONTACT_NOT_FOUND"]

@input_error("Please give me name and phone.")
def add_phone(args, book: AddressBook):
    name, phone = args
    contact = book.find(name)

    if contact:
        return contact.add_phone(phone)
    else:
        contact = Record(name)
        result_add_phone = contact.add_phone(phone)
        book.add_record(contact)
        return result_add_phone

@input_error("Please give me name and phone.")
def remove_phone(args, book: AddressBook):
    name, phone = args
    contact = book.find(name)

    if contact:
        return contact.remove_phone(phone)
    else:
        return TEXT["CONTACT_NOT_FOUND"]


__all__ = [
    "add_phone",
    "remove_phone",
    "change_phone",
    "show_phone",
]
