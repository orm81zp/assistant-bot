import re
from colorama import Fore, Style

from .name import Name
from .phone import Phone
from .birthday import Birthday
from ..constants import TEXT


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __is_valid_phone_number(self, phone_number) -> bool:
        is_counts = len(phone_number) == 10
        is_all_numbers = all(True for number in phone_number if number.isdecimal())

        return True if is_counts and is_all_numbers else False

    def __is_valid_birthday(self, birthday) -> bool:
        is_birthday_matched = re.match(r"^\d{2}\.\d{2}\.\d{4}$", birthday)
        return True if is_birthday_matched else False
    
    def __is_phone_number_exists(self, phone_number) -> bool:
        for phone in self.phones:
            if phone.value == phone_number:
                return True
        return False

    def __get_string_phones(self, delimeter = ', ') -> str:
        return delimeter.join([p.value for p in self.phones]) if len(self.phones) else ""

    def add_phone(self, phone_number):
        if self.__is_valid_phone_number(phone_number):
            if not self.__is_phone_number_exists(phone_number):
                self.phones.append(Phone(phone_number))
                print(Fore.GREEN + TEXT["PHONE_NUMBER_ADDED"] + Style.RESET_ALL)
                return True
            else:
                print(Fore.LIGHTBLACK_EX + TEXT["PHONE_NUMBER_EXISTS"] + Style.RESET_ALL)
        else:
            print(Fore.RED + TEXT["PHONE_VALIDATION"] + Style.RESET_ALL)

    def add_birthday(self, birthday: str):
        birthday = birthday.strip()
        if self.__is_valid_birthday(birthday):
            self.birthday = Birthday(birthday)
            print(Fore.GREEN + TEXT["BIRTHDAY_ADDED"] + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + TEXT["BIRTHDAY_VALIDATION"] + Style.RESET_ALL)

    def find_birthday(self) -> str:
        return self.birthday.value if self.birthday else TEXT["BIRTHDAY_NOT_FOUND"]

    def remove_phone(self, phone_number):
        if self.__is_valid_phone_number(phone_number):
            if self.__is_phone_number_exists(phone_number):
                self.phones = list(filter((lambda p: p.value != phone_number), self.phones))
                print(Fore.GREEN + TEXT["PHONE_NUMBER_DELETED"] + Style.RESET_ALL)
                return True
            else:
                print(Fore.LIGHTBLACK_EX + TEXT["PHONE_NUMBER_NOT_FOUND"] + Style.RESET_ALL)
        else:
            print(Fore.RED + TEXT["PHONE_VALIDATION"] + Style.RESET_ALL)

    def edit_phone(self, old_phone, new_phone):
        if self.__is_phone_number_exists(old_phone):
            if self.__is_valid_phone_number(new_phone):
                phones = map((lambda p: Phone(new_phone) if p.value == old_phone else p), self.phones)
                self.phones = list(phones)
                print(Fore.GREEN + TEXT["PHONE_NUMBER_UPDATED"] + Style.RESET_ALL)
                return True
            else:
                print(Fore.RED + TEXT["PHONE_VALIDATION"] + Style.RESET_ALL)
        else:
            print(Fore.LIGHTBLACK_EX + TEXT["PHONE_NUMBER_NOT_FOUND"] + Style.RESET_ALL)

    def find_phone(self, phone_number):
        if self.__is_phone_number_exists(phone_number):
            for phone in self.phones:
                if phone.value == phone_number:
                    print(phone.value)
        else:
            print(Fore.LIGHTBLACK_EX + TEXT["PHONE_NUMBER_NOT_FOUND"] + Style.RESET_ALL)

    def find_phones(self):
        if len(self.phones) > 0:
            print(self.__get_string_phones())
        else:
            print(Fore.LIGHTBLACK_EX + TEXT["NO_DATA"] + Style.RESET_ALL)
    
    def __str__(self):
        phones = self.__get_string_phones("; ") if len(self.phones) else "no data"
        return f"Contact name: {self.name.value}, phones: {phones}"


__all__ = ["Record"]
