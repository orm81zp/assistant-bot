import os
import sys
import pickle
from pathlib import Path
from colorama import Fore, Style
from ..address_book import AddressBook

DUMP_FILE_NAME = "assistant_data.bin"
DUMP_FILE: Path | None = None
ADDRESS_BOOK: AddressBook | None = None


def start_work() -> AddressBook:
    global DUMP_FILE, ADDRESS_BOOK, DUMP_FILE_NAME
    DUMP_FILE = Path(DUMP_FILE_NAME)

    argv = sys.argv[1:]
    if len(argv) == 1:
        file_name = Path(argv[0])
        if file_name.suffix in [".bin", ".data"]:
            DUMP_FILE = Path(file_name)
            DUMP_FILE_NAME = file_name
        else:
            print(
                Fore.LIGHTBLACK_EX
                + f'The file suffix must end with *.bin or *.data "{DUMP_FILE_NAME}" file is used by default'
                + Style.RESET_ALL
            )

    book = AddressBook()
    if DUMP_FILE.exists():
        with open(DUMP_FILE, "rb") as fh:
            book: AddressBook = pickle.load(fh)
            print(Fore.LIGHTBLACK_EX + "Restored!" + Style.RESET_ALL)

    ADDRESS_BOOK = book
    return ADDRESS_BOOK


def save_address_book(book: AddressBook):
    global DUMP_FILE
    if book and DUMP_FILE:
        with open(str(DUMP_FILE), "wb") as fh:
            pickle.dump(book, fh)
            print(Fore.LIGHTBLACK_EX + "Saved!" + Style.RESET_ALL)


def stop_work():
    global ADDRESS_BOOK
    try:
        if ADDRESS_BOOK:
            save_address_book(ADDRESS_BOOK)
    except Exception:
        print(
            Fore.RED
            + "Oops! Something went wrong, data not be saved!"
            + Style.RESET_ALL
        )
    finally:
        os._exit(0)


def is_yes_prompt(msg="Please confirm"):
    user_input = input(f"{msg} (yes/no) ")
    user_input = user_input.strip().lower()

    return user_input in ["yes", "y"]


__all__ = [
    "start_work",
    "stop_work",
    "is_yes_prompt",
]
