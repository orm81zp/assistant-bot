import pickle
from pathlib import Path

from ..address_book import AddressBook
from ..exceptions import InputBotExseption

DUMP_FILE: Path | None = None

def init_address_book() -> AddressBook:
    global DUMP_FILE
    DUMP_FILE = Path(__file__).resolve().parent.parent / "assistant_data.bin"

    if DUMP_FILE.exists():
        with open(DUMP_FILE, "rb") as fh:
            address_book = pickle.load(fh)
            print("Address Book restored!")
            return address_book
    else:
        address_book = AddressBook()
        return address_book

def save_address_book(book: AddressBook):
    global DUMP_FILE
    if book.has_data() and DUMP_FILE:
        with open(str(DUMP_FILE), "wb") as fh:
            pickle.dump(book, fh)
            print("Address Book saved!")

def parse_input(user_input: str | None):
    if not user_input:
        raise InputBotExseption
    
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def is_yes_prompt(msg = "Are you sure?"):
    user_input = input(f"{msg} (y or n) ")
    if not user_input:
        raise InputBotExseption

    user_input = user_input.strip().lower()
    return user_input in ["yes", "y"]


__all__ = [
    "init_address_book", 
    "save_address_book", 
    "parse_input", 
    "is_yes_prompt", 
]
