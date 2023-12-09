from colorama import Fore, Style
from .commands import COMMANDS

def get_validation_message(cmd):
    """Returns a validation message with the expected arguments by a command. Prints an example of the use"""
    output = Fore.RED + "Validation Error" + Style.RESET_ALL

    for command in COMMANDS:
        commands_list = command["commands"]
        if cmd in commands_list:
            commands_string = "|".join(commands_list)
            arguments = command["arguments"]
            arguments_string = " ".join(arguments)
            output = Fore.RED + f"Please give me {arguments_string} argument{"s" if len(arguments) > 1 else ""}. Type \"help {cmd}\" to see a hint." + Style.RESET_ALL + "\n"
            output += Fore.LIGHTBLACK_EX + f"How to use: {commands_string} {arguments_string}" + Style.RESET_ALL

    return output

__all__ = [
    "get_validation_message",
]
