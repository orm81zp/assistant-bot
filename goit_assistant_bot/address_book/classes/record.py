from colorama import Fore, Style

from .name import Name
from .phone import Phone
from .birthday import Birthday
from .email import Email
from .address import Address
from ..constants import TEXT


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
            if phone == phone_number:
                return phone

        return None

    def add_phone(self, phone_number):
        phone = self.get_phone(phone_number)
        if phone:
            print(Fore.LIGHTBLACK_EX + TEXT["PHONE_NUMBER_EXISTS"] + Style.RESET_ALL)
        else:
            self.phones.append(Phone(phone_number))
            print(Fore.GREEN + TEXT["PHONE_NUMBER_ADDED"] + Style.RESET_ALL)
            return True

    def add_birthday(self, birthday: str) -> bool:
        birthday = birthday.strip()
        message = TEXT["BIRTHDAY_UPDATED"] if self.birthday else TEXT["BIRTHDAY_ADDED"]
        self.birthday = Birthday(birthday)
        print(Fore.GREEN + message + Style.RESET_ALL)
        return self.birthday is not None

    def show_birthday(self):
        if (self.birthday):
            print(self.birthday)
        else:
            print(TEXT["BIRTHDAY_NOT_FOUND"])

    def add_email(self, email: str) -> bool:
        email = email.strip()
        message = TEXT["EMAIL_UPDATED"] if self.email else TEXT["EMAIL_ADDED"]
        self.email = Email(email)
        print(Fore.GREEN + message + Style.RESET_ALL)
        return self.email is not None

    def show_email(self):
        if (self.email):
            print(self.email)
        else:
            print(TEXT["EMAIL_NOT_FOUND"])

    def add_address(self, address: str) -> bool:
        address = address.strip()
        message = TEXT["ADDRESS_UPDATED"] if self.address else TEXT["ADDRESS_ADDED"]
        self.address = Address(address)
        print(Fore.GREEN + message + Style.RESET_ALL)
        return self.address is not None

    def show_address(self):
        if self.address:
            print(self.address)
        else:
            print(TEXT["ADDRESS_NOT_FOUND"])

    def remove_phone(self, phone_number):
        phone = self.get_phone(phone_number)
        if phone:
            self.phones = list(filter((lambda phone: phone != phone_number), self.phones))
            print(Fore.GREEN + TEXT["PHONE_NUMBER_DELETED"] + Style.RESET_ALL)
            return True

        print(Fore.LIGHTBLACK_EX + TEXT["PHONE_NUMBER_NOT_FOUND"] + Style.RESET_ALL)

    def remove_address(self):
        self.address = None
        print(Fore.GREEN + TEXT["ADDRESS_DELETED"] + Style.RESET_ALL)

    def remove_email(self):
        self.email = None
        print(Fore.GREEN + TEXT["EMAIL_DELETED"] + Style.RESET_ALL)

    def remove_birthday(self):
        self.birthday = None
        print(Fore.GREEN + TEXT["BIRTHDAY_DELETED"] + Style.RESET_ALL)

    def edit_phone(self, old_phone, new_phone):
        phone = self.get_phone(old_phone)
        if phone:
            phone.value = new_phone
            print(Fore.GREEN + TEXT["PHONE_NUMBER_UPDATED"] + Style.RESET_ALL)
            return True
        
        print(Fore.LIGHTBLACK_EX + TEXT["PHONE_NUMBER_NOT_FOUND"] + Style.RESET_ALL)

    def find_phone(self, phone_number):
        phone = self.get_phone(phone_number)
        if phone:
            print(phone.value)
        else:
            print(Fore.LIGHTBLACK_EX + TEXT["PHONE_NUMBER_NOT_FOUND"] + Style.RESET_ALL)

    def find_phones(self):
        if len(self.phones) > 0:
            print(self.get_string_phones())
        else:
            print(Fore.LIGHTBLACK_EX + TEXT["NO_DATA_TO_DISPLAY"] + Style.RESET_ALL)

    def __str__(self):
        birthday = f", birthday: {self.birthday}" if self.birthday else ""
        email = f", email: {self.email}" if self.email else ""
        address = f", address: {self.address}" if self.address else ""
        phones = f", phones: {self.get_string_phones("; ")}"
        return f"Contact name: {self.name}{phones}{birthday}{email}{address}"


__all__ = ["Record"]
