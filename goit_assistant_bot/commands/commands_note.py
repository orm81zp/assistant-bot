from ..address_book import AddressBook
from ..decorators import input_error
from .utils import get_validation_message
from .commands import (
    CMD_REMOVE_TAG,
    CMD_ADD_TAG,
    CMD_SHOW_TAG,
    CMD_ADD_NOTE,
    CMD_SEARCH_NOTE_BY_TAG,
    CMD_SHOW_NOTE,
    CMD_REMOVE_NOTE,
    CMD_SEARCH_NOTE
)

@input_error(get_validation_message(CMD_REMOVE_TAG))
def remove_tag(args, book: AddressBook):
    index, tag = args
    index = int(index)
    book.remove_tag(index, tag)

@input_error(get_validation_message(CMD_ADD_TAG))
def add_tag(args, book: AddressBook):
    index, tag = args
    index = int(index)
    book.add_tag(index, tag)

def show_all_tags(_, book: AddressBook):
    book.show_all_tags()

@input_error(get_validation_message(CMD_SHOW_TAG))
def show_tag(args, book: AddressBook):
    index = int(args[0])
    book.show_tag(index)

@input_error(get_validation_message(CMD_ADD_NOTE))
def add_note(args, book: AddressBook):
    content = " ".join(args)
    book.add_note(content)

def show_all_notes(_, book: AddressBook):
    book.find_all_notes()

@input_error(get_validation_message(CMD_SEARCH_NOTE_BY_TAG))
def search_note_by_tag(args, book: AddressBook):
    tag = args[0]
    book.show_notes_by_tag(tag)

@input_error(get_validation_message(CMD_SHOW_NOTE))
def show_note(args, book: AddressBook):
    index = int(args[0])
    book.show_note(index)

@input_error(get_validation_message(CMD_REMOVE_NOTE))
def remove_note(args, book: AddressBook):
    index = int(args[0])
    book.remove_note(index)

@input_error(get_validation_message(CMD_SEARCH_NOTE))
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
