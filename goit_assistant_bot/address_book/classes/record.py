from datetime import datetime
from ..constants import (
    NOT_FOUND,
    EXISTS,
    DELETED,
    UPDATED,
    ADDED,
    EQUAL,
    DATE_OUTPUT_FORMAT,
)
from ..utils import print_diff, print_message
from ..decorators import confirm_prompt
from .name import Name
from .phone import Phone
from .birthday import Birthday
from .email import Email
from .address import Address


not_found_message = print_message(NOT_FOUND)
exists_message = print_message(EXISTS)
deleted_message = print_message(DELETED)
added_message = print_message(ADDED)
updated_message = print_message(UPDATED)
equal_message = print_message(EQUAL)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
        self.email = None
        self.address = None

    def get_phones(self, delimeter=", ", no_data_message="") -> str:
        return (
            delimeter.join([phone.value for phone in self.phones])
            if len(self.phones) > 0
            else no_data_message
        )

    def get_phone(self, phone_number) -> Phone | None:
        for phone in self.phones:
            if str(phone) == phone_number:
                return phone
        return None

    def phone_exists(self, phone_number):
        for phone in self.phones:
            if str(phone) == phone_number:
                return True
        return False

    def get_birthday_datetime(self) -> datetime | None:
        if self.birthday:
            day, month, year = str(self.birthday).split(".")
            birthday = datetime(year=int(year), month=int(month), day=int(day))
            return birthday
        return None

    def get_birthday(self):
        birthday_datetime = self.get_birthday_datetime()
        if birthday_datetime:
            return birthday_datetime.strftime(DATE_OUTPUT_FORMAT)
        return None

    def add_phone(self, new_number):
        phone = self.get_phone(new_number)
        if phone:
            exists_message("Phone")
            return False
        else:
            self.phones.append(Phone(new_number))
            added_message("Phone")
            return True

    def add_birthday(self, birthday) -> bool:
        if self.birthday:
            old_birthday = str(self.birthday)
            self.birthday.value = birthday
            print_diff(old_birthday, birthday)
            updated_message("Birthday")
        else:
            self.birthday = Birthday(birthday)
            added_message("Birthday")

        return self.birthday is not None

    def add_email(self, email) -> bool:
        if self.email is not None:
            old_email = str(self.email)
            self.email.value = email
            print_diff(old_email, email)
            updated_message("Email")
        else:
            self.email = Email(email)
            added_message("Email")

        return self.email is not None

    def add_address(self, address):
        if self.address is not None:
            old_address = str(self.address)
            self.address.value = address
            print_diff(old_address, address)
            updated_message("Address")
        else:
            self.address = Address(address)
            added_message("Address")

        return self.address is not None

    def show_birthday(self):
        if self.birthday:
            print(self.get_birthday())
        else:
            not_found_message("Birthday")

    def show_email(self):
        if self.email:
            print(self.email)
        else:
            not_found_message("Email")

    def show_address(self):
        if self.address:
            print(self.address)
        else:
            not_found_message("Address")

    def show_phone(self):
        if len(self.phones) > 0:
            print(self.get_phones())
        else:
            not_found_message("Phones")

    @confirm_prompt("Existing address will be deleted, continue?")
    def remove_address(self):
        self.address = None
        deleted_message("Address")
        return True

    @confirm_prompt("Existing email will be deleted, continue?")
    def remove_email(self):
        self.email = None
        deleted_message("Email")
        return True

    @confirm_prompt("Existing birthday will be deleted, continue?")
    def remove_birthday(self):
        self.birthday = None
        deleted_message("Birthday")
        return True

    @confirm_prompt("Existing phone number will be deleted, continue?")
    def remove_phone(self, phone_number):
        phone = self.get_phone(phone_number)
        if phone:
            self.phones = list(
                filter((lambda phone: str(phone) != phone_number), self.phones)
            )
            deleted_message("Phone")
            return True

        not_found_message("Phone")
        return False

    @confirm_prompt("Existing name will be changed, continue?")
    def change_name(self, name, new_name):
        if name != new_name:
            self.name.value = new_name
            print_diff(name, new_name)
            updated_message("Name")
            return True

        equal_message("Names")
        return False

    @confirm_prompt("Existing phone number will be updated, continue?")
    def change_phone(self, old_phone, new_phone):
        phone = self.get_phone(old_phone)
        if phone:
            phone.value = new_phone
            print_diff(old_phone, new_phone)
            updated_message("Phone")
            return True

        not_found_message("Phone")
        return False

    def __str__(self):
        birthday = f", birthday: {str(self.birthday) if self.birthday else '-'}"
        email = f", email: {str(self.email) if self.email else '-'}"
        address = f", address: {str(self.address) if self.address else '-'}"
        phones = f", phone: {self.get_phones('; ', '-')}"
        return f"Contact name: {self.name}{phones}{birthday}{email}{address}"


__all__ = ["Record"]
