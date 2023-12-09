from ..address_book import AddressBook
from ..decorators import input_error
from ..address_book import Note

# Tags
@input_error("Please give me <note index> <tag>")
def remove_tag(args, book: AddressBook):
    index, tag = args
    index = int(index)
    book.remove_tag(index, tag)

@input_error("Please give me <note index> <tag>")
def add_tag(args, book: AddressBook):
    index, tag = args
    index = int(index)
    book.add_tag(index, tag)

def show_all_tags(_, book: AddressBook):
    book.show_all_tags()

@input_error("Please give me <note index>")
def show_tag(args, book: AddressBook):
    index = int(args[0])
    book.show_tag(index)

# Notes
@input_error("Please give me <text>")
def add_note(args, book: AddressBook):
    content = " ".join(args)
    book.add_note(content)

def show_all_notes(_, book: AddressBook):
    book.find_all_notes()

@input_error("Please give me <tag>")
def search_note_by_tag(args, book: AddressBook):
    tag = args[0]
    book.show_notes_by_tag(tag)

@input_error("Please give me <note index>")
def show_note(args, book: AddressBook):
    index = int(args[0])
    book.show_note(index)

@input_error("Please give me <note index>")
def remove_note(args, book: AddressBook):
    index = int(args[0])
    book.remove_note(index)

@input_error("Please give me <search_value>")
def search_note(args, book: AddressBook):
    search_value = " ".join(args)
    book.search_note(search_value)

__all__ = [
    "show_all_notes",
    "remove_note",
    "add_note",
    "show_note",
    "add_tag",
    "remove_tag",
    "show_all_tags",
    "show_tag",
    "search_note_by_tag",
    "search_note",
]
