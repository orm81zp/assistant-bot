MENU = """
[Contact commands]
add-contact                     - used to add a new contact: "add-contact <name>"
search-contact                  - used to search contacts by name, birthday, email, phone, address (case-insensitive): "search_contact <search value>"
all-contacts | show-contacts    - used to display all contacts: "all-contacts"
change-contact-name             - used to change a contact name: "change-contact-name <name> <new name>"
remove-contact                  - used to remove a contact: "remove-contact <name>"

[Birthday commands]
add-birthday                    - used to add a birthday: "add-birthday <name> <birthday>"
show-birthday                   - used to display a birthday: "show-birthday <name>"
remove-birthday                 - used to remove a birthday: "remove-birthday <name>"
show-birthdays                  - used to display birthdays that will happen in coming days: "show-birthdays [days range]"

[Address commands]
add-address                     - used to add an address: "add-address <name> <address>"
show-address                    - used to display an address: "show-address <name>"
remove-address                  - used to remove an address: "remove-address <name>"

[Note commands]
add-note                        - used to add a note: "add-note <text>"
show-note                       - used to display a note: "show-note <note id>"
remove-note                     - used to remove a note: "remove-note <note id>"
all-notes | show-notes          - used to display all notes: "all-notes"
search-note                     - used to search notes by content (case-insensitive): "search-note <search value>"
search-note-by-tag              - used to display all notes found by a tag (case-insensitive, strict match): "search-note-by-tag <tag>"

[Tag commands]
add-tag                         - used to add a tag: "add-tag <note id> <tag>"
show-tag                        - used to display a tag: "show-tag <note id>"
remove-tag                      - used to remove a tag: "remove-tag <note id> <tag>"
all-tags | show-tags            - used to display all tags: "all-tags"

[Email commands]
add-email                       - used to add an email: "add-email <name> <email>"
show-email                      - used to display an email: "show-email <name>"
remove-email                    - used to remove an email: "remove-email <name>"

[Phone commands]
add-phone                       - used to add a phone: "add-phone <name> <phone>"
show-phone                      - used to display a phone: "show-phone <name>"
remove-phone                    - used to remove a phone: "remove-phone <name> <phone>"
change-phone                    - used to change a change: "change-phone <name> <old phone> <new phone>"

[Others commands]
hello | start                   - used to display a welcome message: "hello"
close | exit                    - used to close the program: "exit"
help                            - used to display all command: "help"

Types of argumets:
<required>       - required argument
[optional]       - optional argument

Validation rules:
<name>             - Contains from 1 to 30 characters. Example: Max
<address>          - Contains from 10 to 50 characters. Example: 3944 D Street
<email>            - Must be a correct email address. Example: max101@gmail.com
<phone>            - begins with + and consist of 12 digits. Example: +380630000001
<note id>          - Must be a number, starts from 0
<tag>              - Contains from 1 to 15 characters
<text>             - Contains from 10 to 100 characters
<birthday>         - Contains numbers separated by a dot in the following format DD.MM.YYYY. Example: 24.06.2001
[days range]       - must be number. Example: 14
"""

__all__ = ["MENU"]
