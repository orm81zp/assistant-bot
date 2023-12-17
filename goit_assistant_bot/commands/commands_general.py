import os
from colorama import Fore, Style
from ..constants import TEXT
from .commands import COMMANDS, ARGUMENT_TYPES, VALIDATION_RULES


def print_argument_rules(rules: None | dict = None):
    """
    Shows validation rules of arguments.

    Parameters:
        rules (list[dict]): list of argument rules

    Returns: None
    """

    if not rules:
        rules = VALIDATION_RULES

    if rules and len(rules) > 0:
        print(Fore.YELLOW + "Validation rules:" + Style.RESET_ALL)
        for k, v in rules.items():
            print(f"{k:<25} - {v}")


def print_argument_types(types: None | dict = None):
    """
    Shows information of argument types.

    Parameters:
        types (list[dict]): list of argument types

    Returns: None
    """

    if not types:
        types = ARGUMENT_TYPES

    if types and len(types) > 0:
        print(Fore.YELLOW + "Types of argumets:" + Style.RESET_ALL)
        for k, v in types.items():
            print(f"{k:<25} - {v}")


def show_help(args, *_):
    """
    Shows information about all commands or a specific one if it was passed as an argument.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    cmd = str(args[0]).strip().lower() if len(args) > 0 else None
    output = ""

    cmd_found = False
    for command in COMMANDS:
        commands = command["commands"]
        arguments = command["arguments"]
        commands_string = " | ".join(commands)
        arguments_string = " " + " ".join(arguments)

        description = command["description"]

        # show a help for a particular command
        if cmd:
            if cmd in commands:
                cmd_found = True
                description += (
                    ": "
                    + Fore.GREEN
                    + commands[0]
                    + Style.RESET_ALL
                    + arguments_string
                )

                print(
                    Fore.GREEN
                    + commands_string
                    + Style.RESET_ALL
                    + "\n- "
                    + description
                )

                # collect and print rules of a command
                rules = {}
                for argument in arguments:
                    if argument in VALIDATION_RULES:
                        rules[argument] = VALIDATION_RULES[argument]

                if len(rules) > 0:
                    print()
                    print_argument_rules(rules)
                    break
        else:
            description += ": " + commands[0] + arguments_string
            output += f"{commands_string:<25} - {description}\n"

    if cmd:
        if not cmd_found:
            print(
                Fore.LIGHTBLACK_EX
                + f'"{cmd}" not found, type "help" to see all commands'
                + Style.RESET_ALL
            )
    else:
        print(output)
        print_argument_types()
        print()
        print_argument_rules()


def show_bye(*_):
    """
    Shows bye message.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    print(TEXT["BYE"])


def show_hello(*_):
    """
    Shows greeting message.

    Parameters:
        args (list): list of arguments
        book (AddressBook class): an AddressBook instance

    Returns: None
    """

    print(TEXT["GREETING"])


def save(*_):
    """
    Does nothing, the command is processed by a bot.
    """


def clear(*_):
    """Clear screen output."""
    os.system("clear")


__all__ = [
    "show_hello",
    "show_help",
    "show_bye",
    "save",
    "clear",
]
