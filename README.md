# GoIT Assistant Bot

## Description

A personal console bot assistant that helps you manage your contacts and notes.

## Requirements

Python >= 3.12

## Installation

### By GitHub

1. [Download ZIP](https://github.com/orm81zp/goit-assistant-bot) from GitHub
2. Extract
3. Install requirements
4. Run `test_run_bot.py`

### By pip

```
pip install goit-assistant-bot
```

## How to run

Using in the code

```
from goit-assistant-bot import run_bot

run_bot()
```

or directly from the terminal `run_bot` after installation from pip.

## Basic functionality

- Save contacts with names, addresses, phone numbers, email and birthdays to the contact book.
- Display a list of contacts whose birthday is a specified number of days from the current date.
- Check the correctness of the entered phone number and email when creating or editing a record and notify the user in case of incorrect entry.
- Search for contacts among contacts in the book.
- Edit and delete entries from the contact book.
- Keep notes with text information.
- Search by notes.
- Edit and delete notes.

All data (contacts, notes) are stored on the hard disk. Default dump file name is `assistant_data.bin`.
To specify a dump file send its name as a first argument of `run_bot`, for example `run_bot work_contacts.bin`. Acceptable extension is `.bin` or `.data`.
Data is saved after closing the programm by `exit` or `close` commands and restoring after running next time. The Assistant Bot can be restarted without losing data.

### Commands

```
add-contact                    - used to add a new contact: add-contact <name>
search-contact                 - used to search contacts by name, birthday, email, phone, address (case-insensitive): search-contact <search value>
show-contact                   - used to display a contact: show-contact <name>
change-contact-name            - used to change a contact name: change-contact-name <name> <new name>
all-contacts                   - used to display all contacts: all-contacts
remove-contact                 - used to remove a contact: remove-contact <name>
add-birthday                   - used to add a birthday: add-birthday <name> <birthday>
show-birthday                  - used to display a birthday: show-birthday <name>
remove-birthday                - used to remove a birthday: remove-birthday <name>
birthdays                      - used to display birthdays that will happen in coming days (7 days by default): birthdays [days range]
add-address                    - used to add an address: add-address <name> <address>
show-address                   - used to display an address: show-address <name>
remove-address                 - used to remove an address: remove-address <name>
add-email                      - used to add an email: add-email <name> <email>
show-email                     - used to display an email: show-email <name>
remove-email                   - used to remove an email: remove-email <name>
add-phone                      - used to add a phone: add-phone <name> <phone>
show-phone                     - used to display a phone: show-phone <name>
change-phone                   - used to change a phone: change-phone <name> <old phone> <new phone>
remove-phone                   - used to remove a phone: remove-phone <name> <phone>
add-note                       - used to add a note: add-note <text>
show-note                      - used to display a note: show-note <note index>
search-note                    - used to search notes by content (case-insensitive): search-note <search value>
remove-note                    - used to remove a note: remove-note <note index>
all-notes                      - used to display all notes: all-notes
search-note-by-tag             - used to display all notes found by a tag (case-insensitive, strict match): search-note-by-tag <tag>
add-tag                        - used to add a tag: add-tag <note index> <tag>
remove-tag                     - used to remove a tag (strict match): remove-tag <note index> <tag>
all-tags                       - used to display all tags: all-tags
show-tag                       - used to display tags in a note: show-tag <note index>
hello                          - used to display a welcome message: hello
help                           - used to display information about all commands or a particular one: help [command name]
close | exit                   - used to close the program: close

Types of argumets:
<required>                     - required argument
[optional]                     - optional argument

Validation rules:
<name>                         - contains from 1 to 30 characters. Example: Max
<new name>                     - Same as for <name>
<phone>                        - begins with + and consist of 12 digits. Example: +380630000001
<old phone>                    - Same as for <phone>
<new phone>                    - Same as for <phone>
<address>                      - contains from 10 to 100 characters. Example: 3944 D Street
<email>                        - must be a valid email address. Example: max101@gmail.com
<note index>                   - must be a number, starts from 1
<tag>                          - contains from 1 to 15 characters
<text>                         - contains from 10 to 500 characters
<birthday>                     - contains numbers separated by a dot in the following format DD.MM.YYYY. Example: 24.06.2001
<search value>                 - case-insensitive characters. Example: hello world
[days range]                   - (optional) must be number. Example: 14
[command name]                 - (optional) an existing command name. Example: add-phone
```

### Examples of the use some commands

### help

Used to display all commands: `help`.

To display information about a specific command and usage rules type `help [command name]`.

```
Enter a command: help add-birthday
add-birthday
- used to add a birthday: add-birthday <name> <birthday>

Validation rules:
<name>               - contains from 1 to 30 characters. Example: Max
<birthday>           - contains numbers separated by a dot in the following format DD.MM.YYYY. Example: 24.06.2001
```

### add-phone

Used to add a phone: `add-phone <name> <phone>`

```
Enter a command: add-phone John +380731112211
Phone number added.
```

### add-birthday

Used to add a birthday: `add-birthday <name> <birthday>`. Will be replaced if already exists.

```
Enter a command: add-birthday John 28.11.2001
Added.
```

### add-email

Used to add an email: `add-email <name> <email>`. Will be replaced if already exists.

### add-address

Used to add an address: `add-address <name> <address>`. Will be replaced if already exists.

### all-contacts

Used to display all contacts: `all-contacts`

```
Enter a command: all-contacts
+------+---------------+------------+-------+---------+
| Name | Phones        | Birthday   | Email | Address |
+------+---------------+------------+-------+---------+
| John | +380731112211 | 28.11.2001 | -     | -       |
+------+---------------+------------+-------+---------+

```

### remove-contact

Used to remove a contact: `remove-contact <name>`
You need to confirm with "yes" or "y".

```
Enter a command: remove-contact John
Existing contact will be deleted, continue? (yes/no) yes
Deleted.
```

### birthdays

Used to display birthdays that will happen in days range (7 days by default): `birthdays [days range]`

The example of the output with default days range:

```
Enter a command: birthdays
+-----------+----------+
| Weekday   | Contacts |
+-----------+----------+
| Wednesday | Maxima   |
+-----------+----------+
```

The example of the output with a particular days range:

```
Enter a command: birthdays 14
+-----------+----------+
| Weekday   | Contacts |
+-----------+----------+
| Thursday  | Erik     |
| Wednesday | Maxima   |
+-----------+----------+
```

### add-note

Used to add a note: `add-note <text>`

```
Enter a command: add-note Hello world! Let's study something!
Added.
```

### all-notes

Used to display all notes: `all-notes`

```
Enter a command: all-notes
+------------+-------------------------------------+------------+
| Index      | Text                                | Tags       |
+------------+-------------------------------------+------------+
| 1          | Hello world! Let's study something! | -          |
+------------+-------------------------------------+------------+
```

### close or exit

use `close` or `exit` to close the program.

```
Enter a command: exit
Good bye!
Saved!
```
