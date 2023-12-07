import pickle
from pathlib import Path
from colorama import Fore, Style
import os

from ..address_book import AddressBook
from ..exceptions import InputBotExseption

DUMP_FILE: Path | None = None
address_book: AddressBook | None = None

def start_work() -> AddressBook:
    global DUMP_FILE, address_book
    DUMP_FILE = Path(__file__).resolve().parent.parent / "assistant_data.bin"

    book = AddressBook()
    if DUMP_FILE.exists():
        with open(DUMP_FILE, "rb") as fh:
            book: AddressBook = pickle.load(fh)
            print(Fore.YELLOW + "Address Book restored!" + Style.RESET_ALL)
    
    address_book = book
    return address_book

def save_address_book(book: AddressBook):
    global DUMP_FILE
    if book.has_data() and DUMP_FILE:
        with open(str(DUMP_FILE), "wb") as fh:
            pickle.dump(book, fh)
            print(Fore.YELLOW + "Address Book saved!" + Style.RESET_ALL)

def stop_work():
    global address_book
    try:
        if address_book:
            save_address_book(address_book)
    except Exception:
        print(Fore.RED +"Unfortunately, Address Book could not be saved!" + Style.RESET_ALL)
    finally:
        os._exit(0)

def is_yes_prompt(msg = "Are you sure?"):
    user_input = input(f"{msg} (y or n) ")
    if not user_input:
        raise InputBotExseption

    user_input = user_input.strip().lower()
    return user_input in ["yes", "y"]

__all__ = [
    "start_work", 
    "stop_work",
    "is_yes_prompt", 
]
