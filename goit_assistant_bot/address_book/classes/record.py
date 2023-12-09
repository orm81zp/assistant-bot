from colorama import Fore, Style
from ..constants import TEXT
from ..utils import print_diff
from ..decorators import confirm_prompt
from .name import Name
from .phone import Phone
from .birthday import Birthday
from .email import Email
from .address import Address

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None

    def get_string_phones(self, delimeter = ', ', no_data_message = "") -> str:
        return delimeter.join([phone.value for phone in self.phones]) if len(self.phones) > 0 else no_data_message

    def get_phone(self, phone_number) -> Phone | None:
        for phone in self.phones:
            if str(phone) == phone_number:
                return phone

        return None

    def add_phone(self, phone_number):
        phone = self.get_phone(phone_number)
        if phone:
            print(TEXT["EXISTS"])
        else:
            self.phones.append(Phone(phone_number))
            print(TEXT["ADDED"])
            return True

    def add_birthday(self, birthday: str) -> bool:
        old_birthday= self.birthday
        self.birthday = Birthday(birthday)

        if old_birthday:
            print(TEXT["UPDATED"])
            print_diff(str(old_birthday), birthday)
        else:
            print(TEXT["ADDED"])

        return self.birthday is not None

    def add_email(self, email: str) -> bool:
        old_email = self.email
        self.email = Email(email)

        if old_email:
            print(TEXT["UPDATED"])
            print_diff(str(old_email), email)
        else:
            print(TEXT["ADDED"])

        return self.email is not None

    def add_address(self, address: str):
        old_address = self.address
        self.address = Address(address)

        if old_address:
            print(TEXT["UPDATED"])
            print_diff(str(old_address), address)
        else:
            print(TEXT["ADDED"])

        return  self.address is not None

    def show_birthday(self):
        if (self.birthday):
            print(self.birthday)
        else:
            print(TEXT["NOT_FOUND"])

    def show_email(self):
        if (self.email):
            print(self.email)
        else:
            print(TEXT["NOT_FOUND"])

    def show_address(self):
        if self.address:
            print(self.address)
        else:
            print(TEXT["NOT_FOUND"])

    @confirm_prompt()
    def remove_phone(self, phone_number):
        phone = self.get_phone(phone_number)
        if phone:
            self.phones = list(filter((lambda phone: str(phone) != phone_number), self.phones))
            print(TEXT["DELETED"])
            return True

        print(TEXT["NOT_FOUND"])

    @confirm_prompt("Existing name will be changed, continue?")
    def change_name(self, name, new_name):
        if name != new_name:
            self.name = Name(new_name)
            print(TEXT["UPDATED"])
            print_diff(name, new_name)
            return True

        print(TEXT["EQUAL"])
        return False

    @confirm_prompt("Existing address will be deleted, continue?")
    def remove_address(self):
        self.address = None
        print(TEXT["DELETED"])

    @confirm_prompt("Existing email will be deleted, continue?")
    def remove_email(self):
        self.email = None
        print(TEXT["DELETED"])

    @confirm_prompt("Existing birthday will be deleted, continue?")
    def remove_birthday(self):
        self.birthday = None
        print(TEXT["DELETED"])

    @confirm_prompt("Existing phone number will be updated, continue?")
    def edit_phone(self, old_phone, new_phone):
        phone = self.get_phone(old_phone)
        if phone:
            phone.value = new_phone
            print(TEXT["UPDATED"])
            print_diff(old_phone, new_phone)
            return True

        print(TEXT["NOT_FOUND"])

    def find_phones(self):
        if len(self.phones) > 0:
            print(self.get_string_phones())
        else:
            print(TEXT["NO_DATA_TO_DISPLAY"])

    def __str__(self):
        birthday = f", birthday: {self.birthday}" if self.birthday else ""
        email = f", email: {self.email}" if self.email else ""
        address = f", address: {self.address}" if self.address else ""
        phones = f", phones: {self.get_string_phones("; ")}"
        return f"Contact name: {self.name}{phones}{birthday}{email}{address}"


__all__ = ["Record"]
