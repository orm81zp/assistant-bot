from colorama import Fore, Style

TEXT = {
    "CONTACT_DELETED": "Contact deleted.",
    "CONTACT_ADDED": "Contact added.",
    "CONTACT_NOT_FOUND": "Contact not found.",
    "NO_DATA_TO_DISPLAY": "There are no data to display.",

    "PHONE_NUMBER_ADDED": "Phone number added.",
    "PHONE_VALIDATION": Fore.RED + "Phone number failed validation. " + Style.RESET_ALL + "Must begin with + and consist of 12 digits. " + Fore.BLUE +  "Example: +380630000001" + Style.RESET_ALL,
    "PHONE_NUMBER_NOT_FOUND": "Phone number not found.",
    "PHONE_NUMBER_UPDATED": "Phone number updated.",
    "PHONE_NUMBER_DELETED": "Phone number deleted.",
    "PHONE_NUMBER_EXISTS": "Phone number already exists. Use \"change <username> <phone>\" if you want to update it.",

    "NAME_UPDATED": "Name updated.",
    "NAMES_THE_SAME": "Names are the same.",
    "NAME_VALIDATION": Fore.RED + "Name failed validation. " + Style.RESET_ALL +  "Contains from 1 to 30 characters, equivalent to a-zA-Z0-9_.-" + Fore.BLUE + "Examples: Max, Israel-Nolan" + Style.RESET_ALL,

    "BIRTHDAY_ADDED": "Birthday added.",
    "BIRTHDAY_UPDATED": "Birthday updated.",
    "BIRTHDAY_DELETED": "Birthday deleted.",
    "BIRTHDAY_VALIDATION": Fore.RED + "Birthday failed validation. " + Style.RESET_ALL +  "Must be a valid date in DD.MM.YYYY format. " + Fore.BLUE + "Example: 24.10.2001" + Style.RESET_ALL,
    "BIRTHDAY_IN_THE_FUTURE": Fore.RED + "Birthday failed validation. " + Style.RESET_ALL +  "Birthday can't be in the future " + Style.RESET_ALL,
    "BIRTHDAY_NOT_FOUND": Fore.LIGHTBLACK_EX + "Birthday not found. " + Style.RESET_ALL + "Type " + Fore.BLUE + "add-birthday <username> <birthday>" + Style.RESET_ALL + " to add one.",

    "EMAIL_ADDED": "Email added.",
    "EMAIL_UPDATED": "Email updated.",
    "EMAIL_DELETED": "Email deleted.",
    "EMAIL_VALIDATION": Fore.RED + "Email failed validation. " + Style.RESET_ALL +  "Must be a valid email address. " + Fore.BLUE + "Example: dummy21@gmail.com" + Style.RESET_ALL,
    "EMAIL_NOT_FOUND": Fore.LIGHTBLACK_EX + "Email not found. " + Style.RESET_ALL + "Type " + Fore.BLUE + "add-email <username> <email>" + Style.RESET_ALL + " to add one.",

    "ADDRESS_ADDED": "Address added.",
    "ADDRESS_UPDATED": "Address updated.",
    "ADDRESS_DELETED": "Address deleted.",
    "ADDRESS_VALIDATION": Fore.RED + "Address failed validation. " + Style.RESET_ALL +  "Contains from 10 to 50 characters. " + Fore.BLUE + "Example: 3944 D Street" + Style.RESET_ALL,
    "ADDRESS_NOT_FOUND": Fore.LIGHTBLACK_EX + "Address not found. " + Style.RESET_ALL + "Type " + Fore.BLUE + "add-address <username> <address>" + Style.RESET_ALL + " to add one.",
    
    "NOTE_VALIDATION": Fore.RED + "Note failed validation. " + Style.RESET_ALL +  "Contains from 10 to 500 characters.",
    "TAG_VALIDATION": Fore.RED + "Tag failed validation. " + Style.RESET_ALL +  "Contains from 1 to 15 characters.",
    "TAG_REMOVED": "Tag deleted.",
    "TAG_NOT_FOUND": "Tag not found.",
    "TAG_ADDED": "Tag added.",
    "TAG_EXISTS": "Tag exists.",
    "NOTE_ADDED": "Note added.",
    "NOTE_NOT_FOUND": "Note not found.",
    "NOTE_DELETED": "Note deleted.",
}

__all__ = ["TEXT"]
