from colorama import Fore, Style

TEXT = {
    "NOT_FOUND": Fore.LIGHTBLACK_EX + "Not found." + Style.RESET_ALL,
    "EXISTS": Fore.LIGHTBLACK_EX + "Already exists." + Style.RESET_ALL,
    "NO_DATA_TO_DISPLAY": Fore.LIGHTBLACK_EX + "There are no data to display." + Style.RESET_ALL,
    "BYE": "Good bye!",
    "GREETING": "How can I help you?",
}

__all__ = ["TEXT"]