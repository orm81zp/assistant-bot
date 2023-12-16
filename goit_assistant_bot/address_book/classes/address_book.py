from collections import UserDict, defaultdict
from prettytable import PrettyTable, ALL
from ..utils import (
    get_birthdays_per_week,
    generate_uuid,
    is_yes_prompt,
    print_message,
)
from ..constants import (
    NOT_FOUND,
    EXISTS,
    DELETED,
    UPDATED,
    ADDED,
    EQUAL,
    TABLE_MAX_WIDTH,
    TABLE_MIN_WIDTH,
)
from ..decorators import confirm_prompt
from .record import Record
from .note import Note


not_found_message = print_message(NOT_FOUND)
exists_message = print_message(EXISTS)
deleted_message = print_message(DELETED)
added_message = print_message(ADDED)
updated_message = print_message(UPDATED)
equal_message = print_message(EQUAL)


class AddressBook(UserDict):
    __note_uuid = 1

    def __init__(self):
        super().__init__({"contacts": {}, "notes": []})

    # own methods
    def get_note_uuid(self):
        return self.__note_uuid

    def find(self, name) -> Record | None:
        for contact in self.data["contacts"].values():
            if contact.name.value == name:
                return contact
        return None

    def find_with_key(self, name) -> tuple[str, Record] | tuple[None, None]:
        for key, contact in self.data["contacts"].items():
            if contact.name.value == name:
                return (key, contact)
        return (None, None)

    def get_note(self, index) -> Note | None:
        for note in self.data["notes"]:
            if note.uuid == index:
                return note
        return None

    def get_note_by_content(self, content) -> Note | None:
        for note in self.data["notes"]:
            if note.content == content:
                return note
        return None

    def add_record(self, contact: Record):
        if isinstance(contact, Record):
            uuid = generate_uuid()
            self.data["contacts"][uuid] = contact
        else:
            print("Must be Record instance.")

    # For contacts
    def add_contact(self, name):
        contact = self.find(name)
        if contact:
            exists_message("Contact")
        else:
            self.add_record(Record(name))
            added_message("Contact")

    def change_name(self, name, new_name):
        contact = self.find(name)
        if contact:
            if self.find(new_name):
                exists_message("Contact")
            else:
                contact.change_name(name, new_name)
        else:
            not_found_message("Contact")

    def show_all(self):
        contacts = self.data["contacts"].values()
        self._print_all_contacts(contacts)

    def show_contact(self, name):
        contact = self.find(name)
        if contact:
            print(contact)
        else:
            not_found_message("Contact")

    def search_contact(self, search_value):
        found_contacts = []
        search_value = search_value.lower()
        contacts = self.data["contacts"].values()

        for contact in contacts:
            potential_contact: Record = contact

            # searching by name
            if str(potential_contact.name).lower().find(search_value) > -1:
                found_contacts.append(potential_contact)
                continue
            # searching by phone number
            phones = potential_contact.phones
            if len(phones) > 0:
                for phone in phones:
                    if str(phone).find(search_value) > -1:
                        found_contacts.append(potential_contact)
                        continue
            # searching by birthday
            if potential_contact.birthday:
                if str(potential_contact.birthday).find(search_value) > -1:
                    found_contacts.append(potential_contact)
                    continue
            # searching by email
            if potential_contact.email:
                if str(potential_contact.email).lower().find(search_value) > -1:
                    found_contacts.append(potential_contact)
                    continue
            # searching by address
            if potential_contact.address:
                if str(potential_contact.address).lower().find(search_value) > -1:
                    found_contacts.append(potential_contact)
                    continue

        self._print_all_contacts(found_contacts)

    def _print_all_contacts(self, contacts: list[Record]):
        if len(contacts) > 0:
            table = PrettyTable(["Name", "Phones", "Birthday", "Email", "Address"])
            table.align = "l"
            table.max_width = 40
            table.min_width = TABLE_MIN_WIDTH

            for contact in contacts:
                table.add_row(
                    [
                        contact.name,
                        contact.get_phones(no_data_message="-"),
                        contact.birthday or "-",
                        contact.email or "-",
                        contact.address or "-",
                    ]
                )
            print(table)
        else:
            not_found_message("Contacts")

    @confirm_prompt("Existing contact will be deleted, continue?")
    def remove_contact(self, name):
        key, contact = self.find_with_key(name)
        if contact:
            is_removed = self.data["contacts"].pop(key, None)
            if is_removed is not None:
                deleted_message("Contact")
        else:
            not_found_message("Contact")

    # for birthday
    def add_birthday(self, name, birthday):
        contact = self.find(name)
        if contact:
            if contact.birthday:
                if is_yes_prompt("Existing birthday will be updated, continue?"):
                    contact.add_birthday(birthday)
            else:
                contact.add_birthday(birthday)
        else:
            contact = Record(name)
            if contact.add_birthday(birthday):
                self.add_record(contact)

    def show_birthday(self, name):
        contact = self.find(name)
        if contact:
            contact.show_birthday()
        else:
            not_found_message("Contact")

    def remove_birthday(self, name):
        contact = self.find(name)
        if contact:
            contact.remove_birthday()
        else:
            not_found_message("Contact")

    def birthdays(self, days_range=None):
        contacts = []
        for contact in self.data["contacts"].values():
            if contact.birthday:
                birthday = contact.get_birthday_datetime()
                print(birthday)
                contacts.append({"name": str(contact.name), "birthday": birthday})

        get_birthdays_per_week(contacts, days_range)

    # For phone
    def add_phone(self, name, phone):
        contact = self.find(name)
        if contact:
            contact.add_phone(phone)
        else:
            contact = Record(name)
            if contact.add_phone(phone):
                self.add_record(contact)

    def show_phone(self, name):
        contact = self.find(name)
        if contact:
            contact.show_phone()
        else:
            not_found_message("Contact")

    def change_phone(self, name, phone, new_phone):
        contact = self.find(name)
        if contact:
            contact.change_phone(phone, new_phone)
        else:
            not_found_message("Contact")

    def remove_phone(self, name, phone):
        contact = self.find(name)
        if contact:
            contact.remove_phone(phone)
        else:
            not_found_message("Contact")

    # For address
    def add_address(self, name, address):
        contact = self.find(name)
        if contact:
            if contact.address:
                if is_yes_prompt("Existing address will be updated, continue?"):
                    contact.add_address(address)
            else:
                contact.add_address(address)
        else:
            contact = Record(name)
            if contact.add_address(address):
                self.add_record(contact)

    def show_address(self, name):
        contact = self.find(name)
        if contact:
            contact.show_address()
        else:
            not_found_message("Contact")

    def remove_address(self, name):
        contact = self.find(name)
        if contact:
            contact.remove_address()
        else:
            not_found_message("Contact")

    # For email
    def add_email(self, name, email):
        contact = self.find(name)
        if contact:
            if contact.email:
                if is_yes_prompt("Existing email will be updated, continue?"):
                    contact.add_email(email)
            else:
                contact.add_email(email)
        else:
            contact = Record(name)
            if contact.add_email(email):
                self.add_record(contact)

    def show_email(self, name):
        contact = self.find(name)
        if contact:
            contact.show_email()
        else:
            not_found_message("Contact")

    def remove_email(self, name):
        contact = self.find(name)
        if contact:
            contact.remove_email()
        else:
            not_found_message("Contact")

    # For notes
    def add_note(self, content):
        note = self.get_note_by_content(content)
        if note:
            exists_message("A note with the same content")
            print("The note index is", note.uuid)
        else:
            new_note = Note(content, self.__note_uuid)
            self.data["notes"].append(new_note)
            self.__note_uuid += 1
            added_message("Note")

    def show_note(self, index):
        note = self.get_note(index)

        if note:
            table = PrettyTable(["Index", "Text", "Tags"])
            table.align = "l"
            table.max_width = TABLE_MAX_WIDTH
            table.min_width = TABLE_MIN_WIDTH
            table.add_row([note.uuid, note.get_content("-"), note.get_tags("-")])

            print(table)
        else:
            not_found_message("Note")

    def change_note(self, index, content):
        note = self.get_note(index)
        if note:
            note_exists = self.get_note_by_content(content)
            if note_exists:
                exists_message("A note with the same content")
                print("The note index is", note_exists.uuid)
            else:
                note.content = content
                updated_message("Note")
        else:
            not_found_message("Note")

    def search_note(self, search_value):
        search_value = search_value.lower()
        notes = []

        for note in self.data["notes"]:
            if str(note.content).lower().find(search_value) > -1:
                notes.append(note)

        self._print_all_notes(notes)

    def show_all_notes(self):
        self._print_all_notes(self.data["notes"])

    def _print_all_notes(self, notes: list[Note]):
        if len(notes) > 0:
            table = PrettyTable(["Index", "Text", "Tags"])
            table.align = "l"
            table.hrules = ALL
            table.max_width = TABLE_MAX_WIDTH
            table.min_width = TABLE_MIN_WIDTH

            index = 0
            for note in notes:
                table.add_row([note.uuid, note.get_content("-"), note.get_tags("-")])
                index += 1

            print(table)
        else:
            not_found_message("Notes")

    def show_notes_by_tag(self, tag):
        table = PrettyTable(["Index", "Text", "Tags"])
        table.align = "l"
        table.hrules = ALL
        table.max_width = TABLE_MAX_WIDTH
        table.min_width = TABLE_MIN_WIDTH

        for note in self.data["notes"]:
            if note.tag_exists(tag):
                table.add_row(
                    [
                        note.uuid,
                        note.get_content("-"),
                        note.get_tags("-"),
                    ]
                )

        if len(table.rows) > 0:
            print(table)
        else:
            not_found_message("Notes")

    @confirm_prompt("Existing note will be deleted, continue?")
    def remove_note(self, index):
        note = self.get_note(index)

        if note:
            self.data["notes"] = list(
                filter((lambda x: x.uuid != index), self.data["notes"])
            )
            deleted_message("Note")
        else:
            not_found_message("Note")

    # For tags
    def add_tag(self, index, tag):
        note = self.get_note(index)
        if note:
            note.add_tag(tag)
        else:
            not_found_message("Note")

    def show_tag(self, index):
        note = self.get_note(index)
        if note:
            print(note.get_tags())
        else:
            not_found_message("Note")

    @confirm_prompt("Existing tag will be deleted, continue?")
    def remove_tag(self, index, tag):
        note = self.get_note(index)
        if note:
            note.remove_tag(tag)
        else:
            not_found_message("Note")

    def show_all_tags(self):
        if len(self.data["notes"]) > 0:
            notes = defaultdict(list)

            for note in self.data["notes"]:
                for itag in note.tags:
                    notes[str(itag).lower()].append(str(note.uuid))

            if len(notes) > 0:
                table = PrettyTable(["Tags", "Note Index"])
                table.align = "l"
                table.hrules = ALL
                table.max_width = TABLE_MAX_WIDTH
                table.min_width = TABLE_MIN_WIDTH

                for k, v in notes.items():
                    table.add_row(
                        [
                            k,
                            ", ".join(v),
                        ]
                    )
                print(table)
            else:
                not_found_message("Tags")
        else:
            not_found_message("Notes")


__all__ = ["AddressBook"]
