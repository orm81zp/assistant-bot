from colorama import init
from colorama import Fore, Style

from .utils import start_work, stop_work
from .commands import commands_handler, parse_input
from .exceptions import InputBotExseption
from .address_book.exceptions import ValidationValueExseption
from .constants import EXIT_COMMANDS


def run_bot():
    init()

    print("Welcome to the assistant bot!")
    print('Type "help" to see commands!\n')
    book = start_work()

    while True:
        try:
            user_input = input("Enter a command: ")
            command, *user_data = parse_input(user_input)

            if command:
                commands_handler(book, user_data)

                if command in EXIT_COMMANDS:
                    break
            else:
                print(
                    Fore.LIGHTBLACK_EX
                    + 'Invalid command. Type "help" to see all commands!'
                    + Style.RESET_ALL
                )
        except InputBotExseption:
            print(
                Fore.LIGHTBLACK_EX
                + "Please, enter a command to begin."
                + Style.RESET_ALL
            )
        except ValidationValueExseption as err:
            print(err.message)
        except Exception as err:
            print(Fore.RED + f"Oops! Something went wrong, {err}" + Style.RESET_ALL)

    stop_work()


__all__ = ["run_bot"]
