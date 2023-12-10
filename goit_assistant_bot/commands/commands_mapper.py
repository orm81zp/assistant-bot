from .commands_address import add_address, show_address, remove_address
from .commands_birthday import add_birthday, show_birthday, birthdays,remove_birthday
from .commands_contact import show_all, add_contact, show_contact, remove_contact, search_contact, change_contact_name
from .commands_email import add_email, show_email, remove_email
from .commands_general import show_hello, show_help, show_bye
from .commands_phone import add_phone, remove_phone, change_phone, show_phone
from .commands_note import (
    add_note,
    show_all_notes,
    remove_note,
    show_note,
    add_tag,
    remove_tag,
    show_all_tags,
    show_tag,
    search_note_by_tag,
    search_note,
    change_note,
)

from .commands import (
    CMD_ADD_CONTACT,
    CMD_CHANGE_CONTACT_NAME,
    CMD_SHOW_CONTACT,
    CMD_ALL_CONTACTS,
    CMD_REMOVE_CONTACT,
    CMD_SEARCH_CONTACT,
    CMD_ADD_ADDRESS,
    CMD_REMOVE_ADDRESS,
    CMD_SHOW_ADDRESS,
    CMD_ADD_BIRTHDAY,
    CMD_REMOVE_BIRTHDAY,
    CMD_SHOW_BIRTHDAY,
    CMD_BIRTHDAYS,
    CMD_ADD_EMAIL,
    CMD_REMOVE_EMAIL,
    CMD_SHOW_EMAIL,
    CMD_ADD_PHONE,
    CMD_CHANGE_PHONE,
    CMD_REMOVE_PHONE,
    CMD_SHOW_PHONE,
    CMD_ADD_NOTE,
    CMD_REMOVE_NOTE,
    CMD_SEARCH_NOTE_BY_TAG,
    CMD_SEARCH_NOTE,
    CMD_CHANGE_NOTE,
    CMD_SHOW_NOTE,
    CMD_ALL_NOTES,
    CMD_ADD_TAG,
    CMD_REMOVE_TAG,
    CMD_SHOW_TAG,
    CMD_ALL_TAGS,
    CMD_HELLO,
    CMD_HELP,
    EXIT_COMMANDS,
)

MAPPED_COMMANDS = [
    {
        "commands":[CMD_ADD_CONTACT],
        "func": add_contact,
    },
    {
        "commands":[CMD_SEARCH_CONTACT],
        "func": search_contact,
    },
    {
        "commands":[CMD_SHOW_CONTACT],
        "func": show_contact,
    },
    {
        "commands":[CMD_CHANGE_CONTACT_NAME],
        "func": change_contact_name,
    },
    {
        "commands":[CMD_ALL_CONTACTS],
        "func": show_all,
    },
    {
        "commands": [CMD_REMOVE_CONTACT],
        "func": remove_contact,
    },
    {
        "commands": [CMD_ADD_BIRTHDAY],
        "func": add_birthday,
    },
    {
        "commands": [CMD_SHOW_BIRTHDAY],
        "func": show_birthday,
    },
    {
        "commands": [CMD_REMOVE_BIRTHDAY],
        "func": remove_birthday,
    },
    {
        "commands":[CMD_BIRTHDAYS],
        "func": birthdays,
    },
    {
        "commands": [CMD_ADD_ADDRESS],
        "func": add_address,
    },
    {
        "commands": [CMD_SHOW_ADDRESS],
        "func": show_address,
    },
    {
        "commands": [CMD_REMOVE_ADDRESS],

        "func": remove_address,
    },
    {
        "commands": [CMD_ADD_NOTE],
        "func": add_note,
    },
    {
        "commands": [CMD_CHANGE_NOTE],
        "func": change_note,
    },
    {
        "commands": [CMD_SHOW_NOTE],
        "func": show_note,
    },
    {
        "commands":[CMD_SEARCH_NOTE],
        "func": search_note,
    },
    {
        "commands": [CMD_REMOVE_NOTE],
        "func": remove_note,
    },
    {
        "commands": [CMD_ALL_NOTES],
        "func": show_all_notes,
    },
    {
        "commands": [CMD_SEARCH_NOTE_BY_TAG],
        "func": search_note_by_tag,
    },
    {
        "commands": [CMD_ADD_TAG],
        "func": add_tag,
    },
    {
        "commands": [CMD_REMOVE_TAG],
        "func": remove_tag,
    },
    {
        "commands": [CMD_ALL_TAGS],
        "func": show_all_tags,
    },
    {
        "commands": [CMD_SHOW_TAG],
        "func": show_tag,
    },
    {
        "commands": [CMD_ADD_EMAIL],
        "func": add_email,
    },
    {
        "commands": [CMD_SHOW_EMAIL],
        "func": show_email,
    },
    {
        "commands": [CMD_REMOVE_EMAIL],
        "func": remove_email,
    },
    {
        "commands": [CMD_ADD_PHONE],
        "func": add_phone,
    },
    {
        "commands": [CMD_SHOW_PHONE],
        "func": show_phone,
    },
    {
        "commands": [CMD_CHANGE_PHONE],
        "func": change_phone,
    },
    {
        "commands": [CMD_REMOVE_PHONE],
        "func": remove_phone,
    },
    {
        "commands": [CMD_HELLO],
        "func": show_hello,
    },
    {
        "commands": [CMD_HELP],
        "func": show_help,
    },
    {
        "commands": EXIT_COMMANDS,
        "func": show_bye,
    },
]

# create variants commands only from mapped commands with functions
COMMAND_VARIANTS = set()

for i in MAPPED_COMMANDS:
    for command in i["commands"]:
        COMMAND_VARIANTS.add(command)

COMMAND_VARIANTS = list(COMMAND_VARIANTS)

__all__ = [
    "COMMAND_VARIANTS",
    "MAPPED_COMMANDS",
]
