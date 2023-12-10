from collections import UserDict, defaultdict
from prettytable import PrettyTable, ALL
from ..utils import get_birthdays_per_week, generate_uuid
from ..constants import TEXT, TABLE_MAX_WIDTH, TABLE_MIN_WIDTH
from ..decorators import confirm_prompt
from .record import Record
from .note import Note

class AddressBook(UserDict):
    note_uuid = 1
    def __init__(self):
        self.data = {
            "contacts": {},
            "notes": []
        }


    def has_data(self) -> bool:
        return len(self.data["contacts"]) > 0 or len(self.data["notes"]) > 0


    def add_record(self, contact: Record):
        uuid = generate_uuid(contact.name.value)
        self.data["contacts"][uuid] = contact


    def add_contact(self, name):
        self.add_record(Record(name))
        print(TEXT["ADDED"])


    def add_note(self, content: str):
        note = Note(content, AddressBook.note_uuid)
        self.data["notes"].append(note)
        AddressBook.note_uuid += 1
        print(TEXT["ADDED"])

    def change_note(self, index, content):
        note = self.get_note(index)
        if note:
            note.content.value = content
            print(TEXT["UPDATED"])
        else:
            print(TEXT["NOT_FOUND"])

    def add_tag(self, index, tag):
        note = self.get_note(index)
        if note:
            note.add_tag(tag)


    def show_tag(self, index):
        note = self.get_note(index)
        if note:
            print(note.get_tags())
        else:
            print(TEXT["NO_DATA_TO_DISPLAY"])


    @confirm_prompt("Existing tag will be deleted, continue?")
    def remove_tag(self, index, tag):
        note = self.get_note(index)
        if note:
            note.remove_tag(tag)


    def find(self, name) -> Record | None:
        for contact in self.data["contacts"].values():
            if contact.name.value == name:
                return contact
        return None


    def get_note(self, index) -> Note | None:
        for note in self.data["notes"]:
            if note.uuid == index:
                return note
        return None


    def show_all(self, contacts: list[Record]):
        if len(contacts) > 0:
            table = PrettyTable(["Name", "Phones", "Birthday", "Email", "Address"])
            table.align = "l"
            table.max_width = 40
            table.min_width = TABLE_MIN_WIDTH

            for contact in contacts:
                table.add_row([
                    contact.name,
                    contact.get_phones(no_data_message="-"),
                    contact.birthday or "-",
                    contact.email or "-",
                    contact.address or "-",
                ])
            print(table)
        else:
            print(TEXT["NO_DATA_TO_DISPLAY"])


    def find_all(self):
        contacts = self.data["contacts"].values()
        self.show_all(contacts)


    def show_contact(self, name):
        contact = self.find(name)

        if contact:
            self.show_all([contact])


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

        self.show_all(found_contacts)


    def search_note(self, search_value):
        search_value = search_value.lower()
        notes = []

        for note in self.data["notes"]:
            if str(note.content).lower().find(search_value) > -1:
                notes.append(note)

        self.show_all_notes(notes)


    def show_all_notes(self, notes: list[Note]):
        if len(notes) > 0:
            table = PrettyTable(["Index", "Text", "Tags"])
            table.align = "l"
            table.hrules = ALL
            table.max_width = TABLE_MAX_WIDTH
            table.min_width = TABLE_MIN_WIDTH

            index = 0
            for note in notes:
                table.add_row([
                    note.uuid,
                    note.get_content("-"),
                    note.get_tags("-")
                ])
                index += 1

            print(table)
        else:
            print(TEXT["NO_DATA_TO_DISPLAY"])


    def find_all_notes(self):
        self.show_all_notes(self.data["notes"])


    def show_notes_by_tag(self, tag):
        table = PrettyTable(["Index", "Text", "Tags"])
        table.align = "l"
        table.hrules = ALL
        table.max_width = TABLE_MAX_WIDTH
        table.min_width = TABLE_MIN_WIDTH

        for note in self.data["notes"]:
            if note.tag_exists(tag):
                table.add_row([
                    note.uuid,
                    note.get_content("-"),
                    note.get_tags("-"),
                ])

        if len(table.rows) > 0:
            print(table)
        else:
            print(TEXT["NO_DATA_TO_DISPLAY"])


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
                    table.add_row([
                        k,
                        ", ".join(v),
                    ])
                print(table)
            else:
                print(TEXT["NO_DATA_TO_DISPLAY"])
        else:
            print(TEXT["NO_DATA_TO_DISPLAY"])


    @confirm_prompt("Existing contact will be deleted, continue?")
    def remove_contact(self, name):
        contact_key = None
        for key, contact in self.data["contacts"].items():
            if name == str(contact.name):
                contact_key = key
                break

        if contact_key:
            removed_contact = self.data["contacts"].pop(contact_key, None)
            if removed_contact is not None:
                print(TEXT["DELETED"])
        else:
            print(TEXT["NOT_FOUND"])


    @confirm_prompt("Existing note will be deleted, continue?")
    def remove_note(self, index):
        note = self.get_note(index)

        if note:
            self.data["notes"] = list(filter((lambda x: x.uuid != index), self.data["notes"]))
            print(TEXT["DELETED"])
            return True

        print(TEXT["NOT_FOUND"])
        return False


    def show_note(self, index):
        note = self.get_note(index)

        if note:
            table = PrettyTable(["Index", "Text", "Tags"])
            table.align = "l"
            table.max_width = TABLE_MAX_WIDTH
            table.min_width = TABLE_MIN_WIDTH
            table.add_row([
                note.uuid,
                note.get_content("-"),
                note.get_tags("-")
            ])

            print(table)
        else:
            print(TEXT["NOT_FOUND"])


    def birthdays(self, days_range = None):
        contacts = []
        for contact in self.data["contacts"].values():
            if contact.birthday:
                birthday = contact.get_birthday_datetime()
                print(birthday)
                contacts.append({"name": str(contact.name), "birthday": birthday})

        get_birthdays_per_week(contacts, days_range)


__all__ = ["AddressBook"]
