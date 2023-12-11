from ..address_book import AddressBook
from .decorators import input_error
from .utils import get_validation_message
from .commands import (
    CMD_REMOVE_TAG,
    CMD_ADD_TAG,
    CMD_SHOW_TAG,
    CMD_ADD_NOTE,
    CMD_SEARCH_NOTE_BY_TAG,
    CMD_SHOW_NOTE,
    CMD_REMOVE_NOTE,
    CMD_SEARCH_NOTE,
    CMD_CHANGE_NOTE,
)


@input_error(get_validation_message(CMD_REMOVE_TAG))
def remove_tag(args, book: AddressBook):
    """
    Removes a tag for a specific note found by index.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    index, tag = args
    book.remove_tag(int(index), tag)


@input_error(get_validation_message(CMD_ADD_TAG))
def add_tag(args, book: AddressBook):
    """
    Adds a new tag for a specific note found by index.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    index, tag = args
    book.add_tag(int(index), tag)


def show_all_tags(_, book: AddressBook):
    """
    Shows all tags.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    book.show_all_tags()


@input_error(get_validation_message(CMD_SHOW_TAG))
def show_tag(args, book: AddressBook):
    """
    Removes all tags for a specific note found by index.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    index = args[0]
    book.show_tag(int(index))


@input_error(get_validation_message(CMD_ADD_NOTE))
def add_note(args, book: AddressBook):
    """
    Adds a new note.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """
    content = " ".join(args)
    book.add_note(content)


@input_error(get_validation_message(CMD_CHANGE_NOTE))
def change_note(args, book: AddressBook):
    """
    Changes a specific note found by index.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    index, *content = args
    content = " ".join(content)
    book.change_note(int(index), content.strip())


def show_all_notes(_, book: AddressBook):
    """
    Shows all notes.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    book.find_all_notes()


@input_error(get_validation_message(CMD_SEARCH_NOTE_BY_TAG))
def search_note_by_tag(args, book: AddressBook):
    """
    Shows notes found by a specific tag.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    tag = args[0]
    book.show_notes_by_tag(tag)


@input_error(get_validation_message(CMD_SHOW_NOTE))
def show_note(args, book: AddressBook):
    """
    Shows a specific note found by index.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    index = args[0]
    book.show_note(int(index))


@input_error(get_validation_message(CMD_REMOVE_NOTE))
def remove_note(args, book: AddressBook):
    """
    Removes a note found by index.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    index = args[0]
    book.remove_note(int(index))


@input_error(get_validation_message(CMD_SEARCH_NOTE))
def search_note(args, book: AddressBook):
    """
    Searches in all notes.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    search_value = " ".join(args)
    book.search_note(search_value.strip())


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
    "change_note",
]
