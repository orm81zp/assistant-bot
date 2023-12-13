import os
import sys
import pickle
from pathlib import Path
from colorama import Fore, Style
from ..address_book.classes import AddressBook
from ..constants import TEXT

ADDRESS_BOOK: AddressBook | None = None
DUMP_FILE = None


def start_work() -> AddressBook:
    global ADDRESS_BOOK, DUMP_FILE
    default_file_name = "assistant_data.bin"
    DUMP_FILE = Path(default_file_name)

    argv = sys.argv[1:]
    if len(argv) == 1:
        file_name = Path(argv[0])
        if file_name.suffix in [".bin", ".data"]:
            DUMP_FILE = Path(file_name)
        else:
            print(
                Fore.LIGHTBLACK_EX
                + f'The file name must end with *.bin or *.data, "{default_file_name}" file will be used by default.'
                + Style.RESET_ALL
            )

    book = AddressBook()
    if DUMP_FILE.exists():
        try:
            with open(DUMP_FILE, "rb") as fh:
                book: AddressBook = pickle.load(fh)
                print(Fore.YELLOW + "\u2713 Contact book restored!" + Style.RESET_ALL)
        except Exception:
            print(
                Fore.RED
                + "\u02DF Oh! Something went wrong while restoring the contact book!"
                + Style.RESET_ALL
            )

    ADDRESS_BOOK = book
    return ADDRESS_BOOK


def save_address_book():
    global ADDRESS_BOOK, DUMP_FILE
    print(TEXT["SAVE"])

    if ADDRESS_BOOK:
        if DUMP_FILE:
            with open(DUMP_FILE, "wb") as fh:
                pickle.dump(ADDRESS_BOOK, fh)
                print(Fore.YELLOW + "\u2713 Contact book saved!" + Style.RESET_ALL)
        else:
            print(Fore.RED + "The dump file not found." + Style.RESET_ALL)
    else:
        print(Fore.RED + "\u02DF Contact book not found." + Style.RESET_ALL)


def save():
    try:
        save_address_book()
    except Exception:
        print(
            Fore.RED
            + "\u02DF Oh! Something went wrong while saving the contact book!"
            + Style.RESET_ALL
        )


def stop_work():
    save()
    os._exit(0)


__all__ = [
    "start_work",
    "stop_work",
    "save",
]
