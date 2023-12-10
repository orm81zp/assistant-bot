from colorama import Fore, Style

TEXT = {
    "WELCOME": "Welcome to" + Fore.YELLOW + " GoIT Assistant Bot!\n" + Style.RESET_ALL + "Type \"help\" to see all commands!\n",
    "INVALID_COMMAND": Fore.LIGHTBLACK_EX + "Invalid command. Type \"help\"." + Style.RESET_ALL,
    "NO_COMMAND": Fore.LIGHTBLACK_EX + "Please, enter a command to begin." + Style.RESET_ALL,
    "UNEXPECTED_EXCEPTION": Fore.RED + "Oops! Something went wrong!" + Style.RESET_ALL,
    "NOT_FOUND": Fore.LIGHTBLACK_EX + "Not found." + Style.RESET_ALL,
    "EXISTS": Fore.LIGHTBLACK_EX + "Already exists." + Style.RESET_ALL,
    "NO_DATA_TO_DISPLAY": Fore.LIGHTBLACK_EX + "There are no data to display." + Style.RESET_ALL,
    "BYE": Fore.BLACK + "Good bye!" + Style.RESET_ALL,
    "GREETING": "How can I help you?",
    "ENTER_COMMAND": "Enter a command: ",
}

__all__ = ["TEXT"]
