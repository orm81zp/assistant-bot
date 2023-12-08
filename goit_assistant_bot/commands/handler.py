from colorama import Fore, Style
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter

from ..address_book import AddressBook
from ..exceptions import InputBotExseption
from .commands_mapper import COMMANDS, COMMAND_VARIANTS

def show_help(possible_command: str):
    """Display help information by a command"""
    for command in COMMANDS:
        if possible_command in command["commands"]:
            varians = "|".join(command.get("commands", []))
            arguments = command.get("arguments", [])

            print(Fore.LIGHTBLACK_EX
                + varians
                + Style.RESET_ALL
                + Fore.BLUE
                + f" {" ".join(arguments)}"
                + Style.RESET_ALL
            )
            break

def get_prompt_input(message = "Enter a command: ", need_comp = True):
    """Prompts for user input and helps with auto-substitution of possible command options"""
    completer = WordCompleter(COMMAND_VARIANTS, ignore_case=True, sentence=True)
    user_input = None

    while True:
        if need_comp:
            user_input = prompt(message, completer=completer)
        else:
            user_input = prompt(message)

        if user_input:
            break

    return user_input


def parse_input(user_input: str | None):
    """Parses a user input to get a command and arguments"""
    if not user_input:
        raise InputBotExseption

    command_func = None
    cmd = None
    args = []

    if " --help" in user_input:
        user_input_list = user_input.split()
        if "--help" in user_input_list and len(user_input_list) == 2:
            user_input = user_input.replace(" --help", "")
            show_help(user_input_list[0])

    for command in COMMANDS:
        for potential_command in command["commands"]:
            raw_input = user_input.strip().lower()
            command_with_args = potential_command + " "
            found_with_args = raw_input.startswith(command_with_args)

            if potential_command == raw_input or found_with_args:
                cmd = potential_command
                command_func = command["func"]
                if found_with_args:
                    sting_args = user_input.replace(command_with_args, "")
                    args = sting_args.split()
                break

    return (cmd, command_func, args)

def commands_handler(book: AddressBook, user_data):
    """Calls a found command"""
    command_func, args = user_data

    if command_func:
        command_func(args, book)


__all__ = [
    "commands_handler",
    "parse_input",
    "get_prompt_input"
]
