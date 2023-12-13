from colorama import Fore, Style

DELETED = "Deleted."
ADDED = "Added."
UPDATED = "Updated."
NOT_FOUND = "Not found."
EXISTS = "Already exists."
EQUAL = "Are the same."

TEXT = {
    "DELETED": Fore.GREEN + DELETED + Style.RESET_ALL,
    "ADDED": Fore.GREEN + ADDED + Style.RESET_ALL,
    "UPDATED": Fore.GREEN + UPDATED + Style.RESET_ALL,
    "EXISTS": Fore.LIGHTBLACK_EX + EXISTS + Style.RESET_ALL,
    "EQUAL": Fore.LIGHTBLACK_EX + EQUAL + Style.RESET_ALL,
    "NOT_FOUND": Fore.LIGHTBLACK_EX + NOT_FOUND + Style.RESET_ALL,
    "NO_DATA_TO_DISPLAY": Fore.LIGHTBLACK_EX + "No data to display." + Style.RESET_ALL,
    "PHONE_VALIDATION": Fore.RED
    + "Phone number failed validation."
    + Fore.LIGHTBLACK_EX
    + ' Type "help" or "help add-phone" to see a hint.'
    + Style.RESET_ALL,
    "NAME_VALIDATION": Fore.RED
    + "Name failed validation."
    + Fore.LIGHTBLACK_EX
    + ' Type "help" or "help add-contact" to see a hint'
    + Style.RESET_ALL,
    "BIRTHDAY_VALIDATION": Fore.RED
    + "Birthday failed validation."
    + Fore.LIGHTBLACK_EX
    + ' Type "help" or "help add-birthday" to see a hint.'
    + Style.RESET_ALL,
    "BIRTHDAY_IN_THE_FUTURE": Fore.RED
    + "Birthday failed validation."
    + Fore.LIGHTBLACK_EX
    + " The future's date of birth is not accepted."
    + Style.RESET_ALL,
    "EMAIL_VALIDATION": Fore.RED
    + "Email failed validation."
    + Fore.LIGHTBLACK_EX
    + ' Type "help" or "help add-email" to see a hint.'
    + Style.RESET_ALL,
    "ADDRESS_VALIDATION": Fore.RED
    + "Address failed validation."
    + Fore.LIGHTBLACK_EX
    + ' Type "help" or "help add-address" to see a hint.'
    + Style.RESET_ALL,
    "NOTE_VALIDATION": Fore.RED
    + "Note failed validation."
    + Fore.LIGHTBLACK_EX
    + ' Type "help" or "help add-note" to see a hint.'
    + Style.RESET_ALL,
    "TAG_VALIDATION": Fore.RED
    + "Tag failed validation. "
    + Fore.LIGHTBLACK_EX
    + ' Type "help" or "help add-tag" to see a hint.'
    + Style.RESET_ALL,
}


__all__ = [
    "TEXT",
    "DELETED",
    "ADDED",
    "UPDATED",
    "NOT_FOUND",
    "EXISTS",
    "EQUAL",
]
