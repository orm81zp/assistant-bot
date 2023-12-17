import pickle
from pathlib import Path
from colorama import Fore, Style
from ..address_book.classes import AddressBook


class AddressBookManager:
    __book = AddressBook()

    def __init__(self, filename):
        self.filename = Path(filename)
        self.__load()

    def __load(self):
        """Load the contact book from a dump file if one exists"""
        if self.filename.exists():
            filename = self.filename.name
            try:
                with open(str(self.filename), "rb") as fh:
                    self.__book = pickle.load(fh)
                    print(
                        Fore.YELLOW
                        + f'\u2713 Contact book "{filename}" restored!'
                        + Style.RESET_ALL
                    )
            except Exception:
                print(
                    Fore.RED
                    + "\u02DF Oh! Something went wrong while restoring the contact book!"
                    + Style.RESET_ALL
                )

    def get_book(self) -> AddressBook:
        return self.__book

    def save(self):
        """Saves the contact book"""
        try:
            filename = self.filename.name
            with open(str(self.filename), "wb") as fh:
                pickle.dump(self.__book, fh)
                print(
                    Fore.YELLOW
                    + f'\u2713 Contact book "{filename}" saved!'
                    + Style.RESET_ALL
                )
        except Exception:
            print(
                Fore.RED
                + "\u02DF Oh! Something went wrong while saving the contact book!"
                + Style.RESET_ALL
            )


__all__ = ["AddressBookManager"]
