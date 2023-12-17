from colorama import init
from .constants import TEXT
from .utils import start_work, stop_work, save
from .address_book.exceptions import ValidationValueException
from .commands import commands_handler, parse_input, get_prompt_input
from .exceptions import InputBotExseption, UnexpectedException
from .commands import EXIT_COMMANDS, CMD_SAVE


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
                if command == CMD_SAVE:
                    save()
                elif command in EXIT_COMMANDS:
                    break
            else:
                print(TEXT["INVALID_COMMAND"])
        except InputBotExseption:
            print(TEXT["NO_COMMAND"])
        except ValidationValueException as err:
            print(err)
        except KeyboardInterrupt:
            print(TEXT["UNEXPECTED_EXIT"])
            stop_work()
        except UnexpectedException as err:
            print(err)
            print(TEXT["UNEXPECTED_EXCEPTION"])

    stop_work()


__all__ = ["run_bot"]
