# Assistant Bot

## Description

A personal console bot assistant that helps you manage your contacts and notes.

## Requirements

Python >= 3.12

## Installation

```
pip install assistant-bot
```

## How to run

```
from assistant_bot import run_bot

run_bot()
```

or directly from the terminal `assistant-bot`

## Basic functionality

- Save contacts with names, addresses, phone numbers, email and birthdays to the contact book.
- Display a list of contacts whose birthday is a specified number of days from the current date.
- Check the correctness of the entered phone number and email when creating or editing a record and notify the user in case of incorrect entry.
- Search for contacts among contacts in the book.
- Edit and delete entries from the contact book.
- Keep notes with text information.
- Search by notes.
- Edit and delete notes.

All data (contacts, notes) are stored on the hard disk in the package folder. Dump file name is `assistant_data.bin`.
The Assistant Bot can be restarted without losing data.

### Commands

```
add              - used to add a phone number: "add [name] [phone]"
remove           - used to remove a phone number: "remove [name] [phone]"
change           - used to change a phone number: "change [name] [old phone] [new phone]"
phone            - used to display phone numbers: "phone [name]"
all              - used to display all contacts: "all"
add-birthday     - used to add a birthday: "add-birthday [name] [birthday]"
show-birthday    - used to display a birthday: "show-birthday [name]"
birthdays        - used to display birthdays that will happen in the next week: "birthdays"
remove-contact   - used to remove a contact: "remove-contact [name]"
hello            - used to display a welcome message: "hello"
close or exit    - used to close the program: "exit"
help             - used to display available commands: "help"
```

### add

Used to add a phone number: `add [name] [phone]`

```
Enter a command: add John 0970000001
Phone number added.
Enter a command: add John 0630000001
Phone number added.
Enter a command: add Erik 0660000001
Phone number added.
```

### add-birthday

Used to add a birthday: `add-birthday [name] [birthday]`

```
Enter a command: add-birthday John 28.11.2001
Birthday added.
```

### show-birthday

Used to display a birthday: `show-birthday [name]`

```
Enter a command: show-birthday John
28.11.2001
```

### remove-contact

Used to remove a contact: `remove-contact [name]`
Considering that this is a not safe command, you need to confirm your intention with "yes" or "y".

```
Enter a command: remove-contact Erik
Are you sure you want to delete the contact (y or n)? y
Contact deleted
```

### all

Used to display all contacts: `all`

```
Enter a command: all
Contact name: John, phones: 0970000001; 0630000001

```

### change

Used to change a phone number: `change [name] [old phone] [new phone]`

```
Enter a command: change John 0630000001 0730000001
Phone number updated.

```

### phone

Used to display a phone number: `phone [name]`

```
Enter a command: phone John
0970000001, 0730000001
```

### remove

Used to remove a phone number: `remove [name] [phone]`

```
Enter a command: remove John 0970000001
Phone number deleted.
Enter a command: phone John
0730000001

```

### birthdays

Used to display birthdays that will happen in the next week: `birthdays`

The example of the output:

```
Monday: Bill Gates, Jill Valentine
Friday: Kim Kardashian, Jan Koum

```

Let's assume that today is 26.11.2023 (Sunday) and run the `birthdays` command. Just a small reminder that John's birthday is 28.11.2001.

```
Enter a command: birthdays
Tuesday: John
```

### close or exit

use `close` or `exit` to close the program.

```
Enter a command: exit
Good bye!
```
