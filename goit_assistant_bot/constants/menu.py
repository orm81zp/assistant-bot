MENU = """
add              - used to add a phone number: "add <name> <phone>"
remove           - used to remove a phone number: "remove <name> <phone>"
change           - used to change a phone number: "change <name> <old phone> <new phone>"
phone            - used to display phone numbers: "phone <name>"

all              - used to display all contacts: "all"

add-birthday     - used to add a birthday: "add-birthday <name> <birthday>"
show-birthday    - used to display a birthday: "show-birthday <name>"
birthdays        - used to display birthdays that will happen in the next week (7 days by default): "birthdays [days range]"

add-email        - used to add an email: "add-email <name> <email>"
show-email       - used to display an email: "show-email <name>"

add-address      - used to add an address: "add-address  <name> <address>"
show-address     - used to display an address : "show-address  <name>"

remove-contact   - used to remove a contact: "remove-contact <name>"
hello            - used to display a welcome message: "hello"
close or exit    - used to close the program: "exit"
help             - used to display available commands: "help"

Types of argumets:
<required>       - required argument
[optional]       - optional argument

Validation rules of arguments:
phone            - begins with + and consist of 12 digits. Example: +380630000001
birthday         - consists of numbers separated by a dot in the following format DD.MM.YYYY. Example: 24.06.2001
days range       - must be number
"""

__all__ = ["MENU"]
