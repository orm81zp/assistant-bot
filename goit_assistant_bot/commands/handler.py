from colorama import Fore, Style

from ..address_book import AddressBook
from ..exceptions import InputBotExseption
from .commands_mapper import COMMANDS

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

                break

    return (cmd, command, args)

def commands_handler(book: AddressBook, user_data):
    """Function calls a command or display a message a command not found"""
    command, args = user_data

    if command:
        command(args, book)
    else:
        print(Fore.RED + "Invalid command. Type \"help\" to see all commands!" + Style.RESET_ALL)


__all__ = ["commands_handler", "parse_input"]
