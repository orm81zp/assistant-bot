CMD_ADD_ADDRESS = "add-address"
CMD_SHOW_ADDRESS = "show-address"
CMD_REMOVE_ADDRESS = "remove-address"
CMD_ADD_CONTACT = "add-contact"
CMD_SEARCH_CONTACT = "search-contact"
CMD_SHOW_CONTACT = "show-contact"
CMD_CHANGE_CONTACT_NAME = "change-contact-name"
CMD_ALL_CONTACTS = "all-contacts"
CMD_REMOVE_CONTACT = "remove-contact"
CMD_ADD_BIRTHDAY = "add-birthday"
CMD_SHOW_BIRTHDAY = "show-birthday"
CMD_REMOVE_BIRTHDAY = "remove-birthday"
CMD_BIRTHDAYS = "birthdays"
CMD_ADD_EMAIL = "add-email"
CMD_SHOW_EMAIL = "show-email"
CMD_REMOVE_EMAIL = "remove-email"
CMD_ADD_PHONE = "add-phone"
CMD_SHOW_PHONE = "show-phone"
CMD_CHANGE_PHONE = "change-phone"
CMD_REMOVE_PHONE = "remove-phone"
CMD_ADD_NOTE = "add-note"
CMD_SHOW_NOTE = "show-note"
CMD_CHANGE_NOTE = "change-note"
CMD_SEARCH_NOTE = "search-note"
CMD_REMOVE_NOTE = "remove-note"
CMD_ALL_NOTES = "all-notes"
CMD_SEARCH_NOTE_BY_TAG = "search-note-by-tag"
CMD_ADD_TAG = "add-tag"
CMD_REMOVE_TAG = "remove-tag"
CMD_ALL_TAGS = "all-tags"
CMD_SHOW_TAG = "show-tag"
CMD_HELLO = "hello"
CMD_HELP = "help"
CMD_CLOSE = "close"
CMD_EXIT = "exit"

EXIT_COMMANDS = [CMD_CLOSE, CMD_EXIT]

ARG_NAME = "<name>"
ARG_NEW_NAME = "<new name>"
ARG_PHONE = "<phone>"
ARG_OLD_PHONE = "<old phone>"
ARG_NEW_PHONE = "<new phone>"
ARG_ADDRESS = "<address>"
ARG_EMAIL = "<email>"
ARG_NOTE_INDEX = "<note index>"
ARG_TAG = "<tag>"
ARG_TEXT = "<text>"
ARG_BIRTHDAY = "<birthday>"
ARG_SEARCH_VALUE = "<search value>"
ARG_DAYS_RANGE = "[days range]"
ARG_COMMAND_NAME = "[command name]"

VALIDATION_RULES = {
    ARG_NAME: 'equivalent to "a-zA-Z0-9_.-", no spaces. Example: Max, J.Brain, Tom-1',
    ARG_NEW_NAME: f"same as for {ARG_NAME}",
    ARG_PHONE: "begins with + and consist of 12 digits. Example: +380630000001",
    ARG_OLD_PHONE: f"same as for {ARG_PHONE}",
    ARG_NEW_PHONE: f"same as for {ARG_PHONE}",
    ARG_ADDRESS: "from 10 to 100 characters. Example: 3944 D Street",
    ARG_EMAIL: "a valid email address. Example: max101@gmail.com",
    ARG_NOTE_INDEX: "an existing index of a note, starts from 1",
    ARG_TAG: 'from 1 to 15 word characters, equivalent to "a-zA-Z0-9_", no spaces. Example: shopping',
    ARG_TEXT: "from 10 to 500 characters",
    ARG_BIRTHDAY: 'a valid date, equivalent to "DD.MM.YYYY", no future\'s date of birth. Example: 24.06.2001',
    ARG_SEARCH_VALUE: "case-insensitive world characters. Example: hello world",
    ARG_DAYS_RANGE: "(optional) a number of days (7 by default). Example: 14",
    ARG_COMMAND_NAME: "(optional) an existing command name. Example: add-phone",
}

ARGUMET_TYPES = {
    "<required>": "required argument",
    "[optional]": "optional argument",
}

COMMANDS = [
    {
        "commands": [CMD_ADD_CONTACT],
        "arguments": [ARG_NAME],
        "description": "used to add a new contact",
        "rules": {
            ARG_NAME: VALIDATION_RULES.get(ARG_NAME),
        },
    },
    {
        "commands": [CMD_SEARCH_CONTACT],
        "arguments": [ARG_SEARCH_VALUE],
        "description": "used to search contacts by name, birthday, email, phone, address (case-insensitive)",
        "rules": {
            ARG_SEARCH_VALUE: VALIDATION_RULES.get(ARG_SEARCH_VALUE),
        },
    },
    {
        "commands": [CMD_SHOW_CONTACT],
        "arguments": [ARG_NAME],
        "description": "used to display a contact",
        "rules": {
            ARG_NAME: VALIDATION_RULES.get(ARG_NAME),
        },
    },
    {
        "commands": [CMD_CHANGE_CONTACT_NAME],
        "arguments": [ARG_NAME, ARG_NEW_NAME],
        "description": "used to change a contact name",
        "rules": {
            ARG_NAME: VALIDATION_RULES.get(ARG_NAME),
            ARG_NEW_NAME: VALIDATION_RULES.get(ARG_NEW_NAME),
        },
    },
    {
        "commands": [CMD_ALL_CONTACTS],
        "arguments": [],
        "description": "used to display all contacts",
    },
    {
        "commands": [CMD_REMOVE_CONTACT],
        "arguments": [ARG_NAME],
        "description": "used to remove a contact",
        "rules": {
            ARG_NAME: VALIDATION_RULES.get(ARG_NAME),
        },
    },
    {
        "commands": [CMD_ADD_BIRTHDAY],
        "arguments": [ARG_NAME, ARG_BIRTHDAY],
        "description": "used to add a birthday",
        "rules": {
            ARG_NAME: VALIDATION_RULES.get(ARG_NAME),
            ARG_BIRTHDAY: VALIDATION_RULES.get(ARG_BIRTHDAY),
        },
    },
    {
        "commands": [CMD_SHOW_BIRTHDAY],
        "arguments": [ARG_NAME],
        "description": "used to display a birthday",
        "rules": {
            ARG_NAME: VALIDATION_RULES.get(ARG_NAME),
        },
    },
    {
        "commands": [CMD_REMOVE_BIRTHDAY],
        "arguments": [ARG_NAME],
        "description": "used to remove a birthday",
        "rules": {
            ARG_NAME: VALIDATION_RULES.get(ARG_NAME),
        },
    },
    {
        "commands": [CMD_BIRTHDAYS],
        "arguments": [ARG_DAYS_RANGE],
        "description": "used to display birthdays that will happen in coming days (7 days by default)",
        "rules": {
            ARG_DAYS_RANGE: VALIDATION_RULES.get(ARG_DAYS_RANGE),
        },
    },
    {
        "commands": [CMD_ADD_ADDRESS],
        "arguments": [ARG_NAME, ARG_ADDRESS],
        "description": "used to add an address",
        "rules": {
            ARG_NAME: VALIDATION_RULES.get(ARG_NAME),
            ARG_ADDRESS: VALIDATION_RULES.get(ARG_ADDRESS),
        },
    },
    {
        "commands": [CMD_SHOW_ADDRESS],
        "arguments": [ARG_NAME],
        "description": "used to display an address",
        "rules": {
            ARG_NAME: VALIDATION_RULES.get(ARG_NAME),
        },
    },
    {
        "commands": [CMD_REMOVE_ADDRESS],
        "arguments": [ARG_NAME],
        "description": "used to remove an address",
        "rules": {
            ARG_NAME: VALIDATION_RULES.get(ARG_NAME),
        },
    },
    {
        "commands": [CMD_ADD_EMAIL],
        "arguments": [ARG_NAME, ARG_EMAIL],
        "description": "used to add an email",
        "rules": {
            ARG_NAME: VALIDATION_RULES.get(ARG_NAME),
            ARG_EMAIL: VALIDATION_RULES.get(ARG_EMAIL),
        },
    },
    {
        "commands": [CMD_SHOW_EMAIL],
        "arguments": [ARG_NAME],
        "description": "used to display an email",
        "rules": {
            ARG_NAME: VALIDATION_RULES.get(ARG_NAME),
        },
    },
    {
        "commands": [CMD_REMOVE_EMAIL],
        "arguments": [ARG_NAME],
        "description": "used to remove an email",
        "rules": {
            ARG_NAME: VALIDATION_RULES.get(ARG_NAME),
        },
    },
    {
        "commands": [CMD_ADD_PHONE],
        "arguments": [ARG_NAME, ARG_PHONE],
        "description": "used to add a phone",
        "rules": {
            ARG_NAME: VALIDATION_RULES.get(ARG_NAME),
            ARG_PHONE: VALIDATION_RULES.get(ARG_PHONE),
        },
    },
    {
        "commands": [CMD_SHOW_PHONE],
        "arguments": [ARG_NAME],
        "description": "used to display a phone",
        "rules": {
            ARG_NAME: VALIDATION_RULES.get(ARG_NAME),
        },
    },
    {
        "commands": [CMD_CHANGE_PHONE],
        "arguments": [ARG_NAME, ARG_OLD_PHONE, ARG_NEW_PHONE],
        "description": "used to change a phone",
        "rules": {
            ARG_NAME: VALIDATION_RULES.get(ARG_NAME),
            ARG_PHONE: VALIDATION_RULES.get(ARG_PHONE),
            ARG_OLD_PHONE: VALIDATION_RULES.get(ARG_OLD_PHONE),
            ARG_NEW_PHONE: VALIDATION_RULES.get(ARG_NEW_PHONE),
        },
    },
    {
        "commands": [CMD_REMOVE_PHONE],
        "arguments": [ARG_NAME, ARG_PHONE],
        "description": "used to remove a phone",
        "rules": {
            ARG_NAME: VALIDATION_RULES.get(ARG_NAME),
            ARG_PHONE: VALIDATION_RULES.get(ARG_PHONE),
        },
    },
    {
        "commands": [CMD_ADD_NOTE],
        "arguments": [ARG_TEXT],
        "description": "used to add a note",
        "rules": {
            ARG_TEXT: VALIDATION_RULES.get(ARG_TEXT),
        },
    },
    {
        "commands": [CMD_SHOW_NOTE],
        "arguments": [ARG_NOTE_INDEX],
        "description": "used to display a note",
        "rules": {
            ARG_NOTE_INDEX: VALIDATION_RULES.get(ARG_NOTE_INDEX),
        },
    },
    {
        "commands": [CMD_CHANGE_NOTE],
        "arguments": [ARG_NOTE_INDEX, ARG_TEXT],
        "description": "used to change a note",
        "rules": {
            ARG_NOTE_INDEX: VALIDATION_RULES.get(ARG_NOTE_INDEX),
            ARG_TEXT: VALIDATION_RULES.get(ARG_TEXT),
        },
    },
    {
        "commands": [CMD_SEARCH_NOTE],
        "arguments": [ARG_SEARCH_VALUE],
        "description": "used to search notes by content (case-insensitive)",
        "rules": {
            ARG_SEARCH_VALUE: VALIDATION_RULES.get(ARG_SEARCH_VALUE),
        },
    },
    {
        "commands": [CMD_REMOVE_NOTE],
        "arguments": [ARG_NOTE_INDEX],
        "description": "used to remove a note",
        "rules": {
            ARG_NOTE_INDEX: VALIDATION_RULES.get(ARG_NOTE_INDEX),
        },
    },
    {
        "commands": [CMD_ALL_NOTES],
        "arguments": [],
        "description": "used to display all notes",
    },
    {
        "commands": [CMD_SEARCH_NOTE_BY_TAG],
        "arguments": [ARG_TAG],
        "description": "used to display all notes found by a tag (case-insensitive, strict match)",
        "rules": {
            ARG_TAG: VALIDATION_RULES.get(ARG_TAG),
        },
    },
    {
        "commands": [CMD_ADD_TAG],
        "arguments": [ARG_NOTE_INDEX, ARG_TAG],
        "description": "used to add a tag",
        "rules": {
            ARG_NOTE_INDEX: VALIDATION_RULES.get(ARG_NOTE_INDEX),
            ARG_TAG: VALIDATION_RULES.get(ARG_TAG),
        },
    },
    {
        "commands": [CMD_REMOVE_TAG],
        "arguments": [ARG_NOTE_INDEX, ARG_TAG],
        "description": "used to remove a tag (strict match)",
        "rules": {
            ARG_NOTE_INDEX: VALIDATION_RULES.get(ARG_NOTE_INDEX),
            ARG_TAG: VALIDATION_RULES.get(ARG_TAG),
        },
    },
    {
        "commands": [CMD_ALL_TAGS],
        "arguments": [],
        "description": "used to display all tags",
    },
    {
        "commands": [CMD_SHOW_TAG],
        "arguments": [ARG_NOTE_INDEX],
        "description": "used to display tags in a note",
        "rules": {
            ARG_NOTE_INDEX: VALIDATION_RULES.get(ARG_NOTE_INDEX),
        },
    },
    {
        "commands": [CMD_HELLO],
        "arguments": [],
        "description": "used to display a welcome message",
    },
    {
        "commands": [CMD_HELP],
        "arguments": [ARG_COMMAND_NAME],
        "description": "used to display information about all commands or a particular one",
    },
    {
        "commands": EXIT_COMMANDS,
        "arguments": [],
        "description": "used to close the program",
    },
]
