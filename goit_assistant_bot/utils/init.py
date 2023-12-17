import os
import sys
from pathlib import Path
from colorama import Fore, Style
from ..address_book.classes import AddressBook
from .address_book_manager import AddressBookManager

address_book_manager: AddressBookManager | None = None


def start_work() -> AddressBook:
    global address_book_manager
    default_file_name = "assistant_data.bin"
    dump_file = Path(default_file_name)

    argv = sys.argv[1:]
    if len(argv) == 1:
        file_name = Path(argv[0])
        if file_name.suffix in [".bin", ".dat"]:
            dump_file = Path(file_name)
        else:
            print(
                Fore.LIGHTBLACK_EX
                + f'The file name must end with *.bin or *.dat, "{default_file_name}" will be used by default as a dump file.'
                + Style.RESET_ALL
            )

    address_book_manager = AddressBookManager(dump_file)
    book = address_book_manager.get_book()
    return book


def save():
    """Saves the contact book"""
    global address_book_manager

    if address_book_manager:
        address_book_manager.save()


def stop_work():
    """Saves the contact book end run exit command"""
    save()
    os._exit(0)


__all__ = [
    "start_work",
    "stop_work",
    "save",
]
