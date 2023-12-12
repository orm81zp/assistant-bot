from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from ..address_book.classes import AddressBook
from ..exceptions import InputBotExseption
from .commands_mapper import MAPPED_COMMANDS, COMMAND_VARIANTS


def get_prompt_input(message=">>> ", with_completer=True):
    """
    Gets user value from a terminal with completer

    Parameters:
        message (str): a welcome message for entering a command
        need_comp (bool): use or not a completer

    Returns:
        user_input (str): user input value
    """

    completer = WordCompleter(COMMAND_VARIANTS, ignore_case=True, sentence=True)
    user_input = None

    while True:
        if with_completer:
            user_input = prompt(message, completer=completer)
        else:
            user_input = prompt(message)

        if user_input:
            break

    return user_input


def parse_input(user_input: str | None):
    """
    Parses a user input and returns a command, a function and rest of arguments form the user input

    Parameters:
        user_input (str): user input

    Returns:
        cmd (str): a command
        command_func (function): a fcommand function
        args (list): rest of arguments for the user input
    """

    if not user_input:
        raise InputBotExseption

    command_func = None
    cmd = None
    args = []

    for command in MAPPED_COMMANDS:
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
    """
    Calls a command function

    Parameters:
        book (class AddressBook): an instance of AddressBook
        user_data (list):
            command_func (funtion): a command function
            args (list): rest of arguments form the user input

    Returns:
        None
    """

    command_func, args = user_data

    if command_func:
        command_func(args, book)


__all__ = ["commands_handler", "parse_input", "get_prompt_input"]
