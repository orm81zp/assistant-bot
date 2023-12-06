from collections import UserDict
from datetime import datetime

from ..utils import get_birthdays_per_week
from ..constants import TEXT
from .record import Record


class AddressBook(UserDict):
    def has_data(self) -> bool:
        return len(self.data) > 0

    def add_record(self, contact: Record):
        self.data[contact.name.value] = contact

    def find(self, name) -> Record | None:
        return self.data.get(name, None)

    def find_all(self):
        output = ""
        for contact in self.data.values():
            output += f"{contact}\n"
        return output

    def delete(self, name):
        removed_contact = self.data.pop(name, None)
        return TEXT["CONTACT_DELETED"] if removed_contact else TEXT["CONTACT_NOT_FOUND"]

    def birthdays(self) -> str:
        contacts_with_birthdays = list()

        for name in self.data:
            contact: Record = self.data[name]

            if contact.birthday:
                d, m, y = list(map(lambda x: int(x), contact.birthday.value.split(".")))
                contacts_with_birthdays.append({"name": name, "birthday": datetime(y, m, d)})

        return get_birthdays_per_week(contacts_with_birthdays)


__all__ = ["AddressBook"]
