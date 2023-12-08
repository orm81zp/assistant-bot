from ..constants import EXIT_COMMANDS
from .commands import (
    add_phone,
    remove_phone,
    change_phone,
    show_phone,
    show_all,
    add_birthday,
    show_birthday,
    birthdays,
    remove_contact,
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
    show_notes_by_tag,
    remove_address,
    remove_birthday,
    remove_email,
)

COMMANDS = [
    {
        "commands": ["hello", "start", "hi"],
        "command": show_hello,
    },
    {
        "commands": ["help", "commands", "need help", "info"],
        "command": show_menu,
    },
    {
        "commands": ["add-contact", "add contact", "new contact", "create contact", "add phone", "add"],
        "command": add_phone,
    },
    {
        "commands":["all-contacts", "all contacts", "show contacts","show address book","show all book", "show all", "show contacts", "all"],
        "command": show_all,
    },
    {
        "commands": ["show-phone", "show phone", "get phone", "phone"],
        "command": show_phone,
    },
    {
        "commands": ["change-phone", "change contact", "change phone", "change number", "update phone", "update number", "update contact"],
        "command": change_phone,
    },
    {
        "commands": ["remove-phone", "delete number", "remove phone"],
        "command": remove_phone,
    },
    {
        "commands": ["add-birthday", "add birthday", "new birthday", "create birthday"],
        "command": add_birthday,
    },
    {
        "commands": ["show-birthday", "show birthday", "birth day", "birthday"],
        "command": show_birthday,
    },
    {
        "commands": ["remove-birthday", "remove birthday", "delete birthday"],
        "command": remove_birthday,
    },
    {
        "commands":["birthdays", "show-birthdays", "show birthdays", "all birthdays", "get birthdays"],
        "command": birthdays,
    },
    {
        "commands": ["add-email", "add email", "new email", "create email"],
        "command": add_email,
    },
    {
        "commands": ["show-email", "show email", "get email", "email"],
        "command": show_email,
    },
    {
        "commands": ["remove-email", "remove email", "delete email"],
        "command": remove_email,
    },
    {
        "commands": ["add-address", "add address", "new address", "create address"],
        "command": add_address,
    },
    {
        "commands": ["show-address", "show address", "get address", "address"],
        "command": show_address,
    },
    {
        "commands": ["remove-address", "remove address", "delete address"],
        "command": remove_address,
    },
    {
        "commands": ["add-note", "add note", "create note", "new note"],
        "command": add_note,
    },
    {
        "commands": ["show-note", "get note", "note"],
        "command": show_note,
    },
    {
        "commands": ["remove-note", "remove note", "delete note"],
        "command": remove_note,
    },
    {
        "commands": ["all-notes", "show notes", "all notes", "show all notes", "get notes", "notes"],
        "command": show_all_notes,
    },
    {
        "commands": ["show-for-tag", "show for tag", "show notes by tag", "show notes for tag", "notes by tag", "notes for tag", "by tag"],
        "command": show_notes_by_tag,
    },
    {
        "commands": ["add-tag", "add tag", "create tag", "new tag"],
        "command": add_tag,
    },
    {
        "commands": ["remove-tag", "delete tag", "remove tag"],
        "command": remove_tag,
    },
    {
        "commands": ["all-tags", "all tags", "show all tags", "tags"],
        "command": show_all_tags,
    },
    {
        "commands": ["show-tag", "show tag", "get tag", "tag"],
        "command": show_tag,
    },
    {
        "commands": ["remove-contact", "remove contact", "delete contact", "delete-contact", "delete record", "remove record"],
        "command": remove_contact,
    },
    {
        "commands": EXIT_COMMANDS,
        "command": show_bye,
    },
]
