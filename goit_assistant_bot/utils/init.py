import os
import sys
import pickle
from pathlib import Path
from colorama import Fore, Style
from ..address_book.classes import AddressBook
from ..address_book.utils import save_address_book

ADDRESS_BOOK: AddressBook | None = None


def start_work() -> AddressBook:
    global ADDRESS_BOOK
    dump_file_name = "assistant_data.bin"
    dump_file = Path(dump_file_name)

    argv = sys.argv[1:]
    if len(argv) == 1:
        file_name = Path(argv[0])
        if file_name.suffix in [".bin", ".data"]:
            dump_file = Path(file_name)
        else:
            print(
                Fore.LIGHTBLACK_EX
                + f'The file suffix must end with *.bin or *.data, "{dump_file_name}" file will be used by default.'
                + Style.RESET_ALL
            )

    book = AddressBook(str(dump_file))
    if dump_file.exists():
        with open(dump_file, "rb") as fh:
            book: AddressBook = pickle.load(fh)
            print(
                Fore.LIGHTBLACK_EX + "\u2713 Contact book restored!" + Style.RESET_ALL
            )

    ADDRESS_BOOK = book
    return ADDRESS_BOOK


def stop_work():
    global ADDRESS_BOOK
    try:
        if ADDRESS_BOOK:
            save_address_book(ADDRESS_BOOK)
    except Exception:
        print(
            Fore.RED
            + "Oh! Something went wrong, the data was not saved!"
            + Style.RESET_ALL
        )
    finally:
        os._exit(0)


__all__ = [
    "start_work",
    "stop_work",
]
