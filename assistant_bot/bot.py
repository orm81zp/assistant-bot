from .utils import parse_input, init_address_book, save_address_book
from .commands import commands_handler, goodbye
from .exceptions import InputBotExseption
from .constants import EXIT_COMMANDS


def run_bot():
    print("Welcome to the assistant bot!")
    print("Type \"help\" to see all commands!\n")
    book = init_address_book()

    while True:
        try:
            user_input = input("Enter a command: ")
            command, *args = parse_input(user_input)

            if command in EXIT_COMMANDS:
                save_address_book(book)
                goodbye()
                break
            else:
                commands_handler(command, book, args)
        except InputBotExseption:
            print("Please, enter a command to begin.")
        except Exception as err:
            print("Oops! Something went wrong.", err)

__all__ = ["run_bot"]
