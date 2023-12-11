from colorama import Fore, Style
from ..constants import TEXT
from .commands import COMMANDS, ARGUMET_TYPES, VALIDATION_RULES


def print_rules(rules=None):
    """
    Shows validation rules information.

    Parameters:
        rules (list[dict]): list of rules

    Returns: None
    """

    if not rules:
        rules = VALIDATION_RULES

    print(Fore.YELLOW + "Validation rules:" + Style.RESET_ALL)
    for k, v in rules.items():
        print(f"{k:<25} - {v}")


def print_argument_types(types=None):
    """
    Shows argument types information.

    Parameters:
        types (list[dict]): list of types

    Returns: None
    """

    if not types:
        types = ARGUMET_TYPES

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
        commands_string = " | ".join(commands)
        arguments_string = f" {" ".join(command["arguments"])}" if len(command["arguments"]) > 0 else ""
        description = command["description"]
        if cmd:
            if cmd in commands:
                cmd_found = True
                rules = command.get("rules", None)
                description += f": {Fore.GREEN + commands[0] + Style.RESET_ALL}{Fore.BLUE + arguments_string + Style.RESET_ALL}"
                output += f"{Fore.GREEN + commands_string + Style.RESET_ALL}\n- {description}\n"
                print(output)

                if rules:
                    print_rules(rules)
                    break
        else:
            description += f": {commands[0]}{arguments_string}"
            output += f"{commands_string:<25} - {description}\n"

    if cmd:
        if not cmd_found:
            print(Fore.LIGHTBLACK_EX + f"\"{cmd}\" not found, type \"help\" to see all commands" + Style.RESET_ALL)
    else:
        print(output)
        print_argument_types(ARGUMET_TYPES)
        print()
        print_rules(VALIDATION_RULES)


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


__all__ = [
    "show_hello",
    "show_help",
    "show_bye",
]
