from colorama import init
from .constants import TEXT
from .utils import start_work, stop_work
from .commands import commands_handler, parse_input, get_prompt_input
from .exceptions import InputBotExseption, UnexpectedException
from .address_book.exceptions import ValidationValueExseption
from .commands import EXIT_COMMANDS


def run_bot():
    """
    Entry point for running the program. Prompts the user for a command and executes it.
    """

    init()
    print(TEXT["WELCOME"])
    book = start_work()

    while True:
        try:
            user_input = get_prompt_input(TEXT["ENTER_COMMAND"])
            command, *user_data = parse_input(user_input)

            if command:
                commands_handler(book, user_data)
                if command in EXIT_COMMANDS:
                    break
            else:
                print(TEXT["INVALID_COMMAND"])
        except InputBotExseption:
            print(TEXT["NO_COMMAND"])
        except ValidationValueExseption as err:
            print(err.message)
        except UnexpectedException as err:
            print(err)
            print(TEXT["UNEXPECTED_EXCEPTION"])

    stop_work()


__all__ = ["run_bot"]
