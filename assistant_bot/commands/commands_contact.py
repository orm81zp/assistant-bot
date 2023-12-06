from ..address_book import AddressBook
from ..decorators import input_error
from ..constants import TEXT


def show_all(book: AddressBook):
    all_contacts = book.find_all()
    return all_contacts if all_contacts else TEXT["NO_DATA_TO_DISPLAY"]

@input_error("Please give me name.")
def remove_contact(args, book: AddressBook):
    name = args[0]
    contact = book.find(name)

    if contact:
        return book.delete(name)
    else:
        return TEXT["CONTACT_NOT_FOUND"]


__all__ = [
    "show_all",
    "remove_contact",
]
