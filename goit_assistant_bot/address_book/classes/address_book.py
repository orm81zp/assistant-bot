from collections import UserDict, defaultdict
from datetime import datetime
from colorama import Fore, Style
from prettytable import PrettyTable

from ..utils import get_birthdays_per_week
from ..constants import TEXT
from .record import Record
from .note import Note


class AddressBook(UserDict):
    def __init__(self):
        self.data = {
            "contacts": {},
            "notes": []
        }

    def has_data(self) -> bool:
        return len(self.data["contacts"]) > 0 or len(self.data["notes"]) > 0

    def add_record(self, contact: Record):
        self.data["contacts"][contact.name.value] = contact

    def add_note(self, note: Note):
        self.data["notes"].append(note)
        print(Fore.GREEN + TEXT["NOTE_ADDED"] + Style.RESET_ALL)

    def add_tag(self, index: int, tag: str):
        note = self.find_note(index)
        if note:
            note.add_tag(tag)

    def show_tag(self, index: int):
        note = self.find_note(index)
        if note:
            table = PrettyTable()
            table.field_names = ["Index", "Text", "Tags"]
            table.align = 'l'
            table.add_row([
                index,
                note.get_content("-"),
                note.get_tags("-")

            ])
            print(table)

    def remove_tag(self, index: int, tag: str):
        note = self.find_note(index)
        if note:
            note.remove_tag(tag)

    def find(self, name) -> Record | None:
        return self.data["contacts"].get(name, None)

    def find_note(self, index) -> Note | None:
        try:
            note = self.data["notes"][index]
            return note
        except IndexError:
            print(Fore.LIGHTBLACK_EX + TEXT["NOTE_NOT_FOUND"] + Style.RESET_ALL)
            return None

    def find_all(self):
        if len(self.data["contacts"]) > 0:
            table = PrettyTable()
            table.field_names = ['Name', 'Phones', 'Birthday', 'Email', 'Address']
            table.align = 'l'
            for contact in self.data["contacts"].values():
                table.add_row([
                    contact.name,
                    contact.get_string_phones(no_data_message="-"),
                    contact.birthday or "-",
                    contact.email or "-",
                    contact.address or "-",
                ])
            print(table)
        else:
            print(Fore.LIGHTBLACK_EX + TEXT["NO_DATA_TO_DISPLAY"] + Style.RESET_ALL)

    def show_all_notes(self):
        if len(self.data["notes"]) > 0:
            table = PrettyTable()
            table.field_names = ['Index', 'Text', 'Tags']
            table.align = 'l'
            for index in range(len(self.data["notes"])):
                note = self.find_note(index)
                if note:
                    table.add_row([
                        index,
                        note.get_content("-"),
                        note.get_tags("-")
                    ])
            print(table)
        else:
            print(Fore.LIGHTBLACK_EX + TEXT["NO_DATA_TO_DISPLAY"] + Style.RESET_ALL)

    def show_notes_by_tag(self, tag):
        table = PrettyTable()
        table.field_names = ['Index', 'Text', "Tags"]
        table.align = 'l'

        has_data = False
        for index in range(len(self.data["notes"])):
            note = self.find_note(index)
            if note and note.find_tag(tag):
                table.add_row([
                    index,
                    note.get_content("-"),
                    note.get_tags("-"),
                ])
                if not has_data:
                    has_data = True

        if has_data:
            print(table)
        else:
            print(Fore.LIGHTBLACK_EX + TEXT["NO_DATA_TO_DISPLAY"] + Style.RESET_ALL)

    def show_all_tags(self):
        if len(self.data["notes"]) > 0:
            table = PrettyTable()
            table.field_names = ['Tags', 'Note Indexes']
            table.align = 'l'

            notes = defaultdict(list)
            for index in range(len(self.data["notes"])):
                note = self.find_note(index)
                if note:
                    for tag_index in range(len(note.tags)):
                        notes[str(note.tags[tag_index]).lower()].append(str(index))

            for k, v in notes.items():
                table.add_row([
                    k,
                    ', '.join(v),
                ])
            print(table)
        else:
            print(Fore.LIGHTBLACK_EX + TEXT["NO_DATA_TO_DISPLAY"] + Style.RESET_ALL)

    def delete(self, name):
        removed_contact = self.data["contacts"].pop(name, None)
        if removed_contact:
            print(Fore.GREEN + TEXT["CONTACT_DELETED"] + Style.RESET_ALL)
        else:
            print(Fore.LIGHTBLACK_EX + TEXT["CONTACT_NOT_FOUND"] + Style.RESET_ALL)

    def remove_note(self, index: int):
        note = self.find_note(index)

        if note:
            new_notes = []
            for note_index in range(len(self.data["notes"])):
                if note_index != index:
                    new_notes.append(self.data["notes"][note_index])

            self.data["notes"] = new_notes
            print(Fore.GREEN + TEXT["NOTE_DELETED"] + Style.RESET_ALL)
            return True

        print(Fore.LIGHTBLACK_EX + TEXT["NOTE_NOT_FOUND"] + Style.RESET_ALL)
        return False

    def show_note(self, index) -> Record | None:
        note = self.find_note(index)

        if note:
            table = PrettyTable()
            table.field_names = ['Index', 'Text', 'Tags']
            table.align = 'l'
            table.add_row([
                index,
                note.get_content("-"),
                note.get_tags("-")

            ])

            print(table)

    def birthdays(self, days_range = None):
        contacts_with_birthdays = []

        for name in self.data["contacts"]:
            contact: Record = self.data["contacts"][name]

            if contact.birthday:
                d, m, y = list(map(lambda x: int(x), contact.birthday.value.split(".")))
                contacts_with_birthdays.append({"name": name, "birthday": datetime(y, m, d)})

        get_birthdays_per_week(contacts_with_birthdays, days_range)


__all__ = ["AddressBook"]
