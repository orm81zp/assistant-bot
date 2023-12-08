from ..constants import EXIT_COMMANDS
from .commands import (
    add_contact,
    remove_contact,
    add_phone,
    remove_phone,
    change_phone,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
    show_hello,
    show_menu,
    show_bye,
    add_email,
    show_email,
    add_address,
    show_address,
    add_note,
    show_all_notes,
    remove_note,
    show_note,
    add_tag,
    remove_tag,
    show_all_tags,
    show_tag,
    search_note_by_tag,
    remove_address,
    remove_birthday,
    remove_email,
    search_contact,
    search_note,
    change_contact_name,
)

CONTACT_COMMANDS = [
    {
        "commands":["add-contact"],
        "arguments": ["<name>"],
        "func": add_contact,
    },
    {
        "commands":["search-contact"],
        "arguments": ["<search value>"],
        "func": search_contact,
    },
    {
        "commands":["change-contact-name"],
        "arguments": ["<name> <new name>"],
        "func": change_contact_name,
    },
    {
        "commands":["all-contacts", "show-contacts"],
        "arguments": [],
        "func": show_all,
    },
    {
        "commands": ["remove-contact"],
        "arguments": ["<name>"],
        "func": remove_contact,
    },
]

BIRTHDAY_COMMANDS = [
    {
        "commands": ["add-birthday"],
        "arguments": ["<name>", "<birthday>"],
        "func": add_birthday,
    },
    {
        "commands": ["show-birthday"],
        "arguments": ["<name>"],
        "func": show_birthday,
    },
    {
        "commands": ["remove-birthday"],
        "arguments": ["<name>"],
        "func": remove_birthday,
    },
    {
        "commands":["show-birthdays"],
        "arguments": [],
        "func": birthdays,
    },
]

ADDRESS_COMMANDS = [
    {
        "commands": ["add-address"],
        "arguments": ["<name>", "<address>"],
        "func": add_address,
    },
    {
        "commands": ["show-address"],
        "arguments": ["<name>"],
        "func": show_address,
    },
    {
        "commands": ["remove-address"],
        "arguments": ["<name>"],
        "func": remove_address,
    },
]

NOTE_COMMANDS = [
    {
        "commands": ["add-note"],
        "arguments": ["<text>"],
        "func": add_note,
    },
    {
        "commands": ["show-note"],
        "arguments": ["<note id>"],
        "func": show_note,
    },
    {
        "commands":["search-note"],
        "arguments": ["<search value>"],
        "func": search_note,
    },
    {
        "commands": ["remove-note"],
        "arguments": ["<note id>"],
        "func": remove_note,
    },
    {
        "commands": ["all-notes", "show-notes"],
        "arguments": [],
        "func": show_all_notes,
    },
    {
        "commands": ["search-note-by-tag"],
        "arguments": ["<tag>"],
        "func": search_note_by_tag,
    },
]

TAG_COMMANDS = [
    {
        "commands": ["add-tag"],
        "arguments": ["<note id>", "<tag>"],
        "func": add_tag,
    },
    {
        "commands": ["remove-tag"],
        "arguments": ["<note id>", "<tag>"],
        "func": remove_tag,
    },
    {
        "commands": ["all-tags", "show-tags"],
        "arguments": [],
        "func": show_all_tags,
    },
    {
        "commands": ["show-tag"],
        "arguments": ["<note id>"],
        "func": show_tag,
    },
]

EMAIL_COMMANDS = [
    {
        "commands": ["add-email"],
        "arguments": ["<name>", "<email>"],
        "func": add_email,
    },
    {
        "commands": ["show-email"],
        "arguments": ["<name>"],
        "func": show_email,
    },
    {
        "commands": ["remove-email"],
        "arguments": ["<name>"],
        "func": remove_email,
    },
]

PHONE_COMMANDS = [
    {
        "commands": ["add-phone"],
        "arguments": ["<name>", "<phone>"],
        "func": add_phone,
    },
    {
        "commands": ["show-phone"],
        "arguments": ["<name>"],
        "func": show_phone,
    },
    {
        "commands": ["change-phone"],
        "arguments": ["<name>", "<old phone>", "<new phone>"],
        "func": change_phone,
    },
    {
        "commands": ["remove-phone"],
        "arguments": ["<name>", "<phone>"],
        "func": remove_phone,
    },
]

GENERAL_COMMANDS = [
    {
        "commands": ["hello", "start"],
        "arguments": [],
        "func": show_hello,
    },
    {
        "commands": ["help"],
        "arguments": [],
        "func": show_menu,
    },
    {
        "commands": EXIT_COMMANDS,
        "arguments": [],
        "func": show_bye,
    },
]

COMMANDS = GENERAL_COMMANDS + CONTACT_COMMANDS + BIRTHDAY_COMMANDS + ADDRESS_COMMANDS + NOTE_COMMANDS + TAG_COMMANDS + EMAIL_COMMANDS + PHONE_COMMANDS 

COMMAND_VARIANTS = set()

for i in COMMANDS:
    for command in i["commands"]:
        COMMAND_VARIANTS.add(command)

COMMAND_VARIANTS = list(COMMAND_VARIANTS)

__all__ = [
    "COMMAND_VARIANTS",
    "COMMANDS",
]
