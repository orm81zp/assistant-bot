from colorama import Fore, Style

from ..address_book import AddressBook
from ..exceptions import InputBotExseption
from ..constants import EXIT_COMMANDS
from .commands import (
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

COMMANDS = [
    {
        "commands":["hello",'hi','start'],
        "command": show_hello,
    },
    {
        "commands":['add contact','new contact','create contact', "add"],
        "command": add_phone,
    },
    {
        "commands":['show contacts','show address book','show all book', "show all", "all"],
        "command": show_all,
    },
    {
        "commands":['show phone','phone','get phone'],
        "command": show_phone,
    },
    {
        "commands":['change contact','change phone','change number', "update phone", "update number", "update contact", "change", "update"],
        "command": change_phone,
    },
    {
        "commands":['delete number','remove phone','remove', "delete"],
        "command": remove_phone,
    },
    {
        "commands":['help','commands','need help', "info"],
        "command": show_menu,
    },
    {
        "commands":['add birthday','add-birthday','new birthday'],
        "command": add_birthday,
    },
    {
        "commands":['show birthday','show-birthday','birthday', "birth day"],
        "command": show_birthday,
    },
    {
        "commands":['birthdays','show-birthdays','show birthdays', "all birthdays", "get birthdays"],
        "command": birthdays,
    },
    {
        "commands":['remove contact','remove-contact','delete contact', "delete-contact", "delete record", "remove record"],
        "command": remove_contact,
    },
    {
        "commands": EXIT_COMMANDS,
        "command": show_bye,
    },
]

def parse_input(user_input: str | None):
    """Function parse a user input to get a command and possibleits arguments"""
    if not user_input:
        raise InputBotExseption

    command = None
    cmd = None
    args = []

    for command_sample in COMMANDS:
        for potential_command in command_sample["commands"]:
            raw_input = user_input.strip().lower()
            command_with_args = potential_command + " "
            found_with_args = raw_input.startswith(command_with_args)
            if potential_command == raw_input or found_with_args:
                cmd = potential_command
                command = command_sample["command"]
                if found_with_args:
                    sting_args = user_input.replace(command_with_args, "")
                    args = sting_args.split()

    return (cmd, command, args)

def commands_handler(book: AddressBook, user_data):
    """Function calls a command or display a message a command not found"""
    command, args = user_data

    if command:
        command(args, book)
    else:
        print(Fore.RED + "Invalid command. Type \"help\" to see all commands!" + Style.RESET_ALL)

def goodbye():
    """Function says Bye"""
    print(show_bye())


__all__ = ["commands_handler", "goodbye", "parse_input"]
