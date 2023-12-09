from colorama import Fore, Style

TEXT = {
    "DELETED": Fore.GREEN + "Deleted." + Style.RESET_ALL,
    "ADDED": Fore.GREEN + "Added." + Style.RESET_ALL,
    "UPDATED": Fore.GREEN + "Updated." + Style.RESET_ALL,
    "EXISTS": Fore.LIGHTBLACK_EX +"Already exists." + Style.RESET_ALL,
    "EQUAL": Fore.LIGHTBLACK_EX +"Are the same." + Style.RESET_ALL,
    "NOT_FOUND": Fore.LIGHTBLACK_EX + "Not found." + Style.RESET_ALL,
    "NO_DATA_TO_DISPLAY": Fore.LIGHTBLACK_EX + "There are no data to display." + Style.RESET_ALL,
    "PHONE_VALIDATION": Fore.RED + "Phone number failed validation." + Fore.LIGHTBLACK_EX + " Type \"help\" to see a hint" + Style.RESET_ALL,
    "NAME_VALIDATION": Fore.RED + "Name failed validation. " + Fore.LIGHTBLACK_EX + " Type \"help\" to see a hint" + Style.RESET_ALL,
    "BIRTHDAY_VALIDATION": Fore.RED + "Birthday failed validation." + Fore.LIGHTBLACK_EX + " Type \"help\" to see a hint" + Style.RESET_ALL,
    "BIRTHDAY_IN_THE_FUTURE": Fore.RED + "Birthday failed validation." + Fore.LIGHTBLACK_EX +  " Birthday can't be in the future " + Style.RESET_ALL,
    "EMAIL_VALIDATION": Fore.RED + "Email failed validation." + Fore.LIGHTBLACK_EX + " Type \"help\" to see a hint" + Style.RESET_ALL,
    "ADDRESS_VALIDATION": Fore.RED + "Address failed validation." + Fore.LIGHTBLACK_EX + " Type \"help\" to see a hint" + Style.RESET_ALL,
    "NOTE_VALIDATION": Fore.RED + "Note failed validation. " + Fore.LIGHTBLACK_EX + " Type \"help\" to see a hint" + Style.RESET_ALL,
    "TAG_VALIDATION": Fore.RED + "Tag failed validation. " + Fore.LIGHTBLACK_EX + " Type \"help\" to see a hint" + Style.RESET_ALL,
}

__all__ = ["TEXT"]
