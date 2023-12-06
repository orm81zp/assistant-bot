from ..address_book import AddressBook
from ..utils import is_yes_prompt
from .all_commands import (
    add_phone,
    remove_phone,
    change_phone,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
    remove_contact,
    show_hello,
    show_menu,
    show_bye,
)

def commands_handler(command, book: AddressBook, args):
    if command == "add":
        print(add_phone(args, book))
    elif command == "remove":
        print(remove_phone(args, book))
    elif command == "change":
        print(change_phone(args, book))
    elif command == "phone":
        print(show_phone(args, book))
    elif command == "all":
        print(show_all(book))
    elif command == "add-birthday":
        print(add_birthday(args, book))
    elif command == "show-birthday":
        print(show_birthday(args, book))
    elif command == "birthdays":
        print(birthdays(book))
    elif command == "remove-contact":
        if is_yes_prompt("Please confirm the deletion of the contact"):
            print(remove_contact(args, book))
    elif command == "hello":
        print(show_hello())
    elif command == "help":
        print(show_menu())
    else:
        print("Invalid command. Type \"help\" to see all commands!")

def goodbye():
    print(show_bye())


__all__ = ["commands_handler", "goodbye"]
