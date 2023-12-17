from colorama import Fore, Style
from .commands import COMMANDS


def get_validation_message(cmd):
    """
    Returns a validation message with the expected arguments for a command.

    Parameters:
        cmd (str): a command

    Returns:
        output (str): validation message
    """

    output = (
        Fore.RED
        + 'Validation Error. Type "help {cmd}" to see a hint.'
        + Style.RESET_ALL
    )

    for command in COMMANDS:
        commands_list = command["commands"]
        if cmd in commands_list:
            commands_string = " | ".join(commands_list)
            arguments = command["arguments"]
            arguments_string = " ".join(arguments)
            output = (
                Fore.RED
                + f'Please give me {arguments_string}. Type "help {cmd}" to see a hint.'
                + Style.RESET_ALL
                + "\n"
            )
            output += (
                Fore.LIGHTBLACK_EX
                + f"How to use: {commands_string} {arguments_string}"
                + Style.RESET_ALL
            )

    return output


__all__ = [
    "get_validation_message",
]
