from ..address_book import Record, AddressBook
from ..decorators import input_error
from ..constants import TEXT

    
@input_error("Please give me name and birthday.")
def add_birthday(args, book: AddressBook):
    name, birthday = args

    contact = book.find(name)
    if contact:
        return contact.add_birthday(birthday)
    else:
        contact = Record(name)
        result_add_birthday = contact.add_birthday(birthday)

        if contact.birthday is not None:
            book.add_record(contact)
        
        return result_add_birthday

@input_error("Please give me name.")
def show_birthday(args, book: AddressBook):
    name = args[0]

    contact = book.find(name)
    if contact:
        return contact.find_birthday()
    else:
        return TEXT["CONTACT_NOT_FOUND"]

def birthdays(book: AddressBook):
    birthdays = book.birthdays()
    return birthdays if birthdays else TEXT["NO_DATA_TO_DISPLAY"]

__all__ = [
    "add_birthday",
    "show_birthday",
    "birthdays",
]
